#!/usr/bin/env python3
"""Exact verification for the 3^a p q weak-Carmichael parametrization."""

from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    # Deterministic for n < 2^64.
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True

def factor(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d, e))
        d = 3 if d == 2 else d + 2
    if n > 1:
        out.append((n, 1))
    return out

def divisors(n):
    ds = [1]
    for p, e in factor(n):
        base = list(ds)
        pp = 1
        for _ in range(e):
            pp *= p
            ds += [x * pp for x in base]
    return sorted(ds)

def param_solutions(a):
    A = 3 ** a
    ans = set()
    candidates = []
    for k in range(1, A):
        C = (A - 1) * (A + k)
        for d in divisors(C):
            if d <= 2:
                continue
            if (A * d + A - 1) % k:
                continue
            if (A * A + C // d) % k:
                continue
            p = d + 1
            q = 1 + (A * d + A - 1) // k
            if q <= p:
                continue
            candidates.append((k, d, p, q))
            if is_prime(p) and is_prime(q):
                ans.add((p, q))
    return sorted(ans), candidates

def sieve(n):
    mark = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        mark[0] = 0
    if n >= 1:
        mark[1] = 0
    for p in range(2, isqrt(n) + 1):
        if mark[p]:
            mark[p*p:n+1:p] = b"\x00" * (((n - p*p) // p) + 1)
    return [i for i in range(2, n + 1) if mark[i]]

def direct_solutions(a):
    A = 3 ** a
    pmax = 2 * A * A - 3 * A + 2
    ans = set()
    for p in sieve(pmax):
        if p <= 3:
            continue
        # q-1 divides A*p-1.
        N = A * p - 1
        for r in divisors(N):
            q = r + 1
            if q <= p or not is_prime(q):
                continue
            n = A * p * q
            if (n - 1) % (p - 1) == 0 and (n - 1) % (q - 1) == 0:
                ans.add((p, q))
    return sorted(ans)

def main():
    expected = {
        1: [(11, 17)],
        2: [(29, 53), (89, 401)],
        3: [(53, 131), (59, 797), (131, 443)],
        4: [(47, 347), (7841, 37361)],
        5: [(11, 17), (17, 827), (41, 587), (71, 8627), (60017, 2916827)],
        6: [(29, 4229), (137, 49937), (3329, 6761), (41777, 1791497)],
    }
    print("parameter_solutions")
    for a in range(1, 7):
        got, _ = param_solutions(a)
        print(f"a={a}: {got}")
        assert got == expected[a]

    print("direct_crosscheck")
    for a in range(1, 6):
        direct = direct_solutions(a)
        param, _ = param_solutions(a)
        ok = direct == param
        print(f"a={a}: count={len(direct)}, match={ok}")
        assert ok

    _, cands = param_solutions(2)
    print("a=2_structural_candidates")
    for k, d, p, q in cands:
        print(f"k={k}, d={d}, p={p}, q={q}, prime_pair={is_prime(p) and is_prime(q)}")

    print("period_checks")
    for p, q, a0, period in ((29, 53, 2, 6), (89, 401, 2, 20)):
        for t in range(5):
            a = a0 + t * period
            A = 3 ** a
            n = A * p * q
            assert (n - 1) % (p - 1) == 0
            assert (n - 1) % (q - 1) == 0
        print(f"(p,q)=({p},{q}): a == {a0} (mod {period}) verified for first 5 terms")

if __name__ == "__main__":
    main()
