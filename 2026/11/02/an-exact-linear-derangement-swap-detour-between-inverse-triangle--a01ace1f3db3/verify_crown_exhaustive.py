"""Independent direct perfect-matching flip graph enumeration for crown graphs.

Run: python verify_crown_exhaustive.py
Only standard-library Python is required.
"""
from collections import deque
from itertools import permutations
from math import factorial


def disjoint_cycles_permutation(k, direction=1):
    return tuple(3 * (i // 3) + ((i % 3 + direction) % 3)
                 for i in range(3 * k))


def directly_enumerate_flip_graph(n):
    # A matching is a tuple: its i-th entry is the column paired to row i.
    # The omitted diagonal of the crown graph forbids i -> i.
    vertices = {tuple(p) for p in permutations(range(n))
                if all(i != p[i] for i in range(n))}
    def neighbors(m):
        # Four edges on rows r,s form an alternating 4-cycle exactly
        # when both cross edges avoid the omitted diagonal.
        for r in range(n):
            for s in range(r+1,n):
                if (r, m[s]) == (r, r) or (s, m[r]) == (s, s):
                    continue
                candidate = list(m)
                candidate[r], candidate[s] = candidate[s], candidate[r]
                out = tuple(candidate)
                assert out in vertices
                yield out
    return vertices, neighbors


def shortest(vertices, neighbors, start, target):
    q = deque([start])
    distances = {start: 0}
    while q:
        current = q.popleft()
        if current == target:
            return distances[current], len(distances)
        for neighbor in neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                q.append(neighbor)
    return None, len(distances)


if __name__ == '__main__':
    expected = {3:(2,None), 4:(9,None), 5:(44,None),
                6:(265,6), 9:(133496,10)}
    for n,(number, distance) in expected.items():
        vertices, neighbors = directly_enumerate_flip_graph(n)
        assert len(vertices) == number
        if n % 3 == 0:
            k=n//3
            source=disjoint_cycles_permutation(k,1)
            dest=disjoint_cycles_permutation(k,-1)
            got, explored=shortest(vertices, neighbors, source,dest)
            assert got==distance
            print(f'n={n} derangements={len(vertices)} shortest={got} explored={explored}')
        else:
            print(f'n={n} derangements={len(vertices)}')
    print('CROWN_EXHAUSTIVE_INDEPENDENT_PASS')
