#!/usr/bin/env python3
from pathlib import Path
from math import isqrt
import csv

PUBLISHED_COUNTS = [
    1,2,3,4,6,8,12,18,25,38,56,89,138,218,342,547,882,1429,
    2299,3705,5961,9615,15524,25057,40442,65247,105412,170224
]

def least_prime_factors(n):
    lpf = list(range(n + 1))
    if n >= 1:
        lpf[1] = 1
    r = isqrt(n)
    for p in range(2, r + 1):
        if lpf[p] == p:
            for k in range(p * p, n + 1, p):
                if lpf[k] == k:
                    lpf[k] = p
    return lpf

def bitset_from_set(S):
    b = 0
    for x in S:
        b |= 1 << x
    return b

def exact_next(C):
    M = max(C)
    lpf = least_prime_factors(2 * M)
    bits = bitset_from_set(C)
    sums = 0
    for a in C:
        sums |= bits << a
    out = set(C)
    t = sums
    while t:
        low = t & -t
        m = low.bit_length() - 1
        if m >= 2:
            out.add(m if lpf[m] == m else m // lpf[m])
        t -= low
    return out

def first_missing_prime(C):
    M = max(C)
    lpf = least_prime_factors(max(4, 2 * M))
    prev = None
    for p in range(2, 2 * M + 1):
        if lpf[p] == p:
            if p not in C:
                return p, prev
            prev = p
    raise AssertionError("No missing prime found in scan window")

def main():
    C = {1}
    rows = []
    stages = [set(C)]
    for n in range(28):
        M = max(C)
        R, Q = first_missing_prime(C)
        rows.append((n, len(C), M, R, Q if Q is not None else "", int(n >= 1 and Q == M)))
        if n < 27:
            C = exact_next(C)
            stages.append(set(C))

    counts = [len(S) for S in stages]
    assert counts == PUBLISHED_COUNTS, (counts, PUBLISHED_COUNTS)

    for n in range(1, 27):
        M = max(stages[n])
        R, Q = first_missing_prime(stages[n])
        assert Q == M, (n, M, Q, R)

    C26 = stages[26]
    C27 = stages[27]
    assert len(C26) == 105412
    assert max(C26) == 162143
    assert len(C27) == 170224
    assert max(C27) == 262331

    R27, Q27 = first_missing_prime(C27)
    assert R27 == 262321
    assert Q27 == 262313
    assert 262321 not in C27
    assert 262331 in C27

    assert 100188 in C26
    assert 162143 in C26
    assert 100188 + 162143 == 262331
    lpf = least_prime_factors(2 * max(C26))
    assert lpf[262331] == 262331

    assert 2 * max(C26) == 324286
    assert 324286 < 2 * 262321
    for a in C26:
        assert 262321 - a not in C26

    out = Path(__file__).with_name("stage_stats.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n","cardinality","maximum","first_missing_prime","preceding_prime","prime_prefix_reaches_maximum"])
        w.writerows(rows)

    print("VERIFY_OK")
    print("counts_0_27=" + ",".join(map(str, counts)))
    print("first_gap_n=27")
    print("C26_cardinality=105412 C26_maximum=162143")
    print("C27_cardinality=170224 C27_maximum=262331")
    print("R27=262321 Q27=262313")
    print("witness_262331=100188+162143")
    print("pair_sum_262321=absent")

if __name__ == "__main__":
    main()
