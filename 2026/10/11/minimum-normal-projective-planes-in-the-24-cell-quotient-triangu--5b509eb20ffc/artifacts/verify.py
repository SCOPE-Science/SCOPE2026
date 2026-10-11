#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict

# Published vertex-transitive action 12^13 and the three facet-orbit representatives
# for the triangulation ^3 12^13_2 of RP^3 in Koehler--Lutz.
GEN_CYCLES = [
    [(1,5,9),(2,6,10),(3,7,11),(4,8,12)],
    [(1,10),(2,5),(3,12),(4,7),(6,9),(8,11)],
    [(1,7),(2,8),(3,9),(4,10),(5,11),(6,12)],
    [(1,11),(2,10),(3,9),(4,8),(5,7)],
]
FACET_REPS = [(1,2,3,5),(1,2,5,10),(1,2,10,11)]
EXPECTED_WEIGHT_ENUMERATOR = {
    21:60, 23:132, 25:144, 27:240, 29:360,
    31:408, 33:400, 35:240, 37:60, 39:4,
}
EXPECTED_MIN_ORBITS = [12,24,24]
EXPECTED_NORMAL_TYPES = {(18,11):24,(20,10):36}

def perm_from_cycles(cycles):
    p = {i:i for i in range(1,13)}
    for cyc in cycles:
        for a,b in zip(cyc, cyc[1:]+cyc[:1]):
            p[a] = b
    return tuple(p[i] for i in range(1,13))

def compose(p,q):
    return tuple(p[q[i]-1] for i in range(12))

def group_closure(gens):
    identity = tuple(range(1,13))
    G = {identity}
    frontier = [identity]
    while frontier:
        h = frontier.pop()
        for g in gens:
            k = compose(g,h)
            if k not in G:
                G.add(k)
                frontier.append(k)
    return G

def gf2_rank(rows):
    basis = {}
    for x in rows:
        y = x
        while y:
            p = y.bit_length()-1
            if p in basis:
                y ^= basis[p]
            else:
                basis[p] = y
                break
    return len(basis)

def rref_rows(rows, ncols):
    a = [x for x in rows if x]
    pivots = []
    r = 0
    for col in range(ncols-1,-1,-1):
        j = next((j for j in range(r,len(a)) if (a[j]>>col)&1), None)
        if j is None:
            continue
        a[r],a[j] = a[j],a[r]
        for k in range(len(a)):
            if k != r and ((a[k]>>col)&1):
                a[k] ^= a[r]
        pivots.append(col)
        r += 1
        if r == len(a):
            break
    return a[:r], pivots

