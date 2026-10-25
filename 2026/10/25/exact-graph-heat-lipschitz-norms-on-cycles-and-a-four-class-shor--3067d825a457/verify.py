"""Independent numerical and finite Taylor checks for cycle heat Lipschitz norms.

Uses only NumPy, SciPy, and SymPy. Analytic proof is in RESULT.md.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog
import sympy as sp


def laplacian(n):
    L = np.zeros((n,n))
    for j in range(n):
        L[j,j] = 2
        L[j,(j-1)%n] = -1
        L[j,(j+1)%n] = -1
    return L


def predicted_norm(n, t):
    p = expm(-t*laplacian(n))[0]
    k = (n+2)//4
    median = p[k]
    return float(np.abs(p-median).sum())


def direct_lp_norm(n,t):
    H=expm(-t*laplacian(n))
    A=np.zeros((n,n))
    for j in range(n):
        A[j,j]=1
        A[j,(j+1)%n]=-1
    vals=[]
    for j in range(n):
        c=-(H[j]-H[(j+1)%n])
        res=linprog(c,A_ub=np.vstack([A,-A]), b_ub=np.ones(2*n),
                    bounds=[(None,None)]*n,method='highs')
        assert res.success
        vals.append(-res.fun)
    return max(vals)


def exact_taylor_coefficient(n):
    L=sp.zeros(n)
    for j in range(n):
        L[j,j]=2
        L[j,(j+1)%n]=-1
        L[j,(j-1)%n]=-1
    k=(n+2)//4
    # coefficient of t^j in 1 - predicted norm, using signed median expression
    a=sp.Integer(2*k+1)-sp.Rational(n,2)
    first=sp.Integer(0)
    mat=(-L)**k
    for j in range(n):
        d=min(j,n-j)
        if d>k:first+=mat[0,j]/sp.factorial(k)
    first+=a*mat[0,k]/sp.factorial(k)
    observed=sp.expand(2*first)
    expected=sp.Rational(4*k+2-n,math.factorial(k))
    return observed,expected


def main():
    comparisons=0
    for n in range(3,23):
        for t in (0.8,1.6,3.0):
            p=predicted_norm(n,t)
            d=direct_lp_norm(n,t)
            assert abs(p-d)<4e-8,(n,t,p,d)
            comparisons+=1
        if n<=17:
            o,e=exact_taylor_coefficient(n)
            assert o==e,(n,o,e)
    # Confirm strict radial descent for representative positive times.
    radial=0
    for n in range(3,35):
        p=expm(-0.08*laplacian(n))[0]
        for r in range(n//2):
            assert p[r]>p[r+1]-2e-16
            radial+=1
    print('PASS:', comparisons, 'independent linear-program comparisons;',
          '15 exact Taylor coefficients;', radial,'radial inequalities checked.')

if __name__=='__main__':main()
