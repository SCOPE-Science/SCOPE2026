#!/usr/bin/env python3
"""Reproduce finite polynomial-matrix eigenvalues and asymptotic moment checks.
No third-party dependencies.  Numerical tests supplement, not replace, the proof.
"""
from fractions import Fraction
from math import comb, sqrt, pi, factorial


def rising(x, k):
    z = Fraction(1)
    for i in range(k):
        z *= x + i
    return z


def moment_eigenvalues(n, a, b):
    c = a + b + 2
    eigen = [Fraction(1)]
    for k in range(1, n + 1):
        eigen.append(eigen[-1] * Fraction(n-k+1, 1) / (n+c+k-1))
    return eigen


def monomial_operator(n, a, b):
    c = a+b+2
    result = [[Fraction(0) for q in range(n+1)] for i in range(n+1)]
    for q in range(n+1):
        den = rising(n+c, q)
        for j in range(n+1):
            beta_moment = rising(j+a+1,q) / den
            for i in range(j,n+1):
                result[i][q] += beta_moment*comb(n,j)*comb(n-j,i-j)*((-1)**(i-j))
    return result


def spectral_sum(n,c,r):
    lam=1.0
    total=1.0
    for k in range(1,n+1):
        lam *= (n-k+1)/(n+c+k-1)
        total += lam**r
    return total


def asymptotic(n,c,r):
    first = sqrt(pi*n/r)/2
    constant = 1 - c/2
    subleading = sqrt(pi/r)/2*(r*(c-1)**2/4+c/4-1/(8*r))/sqrt(n)
    return first+constant+subleading


def main():
    exact=0
    for n in range(1,8):
        for a,b in [(Fraction(0),Fraction(0)),(Fraction(-1,2),Fraction(-1,2)),
                    (Fraction(1),Fraction(2)),(Fraction(-1,2),Fraction(3,2))]:
            mat=monomial_operator(n,a,b)
            eig=moment_eigenvalues(n,a,b)
            for q in range(n+1):
                assert mat[q][q]==eig[q], (n,a,b,q,mat[q][q],eig[q])
                for i in range(q+1,n+1):
                    assert mat[i][q]==0, (n,a,b,q,i,mat[i][q])
            exact+=1
    exact_traces=0
    for n in range(1,20):
        eigen=moment_eigenvalues(n,Fraction(0),Fraction(0))
        closed=Fraction(4**n*factorial(n)*factorial(n+1), factorial(2*n+1))
        assert sum(eigen)==closed
        exact_traces+=1
    numeric=0
    for c,r in [(1,1), (2,1), (2,2), (2,3), (3.5,2), (0.5,0.75), (8,0.5), (0.2,5)]:
        errs=[]
        for n in [200,2000,20000]:
            diff=spectral_sum(n,c,r)-asymptotic(n,c,r)
            errs.append(abs(diff))
            assert abs(diff) < 30/n, (c,r,n,diff)
            numeric+=1
        assert errs[2]<errs[0], (c,r,errs)
    print(f'PASS {exact} exact rational triangular spectral identities; {exact_traces} exact unweighted trace identities; {numeric} numerical asymptotic comparisons')

if __name__ == '__main__':
    main()
