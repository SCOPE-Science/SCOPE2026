"""Independent partition-level checks of the arbitrary-landmark rook-graph theorem.
Only finite tests; the uniform statement is proved mathematically in RESULT.md.
"""
from collections import Counter, defaultdict
from itertools import combinations
from random import Random


def observed(m, n, markers):
    vertices = [(r, c) for r in range(m) for c in range(n)]
    ids = {v: i for i, v in enumerate(vertices)}
    neigh = [[ids[w] for w in vertices if w != v and (v[0] == w[0] or v[1] == w[1])]
             for v in vertices]
    colors = [0] * len(vertices)
    for i, x in enumerate(markers, 1):
        colors[ids[x]] = i

    def partition(cs):
        D = defaultdict(set)
        for v, c in zip(vertices, cs):
            D[c].add(v)
        return frozenset(frozenset(x) for x in D.values())

    history = [partition(colors)]
    for _ in range(4):
        signatures = [(colors[i], tuple(sorted(Counter(colors[j] for j in neigh[i]).items())))
                      for i in range(len(vertices))]
        code = {s: k for k, s in enumerate(sorted(set(signatures)))}
        colors = [code[s] for s in signatures]
        history.append(partition(colors))
        if history[-1] == history[-2]:
            break
    return history


def predicted(m, n, markers):
    rows = {r: frozenset(i for i, (x, y) in enumerate(markers) if x == r) for r in range(m)}
    cols = {c: frozenset(i for i, (x, y) in enumerate(markers) if y == c) for c in range(n)}
    flip = (m == n and len(set(x for x, _ in markers)) == len(markers)
            and len(set(y for _, y in markers)) == len(markers))
    D = defaultdict(set)
    for r in range(m):
        for c in range(n):
            pair = (tuple(sorted(rows[r])), tuple(sorted(cols[c])))
            if flip:
                pair = min(pair, pair[::-1])
            D[pair].add((r, c))
    return frozenset(frozenset(x) for x in D.values())


def run():
    count = vertices = 0
    for m in range(2, 5):
        for n in range(2, 6):
            board = [(r, c) for r in range(m) for c in range(n)]
            for t in range(0, 4):
                for F in combinations(board, t):
                    obs = observed(m, n, F)
                    want = predicted(m, n, F)
                    assert obs[min(2, len(obs)-1)] == want, (m, n, F, [len(x) for x in obs], len(want))
                    count += 1
                    vertices += m*n
    rng = Random(18011985)
    for m, n in [(5,5),(6,7),(8,8),(9,11)]:
        board = [(r,c) for r in range(m) for c in range(n)]
        for t in range(0, min(9,len(board))+1):
            for _ in range(65):
                F = rng.sample(board, t)
                obs = observed(m, n, F)
                want = predicted(m, n, F)
                assert obs[min(2,len(obs)-1)] == want, (m,n,F)
                count += 1; vertices += m*n
    for m, n, F in [(3,4,[(0,0)]), (4,4,[(0,0),(0,1),(1,2)])]:
        obs = observed(m,n,F)
        assert obs[1] != predicted(m,n,F) and obs[2] == predicted(m,n,F)
    print('VERIFY_REFINEMENT_OK cases=%d vertex_instances=%d sharp_examples=2' % (count,vertices))

if __name__ == '__main__':
    run()
