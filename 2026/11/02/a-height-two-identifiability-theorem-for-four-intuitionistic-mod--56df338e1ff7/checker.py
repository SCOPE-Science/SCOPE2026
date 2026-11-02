"""Exhaustive finite checks for full four-modal accessibility identifiability.

Use: python3 checker.py
The four operations are evaluated directly from their quantifier semantics.
"""
from itertools import combinations
from collections import defaultdict


def all_preorders(n):
    for code in range(1 << (n * n)):
        le = tuple((code >> (i * n)) & ((1 << n) - 1) for i in range(n))
        if any(not (le[i] & (1 << i)) for i in range(n)):
            continue
        if any((le[i] & (1 << j)) and (le[j] & ~le[i]) for i in range(n) for j in range(n)):
            continue
        yield le


def is_poset(le):
    n = len(le)
    return all(not ((le[i] >> j) & 1 and (le[j] >> i) & 1)
               for i in range(n) for j in range(i + 1, n))


def has_strict_triple(le):
    n = len(le)
    return any(i != j and i != k and j != k
               and (le[i] >> j) & 1 and not ((le[j] >> i) & 1)
               and (le[j] >> k) & 1 and not ((le[k] >> j) & 1)
               for i in range(n) for j in range(n) for k in range(n))


def upsets(le):
    n = len(le)
    return [u for u in range(1 << n)
            if all(not ((u >> i) & 1) or (le[i] & u) == le[i] for i in range(n))]


def modal_outputs(le, r, u):
    """Return ordered masks (Prenosil diamond, box, Wijesekera diamond, dual box)."""
    n = len(le)
    rows = [(r >> (i * n)) & ((1 << n) - 1) for i in range(n)]
    out = [0, 0, 0, 0]
    for s in range(n):
        down = [t for t in range(n) if (le[t] >> s) & 1]
        above = [t for t in range(n) if (le[s] >> t) & 1]
        # The raw relational tests below are not replaced by endpoint rules.
        clauses = (
            any(any((rows[t] >> v) & 1 and (u >> v) & 1 for v in range(n)) for t in down),
            all(all(not ((rows[t] >> v) & 1) or ((u >> v) & 1) for v in range(n)) for t in above),
            all(any((rows[t] >> v) & 1 and (u >> v) & 1 for v in range(n)) for t in above),
            any(all(not ((rows[t] >> v) & 1) or ((u >> v) & 1) for v in range(n)) for t in down),
        )
        for j, yes in enumerate(clauses):
            if yes:
                out[j] |= 1 << s
    return tuple(out)


def signature(le, r):
    return tuple(v for u in upsets(le) for v in modal_outputs(le, r, u))


def is_injective(le):
    n = len(le)
    seen = set()
    for r in range(1 << (n * n)):
        s = signature(le, r)
        if s in seen:
            return False
        seen.add(s)
    return True


def check_recovery(le, r):
    n = len(le)
    # Formula from the proof: use a principal maximal singleton, or the
    # complement of a minimal singleton, to read each accessibility bit.
    assert is_poset(le) and not has_strict_triple(le)
    for v in range(n):
        minimal = not any(w != v and (le[w] >> v & 1) for w in range(n))
        maximal = not any(w != v and (le[v] >> w & 1) for w in range(n))
        assert minimal or maximal
        if maximal:
            u = 1 << v
        else:
            u = ((1 << n) - 1) ^ (1 << v)
        assert u in upsets(le)
        obs = modal_outputs(le, r, u)
        for s in range(n):
            source_min = not any(w != s and (le[w] >> s & 1) for w in range(n))
            source_max = not any(w != s and (le[s] >> w & 1) for w in range(n))
            assert source_min or source_max
            if maximal:
                reading = bool((obs[0 if source_min else 2] >> s) & 1)
            else:
                reading = not bool((obs[3 if source_min else 1] >> s) & 1)
            assert reading == bool((r >> (s * n + v)) & 1)


def check_two_chain_minimality():
    le = (0b11, 0b10)
    pairs = ((1, 3), (8, 12), (6, 14), (6, 7))
    for missing, (a, b) in enumerate(pairs):
        A, B = signature(le, a), signature(le, b)
        assert A != B
        assert all(A[i] == B[i] for i in range(len(A)) if i % 4 != missing)
        assert any(A[i] != B[i] for i in range(len(A)) if i % 4 == missing)
    assert is_injective(le)
    print('TWO_CHAIN_ALL_FOUR_ESSENTIAL', len(pairs))


def check_three_chain():
    le = (0b111, 0b110, 0b100)
    # Row 0 has 0 and 2; adding the middle target 1 changes no operation.
    r = (1 << 0) | (1 << 2)
    assert signature(le, r) == signature(le, r | (1 << 1))
    print('THREE_CHAIN_INVISIBLE_MIDDLE_EDGE_OK')


def main():
    counts = []
    for n in (1, 2, 3):
        pre = list(all_preorders(n))
        injective = sum(is_injective(le) for le in pre)
        expected = sum(is_poset(le) and not has_strict_triple(le) for le in pre)
        assert injective == expected, (n, injective, expected)
        for le in pre:
            if is_poset(le) and not has_strict_triple(le):
                for r in range(1 << (n * n)):
                    check_recovery(le, r)
        counts.append((n, len(pre), injective))
    print('EXHAUSTIVE_PREORDER_COUNTS', counts)
    check_two_chain_minimality()
    check_three_chain()

    # Full census on one branching height-two four-world poset.
    le = (0b1101, 0b1110, 0b0100, 0b1000)
    assert is_poset(le) and not has_strict_triple(le)
    assert is_injective(le)
    print('FOUR_WORLD_BRANCHING_ALL_RELATIONS', 1 << 16)

    # The three-chain edge obstruction persists after adjoining other worlds.
    for n in (4,):
        for le in all_preorders(n):
            if not is_poset(le) or not has_strict_triple(le):
                continue
            triple = next((i, j, k) for i in range(n) for j in range(n) for k in range(n)
                          if len({i, j, k}) == 3 and (le[i] >> j) & 1
                          and not ((le[j] >> i) & 1) and (le[j] >> k) & 1
                          and not ((le[k] >> j) & 1))
            a, b, c = triple
            r = (1 << a) | (1 << c)
            assert signature(le, r) == signature(le, r | (1 << b))
        print('FOUR_WORLD_CHAIN_OBSTRUCTION_ALL_PREORDERS_OK')
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
