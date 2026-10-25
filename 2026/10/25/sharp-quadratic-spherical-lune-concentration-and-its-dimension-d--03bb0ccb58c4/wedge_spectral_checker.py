"""Independent numerical quadrature for quadratic spherical-lune concentration.

Uses beta moments and an orthonormal traceless-matrix basis, independently
of the closed-form invariant-block computation in the proof.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


def basis(n):
    out = []
    for k in range(1,n):
        x=np.zeros((n,n),float)
        x[np.arange(k),np.arange(k)]=1/math.sqrt(k*(k+1))
        x[k,k]=-k/math.sqrt(k*(k+1))
        out.append(x)
    for i in range(n):
        for j in range(i+1,n):
            x=np.zeros((n,n),float)
            x[i,j]=x[j,i]=1/math.sqrt(2)
            out.append(x)
    assert len(out)==(n-1)*(n+2)//2
    assert all(abs(np.trace(x))<1e-14 for x in out)
    assert np.linalg.norm(np.einsum('aij,bij->ab',out,out)-np.eye(len(out)))<2e-13
    return np.array(out)


def gram(n,L,nquad=64):
    A=basis(n)
    P=A[:,:2,:2]
    B=A[:,:2,2:]
    C=A[:,2:,2:]
    trC=np.trace(C,axis1=1,axis2=2)
    zz=np.outer(trC,trC)+2*np.einsum('aij,bij->ab',C,C)
    points,weights=leggauss(nquad)
    mat=np.zeros((len(A),len(A)),float)
    for node,weight in zip(points,weights):
        phi=L*node/2
        v=np.array([np.cos(phi),np.sin(phi)])
        p=np.einsum('i,aij,j->a',v,P,v)
        bv=np.einsum('aij,i->aj',B,v)
        kernel=(8*np.outer(p,p)+2*(np.outer(p,trC)+np.outer(trC,p))
             +8*(bv@bv.T)+zz)
        mat+=L*weight*kernel/(8*math.pi)
    return mat


def closed_spectrum(n,L):
    m=n-2
    s=math.sin(L)
    c=math.cos(L)
    q2=m/n
    root=math.sqrt(c*c/4+q2)
    vals=[(L+s*c/2+s*root)/(2*math.pi),
          (L+s*c/2-s*root)/(2*math.pi),
          (L-s*c)/(2*math.pi)]
    vals += [(L+s)/(2*math.pi)]*m
    vals += [(L-s)/(2*math.pi)]*m
    vals += [L/(2*math.pi)]*(m*(m+1)//2-1)
    return sorted(vals)


if __name__=='__main__':
    count=0
    for n in [3,4,5,8]:
        Lc=math.acos(2/n)
        for L in [0.08,0.3,Lc*0.9,Lc,Lc*1.1,math.pi/2,2.4,math.pi-0.05]:
            got=sorted(np.linalg.eigvalsh(gram(n,L)))
            expected=closed_spectrum(n,L)
            assert len(got)==len(expected)
            error=max(abs(x-y) for x,y in zip(got,expected))
            assert error<7e-13,(n,L,error,got,expected)
            assert abs(sum(got)-len(got)*L/(2*math.pi))<5e-13
            q2=(n-2)/n
            w=math.cos(L)/2+math.sqrt(math.cos(L)**2/4+q2)
            sign=math.cos(L)-2/n
            assert (w>1)==(sign>1e-10) or abs(sign)<1e-10
            # Direct Rayleigh check for the proposed optimal quadratic forms.
            A=basis(n)
            matrix=gram(n,L)
            m=n-2
            C=np.zeros((n,n)); C[0,0]=1; C[1,1]=-1
            S=np.diag([m/n,m/n]+[-2/n]*m)
            M=S+w*C
            X=np.zeros((n,n)); X[0,2]=X[2,0]=.5
            def rayleigh(Q):
                co=np.einsum('aij,ij->a',A,Q)
                return float(co@matrix@co/(co@co))
            root=math.sqrt((math.cos(L)/2)**2 + m/n)
            first=(L+math.sin(L)*math.cos(L)/2+math.sin(L)*root)/(2*math.pi)
            second=(L+math.sin(L))/(2*math.pi)
            assert abs(rayleigh(M)-first)<7e-13
            assert abs(rayleigh(X)-second)<7e-13
            assert abs(got[-1]-max(first,second))<7e-13
            count+=6
        print(f'n={n}, transition angle={Lc:.12f}, spectra checked')
    print('PASS',count,'independent spectral/trace/crossover checks')
