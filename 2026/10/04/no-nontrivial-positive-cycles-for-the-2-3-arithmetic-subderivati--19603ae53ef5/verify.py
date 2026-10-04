#!/usr/bin/env python3
from math import gcd

BOUND = 200
NMAX = 200000
COEFFS = [1, 5, 7, 11, 13, 17]

def vp(n, p):
    a = 0
    while n and n % p == 0:
        n //= p
        a += 1
    return a

def D23(n):
    if n == 0:
        return 0
    a = vp(n, 2)
    b = vp(n, 3)
    return n * (3 * a + 2 * b) // 6

def split23(m):
    r = s = 0
    while m % 2 == 0:
        r += 1
        m //= 2
    while m % 3 == 0:
        s += 1
        m //= 3
    return r, s, m

def transition(a, b):
    m = 3 * a + 2 * b
    if m == 0:
        return None
    r, s, u = split23(m)
    return a - 1 + r, b - 1 + s, u

def main():
    # Direct algebra-vs-integer transition checks.
    checked = 0
    for a in range(BOUND + 1):
        for b in range(BOUND + 1):
            if a == 0 and b == 0:
                continue
            ap, bp, u = transition(a, b)
            assert ap >= 0 and bp >= 0
            for c in COEFFS:
                assert gcd(c, 6) == 1
                n = c * (2 ** a) * (3 ** b)
                y = D23(n)
                expected = c * u * (2 ** ap) * (3 ** bp)
                assert y == expected, (a, b, c, y, expected)
            checked += 1

    # Finite graph regression: any closed trajectory contained in the box
    # and returning the coprime multiplier must be one of the two fixed states.
    closed = set()
    for a0 in range(BOUND + 1):
        for b0 in range(BOUND + 1):
            if a0 == 0 and b0 == 0:
                continue
            a, b = a0, b0
            mult = 1
            seen = {}
            for step in range(1000):
                state = (a, b, mult)
                if state in seen:
                    if state == (a0, b0, 1):
                        closed.add((a0, b0))
                    break
                seen[state] = step
                t = transition(a, b)
                if t is None:
                    break
                a, b, u = t
                mult *= u
                if a < 0 or b < 0 or a > BOUND or b > BOUND or mult > 10**12:
                    break
    assert closed == {(2, 0), (0, 3)}, closed

    # Direct fixed-point regression.
    fixed = []
    for n in range(1, NMAX + 1):
        got = (D23(n) == n)
        m = n
        while m % 2 == 0:
            m //= 2
        while m % 3 == 0:
            m //= 3
        expect = ((vp(n, 2), vp(n, 3)) in {(2, 0), (0, 3)})
        assert got == expect, n
        if got:
            fixed.append(n)

    # Low-m obstruction used in the proof.
    low = {}
    for a in range(6):
        for b in range(6):
            m = 3*a + 2*b
            if 0 < m < 6:
                low.setdefault(m, []).append((a,b))
    assert low == {2:[(0,1)], 3:[(1,0)], 4:[(0,2)], 5:[(1,1)]}

    print('VERIFY_OK')
    print('transition_pairs_checked=' + str(checked))
    print('finite_closed_states=' + repr(sorted(closed)))
    print('fixed_point_direct_bound=' + str(NMAX))
    print('fixed_points_count_through_bound=' + str(len(fixed)))

if __name__ == '__main__':
    main()
