"""Exact rational checks of last-coverage probabilities on weighted cycles.

Separate finite absorbing-chain calculation and analytic Jacobian identity.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import sympy as sp


def formula(r, s, k):
    n=len(r)
    assert s!=k
    # path after deleting k: begin a=k-1 mod n, end b=k+1 mod n
    path=[(k-1-j)%n for j in range(n-1)]
    assert path[-1]==(k+1)%n
    j=path.index(s)
    x=sum((r[path[t+1]] for t in range(j)), F(0)) # edge from path[t] (higher index clockwise?) edge index path[t+1]
    y=sum((r[path[t+1]] for t in range(j,n-2)), F(0))
    L=x+y
    return y/L*r[(k-1)%n]/(r[(k-1)%n]+L) + x/L*r[k]/(r[k]+L)


def exact_chain(r,s):
    n=len(r)
    allbits=(1<<n)-1
    transient=[(m,i) for m in range(1,allbits) for i in range(n) if (m&(1<<i)) and (m&(1<<s))]
    idx={state:j for j,state in enumerate(transient)}
    K=len(transient)
    A=[[F(0) for _ in range(K)] for _ in range(K)]
    B=[[F(0) for _ in range(n)] for _ in range(K)]
    for (m,i),j in idx.items():
        A[j][j]=F(1)
        for dest,c in (((i+1)%n,1/r[i]),((i-1)%n,1/r[(i-1)%n])):
            p=c/(1/r[i]+1/r[(i-1)%n])
            mm=m|(1<<dest)
            if mm==allbits:
                B[j][dest]+=p
            else:
                A[j][idx[(mm,dest)]]-=p
    # one Gaussian elimination all rhs, independent of hitting gambler formula
    for col in range(K):
        pivot=next(z for z in range(col,K) if A[z][col])
        A[col],A[pivot]=A[pivot],A[col]
        B[col],B[pivot]=B[pivot],B[col]
        inv=1/A[col][col]
        for j in range(col,K): A[col][j]*=inv
        for k in range(n): B[col][k]*=inv
        for row in range(K):
            if row==col: continue
            factor=A[row][col]
            if factor:
                for j in range(col,K): A[row][j]-=factor*A[col][j]
                for k in range(n): B[row][k]-=factor*B[col][k]
    return B[idx[(1<<s,s)]]


def test():
    checks=0
    for n in range(3,7):
        # fewer exact matrices for 6-vertex, deterministic profiles
        profiles=[tuple(F(x) for x in [1]*n),tuple(F(1+i) for i in range(n)),tuple(F(1+(3*i*i+1)%7,2) for i in range(n))]
        for r in profiles:
            for s in range(n):
                v=exact_chain(r,s)
                assert v[s]==0 and sum(v)==1
                for k in range(n):
                    if k!=s:
                        w=formula(r,s,k)
                        assert w==v[k], (n,r,s,k,v,w)
                        checks+=1
    # Nontrivial exact fair 4-cycle
    r=(F(1),F(2),F(1,2),F(3,2))
    assert all(formula(r,0,k)==F(1,3) for k in (1,2,3))
    checks+=3
    # verify analytic first derivative of probability at homogeneous r
    for n in range(3,11):
        for j in range(n):
            rs=sp.symbols('r0:'+str(n),positive=True)
            for k in range(1,n):
                x=sum(rs[:k-1]); y=sum(rs[k+1:]); L=x+y
                pk=(y/L)*(rs[k-1]/(rs[k-1]+L))+(x/L)*(rs[k]/(rs[k]+L))
                grad=sp.diff(pk,rs[j]).subs({u:1 for u in rs})
                expected=sp.Rational((n-k)*(j==k-1)+k*(j==k)-(1), (n-1)**2)
                assert sp.simplify(grad-expected)==0,(n,j,k,grad,expected)
                checks+=1
        direction=sp.Matrix([(-1)**j*comb(n-1,j) for j in range(n)])
        assert sum(direction)==0
        matrix=sp.Matrix([[(n-k)*(j==k-1)+k*(j==k)-1 for j in range(n)] for k in range(1,n)])
        assert matrix*direction==sp.zeros(n-1,1)
        assert matrix.rank()==n-2
        checks+=2
    print('PASS exact finite-chain, analytic derivatives and rank checks:',checks)

if __name__=='__main__':test()
