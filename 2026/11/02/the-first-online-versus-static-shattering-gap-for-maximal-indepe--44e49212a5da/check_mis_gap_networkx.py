"""Independent library-based cross-check for tree membership shattering (NetworkX)."""
import networkx as nx
from functools import lru_cache

expected = (1, 1, 1, 2, 3, 6, 11, 23)
for n in range(1, 9):
    gs = [nx.empty_graph(1)] if n == 1 else list(nx.nonisomorphic_trees(n))
    assert len(gs) == expected[n - 1]
    gaps = []
    for g in gs:
        vertices = list(g.nodes)
        # Derive maximality directly from NetworkX neighbor sets, without the mask recurrence.
        family = []
        for bits in range(2 ** n):
            chosen = {vertices[i] for i in range(n) if (bits >> i) & 1}
            if any(g.has_edge(u, v) for u in chosen for v in chosen if u < v):
                continue
            if any(v not in chosen and not any(g.has_edge(u, v) for u in chosen)
                   for v in vertices):
                continue
            family.append(frozenset(chosen))
        vc = 0
        for bits in range(1 << n):
            s = {vertices[i] for i in range(n) if (bits >> i) & 1}
            traces = {frozenset(c & s) for c in family}
            if len(traces) == 2 ** len(s):
                vc = max(vc, len(s))
        @lru_cache(None)
        def ldim(remaining):
            if len(remaining) <= 1:
                return 0
            best = 0
            for q in vertices:
                yes = frozenset(i for i in remaining if q in family[i])
                no = remaining - yes
                if yes and no:
                    best = max(best, 1 + min(ldim(no), ldim(yes)))
            return best
        lit = ldim(frozenset(range(len(family))))
        if lit > vc:
            seq = nx.to_prufer_sequence(g) if n >= 3 else []
            gaps.append((vc, lit, seq, sorted(dict(g.degree()).values(), reverse=True)))
    print('n', n, 'classes', len(gs), 'gaps', gaps)
    if n < 8:
        assert not gaps
    else:
        assert len(gaps) == 1 and gaps[0][:2] == (2, 3)
        assert gaps[0][3] == [3, 2, 2, 2, 2, 1, 1, 1]
print('NETWORKX_FOREST_MIS_GAP_CROSSCHECK_PASS')
