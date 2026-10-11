"""Finite-degree computational checks for an elliptic Taylor sign transition.

Only supplementary tests: the asymptotic theorem uses analytic contour estimates.
Uses Python's standard-library Decimal arithmetic (no external dependencies).
"""
from decimal import Decimal, getcontext

getcontext().prec = 75
ONE = Decimal(1)
FOUR = Decimal(4)
P0 = FOUR.ln()


def normalized_coefficients(p, order, differentiate=False):
    """Taylor coefficients of (2/pi) K(sqrt(z))/(p - log(1-z)/2)."""
    p = Decimal(p)
    coeff = [ONE]
    for n in range(1, order + 1):
        coeff.append(coeff[-1] * Decimal((2*n-1)**2) / Decimal(4*n*n))
    a = [ONE/p]
    deriv = [-ONE/(p*p)]
    for n in range(1, order+1):
        conv = sum(a[n-j]/Decimal(2*j) for j in range(1, n+1))
        a.append((coeff[n]-conv)/p)
        if differentiate:
            dconv = sum(deriv[n-j]/Decimal(2*j) for j in range(1, n+1))
            deriv.append(-a[n]/p - dconv/p)
    return (a[-1], deriv[-1]) if differentiate else a[-1]


def nearest_root(n):
    p = P0 + ONE / Decimal(4*n)
    for _ in range(8):
        f, df = normalized_coefficients(p, n, True)
        assert df > 0
        p -= f/df
    f, df = normalized_coefficients(p, n, True)
    assert abs(f) < Decimal('1e-60')
    assert P0 < p < P0 + Decimal('0.1')
    return p


def main():
    # Exact symbolic recurrence spot checks in arbitrary-precision decimals.
    p = P0
    a1 = normalized_coefficients(p, 1)
    a2 = normalized_coefficients(p, 2)
    a3 = normalized_coefficients(p, 3)
    assert abs(a1-(p-2)/(4*p*p)) < Decimal('1e-60')
    assert abs(a2-(3*p-4)**2/(64*p**3)) < Decimal('1e-60')
    assert abs(a3-(75*p**3-230*p*p+240*p-96)/(768*p**4)) < Decimal('1e-60')

    for n in (30, 60, 120, 240):
        a, ap = normalized_coefficients(P0, n, True)
        assert a < 0 and ap > 0
        assert normalized_coefficients(P0+Decimal('0.1'), n) > 0
        root = nearest_root(n)
        k = Decimal(n)*(root-P0)
        print('degree', n, 'n*(p_root-log4) =', f'{k:.14f}')
        # The correction approaches 1/4 only logarithmically.
        assert Decimal('0.25') < k < Decimal('0.35')
    print('All recurrence, derivative, and root checks passed.')

if __name__ == '__main__':
    main()
