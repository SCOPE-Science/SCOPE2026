"""Finite exact and matrix checks for collision-exclusion rigidity."""
from itertools import combinations, permutations
from fractions import Fraction
import numpy as np
from scipy.linalg import expm
import sympy as sp


def edges(n):
    return list(combinations(range(n),2))


def incidence(n,k):
    e=edges(n)
    return sp.Matrix([[int(i in s and j in s) for i,j in e] for s in combinations(range(n),k)])


def sym_rates_regular(n, eps=Fraction(1,4)):
    w={(i,j):Fraction(1) for i,j in edges(n)}
    # Alternating four-cycle on four selected sites; each weighted degree unchanged.
    for pair,sign in [((0,1),1),((1,2),-1),((2,3),1),((0,3),-1)]:
        w[pair]+=sign*eps
    return w


def kap(n,k,w):
    return {S:sum(w[(i,j)] for i,j in combinations(S,2))
        for S in combinations(range(n),k)}


def chain(n,k,w):
    st=list(permutations(range(n),k)); pos={s:i for i,s in enumerate(st)}
    Q=np.zeros((len(st),len(st)))
    for row,s in enumerate(st):
        for label,i in enumerate(s):
            for j in range(n):
                if j==i or j in s: continue
                pair=tuple(sorted((i,j)))
                base=float(w[pair]); frac=0.31+0.025*((i+j)%5)
                rate=base*(frac if i<j else 1-frac)
                ns=list(s);ns[label]=j
                Q[row,pos[tuple(ns)]]+=rate
        Q[row,row]=-sum(Q[row])
    K=np.array([float(sum(w[tuple(sorted((i,j)))] for i,j in combinations(s,2))) for s in st])
    return Q,K


def eigen_check(n,k,w,expected_equal):
    Q,K=chain(n,k,w); killed=Q-np.diag(K)
    eigvals,eigvec=np.linalg.eig(killed)
    idx=np.argmax(eigvals.real)
    h=eigvec[:,idx].real
    if h.mean()<0: h=-h
    assert np.min(h)>0
    R=np.zeros_like(Q)
    for i in range(len(Q)):
        for j in range(len(Q)):
            if i!=j: R[i,j]=Q[i,j]*h[j]/h[i]
        R[i,i]=-sum(R[i])
    gap=np.max(abs(R-Q))
    if expected_equal: assert gap<2e-9,(n,k,gap)
    else: assert gap>1e-5,(n,k,gap)
    if expected_equal:
        t=0.37
        assert np.max(abs(expm(killed*t)-np.exp(-K[0]*t)*expm(Q*t)))<2e-12
    return gap


def run():
    checks=0
    for n in range(3,9):
        m=len(edges(n))
        for k in range(2,n):
            M=incidence(n,k)
            d=M[1:,:]-sp.ones(M.rows-1,1)*M[0,:]
            null=m-d.rank()
            exp=1 if k<=n-2 else m-(n-1)
            assert null==exp, (n,k,null,exp)
            checks+=1
            if n>=4:
                reg=sym_rates_regular(n)
                kk=kap(n,k,reg)
                assert (len(set(kk.values()))==1)==(k==n-1)
                checks+=1
    reg=sym_rates_regular(4)
    assert len(set(kap(4,3,reg).values()))==1
    assert len(set(reg.values()))>1
    gap1=eigen_check(4,3,reg,True)
    gap2=eigen_check(4,2,reg,False)
    gap3=eigen_check(5,3,sym_rates_regular(5),False)
    u={(i,j):Fraction(2) for i,j in edges(5)}
    gap4=eigen_check(5,3,u,True)
    checks+=4
    print('PASS',checks,'exact rank/degree and generator checks',{'equal_gaps':(gap1,gap4),'unequal_gaps':(gap2,gap3)})

if __name__=='__main__':run()
