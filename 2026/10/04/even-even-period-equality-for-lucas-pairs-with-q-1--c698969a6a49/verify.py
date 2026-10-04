#!/usr/bin/env python3
from math import gcd

def recurrence_terms(p, m, kind, limit):
    if kind == "U":
        a, b = 0 % m, 1 % m
    else:
        a, b = 2 % m, p % m
    out = [a]
    if limit == 0:
        return out
    out.append(b)
    for _ in range(2, limit + 1):
        a, b = b, (p * b + a) % m
        out.append(b)
    return out

def period(p, m, kind):
    if kind == "U":
        s0, s1 = 0 % m, 1 % m
    else:
        s0, s1 = 2 % m, p % m
    a, b = s0, s1
    # Since the recurrence-state map has determinant -1 modulo m,
    # it is a permutation of the m^2 states and must return.
    for d in range(1, m * m + 1):
        a, b = b, (p * b + a) % m
        if a == s0 and b == s1:
            return d
    raise AssertionError(("period-not-found", p, m, kind))

def entry_v(p, m):
    pv = period(p, m, "V")
    a, b = 2 % m, p % m
    if b == 0:
        return 1
    for n in range(2, pv + 1):
        a, b = b, (p * b + a) % m
        if b == 0:
            return n
    return None

def v2_abs(n):
    n = abs(n)
    assert n
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e

def v_exact(p, n):
    a, b = 2, p
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, p * b + a
    return b

def main():
    theorem_cases = 0
    entry_cases = 0
    forced_two_adic_cases = 0

    ps = [p for p in range(-40, 41) if p != 0 and p % 2 == 0]
    for p in ps:
        for m in range(4, 161, 2):
            theorem_cases += 1
            e = entry_v(p, m)
            if e is None:
                continue
            entry_cases += 1
            pu = period(p, m, "U")
            pv = period(p, m, "V")
            assert pu == pv, ("period-mismatch", p, m, e, pu, pv)

            mm = m
            t = 0
            while mm % 2 == 0:
                t += 1
                mm //= 2
            if t >= 2:
                forced_two_adic_cases += 1
                assert p % (2 ** t) == 0, ("forced-2-adic-failed", p, m, e, t)

    valuation_cases = 0
    for p in [p for p in range(-80, 81) if p != 0 and p % 2 == 0]:
        ep = v2_abs(p)
        for n in range(0, 101):
            val = v_exact(p, n)
            ev = v2_abs(val)
            expected = 1 if n % 2 == 0 else ep
            assert ev == expected, ("v2-mismatch", p, n, val, ev, expected)
            valuation_cases += 1

    print("VERIFY_OK")
    print("theorem_parameter_pairs=" + str(theorem_cases))
    print("entry_point_cases=" + str(entry_cases))
    print("forced_two_adic_cases=" + str(forced_two_adic_cases))
    print("valuation_cases=" + str(valuation_cases))

if __name__ == "__main__":
    main()
