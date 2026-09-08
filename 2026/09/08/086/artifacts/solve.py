"""Solver: exact Grundy DP for octal .07 (edge-deletion) and .007 (triple-deletion)
lifted to graph boards, over stars S(a,b,c) and bistars B((a,b),(c,d)).

Rules (graph lift per Dailly et al. Def 5):
  .07 : delete any connected 2-set (= any edge's endpoints); remainder arbitrary.
  .007: delete any connected 3-set (= center + 2 distinct neighbors in a tree);
        remainder arbitrary.
Position Grundy = xor of component Grundies. P iff Grundy == 0.
"""
import json, itertools, sys
from functools import lru_cache

# ---------- graph construction ----------
def star(a, b, c):
    """Center 0; arms are chains of given lengths. Returns (n, edges)."""
    edges = []
    nxt = 1
    for L in (a, b, c):
        prev = 0
        for _ in range(L):
            edges.append((prev, nxt))
            prev = nxt
            nxt += 1
    return (nxt, tuple(edges))

def bistar(a, b, c, d):
    """Centers u=0, v=1, edge u-v; u has arms a,b; v has arms c,d."""
    u, v = 0, 1
    edges = [(u, v)]
    nxt = 2
    for center, L in ((u, a), (u, b), (v, c), (v, d)):
        prev = center
        for _ in range(L):
            edges.append((prev, nxt))
            prev = nxt
            nxt += 1
    return (nxt, tuple(edges))

def path_graph(n):
    return (n, tuple((i, i + 1) for i in range(n - 1)))

def adj_of(n, edges):
    adj = [set() for _ in range(n)]
    for x, y in edges:
        adj[x].add(y)
        adj[y].add(x)
    return adj

def components(n, edges, removed):
    """Connected components of G minus removed set. Returns list of frozenset-of-verts."""
    rem = set(removed)
    adj = adj_of(n, edges)
    seen = set()
    comps = []
    for s in range(n):
        if s in rem or s in seen:
            continue
        stack = [s]
        seen.add(s)
        comp = [s]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y in rem or y in seen:
                    continue
                seen.add(y)
                stack.append(y)
                comp.append(y)
        comps.append(frozenset(comp))
    return comps

# ---------- canonical forms (AHU) ----------
def rooted_canon(adj, root, parent):
    kids = []
    for y in adj[root]:
        if y == parent:
            continue
        kids.append(rooted_canon(adj, y, root))
    kids.sort()
    return (tuple(kids),)

def tree_canon(verts, edges):
    verts = list(verts)
    if len(verts) == 1:
        return (0,)
    idx = {v: i for i, v in enumerate(verts)}
    m = len(verts)
    adj = [[] for _ in range(m)]
    for x, y in edges:
        adj[idx[x]].append(idx[y])
        adj[idx[y]].append(idx[x])
    # leaf stripping to find centers
    deg = [len(a) for a in adj]
    import collections
    q = collections.deque([i for i in range(m) if deg[i] <= 1])
    removed = [False] * m
    nrem = m
    while nrem > 2:
        for _ in range(len(q)):
            i = q.popleft()
            if removed[i]:
                continue
            removed[i] = True
            nrem -= 1
            for j in adj[i]:
                if not removed[j]:
                    deg[j] -= 1
                    if deg[j] <= 1:
                        q.append(j)
    centers = [i for i in range(m) if not removed[i]]
    # map back to original labels
    rev = {i: verts[i] for i in range(m)}
    adjO = {v: set() for v in verts}
    for x, y in edges:
        adjO[x].add(y)
        adjO[y].add(x)
    if len(centers) == 1:
        return ('T', rooted_canon(adjO, rev[centers[0]], None))
    else:
        c1, c2 = rev[centers[0]], rev[centers[1]]
        r1 = rooted_canon(adjO, c1, c2)
        r2 = rooted_canon(adjO, c2, c1)
        return ('T', tuple(sorted((r1, r2))))

def forest_key(n, edges, alive=None):
    """Canonical key of forest induced by alive vertices (None = all)."""
    if alive is None:
        alive = frozenset(range(n))
    else:
        alive = frozenset(alive)
    if not alive:
        return ()
    eset = tuple((x, y) for (x, y) in edges if x in alive and y in alive)
    adj = {v: set() for v in alive}
    for x, y in eset:
        adj[x].add(y)
        adj[y].add(x)
    seen = set()
    keys = []
    for s in alive:
        if s in seen:
            continue
        stack = [s]
        seen.add(s)
        comp = [s]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
                    comp.append(y)
        keys.append(tree_canon(comp, eset))
    keys.sort()
    return tuple(keys)

