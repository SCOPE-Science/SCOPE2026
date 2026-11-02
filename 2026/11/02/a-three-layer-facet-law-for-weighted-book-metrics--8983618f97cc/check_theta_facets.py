"""Exact finite checks for facet-count transitions in the shortcut theta metric.

Vertices are reconstructed from every spanning-tree set of tight constraints;
only feasible solutions are retained.  This is not a proof for all dimensions.
"""
from fractions import Fraction
from itertools import combinations, product


def edge_metric(n, t):
    # Index 0 is the base hub; 1 is the second hub; 2,...,n+1 are leaves.
    m = n + 2
    ed = []
    for i, j in combinations(range(m), 2):
        w = t if (i, j) == (0, 1) else (Fraction(2) if i >= 2 else Fraction(1))
        ed.append((i, j, w))
    return ed


def spanning_tree(edge_set, vertex_count):
    parent = list(range(vertex_count))
    def find(a):
        while a != parent[a]:
            a = parent[a]
        return a
    for i, j, _ in edge_set:
        x, y = find(i), find(j)
        if x == y:
            return False
        parent[x] = y
    return len({find(i) for i in range(vertex_count)}) == 1


def vertices_from_active_trees(n, t):
    t = Fraction(t)
    m = n + 2
    edges = edge_metric(n, t)
    solutions = set()
    tree_count = 0
    for inds in combinations(range(len(edges)), m-1):
        tree = [edges[k] for k in inds]
        if not spanning_tree(tree, m):
            continue
        tree_count += 1
        for signs in product((-1, 1), repeat=m-1):
            adj = [[] for _ in range(m)]
            for (i, j, w), sg in zip(tree, signs):
                adj[i].append((j, sg*w))
                adj[j].append((i, -sg*w))
            vals = [None]*m
            vals[0] = Fraction(0)
            q = [0]
            while q:
                i = q.pop()
                for j, inc in adj[i]:
                    if vals[j] is None:
                        vals[j] = vals[i] + inc
                        q.append(j)
            assert all(x is not None for x in vals)
            if all(abs(vals[i]-vals[j]) <= w for i,j,w in edges):
                solutions.add(tuple(vals))
    return solutions, tree_count


def classified_vertices(n, t):
    t = Fraction(t)
    candidates = set()
    for bits in product((0,1), repeat=n):
        # s=0, every leaf at -1 or +1
        candidates.add((Fraction(0),Fraction(0)) + tuple(2*b-1 for b in bits))
        # s=+t, leaf at t-1 or 1
        candidates.add((Fraction(0),t) + tuple(t-1 if not b else Fraction(1) for b in bits))
        # s=-t, leaf at -1 or 1-t
        candidates.add((Fraction(0),-t) + tuple(-Fraction(1) if not b else 1-t for b in bits))
    return candidates


def main():
    total = 0
    for n in (2, 3, 4):
        for t in (Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(7,4),Fraction(2)):
            v, trees = vertices_from_active_trees(n,t)
            predicted = classified_vertices(n,t)
            assert v == predicted, (n,t,len(v),len(predicted),v.symmetric_difference(predicted))
            target = 3*(2**n) if t < 2 else 2**n+2
            assert len(v) == target, (n,t,len(v),target)
            print(f"PASS n={n} t={t} vertices={len(v)} spanning_trees={trees}")
            total += 1
    print(f"EXACT_FINITE_CASES_PASS: {total}")

if __name__ == '__main__':
    main()
