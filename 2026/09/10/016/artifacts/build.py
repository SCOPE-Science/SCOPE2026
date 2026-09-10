"""Build two baseline edge lists on V0 = {0..62} (Steiner order 63, STS bound M=651).
G*: random-order greedy maximal Pasch+triangle-free partial STS (high-girth-regime proxy).
H*: Bose-priority greedy maximal Pasch-free partial STS (algebraic/weaving-regime proxy).
Both Pasch-free => Fano-free (lemma in verify.py). Uses only stdlib.
"""
import random, json, itertools, sys

V = 63
ALL_TRIPLES = list(itertools.combinations(range(V), 3))

def build(order, forbid_triangle):
    pair_edge = {}          # (a,b) a<b -> edge idx
    edges = []              # list of (x,y,z)
    eset = set()            # sorted tuple set for O(1) lookup
    vtx_edges = [[] for _ in range(V)]  # edge indices through vertex
    def edge_through(a, b):
        if a > b: a, b = b, a
        return pair_edge.get((a, b), -1)
    n_pasch_blocks = 0
    n_tri_blocks = 0
    for (x, y, z) in order:
        if (x, y) in pair_edge or (x, z) in pair_edge or (y, z) in pair_edge:
            continue
        # Pasch completion check: exists e1={x,a,b}, e2={y,a,c} with {z,b,c} present.
        # Linearity => pair determines edge, so loop e1 through x only.
        pasch = False
        for e1 in vtx_edges[x]:
            (a, b) = (e for e in edges[e1] if e != x)
            for (p, q) in ((a, b), (b, a)):
                # need edge through y containing p: pair (y,p)
                e2 = edge_through(y, p)
                if e2 < 0:
                    continue
                c = [e for e in edges[e2] if e != y and e != p]
                if len(c) != 1:
                    continue
                c = c[0]
                if c == z or c == q or q == z:
                    continue
                t = tuple(sorted((z, q, c)))
                if t in eset:
                    pasch = True
                    break
            if pasch:
                break
        if pasch:
            n_pasch_blocks += 1
            continue
        if forbid_triangle:
            # Berge-C3 containing T: e1,e2 existing, e1 cap T={u}, e2 cap T={v}, u!=v,
            # e1 cap e2 = {w} single vertex outside T.
            tri = False
            T = (x, y, z)
            Tset = {x, y, z}
            for (u, v) in ((x, y), (x, z), (y, x), (y, z), (z, x), (z, y)):
                for e1 in vtx_edges[u]:
                    eu = edges[e1]
                    if eu[0] == v or eu[1] == v or eu[2] == v:
                        continue  # must meet T only in u (linearity already excludes pairs)
                    for w in (e for e in eu if e != u):
                        e2 = edge_through(v, w)
                        if e2 < 0:
                            continue
                        ev = edges[e2]
                        if any(t in Tset for t in ev if t != v and t != w):
                            continue
                        # e1 cap e2 must be exactly {w}: check no other common vertex
                        common = [t for t in ev if t == u or (t in eu and t != w)]
                        # u in ev? ev contains v,w + one more; u excluded since pair (u,v) free
                        if len([t for t in eu if t in ev]) == 1:
                            tri = True
                            break
                    if tri:
                        break
                if tri:
                    break
            if tri:
                n_tri_blocks += 1
                continue
        ei = len(edges)
        edges.append((x, y, z))
        eset.add((x, y, z))
        pair_edge[(x, y)] = ei
        pair_edge[(x, z)] = ei
        pair_edge[(y, z)] = ei
        vtx_edges[x].append(ei)
        vtx_edges[y].append(ei)
        vtx_edges[z].append(ei)
    return edges, n_pasch_blocks, n_tri_blocks

def bose_priority():
    # Bose triples first (algebraic skeleton), then all others in cyclic-gap lex order.
    MOD = 21
    inv2 = 11  # 2*11=22=1 mod 21
    def circ(a, b):
        return (a + b) * inv2 % MOD
    bose = set()
    for i in range(MOD):
        bose.add(tuple(sorted((i * 3 + 0, i * 3 + 1, i * 3 + 2))))  # placeholder mapping below
    # vertex map: (i,a) -> i*3+a
    bose = set()
    for i in range(MOD):
        bose.add((i * 3 + 0, i * 3 + 1, i * 3 + 2))
    for xx in range(MOD):
        for yy in range(xx + 1, MOD):
            z = circ(xx, yy)
            for a in range(3):
                t = tuple(sorted((xx * 3 + a, yy * 3 + a, z * 3 + ((a + 1) % 3))))
                bose.add(t)
    rest = [t for t in ALL_TRIPLES if t not in bose]
    def gapkey(t):
        d1 = (t[1] - t[0]) % V
        d2 = (t[2] - t[1]) % V
        d3 = (t[0] - t[2]) % V
        return tuple(sorted((d1, d2, d3)))
    rest.sort(key=gapkey)
    return sorted(bose) + rest, len(bose)

def main():
    import sys as _s
    dest = _s.argv[1] if len(_s.argv) > 1 else None
    mode = _s.argv[2] if len(_s.argv) > 2 else 'both'
    out = {}
    rng = random.Random(20260907)
    rorder = ALL_TRIPLES[:]
    rng.shuffle(rorder)
    Ged, pb, tb = build(rorder, forbid_triangle=False)
    bose_order, nbose = bose_priority()
    Hed, pb2, tb2 = build(bose_order, forbid_triangle=False)
    if dest and mode in ('both', 'G'):
        with open(dest, 'w') as f:
            json.dump({'V': V, 'G': Ged, 'H': Hed, 'mode': 'G-paschfree-random',
                       'pb_G': pb}, f)
    if dest and mode == 'both':
        pass
    M = V * (V - 1) // 6
    print(f"V={V} STSbound={M}")
    print(f"G: e={len(Ged)} defect={M-len(Ged)} rho={6*len(Ged)/V**2:.4f} pasch_blocks={pb} tri_blocks={tb}")
    print(f"H: e={len(Hed)} defect={M-len(Hed)} rho={6*len(Hed)/V**2:.4f} pasch_blocks={pb2} (tri allowed)")
    print(f"H: bose triples available={nbose}")
    sG = set(map(tuple, Ged)); sH = set(map(tuple, Hed))
    print(f"symdiff={len(sG ^ sH)} threshold={V*V/200:.2f}")

if __name__ == '__main__':
    main()
