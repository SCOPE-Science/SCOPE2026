#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import isqrt

U_UPPER = Fraction(922616583105498918071628209679061634159251672167426749996626, 10**60)
F0 = Fraction(1, 200)
F_LEFT = Fraction(199, 40000)
F_RIGHT = Fraction(201, 40000)
DELTA_BAR = Fraction(178, 10**6)
LOG_TERMS = 180
SQRT_BITS = 256


def gate(ok, msg):
    if not ok:
        raise RuntimeError(msg)


def sqrt_enclosure(x, bits=SQRT_BITS):
    x = Fraction(x)
    gate(x >= 0, 'negative square-root argument')
    if x == 0:
        return Fraction(0), Fraction(0)
    scale = 1 << bits
    n = x.numerator * scale * scale // x.denominator
    r = isqrt(n)
    while (r + 1) ** 2 * x.denominator <= x.numerator * scale * scale:
        r += 1
    while r ** 2 * x.denominator > x.numerator * scale * scale:
        r -= 1
    lo = Fraction(r, scale)
    hi = lo if lo * lo == x else Fraction(r + 1, scale)
    gate(lo * lo <= x <= hi * hi, 'bad square-root enclosure')
    return lo, hi


@lru_cache(maxsize=None)
def ln_unit(x):
    x = Fraction(x)
    gate(Fraction(1) <= x <= Fraction(2), 'log range reduction failed')
    z = (x - 1) / (x + 1)
    z2 = z * z
    p = z
    s = Fraction(0)
    for k in range(LOG_TERMS):
        s += p / (2 * k + 1)
        p *= z2
    rem = p / ((2 * LOG_TERMS + 1) * (1 - z2))
    return 2 * s, 2 * (s + rem)


LN2_LO, LN2_HI = ln_unit(Fraction(2))


@lru_cache(maxsize=None)
def log2_enclosure(x):
    x = Fraction(x)
    gate(x > 0, 'nonpositive logarithm')
    y = x
    e = 0
    while y < 1:
        y *= 2
        e -= 1
    while y >= 2:
        y /= 2
        e += 1
    lo, hi = ln_unit(y)
    return Fraction(e) + lo / LN2_HI, Fraction(e) + hi / LN2_LO


@lru_cache(maxsize=None)
def entropy_term(x):
    x = Fraction(x)
    gate(Fraction(0) <= x <= Fraction(1), 'probability outside unit interval')
    if x == 0:
        return Fraction(0), Fraction(0)
    lo, hi = log2_enclosure(x)
    return -x * hi, -x * lo


def binary_entropy(x):
    a = entropy_term(x)
    b = entropy_term(1 - x)
    return a[0] + b[0], a[1] + b[1]


def werner_entropy(f):
    a = entropy_term(f)
    b = entropy_term((1 - f) / 3)
    return a[0] + 3 * b[0], a[1] + 3 * b[1]


def purified_distance_upper(f):
    a_lo, _ = sqrt_enclosure(f * F0)
    b_lo, _ = sqrt_enclosure((1 - f) * (1 - F0))
    fidelity_lo = a_lo + b_lo
    q_hi = 1 - fidelity_lo * fidelity_lo
    gate(q_hi >= 0, 'negative distance-square enclosure')
    _, d_hi = sqrt_enclosure(q_hi)
    return d_hi


def main():
    gate(F_LEFT < F0 < F_RIGHT, 'interval does not surround source point')
    gate(F0 - F_LEFT == Fraction(1, 40000), 'left radius changed')
    gate(F_RIGHT - F0 == Fraction(1, 40000), 'right radius changed')

    d_left = purified_distance_upper(F_LEFT)
    d_right = purified_distance_upper(F_RIGHT)
    gate(d_left < DELTA_BAR and d_right < DELTA_BAR, 'purified-distance cap failed')

    # For Werner states the root fidelity with F0 has derivative positive below F0
    # and negative above F0, so purified distance is maximized at an interval endpoint.
    # The two exact endpoint enclosures above therefore certify DELTA_BAR uniformly.

    hbar_hi = binary_entropy(DELTA_BAR)[1]
    log7_hi = log2_enclosure(Fraction(7))[1]
    gbar_hi = DELTA_BAR * log7_hi + hbar_hi
    gate(gbar_hi < Fraction(297363, 10**8), 'continuity penalty threshold failed')

    s0_lo, s0_hi = werner_entropy(Fraction(0))
    s1_lo, s1_hi = werner_entropy(Fraction(1, 100))
    sf_lo, sf_hi = werner_entropy(F_LEFT)
    t = 100 * F_LEFT
    upper_left = sf_hi + (1 - t) * (1 - s0_lo) + t * (U_UPPER - s1_lo)
    gate(upper_left < Fraction(966531, 10**6), 'regularized upper threshold failed')

    # U(f) is decreasing on the interval. Its derivative is
    # log2((1-f)/(3f)) + 100*(U_UPPER-S(W(.01))-1+S(W(0))).
    # The logarithmic term decreases with f, so it suffices to bound the derivative at F_LEFT.
    ratio = (1 - F_LEFT) / (3 * F_LEFT)
    derivative_hi = log2_enclosure(ratio)[1] + 100 * (U_UPPER - s1_lo - 1 + s0_hi)
    gate(derivative_hi < -8, 'monotonicity certificate failed')

    ep_lower = Fraction(97, 100) - Fraction(297363, 10**8)
    einf_upper = Fraction(966531, 10**6)
    gap_lower = ep_lower - einf_upper
    gate(ep_lower == Fraction(96702637, 10**8), 'one-copy threshold changed')
    gate(gap_lower == Fraction(49537, 10**8), 'gap threshold changed')
    gate(gap_lower > 0, 'strict gap lost')

    print('VERIFY_OK')
    print('interval 199/40000 201/40000')
    print('uniform_purified_distance_lt 178/1000000')
    print('continuity_penalty_lt 297363/100000000')
    print('one_copy_EP_gt 96702637/100000000')
    print('regularized_EP_lt 966531/1000000')
    print('uniform_gap_gt 49537/100000000')
    print('upper_derivative_lt -8')


if __name__ == '__main__':
    main()