def main():
    gens = [perm_from_cycles(c) for c in GEN_CYCLES]
    G = group_closure(gens)
    assert len(G) == 24

    facet_orbits = []
    facets = set()
    for rep in FACET_REPS:
        orb = {tuple(sorted(p[v-1] for v in rep)) for p in G}
        facet_orbits.append(len(orb))
        facets |= orb
    assert facet_orbits == [24,12,12]
    assert len(facets) == 48
    facets = sorted(facets)

    edges = sorted({e for f in facets for e in combinations(f,2)})
    triangles = sorted({t for f in facets for t in combinations(f,3)})
    assert (len(edges),len(triangles),len(facets)) == (60,96,48)
    eidx = {e:i for i,e in enumerate(edges)}

    triangle_equations = []
    for t in triangles:
        mask = 0
        for e in combinations(t,2):
            mask ^= 1 << eidx[tuple(sorted(e))]
        triangle_equations.append(mask)
    rank_delta1 = gf2_rank(triangle_equations)
    assert rank_delta1 == 48

    cob_gens = []
    for v in range(2,13):
        mask = 0
        for i,e in enumerate(edges):
            if v in e:
                mask |= 1 << i
        cob_gens.append(mask)
    rank_delta0 = gf2_rank(cob_gens)
    assert rank_delta0 == 11
    assert len(edges)-rank_delta1-rank_delta0 == 1

    # Construct a nullspace basis and select a cocycle outside the coboundaries.
    rr,pivots = rref_rows(triangle_equations,len(edges))
    free = [i for i in range(len(edges)) if i not in pivots]
    nullbasis = []
    for fvar in free:
        x = 1 << fvar
        for row,p in zip(rr,pivots):
            if ((row & x).bit_count() & 1):
                x |= 1 << p
        assert all(((row & x).bit_count() & 1) == 0 for row in triangle_equations)
        nullbasis.append(x)
    assert len(nullbasis) == 12

    B = set()
    for bits in range(1<<11):
        x = 0
        for j,g in enumerate(cob_gens):
            if (bits>>j)&1:
                x ^= g
        B.add(x)
    assert len(B) == 2048
    z0 = next(x for x in nullbasis if x not in B)
    nonzero_coset = {z0 ^ b for b in B}
    assert len(nonzero_coset) == 2048
    weight_enum = Counter(x.bit_count() for x in nonzero_coset)
    assert dict(sorted(weight_enum.items())) == EXPECTED_WEIGHT_ENUMERATOR
    minima = {x for x in nonzero_coset if x.bit_count()==21}
    assert len(minima) == 60

    def actmask(x,p):
        out = 0
        for i,e in enumerate(edges):
            if (x>>i)&1:
                ep = tuple(sorted((p[e[0]-1],p[e[1]-1])))
                out |= 1 << eidx[ep]
        return out

    unseen = set(minima)
    orbit_sizes = []
    while unseen:
        x = next(iter(unseen))
        orb = {actmask(x,p) for p in G}
        assert orb <= minima
        orbit_sizes.append(len(orb))
        unseen -= orb
    assert sorted(orbit_sizes) == EXPECTED_MIN_ORBITS

    tri_to_tets = defaultdict(list)
    for fi,f in enumerate(facets):
        for tri in combinations(f,3):
            tri_to_tets[tuple(sorted(tri))].append(fi)
    assert all(len(v)==2 for v in tri_to_tets.values())

    def normal_data(mask):
        active = [False]*len(facets)
        T=Q=0
        for fi,f in enumerate(facets):
            root=f[0]
            color={root:0}
            for v in f[1:]:
                color[v] = (mask >> eidx[tuple(sorted((root,v)))]) & 1
            for a,b in combinations(f,2):
                assert ((mask >> eidx[tuple(sorted((a,b)))]) & 1) == (color[a]^color[b])
            k=sum(color.values())
            if k in (1,3):
                T += 1
                active[fi] = True
            elif k==2:
                Q += 1
                active[fi] = True
            else:
                assert k in (0,4)
        adj=defaultdict(set)
        arc_count=0
        for tri,fis in tri_to_tets.items():
            vals=[(mask >> eidx[tuple(sorted(e))]) & 1 for e in combinations(tri,2)]
            s=sum(vals)
            assert s in (0,2)
            if s==2:
                a,b=fis
                assert active[a] and active[b]
                adj[a].add(b); adj[b].add(a)
                arc_count += 1
        actives=[i for i,a in enumerate(active) if a]
        assert actives
        seen={actives[0]}; stack=[actives[0]]
        while stack:
            u=stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        connected=(len(seen)==len(actives))
        V=mask.bit_count()
        F=T+Q
        E=arc_count
        chi=V-E+F
        assert E == (3*T+4*Q)//2
        return T,Q,chi,connected

    normal_types=Counter()
    for x in minima:
        T,Q,chi,connected=normal_data(x)
        assert chi==1 and connected
        normal_types[(T,Q)] += 1
    assert dict(normal_types) == EXPECTED_NORMAL_TYPES

    print("VERIFY_OK")
    print("f_vector=(12,60,96,48)")
    print("rank_delta1=48 rank_delta0=11 dim_H1_F2=1")
    print("nonzero_coset_size=2048 cosystole=21 minimizers=60")
    print("weight_enumerator=" + ",".join(f"{w}:{EXPECTED_WEIGHT_ENUMERATOR[w]}" for w in sorted(EXPECTED_WEIGHT_ENUMERATOR)))
    print("minimizer_orbits=12,24,24")
    print("normal_types=(18T,11Q):24;(20T,10Q):36 all_connected_chi1=yes")

if __name__ == '__main__':
    main()
