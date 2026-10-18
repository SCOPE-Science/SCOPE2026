#!/usr/bin/env python3
"""Finite checks for four row-order policies on paired two-dimensional projections.

Requires Python 3.9+ standard library only.  It verifies finite formulas,
not the infinite-dimensional Laplace asymptotics proved analytically.
"""
from fractions import Fraction
from itertools import product
from math import gamma, sqrt


def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in (0, 1))
                       for j in (0, 1)) for i in (0, 1))


def trace_square(A):
    return sum(A[i][j] ** 2 for i in (0, 1) for j in (0, 1))


def pair_projection_test(c, epochs):
    # Unit source rows: (1,0), (c,sqrt(1-c*c)).  For c=3/5,
    # all entries of the two residual projectors are rational.
    if c != Fraction(3, 5):
        raise ValueError('Only c=3/5 needed for exact arithmetic')
    P = (((Fraction(0), Fraction(0)), (Fraction(0), Fraction(1))),
         ((Fraction(16, 25), Fraction(-12, 25)),
          (Fraction(-12, 25), Fraction(9, 25))))
    I = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))

    def outcome(indices):
        A = I
        for i in indices:
            A = matmul(P[i], A)
        return trace_square(A) / 2

    orders = ((0, 1), (1, 0))
    ss = sum((outcome(o * epochs) for o in orders), Fraction(0)) / 2
    rr = sum((outcome(sum(choices, ())) for choices in product(orders, repeat=epochs)),
             Fraction(0)) / (2 ** epochs)
    ff = sum((outcome(sum((o if t % 2 == 0 else o[::-1] for t in range(epochs)), ()))
              for o in orders), Fraction(0)) / 2
    iid = sum((outcome(indices) for indices in product((0, 1), repeat=2 * epochs)),
              Fraction(0)) / (2 ** (2 * epochs))

    h = (1 + c * c) / 2
    proposed = (c ** (4 * epochs - 2) / 2,
                c ** (2 * epochs) * h ** (epochs - 1) / 2,
                c ** (2 * epochs) / 2,
                h ** (2 * epochs - 1) / 2)
    actual = (ss, rr, ff, iid)
    assert actual == proposed, (epochs, actual, proposed)
    return len(orders) + 2 ** epochs + len(orders) + 2 ** (2 * epochs)


def finite_losses(c, n):
    s = len(c)
    h = [(1 + z*z)/2 for z in c]
    miss = (1 - 1/s)**(2*s*n)
    ss = sum(z**(4*n - 2) for z in c) / (2*s)
    rr = sum(z**(2*n) * h0**(n - 1) for z, h0 in zip(c, h)) / (2*s)
    ff = sum(z**(2*n) for z in c) / (2*s)
    iid = sum(2*miss + ((1 - (1-h0)/s)**(2*s*n)-miss)/h0
              for h0 in h) / (2*s)
    return ss, rr, ff, iid


def powerlaw_losses(beta, s, n):
    # Spectral construction: low eigenvalues lambda_j=(j/s)^(1/beta),
    # and high eigenvalues 2-lambda_j; row overlap c_j=1-lambda_j.
    return finite_losses([1-(j/s)**(1/beta) for j in range(1, s+1)], n)


def run():
    exact_cases = sum(pair_projection_test(Fraction(3,5), n) for n in (1,2,3,4))
    assert exact_cases == sum(4 + 2**n + 2**(2*n) for n in (1,2,3,4))
    checked = 0
    for s in (2,3,7,19):
        for n in (1,2,5,10):
            c = [((j*17+3) % 97)/97 for j in range(s)]
            ss,rr,ff,iid=finite_losses(c,n)
            assert -1e-13 <= ss <= rr+1e-13 <= ff+2e-13 <= iid+3e-13
            checked += 1
    for beta,s,n in ((0.5,100000,100),(1.0,100000,100),(2.0,1000000,80)):
        vals=powerlaw_losses(beta,s,n)
        constants=[gamma(beta+1)/(2*(k*n)**beta) for k in (4,3,2,2)]
        for value,limit in zip(vals,constants):
            assert abs(value/limit-1) < 0.15, (beta,n,value,limit)
            checked += 1
    print('PASS: exact enumeration paths',exact_cases,
          '; finite ordering cases',16,
          '; power-law leading-constant comparisons',12,
          '; total checks',exact_cases+checked)
    for beta in (0.5,1.,2.):
        s=100000 if beta<2 else 1000000
        n=80
        ss,rr,ff,iid=powerlaw_losses(beta,s,n)
        print('beta=',beta,'dimension=',2*s,'epochs=',n,
              'RR/SS=',round(rr/ss,6),
              'FF/RR=',round(ff/rr,6),
              'IID/SS=',round(iid/ss,6),
              'limits=',round((4/3)**beta,6),round((3/2)**beta,6),round(2**beta,6))


if __name__=='__main__':
    run()
