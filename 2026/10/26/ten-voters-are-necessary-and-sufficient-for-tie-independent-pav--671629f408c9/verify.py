"""Exact finite cross-check for three-candidate harmonic Thiele voting.

Run with Python 3.10+: python verify.py
No third-party packages required. This is a finite check, not the proof of the
unbounded theorem; the algebraic proof is in RESULT.md.
"""
from itertools import combinations_with_replacement
from math import comb

H6 = (0, 6, 9, 11)
SINGLETONS = (1, 2, 4)
PAIRS = (3, 5, 6)
PATTERNS = range(1, 8)

def scores(counts):
    return {committee: sum(counts[ballot - 1]
            * H6[(committee & ballot).bit_count()]
            for ballot in PATTERNS)
            for committee in range(1, 8)}

def nonnested(s):
    b1 = max(s[c] for c in SINGLETONS)
    b2 = max(s[c] for c in PAIRS)
    one = [c for c in SINGLETONS if s[c] == b1]
    two = [c for c in PAIRS if s[c] == b2]
    return not any(a & b for a in one for b in two)

def compositions(n, types=7):
    for v in combinations_with_replacement(range(types), n):
        out = [0]*types
        for x in v: out[x] += 1
        yield out

def main():
    checked = 0
    frontier = []
    for n in range(0, 11):
        bad = []
        count = 0
        for counts in compositions(n):
            count += 1
            if nonnested(scores(counts)):
                bad.append(tuple(counts))
        assert count == comb(n+6, 6)
        assert len(bad) == (3 if n == 10 else 0), (n, len(bad))
        checked += count
        if n == 10:
            frontier = bad
        print(f'n={n}: {count} anonymous profiles, {len(bad)} nonnested')
    assert checked == comb(17, 7)
    assert len(frontier) == 3
    for counts in frontier:
        s = scores(counts)
        assert nonnested(s)
    # Separate witness with central A=1: 2 B, 2 C, 3 AB, 3 AC.
    # PATTERNS 1=A, 2=B, 3=AB, 4=C, 5=AC, 6=BC, 7=ABC.
    witness = [0, 2, 3, 2, 3, 0, 0]
    assert sum(witness) == 10
    s = scores(witness)
    assert (s[1], s[2], s[4]) == (36,30,30)
    assert (s[3], s[5], s[6]) == (57,57,60)
    print(f'PASS: {checked} anonymous profiles; exactly 3 labeled frontier profiles, one orbit')

if __name__ == '__main__':
    main()
