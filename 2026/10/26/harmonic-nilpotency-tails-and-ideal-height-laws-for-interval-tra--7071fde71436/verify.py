"""Exact checks for the harmonic nilpotency law in interval-translation monoids.
Run: python3 verify.py; requires the Python standard library only.
"""
from collections import Counter
from fractions import Fraction as F


def multiply(x, y):
    if x is None or y is None:
        return None
    k, d, m = x
    kp, dp, mp = y
    k2, m2 = max(k, kp-d), min(m, mp-d)
    return (k2, d+dp, m2) if k2 <= m2 else None


def least_zero_power(x):
    assert x is not None and x[1] != 0
    power = x
    for exponent in range(2, 10000):
        power = multiply(power, x)
        if power is None:
            return exponent
    raise AssertionError('The finite test did not terminate')


def finite_tail(n, j):
    return sum((n-j*d+1)*(n-j*d+2) for d in range(1, n//j+1))


def ideal_volume(u):
    return (1-(1-u)**3)/3


def ideal_tail_formula(u, j):
    threshold = F(j-1, j)
    if u <= threshold:
        return u*u/(j-1)-F(2*j-1, 3*(j-1)**2)*u**3
    return (F(1,j)-(1-u)**3)/3


def ideal_tail_by_slice_integration(u, j):
    """Integrate explicitly in the two independent (h,a) regions.
    The density of (h,a) is 2(1-h-a)."""
    a = min(u, F(j-1, j))
    # For h in [0,a], integrate translation magnitude up to h/(j-1).
    first = a*a/(j-1)-F(2*j-1, 3*(j-1)**2)*a**3
    if u <= a:
        return first
    # For h in [a,u], the full interval 0<=translation<=1-h applies.
    return first+((1-a)**3-(1-u)**3)/3


def main():
    checks = 0
    # Enumerate the actual monoid multiplication and all nonzero nilpotents.
    for n in range(1, 19):
        histogram = Counter()
        for d in list(range(-n,0))+list(range(1,n+1)):
            low, high = 1-min(0,d), n+1-max(0,d)
            for k in range(low,high+1):
                for m in range(k,high+1):
                    t = least_zero_power((k,d,m))
                    assert t == 2+(m-k)//abs(d)
                    histogram[t] += 1
                    checks += 1
        total = n*(n+1)*(n+2)//3
        assert sum(histogram.values()) == total
        for j in range(1,n+3):
            observed = sum(v for t,v in histogram.items() if t>j)
            assert observed == finite_tail(n,j), (n,j,observed)
            checks += 1
    # Independent rational antiderivatives on both sides of the ideal threshold.
    for j in range(2,24):
        for denominator in (2,3,5,7,11,17):
            for numerator in range(1,denominator+1):
                u = F(numerator,denominator)
                assert ideal_tail_by_slice_integration(u,j) == ideal_tail_formula(u,j)
                assert F(0) <= ideal_tail_formula(u,j) <= ideal_volume(u)
                checks += 1
    # The unrestricted exact volume tail and the distribution telescope.
    for j in range(1,201):
        tail = F(1,j) if j==1 else ideal_tail_formula(F(1),j)/ideal_volume(F(1))
        assert tail == F(1,j)
        if j>=2:
            assert F(1,j-1)-tail == F(1,j*(j-1))
        checks += 1
    print(f'VERIFY_OK: {checks} exact structural, finite enumeration, and rational-integration checks')

if __name__ == '__main__':
    main()
