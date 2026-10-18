"""Standalone finite checks for the complete-split fastest-mixing theorem.

Requires Python >=3.10, SymPy, NumPy, and SciPy. Reproduces finite
exact-rational spectra, invariance-restricted LP minima, and samples of
asymmetric feasible kernels. The proof is analytic and does not rely on
finite coverage.
"""
from fractions import Fraction
from itertools import combinations
import random
import numpy as np
from scipy.optimize import linprog
import sympy as sp

checks=0

def check(test, message='verification failure'):
    global checks
    if not bool(test):
        raise AssertionError(message)
    checks += 1


def theoretical(k,m):
    assert k>=2 and m>=2
    if m <= 2*k:
        return Fraction(2,m+2*k), Fraction(m,m+2*k)
    return Fraction(1,m), Fraction(m-k,m)


def kernel(k,m,a,core_edges):
    N=k+m
    P=sp.zeros(N)
    for i in range(k):
        for j in range(m):
            P[i,k+j]=P[k+j,i]=sp.Rational(a.numerator,a.denominator)
    for (i,j),b in core_edges.items():
        P[i,j]=P[j,i]=sp.Rational(b.numerator,b.denominator)
    for i in range(N):
        P[i,i]=1-sum(P[i,j] for j in range(N) if j!=i)
    return P


def slem(P):
    ev=P.eigenvals()
    check(sum(ev.values())==P.rows)
    check(ev.get(sp.Integer(1),0)==1)
    return max(abs(l) for l in ev if l!=1)


def invariant_lp(k,m):
    # variables are (a,b,u): |leaf| <=u, |cross|<=u, |core|<=u.
    A=[]; v=[]
    # leaf = 1-k*a
    A += [[-k,0,-1],[k,0,-1]];v += [-1,1]
    # cross = 1-(m+k)*a
    A += [[-m-k,0,-1],[m+k,0,-1]];v += [-1,1]
    # core = 1-m*a-k*b
    A += [[-m,-k,-1],[m,k,-1]];v += [-1,1]
    # core capacity
    A += [[m,k-1,0]];v += [1]
    # leaf capacity
    A += [[k,0,0]];v += [1]
    res=linprog([0,0,1],A_ub=A,b_ub=v,bounds=[(0,None)]*3,method='highs')
    check(res.success)
    return res.x[2]


def homogeneous_cases():
    for k in range(2,10):
      for m in range(2,13):
        a,mu=theoretical(k,m)
        if m<=2*k:
            b=Fraction(2*k-m,k*(m+2*k))
        else:
            b=Fraction(0)
        B={(i,j):b for i,j in combinations(range(k),2)}
        P=kernel(k,m,a,B)
        check(P==P.T)
        check(all(P[i,j]>=0 for i in range(k+m) for j in range(k+m)))
        check(all(sum(P[i,j] for j in range(k+m))==1 for i in range(k+m)))
        check(slem(P)==sp.Rational(mu.numerator,mu.denominator),f'slem mismatch {k,m}')
        check(abs(invariant_lp(k,m)-float(mu))<1e-8,f'LP mismatch {k,m}')
        if k<=6 and m<=8:
            # Exact determinant spectrum in the symmetry-adapted decomposition.
            c=1-m*sp.Rational(a.numerator,a.denominator)
            lambdas={sp.Integer(1):1,
              1-(m+k)*sp.Rational(a.numerator,a.denominator):1,
              1-k*sp.Rational(a.numerator,a.denominator):m-1,
              c-k*sp.Rational(b.numerator,b.denominator):k-1}
            actual=P.eigenvals()
            expected={}
            for l,mult in lambdas.items():expected[l]=expected.get(l,0)+mult
            check(actual==expected,f'eigenspace mismatch {k,m}')


def face_cases():
    for k in range(2,9):
      for m in range(2,2*k):
        a,mu=theoretical(k,m)
        # The zero core-edge weighting is optimal iff m >= k.
        Z=kernel(k,m,a,{})
        check((slem(Z)==sp.Rational(mu.numerator,mu.denominator))==(m>=k))
        # Canonical all-positive core weighting always remains optimal.
        b=Fraction(2*k-m,k*(m+2*k))
        B={(i,j):b for i,j in combinations(range(k),2)}
        check(slem(kernel(k,m,a,B))==sp.Rational(mu.numerator,mu.denominator))
        # Scale b downward by a factor 1/2: admissible iff the exact
        # core spectral-gap inequality still holds.
        Bh={(i,j):b/2 for i,j in combinations(range(k),2)}
        P=kernel(k,m,a,Bh)
        eigen_ok= (m>=k) or (k*(b/2) >= Fraction(2*(k-m),m+2*k))
        check((slem(P)==sp.Rational(mu.numerator,mu.denominator))==eigen_ok)


def random_feasible_cases():
    rng=random.Random(421976)
    for k,m in [(2,2),(2,6),(3,2),(3,8),(5,3),(5,10),(7,4)]:
        mu=float(theoretical(k,m)[1]); N=k+m
        for _ in range(100):
            # All asymmetric edge probabilities are independent.
            edges=[(i,j) for i in range(k) for j in range(i+1,k)] + [(i,k+j) for i in range(k) for j in range(m)]
            raw=[rng.random() for edge in edges]
            deg=[0.0]*N
            for (i,j),v in zip(edges,raw):deg[i]+=v;deg[j]+=v
            scale=rng.random()/(max(deg)+1e-20)
            P=np.eye(N)
            for (i,j),v in zip(edges,raw):
                w=scale*v;P[i,j]=P[j,i]=w;P[i,i]-=w;P[j,j]-=w
            vals=np.linalg.eigvalsh(P)
            check(np.max(np.abs(vals[:-1]))>=mu-1e-9)
            check(np.min(P)>=-1e-12)
            check(np.max(np.abs(P.sum(axis=1)-1))<1e-12)


def main():
    homogeneous_cases();face_cases();random_feasible_cases()
    print(f'VERIFY_OK {checks} checks')

if __name__=='__main__':main()
