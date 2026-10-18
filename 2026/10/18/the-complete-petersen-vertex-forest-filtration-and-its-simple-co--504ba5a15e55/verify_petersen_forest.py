"""Exact finite Morse and relative-collapse verifier for Petersen forest complexes.
Run with Python 3 standard library; no extra packages or network access.
"""
from collections import Counter, deque

N = 10
EDGES = tuple(sorted(
    {tuple(sorted((i, (i + 1) % 5))) for i in range(5)}
    | {tuple(sorted((5 + i, 5 + ((i + 2) % 5)))) for i in range(5)}
    | {(i, i + 5) for i in range(5)}
))
assert len(EDGES) == 15


def admissible(mask, d):
    verts = [i for i in range(N) if mask & (1 << i)]
    degrees = [0] * N
    nei = [[] for _ in range(N)]
    edge_count = 0
    for i, j in EDGES:
        if ((mask >> i) & 1) and ((mask >> j) & 1):
            degrees[i] += 1
            degrees[j] += 1
            nei[i].append(j)
            nei[j].append(i)
            edge_count += 1
    if max(degrees, default=0) > d:
        return False
    seen = set()
    components = 0
    for i in verts:
        if i not in seen:
            components += 1
            seen.add(i)
            stack = [i]
            while stack:
                for j in nei[stack.pop()]:
                    if j not in seen:
                        seen.add(j)
                        stack.append(j)
    return edge_count == len(verts) - components


def all_faces(d):
    return {m for m in range(1 << N) if admissible(m, d)}


def morse_matching(faces):
    avail = faces.copy()
    pairs = []
    for v in range(N):
        bit = 1 << v
        for low in sorted(avail):
            upper = low | bit
            if not (low & bit) and upper in avail:
                avail.remove(low)
                avail.remove(upper)
                pairs.append((low, upper))
    return pairs, avail


def verify_acyclic(faces, pairs):
    matched = set(pairs)
    assert len(pairs) == len(matched)
    graph = {m: [] for m in faces}
    indeg = {m: 0 for m in faces}
    edge_count = 0
    for upper in faces:
        for i in range(N):
            if upper & (1 << i):
                low = upper ^ (1 << i)
                if low not in faces:
                    continue
                start, finish = (low, upper) if (low, upper) in matched else (upper, low)
                graph[start].append(finish)
                indeg[finish] += 1
                edge_count += 1
    todo = deque(m for m in faces if indeg[m] == 0)
    count = 0
    while todo:
        cur = todo.popleft()
        count += 1
        for dest in graph[cur]:
            indeg[dest] -= 1
            if indeg[dest] == 0:
                todo.append(dest)
    assert count == len(faces), ('directed matching cycle', count, len(faces))
    return edge_count


def relative_collapse(large, sub):
    assert sub.issubset(large)
    active = large.copy()
    steps = 0
    while True:
        opts = []
        for low in active - sub:
            ups = [low | (1 << v) for v in range(N)
                   if not (low & (1 << v)) and (low | (1 << v)) in active]
            if len(ups) != 1 or ups[0] in sub:
                continue
            high = ups[0]
            if any((high | (1 << v)) in active for v in range(N) if not (high & (1 << v))):
                continue
            opts.append((low, high))
        if not opts:
            break
        low, high = min(opts, key=lambda x: (-x[1].bit_count(), x[0]))
        # Every step is a genuine elementary free-face collapse in the CURRENT complex.
        assert low not in sub and high not in sub
        active.remove(low)
        active.remove(high)
        steps += 1
    assert active == sub, (len(active - sub), steps)
    return steps


EXPECTED = {
    0: ((10, 30, 30, 5), 4, {2: 4}),
    1: ((10, 45, 90, 80, 30, 5), None, None),
    2: ((10, 45, 120, 200, 180, 65), 1, {3: 1}),
    3: ((10, 45, 120, 210, 240, 140, 20), 6, {5: 6}),
}


def main():
    ff = {}
    for d in range(4):
        faces = all_faces(d)
        ff[d] = faces
        assert 0 in faces
        nonempty = [m for m in faces if m]
        counts = Counter(m.bit_count()-1 for m in nonempty)
        got_fvec = tuple(counts[i] for i in range(max(counts)+1))
        expected_fvec, numcrit, crit_dims = EXPECTED[d]
        assert got_fvec == expected_fvec
        assert len(nonempty) == sum(expected_fvec)
        if d in (0, 2, 3):
            pairs, critical = morse_matching(faces)
            assert 0 not in critical
            crit = Counter(m.bit_count()-1 for m in critical)
            assert len(critical) == numcrit and dict(crit) == crit_dims
            hasse = verify_acyclic(faces, pairs)
            print('d=%d faces=%d fvec=%s pairs=%d critical=%s hasse=%d DAG_OK' %
                  (d, len(nonempty), expected_fvec, len(pairs), sorted(critical), hasse))
        else:
            print('d=1 faces=%d fvec=%s' % (len(nonempty), expected_fvec))
    assert all(ff[d].issubset(ff[d+1]) for d in (0, 1, 2))
    steps = relative_collapse(ff[2], ff[1])
    assert steps == 180
    print('F2_TO_F1_SIMPLE_COLLAPSE_OK steps=%d deleted_faces=%d' %
          (steps, len(ff[2] - ff[1])))
    print('F3_EQUALS_FINFTY_OK degree_bound=%d' % max(sum(i in edge for edge in EDGES) for i in range(N)))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
