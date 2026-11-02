#!/usr/bin/env python3
"""Reproduce coefficient identities and numerical spot-checks for a dilogarithmic
stationary current functional. This finite checker is not an asymptotic proof.
Uses only Python's standard library.
"""
from decimal import Decimal, localcontext
from math import log, exp, pi


def dilog_half(precision=110):
    with localcontext() as ctx:
        ctx.prec = precision + 15
        x = Decimal(1) / 2
        acc = Decimal(0)
        term = x
        for k in range(1, precision * 6):
            acc += term / (k * k)
            term *= x
        return +acc


def coefficients(lam, degree=240, precision=110):
    with localcontext() as ctx:
        ctx.prec = precision
        lam = Decimal(str(lam))
        L = Decimal(2).ln()
        p0 = (-lam * dilog_half(precision)).exp()
        vals = [p0]
        alt_h = Decimal(0)
        b = []
        for n in range(degree):
            if n:
                alt_h += Decimal(1 if n % 2 else -1) / n
            b.append(lam * (L - alt_h))
            vals.append(sum(b[j] * vals[n-j] for j in range(n+1)) / (n+1))
        return vals


def check():
    with localcontext() as ctx:
        ctx.prec = 110
        L = Decimal(2).ln()
        threshold = (1 - L) / L**2
        assert Decimal('0.6386739') < threshold < Decimal('0.6386740')
        for lam in ('0.2', '0.5', '1', '2', '5', '10'):
            q = coefficients(lam, degree=240)
            x = Decimal(lam)
            q0 = (-x*dilog_half()).exp()
            assert abs(q[0] - q0) < Decimal('1e-90')
            q2_formula = q0 * x * (x*L**2 + L - 1) / 2
            assert abs(q[2] - q2_formula) < Decimal('1e-90')
            assert (q[2] < 0) == (x < threshold)
            A = x * (-(x*Decimal(str(pi*pi/6)))).exp() / 2
            # Float pi is sufficient for loose independent asymptotic trend checks.
            for n in (100, 160, 240):
                assert q[n] < 0 and q[n-1] > 0, (lam,n,q[n])
                asymptotic = -A / Decimal(n*(n-1))
                ratio = q[n] / asymptotic
                assert Decimal('0.45') < ratio < Decimal('1.8'), (lam,n,ratio)
        # Independent quadrature versus a direct polylogarithm power series.
        for z in (0.0, 0.2, 0.5, 0.9):
            a = (1-z)/2
            N = 5000
            s = 0.
            for i in range(N+1):
                y = i/N
                f = -a if i == 0 else log(1-a*y)/y
                weight = 1 if i in (0,N) else (4 if i%2 else 2)
                s += weight*f
            integral = s/(3*N)
            poly = -sum(a**n / n**2 for n in range(1,110))
            assert abs(integral-poly) < 1e-10, (z,integral,poly)
        print('PASS: 6 parameter choices, coefficient recurrence through degree 240,')
        print('      second-coefficient threshold, signed tail samples, and quadrature identity.')
        print('      Finite checks do not prove eventual alternating signs or positivity failure.')

if __name__ == '__main__':
    check()
