"""Exhaustive certificate for first C2-equivalent nonisomorphic finite posets.

Only Python 3 standard library is required. The strict order is represented by
successor bitmasks. No sampled or probabilistic computation is used.
"""
from collections import defaultdict
from pathlib import Path
import json

EXPECTED_COUNTS = {1: 1, 2: 2, 3: 5, 4: 16, 5: 63,
                   6: 318, 7: 2045, 8: 16999}
EXPECTED_C2_CLASSES = {1: 1, 2: 2, 3: 5, 4: 16, 5: 63,
                       6: 318, 7: 2045, 8: 16997}


def strict_pairs(P):
    return [[i, j] for i, row in enumerate(P) for j in range(len(P))
            if row & (1 << j)]


def is_order(P):
    n = len(P)
    if any(P[i] & (1 << i) for i in range(n)):
        return False
    for i in range(n):
        for j in range(n):
            if P[i] & (1 << j) and (P[j] & ~P[i]):
                return False
    return True


def downset(P, S):
    # If x<y and y belongs to S, x must also belong to S.
    return all(not (P[x] & S) or (S & (1 << x)) for x in range(len(P)))


def add_maximal(P, S):
    n = len(P)
    return tuple((P[i] | ((1 << n) if S & (1 << i) else 0))
                 for i in range(n)) + (0,)


def signature(P):
    n = len(P)
    return tuple(sorted((P[i].bit_count(),
                         sum(bool(P[j] & (1 << i)) for j in range(n)))
                        for i in range(n)))


def isomorphic(A, B):
    """Exact bijective backtracking, preserving both directions of strict order."""
    n = len(A)
    if len(B) != n or signature(A) != signature(B):
        return False
    dA = [(A[i].bit_count(), sum(bool(A[j] & (1 << i)) for j in range(n)))
          for i in range(n)]
    dB = [(B[i].bit_count(), sum(bool(B[j] & (1 << i)) for j in range(n)))
          for i in range(n)]
    bins = {x: [j for j in range(n) if dB[j] == x] for x in set(dA)}
    order = sorted(range(n), key=lambda i: (len(bins[dA[i]]), dA[i]))
    f, occupied = {}, set()

    def search(t):
        if t == n:
            return True
        i = order[t]
        for j in bins[dA[i]]:
            if j in occupied:
                continue
            if any(bool(A[i] & (1 << a)) != bool(B[j] & (1 << b))
                   or bool(A[a] & (1 << i)) != bool(B[b] & (1 << j))
                   for a, b in f.items()):
                continue
            f[i] = j
            occupied.add(j)
            if search(t + 1):
                return True
            del f[i]
            occupied.remove(j)
        return False

    return search(0)


def generate(previous):
    """Every n-poset is formed by adding a maximal point above an ideal."""
    n = len(previous[0]) + 1
    classes, output = defaultdict(list), []
    candidates = 0
    for P in previous:
        for S in range(1 << (n - 1)):
            if not downset(P, S):
                continue
            Q = add_maximal(P, S)
            assert is_order(Q)
            candidates += 1
            bucket = classes[signature(Q)]
            if not any(isomorphic(Q, Z) for Z in bucket):
                bucket.append(Q)
                output.append(Q)
    assert len(output) == EXPECTED_COUNTS[n]
    return output, candidates


def all_c2_classes(Ps):
    """Joint exact refinement by <, > and incomparability 2-types."""
    n = len(Ps[0])
    colors = {(i, v): 0 for i in range(len(Ps)) for v in range(n)}
    for _ in range(2 * n + 4):
        descriptions = {}
        for k, P in enumerate(Ps):
            for v in range(n):
                below = []
                above = []
                incomparable = []
                for u in range(n):
                    if u == v:
                        continue
                    if P[u] & (1 << v):
                        below.append(colors[k, u])
                    elif P[v] & (1 << u):
                        above.append(colors[k, u])
                    else:
                        incomparable.append(colors[k, u])
                descriptions[k, v] = (colors[k, v], tuple(sorted(below)),
                                       tuple(sorted(above)),
                                       tuple(sorted(incomparable)))
        dictionary = {s: c for c, s in enumerate(sorted(set(descriptions.values())))}
        new_colors = {key: dictionary[s] for key, s in descriptions.items()}
        if new_colors == colors:
            break
        colors = new_colors
    groups = defaultdict(list)
    for k in range(len(Ps)):
        groups[tuple(sorted(colors[k, v] for v in range(n)))].append(k)
    return list(groups.values())


def load_witnesses():
    return json.loads(Path(__file__).with_name('witnesses.json').read_text('utf-8'))


def run():
    recorded = load_witnesses()
    expected_ambiguous = []
    for case in recorded['cases']:
        two = []
        for name in ('A', 'B'):
            pairs = case[name]
            mask = [0] * 8
            for i, j in pairs:
                mask[i] |= 1 << j
            Q = tuple(mask)
            assert is_order(Q)
            two.append(Q)
        assert not isomorphic(*two)
        assert len(all_c2_classes(two)) == 1
        expected_ambiguous.append(frozenset(tuple(tuple(x) for x in strict_pairs(P)) for P in two))

    current = [(0,)]
    print('n=1 posets=1 C2_classes=1')
    for n in range(2, 9):
        current, num_candidates = generate(current)
        equivalence_classes = all_c2_classes(current)
        assert len(equivalence_classes) == EXPECTED_C2_CLASSES[n]
        ambiguous = [group for group in equivalence_classes if len(group) > 1]
        assert all(len(group) == 2 for group in ambiguous)
        print(f'n={n} posets={len(current)} C2_classes={len(equivalence_classes)} '
              f'ambiguous_pairs={len(ambiguous)} candidates={num_candidates}')
        if n < 8:
            assert ambiguous == []
        else:
            classes_as_pairs = [frozenset(tuple(tuple(x) for x in strict_pairs(current[i]))
                                          for i in group)
                                for group in ambiguous]
            assert set(classes_as_pairs) == set(expected_ambiguous)
    print('VERIFY_OK: exactly two 2-element C2 classes at n=8; none before')


if __name__ == '__main__':
    run()
