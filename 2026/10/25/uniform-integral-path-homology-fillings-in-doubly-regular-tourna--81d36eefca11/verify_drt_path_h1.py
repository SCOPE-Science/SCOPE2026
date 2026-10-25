#!/usr/bin/env python3
"""Reproducible integer-chain checks for the first path homology of doubly regular tournaments.

Only standard Python is required. Every 2-chain constructed here is a sum of
transitive directed 2-paths, so its boundary lies in the allowed 1-chain lattice.
Finite checks illustrate, rather than replace, the general counting proof.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations


def paley_arcs(q):
    assert q % 4 == 3 and q > 3
    residues = {a*a % q for a in range(1,q)}
    return {(a,b) for a in range(q) for b in range(q)
            if a != b and (b-a)%q in residues}


def cyclic_arcs(q):
    half=(q-1)//2
    return {(a,b) for a in range(q) for b in range(q)
            if 1 <= (b-a)%q <= half}


def combine(*items):
    z=defaultdict(int)
    for coeff, v in items:
        for k, x in v.items():
            z[k] += coeff*x
    return {k:v for k,v in z.items() if v}


def oriented_edge(a,b,E):
    if (a,b) in E: return {(a,b):1}
    assert (b,a) in E
    return {(b,a):-1}


def triangle_cycle(a,b,c,E):
    return combine((1,oriented_edge(a,b,E)),
                   (1,oriented_edge(b,c,E)),
                   (1,oriented_edge(c,a,E)))


def boundary_path(a,b,c,E):
    assert (a,b) in E and (b,c) in E and (a,c) in E
    return {(a,b):1,(b,c):1,(a,c):-1}


def triangle_fill(a,b,c,q,E):
    target=triangle_cycle(a,b,c,E)
    # All three cyclic orders of a directed triangle are handled at once.
    if ((a,b) in E and (b,c) in E and (c,a) in E):
        seq=(a,b,c);sgn=1
    elif ((a,c) in E and (c,b) in E and (b,a) in E):
        seq=(a,c,b);sgn=-1
    else:
        # Enumerate transitive orders. The exterior 1-chain of an unordered
        # triangle is +/- the boundary of its unique transitive 2-path.
        for x,y,z in permutations((a,b,c)):
            if (x,y) in E and (y,z) in E and (x,z) in E:
                B=boundary_path(x,y,z,E)
                if target==B: return [(1,(x,y,z))]
                if target==combine((-1,B)): return [(-1,(x,y,z))]
        raise AssertionError('transitive order missing')
    x,y,z=seq
    for d in range(q):
        if d in (a,b,c): continue
        if all((d,u) in E for u in (x,y,z)):
            return [(sgn,(d,x,y)),(sgn,(d,y,z)),(sgn,(d,z,x))]
        if all((u,d) in E for u in (x,y,z)):
            return [(sgn,(x,y,d)),(sgn,(y,z,d)),(sgn,(z,x,d))]
    raise AssertionError('directed triangle has no dominating/dominated apex')


def verify(q):
    E=paley_arcs(q)
    t=(q-3)//4
    assert len(E)==q*(q-1)//2
    for x in range(q):
        assert sum((x,y) in E for y in range(q))==2*t+1
    for a,b in combinations(range(q),2):
        assert sum((a,w) in E and (b,w) in E for w in range(q))==t
        assert sum((w,a) in E and (w,b) in E for w in range(q))==t
    directed_cycles=0
    filling_length=Counter()
    for a,b,c in combinations(range(q),3):
        if ((a,b) in E and (b,c) in E and (c,a) in E) or \
           ((a,c) in E and (c,b) in E and (b,a) in E):
            directed_cycles+=1
            apex=sum((all((d,u) in E for u in (a,b,c)) or
                     all((u,d) in E for u in (a,b,c)))
                     for d in range(q) if d not in (a,b,c))
            assert apex==t,(q,(a,b,c),apex,t)
        fill=triangle_fill(a,b,c,q,E)
        bdy=defaultdict(int)
        for s,(x,y,z) in fill:
            assert (x,y) in E and (y,z) in E and (x,z) in E
            for edge,coef in boundary_path(x,y,z,E).items():
                bdy[edge]+=s*coef
        assert {k:v for k,v in bdy.items() if v}==triangle_cycle(a,b,c,E)
        filling_length[len(fill)]+=1
    # The triangles through vertex 0 form an INTEGRAL basis of the cycle
    # lattice: each has a unique non-star edge with coefficient +/-1.
    # The checks above therefore give a filling for every integer 1-cycle.
    for a,b in combinations(range(1,q),2):
        fill=triangle_fill(0,a,b,q,E)
        assert len(fill) in (1,3)
    assert directed_cycles==q*(q*q-1)//24
    print(f'PALEY_{q} doubly_regular_t={t} directed_triangles={directed_cycles} '
          f'triangle_fill_lengths={dict(sorted(filling_length.items()))} '
          f'integral_cycle_generators={(q-1)*(q-2)//2}')


def rank_mod_vectors(vectors,p):
    basis={}
    for vv in vectors:
        v={k:(c%p) for k,c in vv.items() if c%p}
        while v:
            k=min(v);c=v[k]
            if k not in basis:
                inv=pow(c,-1,p)
                basis[k]={j:cj*inv%p for j,cj in v.items() if cj*inv%p}
                break
            for j,cj in basis[k].items():
                x=(v.get(j,0)-c*cj)%p
                if x:v[j]=x
                else:v.pop(j,None)
    return len(basis)


def boundary_two_spans(E,q):
    edge_ids={e:i for i,e in enumerate(sorted(E))}
    gens=[]
    same_endpoints=defaultdict(list)
    for a,b,c in permutations(range(q),3):
        if (a,b) in E and (b,c) in E:
            if (a,c) in E:
                gens.append({edge_ids[(a,b)]:1, edge_ids[(b,c)]:1, edge_ids[(a,c)]:-1})
            else:
                same_endpoints[(a,c)].append(b)
    for (a,c), middles in same_endpoints.items():
        z=middles[0]
        for b in middles[1:]:
            gen=defaultdict(int)
            for e,sgn in [((a,b),1),((b,c),1),((a,z),-1),((z,c),-1)]:
                gen[edge_ids[e]]+=sgn
            gens.append({k:v for k,v in gen.items() if v})
    return gens


if __name__ == '__main__':
    for q in (7,11,19,23,31):verify(q)
    for name,E in [('Paley_7',paley_arcs(7)),('cyclic_7',cyclic_arcs(7)),
                   ('Paley_11',paley_arcs(11))]:
        gens=boundary_two_spans(E,len({x for e in E for x in e}))
        q=len({x for e in E for x in e})
        cycle_rank=len(E)-q+1
        ranks={p:rank_mod_vectors(gens,p) for p in (2,3,5,101)}
        h1={p:cycle_rank-r for p,r in ranks.items()}
        print(f'CHAIN_RANK {name} cycle_rank={cycle_rank} boundary2_mod_p={ranks} h1_mod_p={h1}')
        if name.startswith('Paley'):assert all(r==cycle_rank for r in ranks.values())
        else:assert all(r==cycle_rank-1 for r in ranks.values())
    print('VERIFY_OK_DRT_INTEGRAL_PATH_H1')
