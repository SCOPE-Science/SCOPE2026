"""Exact finite checks for the minimum-genus perfect-semigroup classification.

Run: python3 verify.py
Only the standard Python library is used.
"""
from itertools import combinations


def predicted(F):
    assert F >= 3
    k = F // 2
    baseline = frozenset(range(k + 1, F - 1))
    ans = {baseline}
    if F % 2 == 0:
        for a in range((F + 3) // 3, k):
            ans.add(frozenset(range(a, k)) | frozenset(range(F + 1 - a, F - 1)))
    return ans


def is_perfect_semigroup(F, pos):
    S = {0} | set(pos)
    for x in S:
        for y in S:
            if x + y <= F and x + y not in S:
                return False
    for h in range(1, F + 1):
        if h not in S and (h - 1 in S) and ((h + 1 in S) or h == F):
            return False
    return True


def exhaustive(F):
    k = F // 2
    expected_genus = k + 2
    winners = set()
    better = []
    candidate_count = 0
    for mask in range(1 << (F - 2)):
        pos = frozenset(x for x in range(1, F - 1) if mask & (1 << (x - 1)))
        if len(pos) > F - expected_genus:
            # More retained elements would contradict the asserted genus bound.
            # Check these rather than discarding them.
            if is_perfect_semigroup(F, pos):
                better.append(tuple(sorted(pos)))
            continue
        if len(pos) < F - expected_genus:
            continue
        candidate_count += 1
        if is_perfect_semigroup(F, pos):
            winners.add(pos)
    assert not better, (F, better[:2])
    assert winners == predicted(F), (F, winners, predicted(F))
    return len(winners), candidate_count


def check_constructed(F):
    p = predicted(F)
    k = F // 2
    assert len(p) == (1 if F % 2 else 1 + (k - 1) // 3)
    for pos in p:
        assert F - len(pos) == k + 2, (F, pos)
        assert is_perfect_semigroup(F, pos), (F, pos)
    return len(p)


if __name__ == '__main__':
    all_counts = []
    for F in range(3, 21):
        count, considered = exhaustive(F)
        all_counts.append((F, count))
        print(f'F={F} extremizers={count} fixed-size-masks={considered}')
    for F in range(21, 301):
        check_constructed(F)
    print('PASS: exhaustive Frobenius values 3..20, constructions 21..300')
