"""Numerical consistency checks for the stated EOS asymptotic formulas.

Uses only the Python standard library. These finite checks do not prove the asymptotic theorem.
Run: python3 check_eos.py
"""
from decimal import Decimal, localcontext
from math import gcd

CASES = [(2, 1), (3, 1), (5, 2), (7, 3), (11, 4)]


def verify_case(n, k):
    assert n >= 2 and 1 <= k < n and gcd(k, n) == 1
    with localcontext() as ctx:
        ctx.prec = 85
        A = Decimal(24 * n)
        B = Decimal(k) / Decimal(n)
        EPS = (-A / Decimal(2 * n)).exp()
        J = list(range(k - n, k))
        tau = {j: j + k if j < 0 else j + k - n for j in J}
        assert len(set(tau.values())) == n
        s = {-1: Decimal('0.5')}
        j = -1
        for _ in range(n - 1):
            sj = s[j] + (Decimal(1) if j == 0 else (-Decimal(1) if j == -1 else Decimal(0)))
            j = tau[j]
            assert j not in s
            s[j] = sj
        assert set(s) == set(J) and s[0] == Decimal('-0.5')
        assert all(v in [Decimal('0.5'), Decimal('-0.5')] for v in s.values())

        def g(x):
            return Decimal(1) / (Decimal(1) + (-A * x).exp())

        def iterate(x):
            xx = x
            der = Decimal(1)
            for _ in range(n):
                v = g(xx)
                der *= 1 - A * v * (1 - v)
                xx = xx + B - v
            return xx, der

        x0 = Decimal(1) / Decimal(2 * n) - EPS / 2
        for _ in range(15):
            end, deriv = iterate(x0)
            step = (end - x0) / (deriv - 1)
            x0 -= step
            if abs(step) < Decimal('1e-70'):
                break
        end, lam = iterate(x0)
        assert abs(end - x0) < Decimal('1e-65')
        assert 0 < lam < 1
        x = x0
        pts = {}
        for _ in range(n):
            j = int((Decimal(n) * x).to_integral_value(rounding='ROUND_FLOOR'))
            assert j in J and j not in pts
            pts[j] = x
            x = x + B - g(x)
        assert set(pts) == set(J)
        assert abs(x - x0) < Decimal('1e-65')
        err_profile = max(abs((pts[j] - (Decimal(j) + Decimal('0.5')) / Decimal(n)) / EPS - s[j]) for j in J)
        err_mult = abs((1 - lam) / (2 * A * EPS) - 1)
        assert err_profile < Decimal('0.001')
        assert err_mult < Decimal('0.0001')
        print('PASS', n, k, 'profile_err', float(err_profile), 'multiplier_ratio_err', float(err_mult))


if __name__ == '__main__':
    for nk in CASES:
        verify_case(*nk)
    print('PASS: 5 high-precision periodic-orbit cases')
