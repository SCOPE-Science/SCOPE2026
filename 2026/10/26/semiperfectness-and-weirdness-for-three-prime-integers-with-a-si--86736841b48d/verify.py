"""Independent finite checks for a classification of semiperfect integers.

The infinite classification follows from the proof, not these bounded checks.
Run: python3 verify.py
"""
from math import isqrt

SEEDS = {350: (2, 7, 10, 25), 490: (1, 10, 35),
         550: (1, 5, 10), 650: (2,)}


def divisors(n):
    low, high = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
    return low + high[::-1]


def semiperfect(n):
    bits = 1
    mask = (1 << (n + 1)) - 1
    for d in divisors(n)[:-1]:
        bits = (bits | (bits << d)) & mask
    return bool(bits & (1 << n))


def sigma(n):
    return sum(divisors(n))


def primes_to(limit):
    return [n for n in range(3, limit + 1, 2)
            if all(n % d for d in range(3, isqrt(n) + 1, 2))]


def predicted(p, q, a, b):
    return p == 3 or (p == 5 and
                      ((q == 7 and (a >= 2 or b >= 2))
                       or (q in (11, 13) and a >= 2)))


def main():
    for n, excluded in SEEDS.items():
        proper = divisors(n)[:-1]
        assert len(set(excluded)) == len(excluded)
        assert all(d in proper for d in excluded)
        assert sum(excluded) == sigma(n) - 2 * n
        assert sigma(n) - n - sum(excluded) == n
        assert semiperfect(n)
        assert all(not semiperfect(d) for d in proper)

    assert sigma(70) > 140 and not semiperfect(70)
    assert sigma(110) < 220 and sigma(130) < 260

    tested = 0
    weird = []
    primes = primes_to(97)
    for i, p in enumerate(primes):
        for q in primes[i + 1:]:
            pa, a = p, 1
            while 2 * pa * q <= 20000:
                qb, b = q, 1
                while 2 * pa * qb <= 20000:
                    n = 2 * pa * qb
                    truth = semiperfect(n)
                    expect = predicted(p, q, a, b)
                    assert truth == expect, (n, p, q, a, b, truth, expect)
                    if sigma(n) > 2 * n and not truth:
                        weird.append(n)
                    tested += 1
                    qb *= q
                    b += 1
                pa *= p
                a += 1
    assert weird == [70], weird
    print('VERIFY_OK: four exact divisor-complement certificates;'
          ' four primitive seeds; %d independent finite semiperfect cases;'
          ' unique weird instance 70 below 20000.' % tested)


if __name__ == '__main__':
    main()
