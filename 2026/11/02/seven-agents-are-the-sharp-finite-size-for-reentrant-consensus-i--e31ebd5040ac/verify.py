"""Exact interval certificate for finite equally spaced HK opinion dynamics.
Run: python3 verify.py
Requires only the Python standard library.  Fractions are exact.
The proof of completeness is given in RESULT.md; see certificate.tsv.
"""
from fractions import Fraction as Q
from pathlib import Path


def group_sizes(v):
    out = []
    for y in v:
        if out and out[-1][0] == y:
            out[-1] = (y, out[-1][1] + 1)
        else:
            out.append((y, 1))
    return tuple(size for _, size in out)


def neighbors(v, d):
    n = len(v)
    return tuple(tuple(j for j in range(n) if abs(v[j] - v[i]) * d <= 1)
                 for i in range(n))


def update(v, graph):
    return tuple(sum((v[j] for j in g), Q(0)) / len(g) for g in graph)


def subdivide(a, b, v):
    # For v = x/d on a region (a,b], an edge changes exactly at d=1/|v_j-v_i|.
    cuts = {a, b}
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            diff = abs(v[j] - v[i])
            if diff > 0:
                threshold = Q(1) / diff
                if a < threshold < b:
                    cuts.add(threshold)
    sorted_cuts = sorted(cuts)
    return [(sorted_cuts[k], sorted_cuts[k + 1])
            for k in range(len(sorted_cuts) - 1)]


def exact_partition(n):
    if not 1 <= n <= 7:
        raise ValueError('Proof certificate covers exactly 1<=n<=7')
    active = [(Q(0), Q(1), tuple(Q(j) for j in range(n)), 0)]
    final = []
    for _ in range(30):
        next_active = []
        for a, b, v, t in active:
            assert tuple(sorted(v)) == v
            for left, right in subdivide(a, b, v):
                # Edges at the included right endpoint obey the same <= graph.
                d = (left + right) / 2
                graph = neighbors(v, d)
                assert graph == neighbors(v, right)
                nxt = update(v, graph)
                assert tuple(sorted(nxt)) == nxt
                if nxt == v:
                    final.append((left, right, t, group_sizes(v)))
                else:
                    next_active.append((left, right, nxt, t + 1))
        if not next_active:
            break
        active = next_active
    else:
        raise AssertionError('The finite exact partition did not close')
    final.sort(key=lambda z: z[0])
    assert final[0][0] == 0 and final[-1][1] == 1
    assert all(final[i][1] == final[i+1][0]
               for i in range(len(final)-1))
    return final


def consensus_expected(n, d):
    if n <= 5:
        return True
    if n == 6:
        return d <= Q(4, 7)
    return (d <= Q(48, 61) or
            Q(4, 5) < d <= Q(288, 337) or
            Q(72, 79) < d <= Q(1728, 1861))


def parse_certificate(path):
    lines = path.read_text(encoding='utf-8').splitlines()
    assert lines[0] == 'n\tleft_exclusive\tright_inclusive\tfreeze_time\tcluster_sizes'
    out = {n: [] for n in range(1, 8)}
    for line in lines[1:]:
        n, a, b, t, sizes = line.split('\t')
        out[int(n)].append((Q(a), Q(b), int(t), tuple(int(v) for v in sizes.split(','))))
    return out


def verify():
    path = Path(__file__).resolve().with_name('certificate.tsv')
    saved = parse_certificate(path)
    counts, max_time = {}, 0
    for n in range(1, 8):
        actual = exact_partition(n)
        assert actual == saved[n], ('different certificate', n)
        counts[n] = len(actual)
        endpoints = {v for left, right, _, _ in actual for v in (left, right)}
        if n == 6:
            assert Q(4, 7) in endpoints
        if n == 7:
            assert {Q(48, 61), Q(4, 5), Q(288, 337), Q(72, 79),
                    Q(1728, 1861)} <= endpoints
        for a, b, t, sizes in actual:
            max_time = max(max_time, t)
            assert sum(sizes) == n
            assert sizes in ((n,), (3, 3), (3, 1, 3))
            for d in ((a + b) / 2, b):
                assert (len(sizes) == 1) == consensus_expected(n, d)
                state = tuple(Q(j) * d for j in range(n))
                for step in range(t):
                    graph = neighbors(state, Q(1))
                    new_state = update(state, graph)
                    assert new_state != state, (n, d, step)
                    state = new_state
                assert update(state, neighbors(state, Q(1))) == state
                assert group_sizes(state) == sizes
    assert counts == {1:1, 2:1, 3:2, 4:5, 5:10, 6:11, 7:26}
    assert max_time == 12
    print('PASS: exact exhaustive half-open interval certificate for n=1..7')
    print('Terminal intervals by n:', counts)
    print('Maximum freezing time:', max_time)
    print('PASS: right-endpoint equalities, midpoint trajectories and phase classification')

if __name__ == '__main__':
    verify()
