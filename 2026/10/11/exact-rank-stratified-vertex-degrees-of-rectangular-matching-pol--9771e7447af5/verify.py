"""Independent finite cross-check for the matching-polytope rank-degree theorem.
Run: python3 verify.py; uses only the Python standard library.
Finite computations corroborate, but do not prove, the universal theorem.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb, factorial


def matching_list(a, b):
    ans = []
    for k in range(min(a, b) + 1):
        for left in combinations(range(a), k):
            for right in combinations(range(b), k):
                for assignment in permutations(right):
                    ans.append(frozenset(zip(left, assignment)))
    return ans


def are_adjacent(x, y):
    edges = x ^ y
    if not edges:
        return False
    neighbors = {}
    for i, j in edges:
        left, right = ('L', i), ('R', j)
        neighbors.setdefault(left, set()).add(right)
        neighbors.setdefault(right, set()).add(left)
    if any(len(nbrs) > 2 for nbrs in neighbors.values()):
        return False
    seen = set()
    todo = [next(iter(neighbors))]
    while todo:
        vertex = todo.pop()
        if vertex not in seen:
            seen.add(vertex)
            todo.extend(neighbors[vertex] - seen)
    return len(seen) == len(neighbors)


def falling(k, t):
    return factorial(k) // factorial(k-t)


def rank_degree(a, b, k):
    p, q = a-k, b-k
    alpha = sum(falling(k, t) for t in range(1, k+1))
    beta = sum(comb(k,t)*factorial(t-1) for t in range(2,k+1))
    return p*q + (p+1)*(q+1)*alpha + beta


def check(a, b):
    vertices = matching_list(a, b)
    actual = Counter()
    for i, x in enumerate(vertices):
        for y in vertices[i+1:]:
            if are_adjacent(x, y):
                actual[x] += 1
                actual[y] += 1
    for k in range(min(a, b)+1):
        observed = [actual[x] for x in vertices if len(x) == k]
        expected = rank_degree(a,b,k)
        assert len(observed) == comb(a,k)*comb(b,k)*factorial(k), (a,b,k)
        assert all(t == expected for t in observed), (a,b,k,expected,set(observed))
    return len(vertices)


def main():
    tested = 0
    for a,b in [(1,1),(1,4),(2,2),(2,3),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)]:
        count=check(a,b)
        tested+=count
        print('PASS',a,b,'vertices',count,'degrees', [rank_degree(a,b,k) for k in range(min(a,b)+1)])
    for a in range(1,41):
        for b in range(a,41):
            seq = [rank_degree(a,b,k) for k in range(a+1)]
            if a == 1:
                assert len(set(seq)) == 1
            elif a == b == 2:
                assert seq[0] < seq[1] == seq[2]
            else:
                assert all(x<y for x,y in zip(seq,seq[1:]))
    print('VERIFY_OK vertex_count',tested,'integer_pairs',820)

if __name__ == '__main__':
    main()
