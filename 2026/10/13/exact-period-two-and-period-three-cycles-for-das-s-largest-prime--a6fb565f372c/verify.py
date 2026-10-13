#!/usr/bin/env python3
from math import isqrt

KMAX = 500
NMAX = 5000

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def lpf(n):
    if n < 2:
        raise ValueError("largest prime factor requires n >= 2")
    x = n
    ans = 1
    d = 2
    while d * d <= x:
        while x % d == 0:
            ans = d
            x //= d
        d = 3 if d == 2 else d + 2
    if x > 1:
        ans = x
    return ans

def phi(k, n):
    return n + k if is_prime(n) else lpf(n)

def canon(cyc):
    cyc = tuple(cyc)
    return min(cyc[i:] + cyc[:i] for i in range(len(cyc)))

def predicted_two(k):
    out = set()
    for p in range(2, k + 1):
        if is_prime(p) and k % p == 0 and lpf(k // p + 1) <= p:
            out.add(canon((p, p + k)))
    return out

def predicted_three(k):
    kp1 = k + 1
    if kp1 & (kp1 - 1):
        return set()
    if not is_prime(k + 2):
        return set()
    return {canon((2, k + 2, 2 * k + 2))}

def observed(k):
    two, three = set(), set()
    seen_global = set()
    for start in range(2, NMAX + 1):
        if start in seen_global:
            continue
        path, pos = [], {}
        x = start
        while x not in pos and x not in seen_global and x <= max(NMAX, 3 * KMAX + 10):
            pos[x] = len(path)
            path.append(x)
            x = phi(k, x)
        if x in pos:
            cyc = path[pos[x]:]
            if len(cyc) == 2:
                two.add(canon(tuple(cyc)))
            elif len(cyc) == 3:
                three.add(canon(tuple(cyc)))
        seen_global.update(path)
    return two, three

def main():
    mismatches = 0
    for k in range(1, KMAX + 1):
        two, three = observed(k)
        if two != predicted_two(k):
            mismatches += 1
        if three != predicted_three(k):
            mismatches += 1
    if mismatches:
        raise SystemExit(f"VERIFY_FAIL mismatches={mismatches}")
    print(f"VERIFY_OK k_max={KMAX} n_max={NMAX} period2_period3_mismatches=0")

if __name__ == "__main__":
    main()
