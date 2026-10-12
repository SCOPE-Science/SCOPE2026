#!/usr/bin/env python3
"""Exact rational verification of a two-by-two sign-sketch subspace-iteration law.

No numerical tolerance and no appeal to random trials: enumerate all sign-line
sequences for short sketches, including nonsymmetric inputs, and compare with a
closed form. The universal claims for arbitrary widths and powers follow from
the separately supplied analytic proof, not these finite checks.
"""
from fractions import Fraction as F
from itertools import product


def transpose(X):
    return tuple(tuple(X[j][i] for j in range(2)) for i in range(2))


def multiply(X, Y):
    return tuple(tuple(sum(X[i][k] * Y[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def power(X, exponent):
    value = ((F(1), F(0)), (F(0), F(1)))
    for _ in range(exponent):
        value = multiply(value, X)
    return value


def matvec(X, v):
    return tuple(sum(X[i][j] * v[j] for j in range(2)) for i in range(2))


def dot(u, v):
    return sum(u[i] * v[i] for i in range(2))


def rotate(co, si):
    assert co*co + si*si == 1
    return ((co, -si), (si, co))


def from_svd(a, b, left, right):
    """Build U diag(a,b) V^T for arbitrary rational orthogonal U,V."""
    U, V = rotate(*left), rotate(*right)
    return multiply(multiply(U, ((a, F(0)), (F(0), b))), transpose(V))


def exact_enumeration(A, a, b, q, ell):
    AAT = multiply(A, transpose(A))
    Y_operator = multiply(power(AAT, q), A)
    # Two equiprobable projective sign lines represent the four sign vectors.
    lines = ((F(1), F(1)), (F(1), F(-1)))
    total = F(0)
    for labels in product((0, 1), repeat=ell):
        if 0 in labels and 1 in labels:
            squared_error = b*b  # Y full rank: truncated SVD is optimal.
        else:
            y = matvec(Y_operator, lines[labels[0]])
            squared_error = a*a+b*b-dot(y, matvec(AAT,y))/dot(y,y)
        total += squared_error
    return total/F(2**ell)


def formula(a, b, c, q, ell):
    rho = (b/a)**(4*q+2)
    H = rho*((1-c)/(c+rho*(1-c)) + c/(1-c+rho*c))
    return b*b+(a*a-b*b)*H/F(2**ell)


def run():
    tested = 0
    angles = [(F(1),F(0)), (F(3,5),F(4,5)), (F(5,13),F(12,13))]
    for a,b in [(F(3),F(1)), (F(5),F(2))]:
        for left in angles:
            for right in angles:
                A=from_svd(a,b,left,right)
                c=(right[0]+right[1])**2/2
                for q in range(4):
                    for ell in range(1,6):
                        risk=exact_enumeration(A,a,b,q,ell)
                        predicted=formula(a,b,c,q,ell)
                        assert risk==predicted, (a,b,left,right,q,ell,risk,predicted)
                        rho=(b/a)**(4*q+2)
                        low=b*b+(a*a-b*b)*2*rho/(1+rho)/F(2**ell)
                        high=b*b+(a*a-b*b)/F(2**ell)
                        assert low<=risk<=high
                        if c==F(1,2):
                            assert risk==low
                        tested+=1
        # Singular right frame aligned with sign vectors (Hadamard basis).
        A=(((a+b)/2, (a-b)/2), ((a-b)/2, (a+b)/2))
        for q in range(5):
            for ell in range(1,6):
                risk=exact_enumeration(A,a,b,q,ell)
                assert risk == b*b+(a*a-b*b)/F(2**ell)
                tested+=1
    print('Verified',tested,'exact-rational identities and inequality cases.')

if __name__=='__main__':
    run()
