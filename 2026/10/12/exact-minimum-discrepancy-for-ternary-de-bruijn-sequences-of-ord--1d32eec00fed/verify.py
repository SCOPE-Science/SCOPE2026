#!/usr/bin/env python3
"""Independent exact verification of a finite cyclic de Bruijn word and its discrepancy."""
from itertools import combinations
from collections import Counter

ALPHABET_SIZE = 3
ORDER = 5
WITNESS = "012121020122200112011010211022210120002201011122122021001002120221111000202021221121101220020021010012021110202220111112002212120120102000021122012101100201121222202010001022102121120200101012111210022222110011021022022000111011222120012210000"

def verify(w, q, n):
    N = q ** n
    assert len(w) == N and set(w) == {str(k) for k in range(q)}
    assert Counter(w) == {str(k): N // q for k in range(q)}
    windows = ["".join(w[(i + j) % N] for j in range(n)) for i in range(N)]
    assert len(set(windows)) == N
    assert len({"".join(str(k) for k in v) for v in __import__('itertools').product(range(q), repeat=n)}) == N
    pairs = []
    for a,b in combinations(range(q),2):
        balance = 0
        low = high = 0
        for c in w:
            balance += (c == str(a)) - (c == str(b))
            low = min(low, balance)
            high = max(high, balance)
        assert balance == 0
        pairs.append((a,b,low,high,high-low))
    D = max(p[-1] for p in pairs)
    assert D == n
    # Independent direct factor scan, including all wraparound factors.
    for start in range(N):
        count = [0]*q
        for length in range(1,N+1):
            count[int(w[(start+length-1)%N])] += 1
            assert max(count)-min(count) <= n
    assert str(0)*n in windows
    print(f"VERIFY_OK q={q} n={n} period={N} windows={len(set(windows))} discrepancy={D} pairs={pairs}")

if __name__ == '__main__':
    verify(WITNESS, ALPHABET_SIZE, ORDER)
