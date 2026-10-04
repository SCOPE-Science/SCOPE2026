from fractions import Fraction
from math import isqrt

DIGITS = 70
SCALE = 10 ** DIGITS


def sqrt_bounds(x):
    """Exact rational bounds lo <= sqrt(x) <= hi for nonnegative Fraction x."""
    assert isinstance(x, Fraction) and x >= 0
    num = x.numerator * SCALE * SCALE
    den = x.denominator
    a = isqrt(num // den)
    lo = Fraction(a, SCALE)
    if a * a * den == x.numerator * SCALE * SCALE:
        hi = lo
    else:
        hi = Fraction(a + 1, SCALE)
    assert lo * lo <= x <= hi * hi
    return lo, hi


def F_interval(Omega, lo, hi):
    """Outward interval for F_Omega(rho), using monotonicity in rho."""
    assert lo <= hi
    assert Omega * lo >= 1

    def lower_at(rho):
        D = rho * rho + Omega * rho * (1 - rho * rho)
        _, root_hi = sqrt_bounds(D)
        return (Omega * rho - root_hi) / (Omega + rho)

    def upper_at(rho):
        D = rho * rho + Omega * rho * (1 - rho * rho)
        root_lo, _ = sqrt_bounds(D)
        return (Omega * rho - root_lo) / (Omega + rho)

    out_lo = lower_at(lo)
    out_hi = upper_at(hi)
    assert out_lo <= out_hi
    return out_lo, out_hi


def certify_small_horizon(N):
    Omega = Fraction((N + 2) ** 2, 8)
    cutoff = Fraction(1, 1) / Omega
    lo = hi = Fraction(1, 1)
    for k in range(N + 1):
        if hi < cutoff:
            return k
        assert lo >= cutoff, (N, k, lo, hi, cutoff)
        lo, hi = F_interval(Omega, lo, hi)
    raise AssertionError((N, 'no certified shooting crossing'))


def certify_varpi_upper():
    # varpi/2 = integral_0^1 1/sqrt((1-x) S(x)) dx,
    # S(x)=1+x+x^2+x^3.  On [a,b], S(x)>=S(a).
    total = Fraction(0, 1)
    for j in range(16):
        a = Fraction(j, 16)
        b = Fraction(j + 1, 16)
        S = 1 + a + a * a + a * a * a
        _, sqrt1a_hi = sqrt_bounds(1 - a)
        sqrt1b_lo, _ = sqrt_bounds(1 - b)
        sqrtS_lo, _ = sqrt_bounds(S)
        total += (sqrt1a_hi - sqrt1b_lo) / sqrtS_lo
    varpi_upper = 4 * total
    assert varpi_upper < Fraction(27, 10)
    return varpi_upper


def certify_tail():
    # For N=21+m: 800(N+1)^2 - 729(N+2)^2
    # = 71 m^2 + 1666 m + 1559 > 0 for every integer m>=0.
    assert 1559 > 0 and 1666 > 0 and 71 > 0
    # Spot-check the symbolic expansion at several exact integers.
    for m in (0, 1, 2, 17, 100):
        N = 21 + m
        lhs = 800 * (N + 1) ** 2 - 729 * (N + 2) ** 2
        rhs = 71 * m * m + 1666 * m + 1559
        assert lhs == rhs and rhs > 0


upper = certify_varpi_upper()
triggers = {}
for N in range(2, 21, 2):
    triggers[N] = certify_small_horizon(N)
certify_tail()

assert triggers == {2: 1, 4: 3, 6: 4, 8: 6, 10: 8, 12: 9, 14: 11, 16: 13, 18: 14, 20: 16}
print('VERIFY_OK')
