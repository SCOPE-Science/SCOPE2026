#!/usr/bin/env python3
"""Independent finite-prime Hasse-Witt checks for the Chebyshev plane quartic.

The proof of the all-primes theorem is geometric and uses CM; this program
only verifies finite-prime instances and exact elliptic j computations.
"""
from math import comb
from fractions import Fraction


def quartic_j(a, b, c):
    I = 12*a*c + b*b
    J = 72*a*b*c - 2*b*b*b
    return Fraction(1728*4*I**3, 4*I**3-J*J)


def rank_mod(A, p):
    A = [[a % p for a in row] for row in A]
    r = 0
    for j in range(len(A[0])):
        pivot = next((k for k in range(r, len(A)) if A[k][j]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        scale = pow(A[r][j], -1, p)
        A[r] = [scale*x % p for x in A[r]]
        for k in range(len(A)):
            if k == r:
                continue
            q = A[k][j]
            A[k] = [(a-q*b) % p for a,b in zip(A[k],A[r])]
        r += 1
        if r == len(A):
            break
    return r


def hasse_witt(p):
    # Coefficient dictionary for (-x^4+4x^2-2)^m modulo p.
    powers = [{0: 1}]
    for m in range(1, p):
        out = {}
        for i,v in powers[-1].items():
            for j,w in ((0,-2),(2,4),(4,-1)):
                out[i+j] = (out.get(i+j,0)+v*w)%p
        powers.append(out)
    # Plane quartic adjoint-monomial basis (1,x,y).
    mons = ((0,0),(1,0),(0,1))
    H=[]
    for i,j in mons:
        row=[]
        for k,l in mons:
            X=p*i-k+p-1; Y=p*j-l+p-1
            if Y<0 or Y>4*(p-1) or Y%4:
                row.append(0);continue
            b=Y//4
            row.append(comb(p-1,b)*powers[p-1-b].get(X,0)%p)
        H.append(row)
    return H


def run():
    assert quartic_j(1,0,2) == 1728
    assert quartic_j(1,-4,2) == 8000
    assert quartic_j(2,0,2) == 1728
    # Two polynomial identities for the quotient maps, cleared of denominators:
    # (x^2-2)^2 - (y^4+2) = x^4-4*x^2+2-y^4;
    # x^4*((2/x^2-2)^2-2*((y/x)^4+1)) = 2*(x^4-4*x^2+2-y^4).
    for x in range(-5,6):
        for y in range(-3,4):
            f=x**4-4*x*x+2-y**4
            assert (x*x-2)**2-y**4-2==f
            assert (4-8*x*x+4*x**4-2*y**4-2*x**4)==2*f
    primes=(3,5,7,11,13,17,19,23,29,31,37,41,43,47,53)
    values={1:0,3:2,5:1,7:3}
    for p in primes:
        H=hasse_witt(p)
        a=3-rank_mod(H,p)
        expected=values[p%8]
        assert a==expected, (p,a,expected)
        print('p=%d residue=%d H=%s a=%d OK' % (p,p%8,H,a))
    print('VERIFY_OK')

if __name__=='__main__':
    run()
