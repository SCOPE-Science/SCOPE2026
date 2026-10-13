#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import ceil

@lru_cache(None)
def partitions(n, cap=None):
    if cap is None or cap > n:
        cap = n
    out = []
    def rec(rem, mx, cur):
        if rem == 0:
            out.append(tuple(cur))
            return
        for x in range(min(rem, mx), 0, -1):
            rec(rem-x, x, cur+[x])
    rec(n, cap, [])
    return tuple(out)

def feasible(profile, s, t):
    maxima = [p[0] for p in profile]
    for i in range(len(maxima)):
        for j in range(i+1, len(maxima)):
            a, b = maxima[i], maxima[j]
            if (a >= s and b >= t) or (a >= t and b >= s):
                return False
    return True

def brute(ns, s, t):
    best = None
    for prof in product(*(partitions(n) for n in ns)):
        if feasible(prof, s, t):
            c = sum(len(p) for p in prof)
            if best is None or c < best:
                best = c
    return best

def formula(ns, s, t):
    first = sum(ceil(n/(t-1)) for n in ns)
    if s == 1:
        return first
    second = min(1 + sum(ceil(ns[i]/(s-1)) for i in range(len(ns)) if i != j)
                 for j in range(len(ns)))
    return min(first, second)

def main():
    cases = 0
    for r in range(2, 5):
        for ns in combinations_with_replacement(range(1, 6), r):
            for s in range(1, 5):
                for t in range(max(2, s), 5):
                    cases += 1
                    b = brute(ns, s, t)
                    f = formula(ns, s, t)
                    if b != f:
                        raise SystemExit(f"MISMATCH ns={ns} s={s} t={t}: brute={b} formula={f}")
    assert cases == 1080, cases
    print("ALL CHECKS PASSED; parameter_cases=1080; host_parts=2..4; part_sizes=1..5; shore_sizes=1<=s<=t<=4,t>=2")

if __name__ == '__main__':
    main()
