#!/usr/bin/env python3
"""Exact integer verification of gap-block and exponent-spacing laws.

Uses direct additive dynamic programming, a separate Apéry-residue membership
criterion, and transition coefficients of the semigroup polynomial.
"""
from collections import Counter


def predicted(d, t):
    return Counter({**{ell: t * (t + 1) for ell in range(1, d)},
                    **{d * j: 1 for j in range(1, t + 1)}})


def blocks(data, desired):
    out = Counter()
    i = 0
    while i < len(data):
        if data[i] != desired:
            i += 1
            continue
        j = i
        while j < len(data) and data[j] == desired:
            j += 1
        out[j - i] += 1
        i = j
    return out


def run():
    cases = 0
    integers = 0
    gap_blocks = 0
    for d in range(2, 13):
        for t in range(2, 17):
            a = d * t + 1
            b = a + d
            assert __import__('math').gcd(a, b) == 1
            conductor = (a - 1) * (b - 1)
            in_semigroup = bytearray(conductor + 1)
            in_semigroup[0] = 1
            for n in range(1, conductor + 1):
                in_semigroup[n] = (n >= a and in_semigroup[n - a]) or (n >= b and in_semigroup[n - b])
            assert in_semigroup[conductor] == 1
            # k = d^{-1} r modulo a, since d t = a - 1.
            for n in range(conductor + 1):
                r = n % a
                k = (-t * r) % a
                assert in_semigroup[n] == (n >= k * b), (d, t, n)
            observed = blocks(in_semigroup[:conductor], 0)
            expected = predicted(d, t)
            assert observed == expected, (d, t, observed, expected)
            # For Q(x)=(1-x)*sum_{s in S} x^s, coefficients are switches.
            exponents = [0]
            for n in range(1, conductor + 1):
                if in_semigroup[n] != in_semigroup[n - 1]:
                    exponents.append(n)
            assert exponents[-1] == conductor
            exponent_spacings = Counter(v - u for u, v in zip(exponents, exponents[1:]))
            assert exponent_spacings == Counter({k: 2*v for k,v in expected.items()}), (d,t)
            assert sum(k*v for k,v in observed.items()) == conductor // 2
            assert sum(k*v for k,v in exponent_spacings.items()) == conductor
            assert len(exponents) == 2 * sum(expected.values()) + 1
            cases += 1
            integers += conductor + 1
            gap_blocks += sum(observed.values())
    # A second, direct non-DP oracle including nonminimal and repeated sums.
    naive_cases = 0
    for d in range(2, 8):
        for t in range(2, 7):
            a, b = d*t+1, d*t+d+1
            conductor = (a-1)*(b-1)
            brute = {x*a+y*b for x in range(conductor//a+1) for y in range(conductor//b+1) if x*a+y*b<=conductor}
            expected = predicted(d,t)
            assert blocks([n in brute for n in range(conductor)], False) == expected
            naive_cases+=1
    print('VERIFY_OK general_cases=%d checked_integers=%d gap_blocks=%d independent_enumeration_cases=%d exact_integer=yes' % (cases,integers,gap_blocks,naive_cases))
    for d,t in [(2,2),(3,2),(4,3)]:
        a=d*t+1; b=a+d
        print('EXAMPLE d=%d t=%d a=%d b=%d gap_block_counts=%s' % (d,t,a,b,sorted(predicted(d,t).items())))

if __name__ == '__main__':
    run()
