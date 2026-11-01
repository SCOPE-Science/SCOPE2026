"""Exact finite verification of a parallel-path Hom-complex classification.

No third-party packages are required. Runs: python3 theta_hom_checker.py
"""
from collections import Counter, defaultdict, deque
from itertools import product


def network(lengths):
    assert len(lengths) >= 3 and all(L >= 2 for L in lengths)
    paths = []
    nxt = 2
    for L in lengths:
        p = [0] + list(range(nxt, nxt + L - 1)) + [1]
        nxt += L - 1
        paths.append(p)
    neighbors = [set() for _ in range(nxt)]
    for p in paths:
        for u, v in zip(p, p[1:]):
            neighbors[u].add(v)
            neighbors[v].add(u)
    return paths, neighbors


def winding_options(lengths, q):
    # Independent arithmetic enumeration of all integral winding vectors.
    ranges = [range(-L, L+1, 2) for L in lengths]
    counts = Counter()
    for ss in product(*ranges):
        if all((s-ss[0]) % q == 0 for s in ss):
            w = tuple((s-ss[0]) // q for s in ss[1:])
            counts[w] += 1
    return counts


def colorings(paths, neighbors, q):
    # Enumerate all homomorphisms independently via signed walks, fixing root 0,
    # then shifting by the target's rotational symmetry.
    by_branch = []
    for path in paths:
        L = len(path) - 1
        grouped = defaultdict(list)
        for increments in product((-1, 1), repeat=L):
            s = 0
            internal = []
            for a in increments[:-1]:
                s += a
                internal.append(s % q)
            s += increments[-1]
            grouped[s % q].append((tuple(internal), sum(increments)))
        by_branch.append(grouped)
    ans = set()
    for b in range(q):
        for entry in product(*(d[b] for d in by_branch)):
            base = [None] * len(neighbors)
            base[0] = 0
            base[1] = b
            for p, (interior, _) in zip(paths, entry):
                for v, c in zip(p[1:-1], interior):
                    base[v] = c
            for shift in range(q):
                ans.add(tuple((c + shift) % q for c in base))
    return sorted(ans)


def component_data(lengths, q):
    paths, neighbors = network(lengths)
    colors = colorings(paths, neighbors, q)
    index = {f: i for i, f in enumerate(colors)}
    assert len(index) == len(colors)
    def winds(f):
        ss = []
        for path in paths:
            inc = []
            for u,v in zip(path, path[1:]):
                diff = (f[v] - f[u]) % q
                assert diff in (1, q-1)
                inc.append(1 if diff == 1 else -1)
            ss.append(sum(inc))
        return tuple((s-ss[0])//q for s in ss[1:])
    winds_by_vertex = [winds(f) for f in colors]
    moves = []
    for i, f in enumerate(colors):
        adjacent = set()
        flippable = []
        for v in range(len(f)):
            admissible = set(range(q))
            for u in neighbors[v]:
                admissible &= {(f[u]-1)%q, (f[u]+1)%q}
            others = admissible-{f[v]}
            assert len(others) <= 1
            if others:
                alternative = others.pop()
                ff = list(f);ff[v] = alternative
                j = index[tuple(ff)]
                assert winds_by_vertex[j] == winds_by_vertex[i]
                adjacent.add(j)
                flippable.append((v,alternative))
        moves.append((adjacent,flippable))
    seen = set()
    components = []
    labels = [-1] * len(colors)
    for i in range(len(colors)):
        if i in seen: continue
        queue = deque([i]);seen.add(i);component=[]
        while queue:
            j=queue.popleft();component.append(j)
            for k in moves[j][0]:
                if k not in seen:
                    seen.add(k);queue.append(k)
        for j in component: labels[j]=len(components)
        assert len({winds_by_vertex[j] for j in component})==1
        components.append(component)
    cells = [Counter() for _ in components]
    for i, f in enumerate(colors):
        # Every cube has a unique lexicographically minimal corner.
        # The selected coordinates must be pairwise nonadjacent because C_q
        # contains no four-cycle for odd q>=5.
        choices = [(v,alt) for v,alt in moves[i][1] if f[v]<alt]
        for mask in range(1 << len(choices)):
            selected = [choices[k][0] for k in range(len(choices)) if (mask>>k)&1]
            if any(b in neighbors[a] for j,a in enumerate(selected) for b in selected[j+1:]):
                continue
            cells[labels[i]][len(selected)] += 1
    observed = defaultdict(list)
    for members,cell_hist in zip(components,cells):
        chi = sum((-1)**d*cnt for d,cnt in cell_hist.items())
        observed[winds_by_vertex[members[0]]].append((chi,len(members)))
    predicted = winding_options(lengths,q)
    assert set(observed) == set(predicted), (lengths,q,observed,predicted)
    for winding,t in predicted.items():
        found = observed[winding]
        assert len(found) == (1 if t >= 2 else q), (lengths,q,winding,t,found)
        assert all(chi == (0 if t >= 2 else 1) for chi,_ in found), (lengths,q,winding,t,found)
    return len(colors),len(components),sum(t>=2 for t in predicted.values()),sum(t==1 for t in predicted.values())*q,sum(sum(c.values()) for c in cells)


def main():
    cases = [
        (5,(2,2,2)), (5,(2,2,3)), (5,(2,3,3)), (5,(2,3,7)),
        (5,(3,3,3)), (5,(3,3,4)), (5,(3,4,6)), (5,(2,4,4)),
        (5,(2,3,4,4)), (5,(3,3,3,3)),
        (7,(2,3,4)), (7,(3,3,3)), (7,(3,4,6)), (7,(3,4,5)),
        (9,(4,4,4)), (9,(4,5,7)), (9,(4,4,5)),
        (7,(2,2,2,2)), (5,(2,2,3,3)),
    ]
    total_col = total_cells = 0
    for q,lengths in cases:
        a,b,c,d,e = component_data(lengths,q)
        print(f'q={q}, paths={lengths}, homomorphisms={a}, components={b}, circles={c}, points={d}, cells={e}')
        total_col += a;total_cells += e
    print(f'ALL_PARALLEL_PATH_HOM_CASES_PASS cases={len(cases)} colorings={total_col} cells={total_cells}')

if __name__=='__main__':
    main()
