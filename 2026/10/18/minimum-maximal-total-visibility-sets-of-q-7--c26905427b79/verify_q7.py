"""Independent finite checks for lower total mutual visibility in the seven-cube.

Run: python3 q7_visibility_verify.py
No external packages required.
"""
from itertools import combinations
from collections import Counter
from collections import deque

N = 7
VERTICES = tuple(range(1 << N))
EVEN = tuple(x for x in VERTICES if x.bit_count() % 2 == 0)
ADJ = {x: tuple(x ^ (1 << i) for i in range(N)) for x in VERTICES}


def distance(x, y):
    return (x ^ y).bit_count()


def total_visible_direct(selected):
    """Use shortest-path BFS in the hypercube, not the distance-two criterion."""
    selected = set(selected)
    for start in VERTICES:
        for end in range(start + 1, 1 << N):
            blocked = selected - {start, end}
            seen = {start}
            queue = deque([(start, 0)])
            found = False
            goal = distance(start, end)
            while queue:
                x, d = queue.popleft()
                if x == end:
                    found = (d == goal)
                    break
                if d == goal:
                    continue
                for y in ADJ[x]:
                    if y not in seen and y not in blocked:
                        seen.add(y)
                        queue.append((y, d + 1))
            if not found:
                return False
    return True


def is_independent(code):
    return all(distance(x, y) >= 4 for x, y in combinations(code, 2))


def check():
    index = {x: i for i, x in enumerate(EVEN)}
    closed = {}
    for x in EVEN:
        closed[x] = sum(1 << i for i, y in enumerate(EVEN) if distance(x, y) <= 2)
    full = (1 << len(EVEN)) - 1
    assert all(mask.bit_count() == 22 for mask in closed.values())

    triple_independent = triple_dominating = 0
    for c in combinations(EVEN, 3):
        if not is_independent(c):
            continue
        triple_independent += 1
        if closed[c[0]] | closed[c[1]] | closed[c[2]] == full:
            triple_dominating += 1
    assert triple_dominating == 0

    four_independent = four_dominating = 0
    distance_profiles = Counter()
    normalized_count = 0
    for c in combinations(EVEN, 4):
        if not is_independent(c):
            continue
        four_independent += 1
        dominated = closed[c[0]] | closed[c[1]] | closed[c[2]] | closed[c[3]]
        if dominated != full:
            continue
        four_dominating += 1
        profile = tuple(sorted(distance(x, y) for x, y in combinations(c, 2)))
        distance_profiles[profile] += 1
        if 0 in c:
            normalized_count += 1
    assert four_dominating == 1120
    assert normalized_count == 70
    assert distance_profiles == {(4, 4, 4, 4, 6, 6): 1120}

    C = (0x00, 0x3f, 0x47, 0x78)
    assert is_independent(C)
    assert all(any(distance(u, x) <= 2 for x in C) for u in EVEN)
    X = tuple(sorted(set(C) | {c ^ 0x01 for c in C}))
    assert len(X) == 8
    assert total_visible_direct(X)
    assert not total_visible_direct((0, 3))

    def parity_simplex():
        return tuple(sum(((v & a).bit_count() % 2) << (a - 1)
                         for a in range(1, 8)) for v in range(8))
    S = parity_simplex()
    assert len(set(S)) == 8
    assert all(x.bit_count() % 2 == 0 for x in S)
    assert is_independent(S)
    T = tuple(sorted(set(S) | {x ^ 1 for x in S}))
    assert len(T) == 16
    assert total_visible_direct(T)

    print('VERIFICATION_OK n=7 parity_vertices=64'
          f' independent_triples={triple_independent}'
          f' dominating_triples={triple_dominating}'
          f' independent_quadruples={four_independent}'
          f' dominating_quadruples={four_dominating}'
          f' containing_zero={normalized_count}'
          f' minimum_maximal_total_sets={four_dominating ** 2}'
          ' maximum_example=16 direct_shortest_path_checks=PASS')


if __name__ == '__main__':
    check()
