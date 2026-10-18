#!/usr/bin/env python3
"""Exact rational independent-matrix verification of staggered averaging commutators.
Run with: python3 check.py. The proof of all depths is in RESULT.md.
"""
from fractions import Fraction
from math import cos, pi, sin, sqrt


def matrix_multiply(A, B):
    r, h, c = len(A), len(B), len(B[0]); assert len(A[0]) == h
    return [[sum(A[i][k]*B[k][j] for k in range(h)) for j in range(c)] for i in range(r)]

def direct_matrix(n, t):
    masses = [t if k % 2 == 0 else 1-t for k in range(2*n)]
    # cell 2i lies in unshifted i and shifted i-1; cell 2i+1 in both i.
    original = [k//2 for k in range(2*n)]
    shifted = [(k//2 - (k%2==0)) % n for k in range(2*n)]
    P = [[masses[j] if original[i]==original[j] else Fraction(0) for j in range(2*n)] for i in range(2*n)]
    Q = [[masses[j] if shifted[i]==shifted[j] else Fraction(0) for j in range(2*n)] for i in range(2*n)]
    PQ=matrix_multiply(P,Q); QP=matrix_multiply(Q,P)
    return [[PQ[i][j]-QP[i][j] for j in range(2*n)] for i in range(2*n)],masses

def endpoint_norm(A,masses):
    return max(sum(abs(A[i][j])*masses[i] for i in range(len(A)))/masses[j] for j in range(len(A)))

def endpoint_claim(n,t):
    return 2*max(t,1-t)*(max(t,1-t) if n>=3 else abs(2*t-1))

def check():
    tests=0
    for n in range(2,13):
        for denom in (3,4,5,7,8,11,13,17):
            for numerator in range(1,denom):
                t=Fraction(numerator,denom)
                A,masses=direct_matrix(n,t)
                direct=endpoint_norm(A,masses)
                expected=endpoint_claim(n,t)
                assert direct==expected,(n,t,direct,expected)
                # Weighted skew-adjointness of the integral kernel.
                for i in range(2*n):
                    for j in range(2*n):
                        assert masses[i]*A[i][j] == -masses[j]*A[j][i]
                tests+=1
    for n in range(2,20):
        for numerator,denom in ((1,10),(1,4),(1,2),(3,4),(9,10)):
            t=numerator/denom
            c=[abs((1-t)+t*complex(cos(2*pi*k/n),sin(2*pi*k/n))) for k in range(n)]
            mu=[sqrt(max(0,1-x*x))*x for x in c]
            formula=[2*sqrt(t*(1-t))*abs(sin(pi*k/n))*sqrt(max(0,1-4*t*(1-t)*sin(pi*k/n)**2)) for k in range(n)]
            assert max(abs(x-y) for x,y in zip(mu,formula))<1e-12
            tests+=1
    print('PASS: %d exact endpoint and Fourier consistency cases' % tests)
if __name__ == '__main__': check()
