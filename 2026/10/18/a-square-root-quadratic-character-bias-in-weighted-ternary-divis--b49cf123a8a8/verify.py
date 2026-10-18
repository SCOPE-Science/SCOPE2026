"""Exact finite checks for the normalized ternary ordered-divisor convolution.

Run: python3 verify.py
No third-party packages are used. These checks do not prove the asymptotic.
"""
from fractions import Fraction


def least_prime_factors(n):
    spf = list(range(n + 1))
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, n + 1, p):
                if spf[m] == m:
                    spf[m] = p
    return spf


def direct_value(n, spf):
    value = Fraction(1)
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        value *= Fraction((e + 1) * (e + 2), 6)
    return value


def independent_convolution(nmax):
    # Independently enumerate c and the exact convolution 1*1_square*c.
    c = [Fraction(0) for _ in range(nmax + 1)]
    c[1] = Fraction(1)
    spf = least_prime_factors(nmax)
    for n in range(2, nmax + 1):
        m = n
        v = Fraction(1)
        while m > 1:
            p = spf[m]
            exponent = 0
            while m % p == 0:
                m //= p
                exponent += 1
            if exponent <= 2:
                v = Fraction(0)
                break
            v *= Fraction(4, 3) if exponent == 3 else Fraction(2, 3)
        c[n] = v
    result = [Fraction(0) for _ in range(nmax + 1)]
    # convolution with square indicator
    intermediate = [Fraction(0) for _ in range(nmax + 1)]
    for k in range(1, int(nmax ** 0.5) + 1):
        sq = k * k
        for m in range(1, nmax // sq + 1):
            if c[m]:
                intermediate[m * sq] += c[m]
    # convolution with constant-one function, via divisor distribution
    for d in range(1, nmax + 1):
        if intermediate[d]:
            for n in range(d, nmax + 1, d):
                result[n] += intermediate[d]
    return result, spf


def main():
    nmax = 20000
    via_convolution, spf = independent_convolution(nmax)
    s1 = Fraction(0)
    s2 = Fraction(0)
    for n in range(1, nmax + 1):
        direct = direct_value(n, spf)
        assert direct == via_convolution[n], (n, direct, via_convolution[n])
        if n % 3 == 1:
            s1 += direct
        elif n % 3 == 2:
            s2 += direct
    print("EXACT_COEFFICIENT_IDENTITIES", nmax)
    print("MOD3_DIFFERENCE", str(s1 - s2))
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
