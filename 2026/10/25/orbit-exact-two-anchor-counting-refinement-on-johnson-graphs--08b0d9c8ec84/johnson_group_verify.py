"""Independent small-case check via explicit pointwise-stabilizer permutations.

Uses direct binary adjacency, independent refinement code, and disjoint-set
orbits of a concrete automorphism group (coordinate permutations, plus
complementation when the ground-set size is twice the vertex weight).
Run: python johnson_group_verify.py
"""
from itertools import combinations, permutations
from collections import defaultdict, Counter


def test(n, k, r):
    vertices = [sum(1 << i for i in c) for c in combinations(range(n), k)]
    index = {v: j for j, v in enumerate(vertices)}
    A = (1 << k) - 1
    B = (1 << (k-r)) - 1
    for i in range(k, k+r):
        B |= 1 << i
    adj = [[j for j, w in enumerate(vertices) if i != j and
            (v & w).bit_count() == k - 1] for i, v in enumerate(vertices)]
    colors = [2] * len(vertices)
    colors[index[A]] = 0
    colors[index[B]] = 1
    while True:
        signatures = [(colors[i], tuple(sorted(Counter(colors[j] for j in nbr).items())))
                      for i, nbr in enumerate(adj)]
        mapping = {sig: z for z, sig in enumerate(sorted(set(signatures)))}
        updated = [mapping[sig] for sig in signatures]
        if len(set(updated)) == len(set(colors)):
            break
        colors = updated

    parent = list(range(len(vertices)))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        px, py = root(x), root(y)
        if px != py: parent[px] = py

    full_mask = (1 << n) - 1
    valid_actions = 0
    for p in permutations(range(n)):
        def move(v):
            out = 0
            for i, j in enumerate(p):
                if (v >> i) & 1:
                    out |= 1 << j
            return out
        pa, pb = move(A), move(B)
        for complement in (False, True) if n == 2*k else (False,):
            if (pa ^ (full_mask if complement else 0)) != A or \
               (pb ^ (full_mask if complement else 0)) != B:
                continue
            valid_actions += 1
            for i, v in enumerate(vertices):
                w = move(v) ^ (full_mask if complement else 0)
                union(i, index[w])
    orbits = defaultdict(set)
    for i, color in enumerate(colors):
        orbits[root(i)].add(color)
    assert all(len(s) == 1 for s in orbits.values())
    assert len(orbits) == len(set(colors))
    return len(vertices),len(orbits),valid_actions


def main():
    cases=0
    total=0
    for n in range(2,9):
        for k in range(1,n//2 + 1):
            for r in range(1,k+1):
                v,orbit,acts=test(n,k,r)
                cases+=1
                total+=v
                if (n,k,r) in {(6,3,1),(7,3,1),(8,4,2)}:
                    print('sample',n,k,r,'vertices',v,'orbits',orbit,'fixing_automorphisms',acts)
    print('GROUP_CHECKS_PASS')
    print('parameter_cases:',cases)
    print('total_vertex_instances:',total)

if __name__=='__main__':main()
