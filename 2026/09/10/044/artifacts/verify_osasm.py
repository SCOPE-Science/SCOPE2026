#!/usr/bin/env python3
"""Exhaustive ASM/DSASM/OSASM enumeration to n=5 with odd-OSASM r=1 slice test.

Replay: python3 verify_osasm.py  -> prints VERIFY_OK on success.
Stdlib only. Exhaustively generates all n x n ASMs (n<=5) by valid-row
backtracking with column partial-sum/alternation pruning, filters to DSASMs
by transpose symmetry, filters to OSASMs (even: all diagonal zero;
odd: exactly one nonzero diagonal, per BFK Sec 8), and checks:
  - ASM counts 1,2,7,42,429 (MRR/Zeilberger/Kuperberg values)
  - DSASM counts 1,2,5,16,67 (BFK Table 1)
  - OSASM counts 1,1,4,3,32 (BFK Table 3)
  - BFK (8.3) refined values for n<=4
  - Kumari odd product P_n at t=1 for orders 1,3,5
  - palindromicity of X^O_{2n+1}(1,t): n=1 (order 3) symmetric; n=2 (order 5)
    NOT symmetric under any shift, minimal witness (n,k)=(2,1): c1=3 vs c4=9.
"""
import itertools
import math
from collections import Counter


def valid_rows(n):
    rows = []
    for tup in itertools.product([-1, 0, 1], repeat=n):
        if sum(tup) != 1:
            continue
        nz = [x for x in tup if x != 0]
        if nz[0] != 1 or nz[-1] != 1:
            continue
        if any(a == b for a, b in zip(nz, nz[1:])):
            continue
        rows.append(tup)
    return rows


def gen_asms(n):
    rows = valid_rows(n)
    out = []
    col = [0] * n
    last = [0] * n
    mat = []

    def bt(r):
        if r == n:
            if all(c == 1 for c in col):
                for j in range(n):
                    nz = [mat[i][j] for i in range(n) if mat[i][j] != 0]
                    if sum(nz) != 1 or nz[0] != 1 or nz[-1] != 1:
                        return
                    if any(a == b for a, b in zip(nz, nz[1:])):
                        return
                out.append(tuple(mat[i] for i in range(n)))
            return
        for row in rows:
            if (r == 0 or r == n - 1) and sum(1 for x in row if x != 0) != 1:
                continue
            ok = True
            for j in range(n):
                if col[j] + row[j] not in (0, 1):
                    ok = False
                    break
                if row[j] != 0 and last[j] != 0 and row[j] == last[j]:
                    ok = False
                    break
                if row[j] != 0 and last[j] == 0 and row[j] != 1:
                    ok = False
                    break
            if not ok:
                continue
            mat.append(row)
            old = list(last)
            for j in range(n):
                col[j] += row[j]
                if row[j] != 0:
                    last[j] = row[j]
            bt(r + 1)
            mat.pop()
            for j in range(n):
                col[j] -= row[j]
            for j in range(n):
                last[j] = old[j]

    bt(0)
    return out


def is_dsasm(M):
    n = len(M)
    return all(M[i][j] == M[j][i] for i in range(n) for j in range(n))


def is_osasm(M):
    n = len(M)
    d = sum(1 for i in range(n) if M[i][i] != 0)
    if n % 2 == 0:
        return d == 0
    return d == 1


def kumari_odd_product(n):
    # P_n = 2^{n-1}(3n+2)!/(2n+1)! prod_{i=1}^n (6i-2)!/(2n+2i+1)!
    # exact integer arithmetic
    from math import factorial as f
    num = (2 ** (n - 1)) * f(3 * n + 2)
    den = f(2 * n + 1)
    for i in range(1, n + 1):
        num *= f(6 * i - 2)
        den *= f(2 * n + 2 * i + 1)
    assert num % den == 0
    return num // den


def main():
    exp_asm = {1: 1, 2: 2, 3: 7, 4: 42, 5: 429}
    exp_ds = {1: 1, 2: 2, 3: 5, 4: 16, 5: 67}
    exp_os = {1: 1, 2: 1, 3: 4, 4: 3, 5: 32}
    dist = {}
    for n in [1, 2, 3, 4, 5]:
        A = gen_asms(n)
        assert len(A) == exp_asm[n], f"ASM({n})={len(A)} expected {exp_asm[n]}"
        ds = [M for M in A if is_dsasm(M)]
        assert len(ds) == exp_ds[n], f"DSASM({n})={len(ds)} expected {exp_ds[n]}"
        os = [M for M in ds if is_osasm(M)]
        assert len(os) == exp_os[n], f"OSASM({n})={len(os)} expected {exp_os[n]}"
        ct = Counter(M[0].index(1) + 1 for M in os)
        dist[n] = dict(sorted(ct.items()))
        print(f"order {n}: ASM={len(A)} DSASM={len(ds)} OSASM={len(os)} T={dict(sorted(ct.items()))}")
    # BFK (8.3) refined checks at r=1
    assert dist[1] == {1: 1}, dist[1]
    assert dist[2] == {2: 1}, dist[2]
    assert dist[3] == {1: 1, 2: 2, 3: 1}, dist[3]
    assert dist[4] == {2: 1, 3: 1, 4: 1}, dist[4]
    assert dist[5] == {1: 3, 2: 7, 3: 9, 4: 9, 5: 4}, dist[5]
    # Kumari odd product t=1 match
    for n, order in [(1, 3), (2, 5)]:
        assert sum(dist[order].values()) == kumari_odd_product(n), (n, order)
    print(f"Kumari P_1={kumari_odd_product(1)} P_2={kumari_odd_product(2)} match t=1 sums")
    # palindromicity: order 3 symmetric (shift 4), order 5 fails under every shift
    P3 = dist[3]
    assert {4 - t: P3[t] for t in P3} == P3
    print("order-3 X^O_3(1,t) palindromic (shift 4): True")
    P5 = dist[5]
    d5 = max(P5)
    assert d5 == 5
    std_pal = all(P5.get(k, 0) == P5.get(d5 - k, 0) for k in range(0, d5 + 1))
    print(f"order-5 standard palindromicity c_k=c_{{5-k}}: {std_pal} "
          f"(c1={P5.get(1,0)} vs c4={P5.get(4,0)}; c2={P5.get(2,0)} vs c3={P5.get(3,0)})")
    assert not std_pal
    shifts_ok = []
    for m in range(0, 10):
        if {m - t: P5[t] for t in P5} == P5:
            shifts_ok.append(m)
    print(f"order-5 shifts with t^m P(1/t)==P: {shifts_ok}")
    assert shifts_ok == []
    print("MINIMAL_WITNESS (n,k)=(2,1): order-5 c1=3 vs c4=9; also c2=7 vs c3=9")
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
