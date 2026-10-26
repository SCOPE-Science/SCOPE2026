"""Exact finite certificates for shattering by minimal dominating sets of paths.
Stdlib Python 3; 0-based vertices, with P_n having n vertices.
"""
import itertools
import json
from functools import lru_cache


def minimal_dominators(n):
    N = [(1 << v) | (1 << (v - 1) if v else 0) |
         (1 << (v + 1) if v + 1 < n else 0) for v in range(n)]
    def dominates(bits):
        return all(bits & hood for hood in N)
    return tuple(bits for bits in range(1, 1 << n)
                 if dominates(bits) and
                 all(not dominates(bits & ~(1 << v)) for v in range(n) if bits & (1 << v)))


def alternative_enumerator(n):
    """Minimal transversals by backtracking through undominated neighborhoods."""
    neighborhoods = [sum(1 << u for u in range(n) if abs(u - v) <= 1)
                     for v in range(n)]
    found = set()
    def walk(bits):
        undominated = next((mask for mask in neighborhoods if not (bits & mask)), None)
        if undominated is None:
            if all(any((bits & ~(1 << v)) & hood == 0 for hood in neighborhoods)
                   for v in range(n) if bits & (1 << v)):
                found.add(bits)
            return
        for v in range(n):
            if undominated >> v & 1:
                walk(bits | (1 << v))
    walk(0)
    return tuple(sorted(found))


def finite_dimensions(concepts, n):
    size = len(concepts)
    allbits = (1 << size) - 1
    query = tuple(sum((1 << a) for a, c in enumerate(concepts) if c >> v & 1)
                  for v in range(n))
    @lru_cache(None)
    def ldim(S):
        score = 0
        for q in query:
            yes = S & q
            if yes and yes != S:
                score = max(score, 1 + min(ldim(yes), ldim(S ^ yes)))
        return score
    vc = 0
    for d in range(1, n + 1):
        witness = None
        for qs in itertools.combinations(range(n), d):
            traces = {sum((1 << j) for j, v in enumerate(qs) if c >> v & 1)
                      for c in concepts}
            if len(traces) == (1 << d):
                witness = qs
                break
        if witness is None:
            break
        vc = d
    return vc, ldim(allbits), query


def make_tree(concepts, n, depth):
    N = len(concepts)
    Q = tuple(sum(1 << i for i, c in enumerate(concepts) if c >> v & 1)
              for v in range(n))
    @lru_cache(None)
    def possible(S, d):
        if d == 0:
            return bool(S)
        for q in Q:
            y = S & q
            if y and y != S and possible(y, d - 1) and possible(S ^ y, d - 1):
                return True
        return False
    assert possible((1 << N) - 1, depth)
    def extract(S, d):
        if d == 0:
            return {'witness': concepts[(S & -S).bit_length() - 1]}
        for v, q in enumerate(Q):
            yes = S & q
            if yes and yes != S and possible(yes, d - 1) and possible(S ^ yes, d - 1):
                return {'query': v, 'zero': extract(S ^ yes, d - 1),
                        'one': extract(yes, d - 1)}
        raise RuntimeError('No witness')
    return extract((1 << N) - 1, depth)


def verify_tree(node, n, depth, history=(), admissible=None):
    if admissible is None:
        admissible = frozenset(minimal_dominators(n))
    if depth == 0:
        c = node['witness']
        assert 0 <= c < 1 << n
        assert c in admissible
        assert all(((c >> q) & 1) == value for q, value in history)
        return [c]
    assert set(node) == {'query', 'zero', 'one'}
    q = node['query']
    assert 0 <= q < n
    return (verify_tree(node['zero'], n, depth - 1, history + ((q, 0),), admissible) +
            verify_tree(node['one'], n, depth - 1, history + ((q, 1),), admissible))


def main():
    profile = []
    for n in range(1, 12):
        concepts = minimal_dominators(n)
        assert concepts == alternative_enumerator(n)
        vc, ld, _ = finite_dimensions(concepts, n)
        profile.append([n, len(concepts), vc, ld])
        if n < 11:
            assert vc == ld, (n, vc, ld)
        else:
            assert (len(concepts), vc, ld) == (36, 4, 5)
    concepts = minimal_dominators(11)
    trace_indices = (0, 2, 7, 9)
    pattern_witness = {}
    for c in concepts:
        pat = sum(((c >> v) & 1) << j for j, v in enumerate(trace_indices))
        pattern_witness.setdefault(str(pat), c)
    assert len(pattern_witness) == 16
    # This exhausts all five-element subsets of P_11. Any shattered set of size >=5
    # would contain a shattered set of size 5.
    five_counts = {}
    for qs in itertools.combinations(range(11), 5):
        patterns = {sum(((c >> v) & 1) << j for j, v in enumerate(qs))
                    for c in concepts}
        assert len(patterns) < 32
        five_counts[len(patterns)] = five_counts.get(len(patterns), 0) + 1
    assert sum(five_counts.values()) == 462
    tree = make_tree(concepts, 11, 5)
    witnesses = verify_tree(tree, 11, 5)
    assert len(witnesses) == len(set(witnesses)) == 32
    result = {'profile': profile, 'path11_shattered_four': list(trace_indices),
              'pattern_witnesses': pattern_witness,
              'five_projection_histogram': dict(sorted(five_counts.items())),
              'depth_five_tree': tree}
    text = json.dumps(result, sort_keys=True, indent=2) + '\n'
    from pathlib import Path
    path = Path('certificates.json')
    if path.exists():
        assert path.read_text(encoding='utf-8') == text, 'Attached certificate changed'
    path.write_text(text, encoding='utf-8')
    print('PROFILE', profile)
    print('FIVE_SUBSETS_EXHAUSTED', sum(five_counts.values()))
    print('PATH11_MINIMAL_DOMINATORS', len(concepts))
    print('TREE_LEAVES', len(witnesses))
    print('ALL_CHECKS_PASS')


if __name__ == '__main__':
    main()
