"""Exact noncrossing-dissection census and orbit refinement of even polygons.
Python 3 standard library only; all graphs in the proof are covered.
"""
from collections import Counter, defaultdict

def crossing(e, f):
    a, b = e; c, d = f
    return len({a, b, c, d}) == 4 and ((a < c < b) != (a < d < b))

def chords(n):
    return [(a, b) for a in range(n) for b in range(a + 2, n)
            if (b - a) % 2 == 1 and (a, b) != (0, n - 1)]

def all_dissections(n):
    E = chords(n)
    forbidden = [sum(1 << j for j in range(i+1, len(E))
                     if crossing(E[i], E[j])) for i in range(len(E))]
    def visit(i, blocked, mask):
        if i == len(E):
            yield tuple(E[j] for j in range(len(E)) if mask & (1 << j))
            return
        yield from visit(i + 1, blocked, mask)
        if not blocked & (1 << i):
            yield from visit(i + 1, blocked | forbidden[i], mask | (1 << i))
    yield from visit(0, 0, 0)

def dihedral_images(n, edges):
    for slope in (1, -1):
        for shift in range(n):
            mapping = tuple((slope * i + shift) % n for i in range(n))
            mapped = tuple(sorted(tuple(sorted((mapping[u], mapping[v]))) for u, v in edges))
            yield mapping, mapped

def standard(n, edges):
    return min(E for _, E in dihedral_images(n, edges))

def graph(n, edges):
    G = [set() for _ in range(n)]
    for i in range(n):
        j = (i + 1) % n
        G[i].add(j); G[j].add(i)
    for i, j in edges:
        G[i].add(j); G[j].add(i)
    return G

def refine(G):
    n = len(G)
    colors = [0] * n
    for r in range(n + 1):
        signatures = [(colors[v], tuple(sorted(Counter(colors[u] for u in G[v]).items())))
                      for v in range(n)]
        ids = {a:i for i,a in enumerate(sorted(set(signatures)))}
        nxt = [ids[a] for a in signatures]
        if len(set(nxt)) == len(set(colors)):
            return nxt, r
        colors = nxt
    raise RuntimeError('Unstable partition')

def orbit_partition(n, edges):
    edge_set = tuple(sorted(edges))
    parent = list(range(n))
    def root(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    auts = 0
    for mapping, mapped in dihedral_images(n, edges):
        if mapped != edge_set: continue
        auts += 1
        for x,y in enumerate(mapping):
            parent[root(x)] = root(y)
    return tuple(root(x) for x in range(n)), auts

def census(n):
    raw = 0; graphs = set(); counter = Counter(); bad = []
    for edges in all_dissections(n):
        raw += 1
        canon = standard(n, edges)
        if canon in graphs: continue
        graphs.add(canon)
        counter[len(canon)] += 1
        G = graph(n, canon)
        colors, r = refine(G)
        orbits, automorphisms = orbit_partition(n, canon)
        if any(colors[u] == colors[v] and orbits[u] != orbits[v]
               for u in range(n) for v in range(n)):
            bad.append((canon, sorted(Counter(colors).values()),
                        sorted(Counter(orbits).values()), automorphisms, r))
    return raw, len(graphs), dict(sorted(counter.items())), bad

def main():
    expected = {4:(1,1,0), 6:(4,2,0), 8:(21,4,0),
                10:(126,13,0),12:(818,48,1)}
    for n in expected:
        raw,num,by_chords,bad = census(n)
        print(f'n={n}: labeled={raw} dihedral_classes={num} '+
              f'failures={len(bad)} chord_distribution={by_chords}')
        if bad: print('unique_exception:', bad)
        assert (raw,num,len(bad)) == expected[n]
    print('PRIMARY_EXHAUSTIVE_PASS')

if __name__ == '__main__':
    main()
