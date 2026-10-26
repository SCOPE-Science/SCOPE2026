#!/usr/bin/env python3
"""Finite exact checks of the nonlinear helical-transposition cycle theorem.

Uses only additive XOR and integer enumeration; no external packages.
Finite tests corroborate but cannot replace the all-dimensional proof.
"""
from itertools import product


def admissible(q, w, z, c):
    d = w ^ z
    def f(s):
        y = s ^ c
        return y ^ (d if y in (w, z) else 0)
    for x in range(q):
        for y in range(q):
            l = f(x) ^ f(x ^ f(y))
            r = f(x ^ f(y ^ f(x)))
            assert l == r, (q, w, z, c, x, y)


def update(state, q, w, z, c):
    *xs, b = state
    d = w ^ z
    ys = []
    for x in xs:
        v = x ^ b ^ c
        e = c ^ (d if v in (w, z) else 0)
        ys.append(x ^ e)
        b ^= e
    return tuple(ys) + (b,)


def check_case(q, w, z, c, m):
    d = w ^ z
    predicted_f1 = q * (q-2)**m if c == 0 else (q*2**m if c == d else 0)
    predicted_f2 = (q*(q-4)**m if (m%2 == 0 and c not in (0,d))
                    else q**(m+1))
    observed_f1 = observed_f2 = 0
    for state in product(range(q), repeat=m+1):
        s1 = update(state, q, w, z, c)
        s2 = update(s1, q, w, z, c)
        assert update(update(s2,q,w,z,c),q,w,z,c) == state, (q,w,z,c,m,state)
        observed_f1 += s1 == state
        observed_f2 += s2 == state
    assert (observed_f1,observed_f2) == (predicted_f1,predicted_f2), (q,w,z,c,m,observed_f1,observed_f2,predicted_f1,predicted_f2)
    assert (predicted_f2 - predicted_f1)%2 == 0
    assert (q**(m+1) - predicted_f2)%4 == 0
    return (predicted_f1,(predicted_f2-predicted_f1)//2,(q**(m+1)-predicted_f2)//4)


def main():
    ncases = 0
    for q in (8,):
        for w in range(1,q):
            for z in range(w+1,q):
                for c in range(q):
                    admissible(q,w,z,c)
                    for m in (1,2,3):
                        check_case(q,w,z,c,m)
                        ncases += 1
    print('ALL_Q8_NONZERO_TRANSPOITIONS_AND_SHIFTS_PASS',ncases)
    ncases16=0
    for w,z in ((1,2),(2,7)):
        for c in (0,w^z,4,5):
            admissible(16,w,z,c)
            for m in (1,2):
                check_case(16,w,z,c,m)
                ncases16 += 1
    print('SELECTED_Q16_TRANSPOITIONS_AND_SHIFTS_PASS',ncases16)
    assert check_case(8,1,2,4,2) == (0,8*(8-4)**2//2, (8**3-8*(8-4)**2)//4)
    print('MIXED_PERIOD_EXAMPLE_Q8_M2_C4',check_case(8,1,2,4,2))
    print('ALL_UNBOUNDED_PARAMETERS_REQUIRE_ANALYTICAL_PROOF')

if __name__ == '__main__':
    main()
