"""Exact and independent numerical verification of the K_{p,p,q} fastest-mixing formulas.

Run: python verify.py
Requires Python >=3.9, NumPy and SciPy; see requirements.txt.
The proof for arbitrary parameters is contained in RESULT.md, not inferred from finite checks.
"""
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog


def solution(p, q):
    """Return optimal SLEM and the full interval of automorphism-invariant optimizers."""
    p, q = int(p), int(q)
    if q * 2 <= p:
        t = F(2*p-q, 6*p)
        y = F(1,2*p)
        x = F(2*p-q,3*p*p)
        return t,y,x,x
    if q <= p:
        t = F(p,3*p+2*q)
        x = y = F(2,3*p+2*q)
        return t,y,x,x
    if q <= 4*p:
        t = F(q,4*p+q)
        y = F(2,4*p+q)
        if q <= 2*p:
            lo=F(2*(2*p-q),p*(4*p+q))
            hi=F(2,4*p+q)
        else:
            lo=F(0)
            hi=F(4*p-q,p*(4*p+q))
        return t,y,lo,hi
    t=F(q-2*p,q)
    y=F(1,q)
    return t,y,F(0),F(0)


def modes(p,q,x,y):
    return (1-(2*p*x+q*y),1-(p*x+q*y),1-2*p*y,1-(2*p+q)*y)


def feasible(p,q,x,y):
    return x>=0 and y>=0 and p*x+q*y<=1 and 2*p*y<=1


def matrix(p,q,x,y):
    N=2*p+q
    P=np.eye(N)
    for i in range(N):
        for j in range(i+1,N):
            a,b=(0 if i<p else 1 if i<2*p else 2),(0 if j<p else 1 if j<2*p else 2)
            w=float(x if {a,b}=={0,1} else y if a!=b else 0)
            P[i,j]=P[j,i]=w
            P[i,i]-=w
            P[j,j]-=w
    return P


def independent_lp(p,q):
    # LP variables: x, y, SLEM.  Four nontrivial Laplacian modes.
    coeff=((2*p,q),(p,q),(0,2*p),(0,2*p+q))
    A=[];B=[]
    for a,b in coeff:
        A += [[a,b,-1],[-a,-b,-1]]
        B += [1,-1]
    A += [[p,q,0],[0,2*p,0]]
    B += [1,1]
    ans=linprog((0,0,1), A_ub=A,b_ub=B, bounds=((0,None),(0,None),(0,None)),method='highs')
    assert ans.success, (p,q,ans.message)
    return ans.x


def run():
    exact=0; lp=0; dense=0; interval=0
    for p in range(2,16):
        for q in range(2,61):
            t,y,lo,hi=solution(p,q)
            assert 0<=lo<=hi,(p,q,lo,hi)
            for x in (lo,hi,(lo+hi)/2):
                assert feasible(p,q,x,y),(p,q,x,y)
                assert max(abs(z) for z in modes(p,q,x,y))==t,(p,q,x,y,t,modes(p,q,x,y))
                exact+=1
            if q>=2*p and q<=4*p:
                assert lo==0,(p,q,lo)
            if q>4*p:
                assert lo==hi==0,(p,q)
            if (p<=9 and q<=31) or (p in (11,13,15) and q in (2,p//2,p,2*p,4*p,4*p+1)):
                xx,yy,tt=independent_lp(p,q)
                assert abs(tt-float(t))<2e-8,(p,q,tt,t)
                lp+=1
            if p<=7 and q<=12 and ((p+q)%3==0 or q in (p,2*p)):
                for x in (lo,hi):
                    P=matrix(p,q,x,y)
                    ev=np.linalg.eigvalsh(P)
                    assert np.min(P)>-1e-12 and np.max(abs(P.sum(axis=0)-1))<1e-11
                    assert abs(ev[-1]-1)<1e-10
                    assert abs(max(abs(z) for z in ev[:-1])-float(t))<2e-10,(p,q,t,ev)
                    dense+=1
    # Boundary stress-tests over rational p/q, including integer equality cases.
    for p in range(4,24,2):
        for q in (p//2,p,2*p,4*p):
            t,y,lo,hi=solution(p,q)
            assert feasible(p,q,lo,y) and feasible(p,q,hi,y)
            assert all(abs(z)<=t for z in modes(p,q,lo,y))
            assert all(abs(z)<=t for z in modes(p,q,hi,y))
            interval+=1
    print(f'VERIFY_OK exact_endpoint_and_midpoint_cases={exact} independent_lp_instances={lp} full_dense_eigensystems={dense} phase_boundary_cases={interval}')

if __name__=='__main__':run()
