"""Direct exhaustive BFS in the one-edge flip graph of odd matchings.
Uses the combinatorial definition of a legal move; no distance formula.
"""
from collections import Counter, deque
from functools import lru_cache

@lru_cache(None)
def perfect_pairings(vertices):
    if not vertices:
        return ((),)
    a = vertices[0]
    return tuple(((a, b),) + rest for i, b in enumerate(vertices[1:], 1)
                 for rest in perfect_pairings(vertices[1:i] + vertices[i + 1:]))

def all_odd_matchings(n):
    return tuple(tuple(sorted(p)) for hole in range(n)
                 for p in perfect_pairings(tuple(v for v in range(n) if v != hole)))

def verify(n):
    matchings = all_odd_matchings(n)
    index = {m: i for i, m in enumerate(matchings)}
    assert len(index) == len(matchings)
    m = (n - 1) // 2
    assert len(matchings) == __import__('math').factorial(n) // (2**m * __import__('math').factorial(m))
    adjacency = []
    for M in matchings:
        covered = set(v for edge in M for v in edge)
        hole = next(v for v in range(n) if v not in covered)
        successors = set()
        for a, b in M:
            for used in (a, b):
                new_edge = tuple(sorted((hole, used)))
                new_state = tuple(sorted((set(M) - {(a, b)}) | {new_edge}))
                assert new_state in index
                successors.add(index[new_state])
        adjacency.append(successors)
    assert all(len(row) == n - 1 for row in adjacency)
    assert all(i in adjacency[j] for j, nbrs in enumerate(adjacency) for i in nbrs)
    dist = [-1] * len(matchings)
    dist[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        for y in adjacency[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)
    assert -1 not in dist
    hist = [Counter(dist)[i] for i in range(max(dist) + 1)]
    print(f'n={n} vertices={len(matchings)} edges={sum(map(len,adjacency))//2} '
          f'degree={n-1} diameter={max(dist)} distance_layers={hist}')
    return hist

if __name__ == '__main__':
    for n in (3, 5, 7, 9, 11):
        verify(n)