class Game:
    def __init__(self, code):
        assert code in ('.07', '.007')
        self.code = code
        self.memo = {}

    def moves(self, n, edges, alive):
        """Yield removed-vertex-tuples for all legal moves on the alive subgraph."""
        alive = set(alive)
        if self.code == '.07':
            for (x, y) in edges:
                if x in alive and y in alive:
                    yield (x, y)
        else:
            adj = {v: [] for v in alive}
            for (x, y) in edges:
                if x in alive and y in alive:
                    adj[x].append(y)
                    adj[y].append(x)
            for c in alive:
                nb = adj[c]
                if len(nb) >= 2:
                    for i in range(len(nb)):
                        for j in range(i + 1, len(nb)):
                            yield (c, nb[i], nb[j])

    def grundy_key(self, key, n, edges, alive):
        if key in self.memo:
            return self.memo[key]
        if not alive:
            self.memo[key] = 0
            return 0
        # split into components; xor
        # find components
        alive = frozenset(alive)
        eset = [(x, y) for (x, y) in edges if x in alive and y in alive]
        adj = {v: set() for v in alive}
        for x, y in eset:
            adj[x].add(y)
            adj[y].add(x)
        seen = set()
        comps = []
        for s in alive:
            if s in seen:
                continue
            stack = [s]
            seen.add(s)
            comp = [s]
            while stack:
                x = stack.pop()
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
                        comp.append(y)
            comps.append(frozenset(comp))
        if len(comps) > 1:
            g = 0
            for cp in comps:
                g ^= self.grundy_key(forest_key(n, edges, cp), n, edges, cp)
            self.memo[key] = g
            return g
        # connected: mex of option xors
        opts = set()
        for mv in self.moves(n, edges, alive):
            rem = set(mv)
            rest = alive - rem
            if not rest:
                opts.add(0)
                continue
            g = 0
            # components of rest
            seen2 = set()
            for s in rest:
                if s in seen2:
                    continue
                stack = [s]
                seen2.add(s)
                comp = [s]
                while stack:
                    x = stack.pop()
                    for y in adj[x]:
                        if y in rest and y not in seen2:
                            seen2.add(y)
                            stack.append(y)
                            comp.append(y)
                cp = frozenset(comp)
                g ^= self.grundy_key(forest_key(n, edges, cp), n, edges, cp)
            opts.add(g)
        g = 0
        while g in opts:
            g += 1
        self.memo[key] = g
        return g

    def solve_connected(self, n, edges):
        alive = frozenset(range(n))
        key = forest_key(n, edges, alive)
        g = self.grundy_key(key, n, edges, alive)
        # gather witness info
        adj = adj_of(n, edges)
        if g != 0:
            # find winning move (option xor 0), prefer bridge move if present
            for mv in self.moves(n, edges, alive):
                rest = alive - set(mv)
                if not rest:
                    ox = 0
                else:
                    ox = 0
                    seen2 = set()
                    for s in rest:
                        if s in seen2:
                            continue
                        stack = [s]
                        seen2.add(s)
                        comp = [s]
                        while stack:
                            x = stack.pop()
                            for y in adj[x]:
                                if y in rest and y not in seen2:
                                    seen2.add(y)
                                    stack.append(y)
                                    comp.append(y)
                        cp = frozenset(comp)
                        ox ^= self.grundy_key(forest_key(n, edges, cp), n, edges, cp)
                if ox == 0:
                    return g, {'move': sorted(mv), 'rest_xor': ox}
            raise RuntimeError('N-position without winning move?!')
        else:
            # P: record number of options (exhaustiveness checked by verifier)
            nopts = sum(1 for _ in self.moves(n, edges, alive))
            return g, {'n_options': nopts}

def enum_stars(L=6):
    out = []
    for a in range(L + 1):
        for b in range(a, L + 1):
            for c in range(b, L + 1):
                out.append((a, b, c))
    return out

def enum_sides(L=6):
    out = []
    for a in range(L + 1):
        for b in range(a, L + 1):
            out.append((a, b))
    return out

def enum_bistars(L=6):
    sides = enum_sides(L)
    out = []
    for i, s1 in enumerate(sides):
        for s2 in sides[i:]:
            out.append((s1, s2))
    return out

def main():
    results = {}
    for code in ('.07', '.007'):
        G = Game(code)
        tab = {'stars': {}, 'bistars': {}}
        for (a, b, c) in enum_stars():
            n, e = star(a, b, c)
            g, w = G.solve_connected(n, e)
            tab['stars'][f'{a},{b},{c}'] = {'grundy': g,
                                            'outcome': 'P' if g == 0 else 'N',
                                            'witness': w}
        for (s1, s2) in enum_bistars():
            n, e = bistar(s1[0], s1[1], s2[0], s2[1])
            g, w = G.solve_connected(n, e)
            tab['bistars'][f'{s1[0]},{s1[1]};{s2[0]},{s2[1]}'] = {
                'grundy': g, 'outcome': 'P' if g == 0 else 'N', 'witness': w}
        results[code] = tab
        with open(f'tables_{code[1:]}.json', 'w') as f:
            json.dump(tab, f)
        # summary
        sp = sum(1 for v in tab['stars'].values() if v['outcome'] == 'P')
        bp = sum(1 for v in tab['bistars'].values() if v['outcome'] == 'P')
        print(f'{code}: stars P={sp}/84 N={84-sp}; bistars P={bp}/406 N={406-bp}; '
              f'memo states={len(G.memo)}')
        # symmetric bistar check
        for (s1, s2) in enum_bistars():
            if s1 == s2:
                o = tab['bistars'][f'{s1[0]},{s1[1]};{s2[0]},{s2[1]}']['outcome']
                print(f'  sym {s1} x {s2}: {o}')
                break
    # check symmetric lemma status quickly
    for code in ('.07', '.007'):
        tab = results[code]
        sym = [(k, v['outcome']) for k, v in tab['bistars'].items()
               if k.split(';')[0] == k.split(';')[1]]
        from collections import Counter
        print(code, 'symmetric outcomes:', Counter(o for _, o in sym))

if __name__ == '__main__':
    main()
