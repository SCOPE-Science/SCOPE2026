#!/usr/bin/env python3
"""Independent canonical-word census for the 9/4-power-free curling problem.

Python 3 standard library only. All strings are 0-indexed and fixed-length.
"""
from collections import Counter
from fractions import Fraction

N = 84
TRANSFORMS = (
    "112112212112122112212112211212211221211212212112211212211221211221121221211212211211",
    "112112212112122112212112211212211221211212212112211212211221211221121221211212211212",
)

def forbidden_power_end(s):
    n = len(s)
    for p in range(1, (4*n)//9 + 1):
        k = (9*p + 3)//4
        if k <= n and s[-k:-p] == s[-(k-p):]:
            return True
    return False

def forbidden_overlap_end(s):
    n = len(s)
    for p in range(1, (n-1)//2 + 1):
        if s[-(2*p+1):-p] == s[-(p+1):]:
            return True
    return False

def last_curl(s):
    for p in range(1, len(s)//2 + 1):
        if s[-2*p:-p] == s[-p:]:
            return "2"
    return "1"

def critical_exponent(s):
    """Largest exponent of any factor, using an exact rational comparison."""
    best = Fraction(1)
    for p in range(1, len(s)//2 + 1):
        run = 0
        for j in range(len(s)-p):
            run = run+1 if s[j] == s[j+p] else 0
            if run >= p:
                value = Fraction(p+run, p)
                if value > best:
                    best = value
    return best

def run():
    # Restricted-growth encoding produces one representative for each orbit
    # of global alphabet permutations. For a used maximum symbol M, the
    # next symbol may be any of 0,...,min(M+1,2).
    level = [("", "", -1)]
    for n in range(1, N+2):
        nxt = []
        for w, t, m in level:
            for c in range(min(2, m+1) + 1):
                v = w + str(c)
                if forbidden_power_end(v):
                    continue
                cv = t + last_curl(v)
                if forbidden_overlap_end(cv):
                    continue
                nxt.append((v, cv, max(m, c)))
        level = nxt
        if n == N:
            assert len(level) == 1728
            assert all(m == 2 for _,_,m in level)
            table = Counter((str(critical_exponent(w)), t) for w,t,_ in level)
            assert set(t for _,t in table) == set(TRANSFORMS)
            expect = {
               ("2", TRANSFORMS[0]): 672,
               ("2", TRANSFORMS[1]): 336,
               ("11/5", TRANSFORMS[0]): 480,
               ("11/5", TRANSFORMS[1]): 240,
            }
            assert table == expect, (table, expect)
            assert len(TRANSFORMS[0]) == len(TRANSFORMS[1]) == N
            assert TRANSFORMS[0][:83] == TRANSFORMS[1][:83]
            assert TRANSFORMS[0][-1] == "1" and TRANSFORMS[1][-1] == "2"
            # Every final word uses all three symbols, so each representative
            # corresponds to exactly 3!=6 labeled words.
            for w,t,m in level:
                assert len(w) == N and len(t) == N
                assert t == "".join(last_curl(w[:j]) for j in range(1,N+1))
            print("canonical", len(level), "labeled", 6*len(level))
            print("stratified labeled counts", { (e,t[-1]):6*c for (e,t),c in table.items()})
        if n == N+1:
            assert len(level) == 0
    print("POWER94_CURLING_CANONICAL_VERIFY_OK")

if __name__ == "__main__":
    run()
