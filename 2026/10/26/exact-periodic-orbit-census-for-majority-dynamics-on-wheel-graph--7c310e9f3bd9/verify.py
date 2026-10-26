"""Independent finite checks of the wheel-majority two-cycle formula.

Standard library only. Usage: python verify.py
The theorem for all sizes follows from the proof, not this finite test.
"""
from collections import Counter
from math import comb


def run_polynomial(length):
    out = Counter({(0, 0): 1, (length, length): 1})
    for blocks in range(1, length + 1):
        for ones in range(2 * blocks, length - blocks + 1):
            zeros = length - ones
            numerator = (length * comb(ones - blocks - 1, blocks - 1)
                         * comb(zeros - 1, blocks - 1))
            assert numerator % blocks == 0
            out[(ones, ones - blocks)] += numerator // blocks
    return out


def hub_flipping_count(n):
    q = run_polynomial(n if n % 2 else n // 2)
    if n % 2 == 0:
        out = Counter()
        for (s, e), a in q.items():
            for (t, f), b in q.items():
                out[(s+t, e+f)] += a*b
        q = out
    return sum(value for (s, e), value in q.items()
               if 2*s > n and 2*e < n)


def step(n, x, hub):
    out = 0
    for i in range(n):
        left = (x >> ((i-1) % n)) & 1
        right = (x >> ((i+1) % n)) & 1
        if left + right + hub >= 2:
            out |= 1 << i
    weight = x.bit_count()
    next_hub = hub if 2*weight == n else int(2*weight > n)
    return out, next_hub


def direct_census(n):
    fixed = 0
    stable_hub_period_two_states = 0
    switching_hub_period_two_states = 0
    for hub in (0, 1):
        for x in range(1 << n):
            y, next_hub = step(n, x, hub)
            if (y, next_hub) == (x, hub):
                fixed += 1
            elif step(n, y, next_hub) == (x, hub):
                if next_hub == hub:
                    stable_hub_period_two_states += 1
                else:
                    switching_hub_period_two_states += 1
    return fixed, stable_hub_period_two_states, switching_hub_period_two_states


def main():
    for n in range(3, 15):
        h = hub_flipping_count(n)
        actual = direct_census(n)
        expected = (2, 4 if n % 2 == 0 else 0, 2*h)
        assert actual == expected, (n, actual, expected)
        print(f"n={n:2d} switching_two_cycles={h:4d} "
              f"fixed={actual[0]} fixed_hub_two_cycles={actual[1]//2} verified")
    print('VERIFY_OK: independent exhaustive checks through n=14')


if __name__ == '__main__':
    main()
