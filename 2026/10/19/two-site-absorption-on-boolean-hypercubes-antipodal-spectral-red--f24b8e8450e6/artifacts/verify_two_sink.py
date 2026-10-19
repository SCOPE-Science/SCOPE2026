"""Exact two-sink hypercube spectral projection and absorbing walk checks.

Python 3, numpy, scipy. Finite tests only corroborate analytic formulas.
"""
import itertools
import math
import numpy as np
from scipy.linalg import expm

def kraw(d,k,w):
    return sum((-1)**j*math.comb(w,j)*math.comb(d-w,k-j)
               for j in range(max(0,k-(d-w)),min(k,w)+1))

def absorption_formula(d,s,x):
    h=s.bit_count()
    w=x.bit_count()
    z=(x^s).bit_count()
    b=2**d
    if h==d:
        return sum(kraw(d,k,w)**2/math.comb(d,k) for k in range(d+1))/b
    assert 1<=h<=d-1
    total=2
    for k in range(1,d):
        C=math.comb(d,k)
        Kh=kraw(d,k,h)
        Kw=kraw(d,k,w)
        Kz=kraw(d,k,z)
        assert C*C-Kh*Kh>0
        total+=(C*(Kw*Kw+Kz*Kz)-2*Kh*Kw*Kz)/(C*C-Kh*Kh)
    return total/b

def adjacency(d):
    b=1<<d
    h=np.zeros((b,b))
    for x in range(b):
        for i in range(d):
            h[x,x^(1<<i)]=1
    return h

def spectral_bright(d,s):
    b=1<<d
    coords=np.arange(b)
    W=np.empty((b,b))
    for x in range(b):
        for t in range(b):
            W[x,t]=(-1)**((x&t).bit_count())/np.sqrt(b)
    P=np.zeros((b,b))
    totalrank=0
    for k in range(d+1):
        U=W[:,[t for t in range(b) if t.bit_count()==k]]
        vecs=U@(U[[0,s],:].T)
        q,sigma,_=np.linalg.svd(vecs,full_matrices=False)
        rank=int(sum(sigma>1e-9))
        P+=q[:,:rank]@q[:,:rank].T
        totalrank+=rank
    return P,totalrank

def main():
    checks=0
    for d in range(2,7):
        b=1<<d
        for h in range(1,d+1):
            s=(1<<h)-1
            P,rank=spectral_bright(d,s)
            assert rank == (d+1 if h==d else 2*d)
            checks+=1
            assert np.linalg.norm(P@P-P)<1e-11
            assert abs(np.trace(P)-rank)<1e-10
            checks+=2
            probs=np.array([absorption_formula(d,s,x) for x in range(b)])
            assert max(abs(probs-np.diag(P)))<2e-12
            checks+=b
            assert abs(sum(probs)-rank)<2e-10
            checks+=1
            if h==d:
                P_single,_=spectral_bright(d,0)
                # Single detector computed by directly taking one spectral vector per level.
                W=np.array([[(-1)**((x&t).bit_count())/np.sqrt(b) for t in range(b)] for x in range(b)])
                single=np.zeros((b,b))
                for k in range(d+1):
                    U=W[:,[t for t in range(b) if t.bit_count()==k]]
                    v=U@U[0,:]
                    single+=np.outer(v,v)/np.dot(v,v)
                assert np.linalg.norm(P-single)<1e-11
                checks+=1
    # Direct non-Hermitian absorption dynamics for random positive, unequal rates.
    for d in range(2,6):
        b=1<<d
        H=adjacency(d)
        for h in range(1,d+1):
            s=(1<<h)-1
            P,rank=spectral_bright(d,s)
            Heff=H-0.5j*np.diag([1.7 if v==0 else 0.8 if v==s else 0 for v in range(b)])
            U=expm(-1j*Heff*280)
            residual=U.conj().T@U
            assert np.linalg.norm(residual-(np.eye(b)-P),ord=2)<4e-6
            checks+=1
    print('checks=',checks)
    print('d=5, nonantipodal bright=',2*5,'antipodal bright=',5+1)
    print('d=5, mean absorption nonantipodal=',2*5/2**5,'antipodal=',(5+1)/2**5)

if __name__=='__main__':
    main()
