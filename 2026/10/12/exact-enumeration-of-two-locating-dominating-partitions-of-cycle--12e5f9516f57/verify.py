#!/usr/bin/env python3
"""Independent finite checks for the cycle LD-partition run criterion and enumeration.

Run: python3 verify.py (Python 3 standard library only).
The proof for all cycle orders is mathematical; these are bounded cross-checks.
"""
from fractions import Fraction

BAD3 = {(0,0,0), (1,1,1)}
BAD5 = {(0,0,1,0,0), (1,1,0,1,1)}


def criterion(word):
    n = len(word)
    if n < 5:
        raise ValueError("run criterion requires n>=5")
    return (all(tuple(word[(i+j)%n] for j in range(3)) not in BAD3
                for i in range(n))
            and all(tuple(word[(i+j)%n] for j in range(5)) not in BAD5
                    for i in range(n)))


def locating_dominating(word, color):
    n = len(word)
    signatures = set()
    for i in range(n):
        if word[i] == color:
            continue
        signature = frozenset(j for j in ((i-1) % n, (i+1) % n)
                          if word[j] == color)
        if not signature or signature in signatures:
            return False
        signatures.add(signature)
    return True


def direct_counts():
    counts = {}
    tested = 0
    for n in range(4, 17):
        accepted = 0
        for mask in range(1 << n):
            word = tuple((mask >> i) & 1 for i in range(n))
            direct = locating_dominating(word, 0) and locating_dominating(word, 1)
            if n >= 5:
                assert direct == criterion(word), (n, mask, direct)
            accepted += direct
            tested += 1
        counts[n] = accepted
    return counts, tested


# Polynomial transfer for cyclic run words, independent of binary string search.
# A state holds two preceding run lengths. Adding length c avoids triple 2,1,2.
STATES = ((1,1), (1,2), (2,1), (2,2))
EDGES = [[] for _ in STATES]
for a,(u,v) in enumerate(STATES):
    for c in (1,2):
        if (u,v,c) != (2,1,2):
            EDGES[a].append((STATES.index((v,c)), c))


def transfer_counts(max_n=40):
    # powers of T, where each entry is a polynomial in x truncated at max_n
    # Since T itself is homogeneous in positive degrees, no infinite sums arise.
    P = [[{0: int(a == b)} for b in range(4)] for a in range(4)]
    weight = [Fraction(0) for _ in range(max_n+1)]
    for r in range(1, max_n+1):
        nxt = [[{} for _ in range(4)] for _ in range(4)]
        for a in range(4):
            for b in range(4):
                for deg,coefficient in P[a][b].items():
                    for c,step in EDGES[b]:
                        nd=deg+step
                        if nd <= max_n:
                            nxt[a][c][nd]=nxt[a][c].get(nd,0)+coefficient
        P=nxt
        if r % 2 == 0:
            for a in range(4):
                for n,coefficient in P[a][a].items():
                    weight[n] += Fraction(2*n*coefficient, r)
    ans=[]
    for t in weight:
        assert t.denominator == 1
        ans.append(int(t))
    return ans


def generating_counts(max_n):
    # A(x) = P(x)/Q(x), Q=1-x^2-x^4-2x^5-x^6-x^8.
    coeff = {4:4, 5:10, 6:10, 7:4, 8:12, 9:4, 10:4, 12:2}
    delays = ((2,1),(4,1),(5,2),(6,1),(8,1))
    a = [0] * (max_n + 1)
    for n in range(max_n+1):
        a[n] = coeff.get(n,0) + sum(m*a[n-d] for d,m in delays if n>=d)
    return a


def main():
    brute, tested=direct_counts()
    transfer=transfer_counts(40)
    generating=generating_counts(40)
    for n in range(4,17):
        assert brute[n] == generating[n], (n, brute[n], generating[n])
    for n in range(5,41):
        assert transfer[n] == generating[n], (n, transfer[n], generating[n])
    assert transfer[2] == 2 and transfer[4] == 6
    assert brute[4] == 4
    print("ALL CHECKS PASSED")
    print("binary_words_checked=" + str(tested))
    print("word_orders=4..16; structural_equivalence_orders=5..16")
    print("independent_transfer_and_rational_gf_orders=5..40")
    print("low_order_correction=transfer[2]:2, transfer[4]:6, true[4]:4")
    print("counts_n4..18="+repr(generating[4:19]))
    print("a_40="+str(generating[40]))

if __name__ == '__main__':
    main()
