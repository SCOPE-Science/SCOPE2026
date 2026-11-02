#!/usr/bin/env python3
"""Exact finite-size checks for the triangular-rung antiferromagnetic Ising tube."""
from itertools import product

STATES = range(8)

def rung_bad(s):
    return sum(((s >> i) & 1) == ((s >> ((i + 1) % 3)) & 1) for i in range(3))

def leg_bad(a, b):
    return sum(((a >> i) & 1) == ((b >> i) & 1) for i in range(3))

def mag(s):
    return 2 * s.bit_count() - 3

def energy(columns, field):
    n = len(columns)
    bad = sum(rung_bad(s) + leg_bad(s, columns[(j + 1) % n]) for j, s in enumerate(columns))
    return 2 * bad - 6 * n - field * sum(map(mag, columns))

def exhaustive(n, field):
    best = None
    count = 0
    for columns in product(STATES, repeat=n):
        val = energy(columns, field)
        if best is None or val < best:
            best, count = val, 1
        elif val == best:
            count += 1
    return best, count

def transfer(n, field):
    minimum = None
    multiplicity = 0
    for start in STATES:
        states = {start: (rung_bad(start) - field * mag(start), 1)}
        for _ in range(1, n):
            updated = {}
            for last, (val, count) in states.items():
                for nxt in STATES:
                    candidate = val + 2 * leg_bad(last, nxt) + 2 * rung_bad(nxt) - field * mag(nxt)
                    if nxt not in updated or candidate < updated[nxt][0]:
                        updated[nxt] = (candidate, count)
                    elif candidate == updated[nxt][0]:
                        updated[nxt] = (candidate, updated[nxt][1] + count)
            states = updated
        for last, (val, count) in states.items():
            candidate = val + 2 * leg_bad(last, start) - 6 * n + rung_bad(start)
            if minimum is None or candidate < minimum:
                minimum, multiplicity = candidate, count
            elif candidate == minimum:
                multiplicity += count
    return minimum, multiplicity

def power_sum(n, a):
    # Characteristic roots of t^2 - a t - 1.
    x, y = 2, a
    for _ in range(n):
        x, y = y, a * y + x
    return x

def predicted(n, field):
    if field == 0:
        return (-4*n, 6) if n % 2 == 0 else (-4*n + 6, 2*n*(n*n+3*n-1))
    if field == 1:
        return (-4*n, 6) if n % 2 == 0 else (-4*n+3, n*(n*n-1)//4)
    if field == 2:
        return -4*n, power_sum(n, 2) + 2*power_sum(n, -1)
    if field == 3:
        return -5*n, 2**n+2*(-1)**n
    if field == 4:
        return -6*n, power_sum(n, 3) + 2*(-1)**n
    if field == 5:
        return -9*n, 1
    raise ValueError(field)

def main():
    checks = 0
    for n in range(3, 31):
        for h in range(6):
            got = transfer(n, h)
            want = predicted(n, h)
            assert got == want, (n, h, got, want)
            checks += 1
    brute = 0
    for n in range(3, 7):
        for h in range(6):
            assert exhaustive(n, h) == predicted(n, h), (n,h)
            brute += 1
    print(f"PASS: {checks} exact transfer-matrix energy/multiplicity cases (lengths 3..30, fields 0..5).")
    print(f"PASS: {brute} independent full-spin-enumeration cases (lengths 3..6, fields 0..5).")
    print('n    G(0)   G(0<h<2)   G(2)   G(2<h<4)   G(4)')
    for n in (3,4,5,6,7,8,9,10):
        print(f"{n:<4} {predicted(n,0)[1]:<6} {predicted(n,1)[1]:<10} {predicted(n,2)[1]:<6} {predicted(n,3)[1]:<10} {predicted(n,4)[1]}")

if __name__ == '__main__':
    main()
