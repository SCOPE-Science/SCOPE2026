#!/usr/bin/env python3
"""Direct reduced Laplacian Smith forms for multi-crown graphs.
Independent of the proof's presentation reduction. Requires sympy.
"""
from math import gcd
from sympy import ZZ, zeros
from sympy.matrices.normalforms import smith_normal_form


def crown_laplacian(n, k):
    N = 2*n
    L = zeros(N)
    for i in range(n):
        for j in range(n):
            w = k if i == j else 1
            L[i,i] += w
            L[n+j,n+j] += w
            L[i,n+j] -= w
            L[n+j,i] -= w
    return L


def invariants_of_direct_sum(cyclic_orders):
    # Assemble canonical invariant factors using a diagonal presentation.
    d = smith_normal_form(__import__('sympy').diag(*cyclic_orders), domain=ZZ)
    return sorted([abs(int(d[i,i])) for i in range(d.rows) if abs(int(d[i,i])) != 1])


def main():
    tests = 0
    for n in range(3,13):
        for k in range(0,9):
            lap = crown_laplacian(n,k)
            red = lap[:2*n-1,:2*n-1]
            diag = smith_normal_form(red,domain=ZZ)
            actual = sorted([abs(int(diag[i,i])) for i in range(diag.rows) if abs(int(diag[i,i])) != 1])
            g = gcd(n,k-1)
            h = n*(n-2+2*k)//g
            t = (n-1+k)*(n-2+2*k)
            expected = invariants_of_direct_sum([g,h]*(n-2)+[t])
            assert actual == expected, (n,k,actual,expected)
            assert all(int(sum(lap.row(i))) == 0 for i in range(lap.rows))
            tests += 1
    print('SMITH_FORM_ALL_PASS', tests, 'cases n=3..12 k=0..8')
    for n,k in [(4,3),(6,3),(8,3),(10,3)]:
        d = smith_normal_form(crown_laplacian(n,k)[:2*n-1,:2*n-1],domain=ZZ)
        v = [abs(int(d[i,i])) for i in range(d.rows) if abs(int(d[i,i]))>1]
        print('EXAMPLE',n,k,v)

if __name__=='__main__':main()
