#!/usr/bin/env python3
"""Exact integral carrier computation for the ordinary matching complex of GP(8,3).

Only Python's standard library is required. All simplices, chain signs,
Morse cancellations, graph symmetries, and lattice minors are recomputed.
"""
from collections import defaultdict, deque
from functools import lru_cache
from itertools import combinations
from fractions import Fraction
from math import gcd

MORSE_VERTEX_ORDER = (20,22,7,0,3,15,6,21,13,23,8,17,10,12,16,18,11,4,5,9,2,1,14,19)
# Orbit representative index: (size, integral rank, column indices, row indices, determinant).
ORBIT_WITNESSES = {
 0:(96,8,(61,450,337,64,190,261,683,408),(0,1,2,3,4,5,6,7),1),
 1:(96,7,(499,836,135,113,298,512,738),(0,1,2,3,4,5,7),-1),
 2:(96,7,(95,628,667,213,55,112,524),(0,1,2,3,4,5,7),1),
 3:(96,7,(329,468,505,222,533,823,177),(0,1,2,3,4,5,7),1),
 4:(96,4,(188,751,449,56),(0,1,3,4),1),
 6:(96,8,(230,349,201,552,42,764,704,484),(0,1,2,3,4,5,6,7),-1),
 7:(96,8,(398,249,89,304,159,223,631,633),(0,1,2,3,4,5,6,7),1),
 9:(96,8,(815,114,902,409,557,758,196,357),(0,1,2,3,4,5,6,7),1),
 13:(96,7,(834,256,315,766,461,821,370),(0,1,2,3,4,5,7),1),
 17:(48,7,(598,773,526,246,145,400,375),(0,1,2,3,4,5,7),-1),
}

def graph_edges():
    n=8
    return sorted({tuple(sorted(e)) for i in range(n)
      for e in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+3)%n))})

def matchings(E):
    conflict=[]
    for a,b in E:
        conflict.append(sum(1<<j for j,(u,v) in enumerate(E) if a in (u,v) or b in (u,v)))
    family={0}
    for j in range(len(E)):
        family |= {s|(1<<j) for s in family if not(s&conflict[j])}
    return family

def oriented_sign(simplex,index):
    return -1 if (simplex & ((1<<index)-1)).bit_count() & 1 else 1

def all_hasse_acyclic(faces,pair_map):
    indeg={s:0 for s in faces}; outs=defaultdict(list); ncover=0
    for upper in faces:
        bits=upper
        while bits:
            b=bits&-bits;bits^=b
            lower=upper^b
            if not lower:continue
            ncover+=1
            src,dst=(lower,upper) if pair_map.get(lower)==upper else (upper,lower)
            outs[src].append(dst);indeg[dst]+=1
    q=deque(s for s in faces if indeg[s]==0);visited=0
    while q:
        src=q.popleft();visited+=1
        for dst in outs[src]:
            indeg[dst]-=1
            if indeg[dst]==0:q.append(dst)
    assert visited==len(faces) and ncover==53256

def exact_rank(vectors):
    # Rational row-echelon rank of columns, with exact Fraction arithmetic.
    echelon={}
    for a in vectors:
        v=[Fraction(t) for t in a]
        for p in sorted(echelon):
            c=v[p]
            if c:v=[x-c*y for x,y in zip(v,echelon[p])]
        nz=next((j for j,t in enumerate(v) if t),None)
        if nz is not None:
            c=v[nz];echelon[nz]=[t/c for t in v]
    return len(echelon)

def determinant(A):
    # Bareiss fraction-free determinant (all entries and divisions integral).
    B=[list(map(int,row)) for row in A];n=len(B)
    assert all(len(row)==n for row in B)
    if not n:return 1
    sign=1;previous=1
    for k in range(n-1):
        pivot=B[k][k]
        if pivot==0:
            p=next((i for i in range(k+1,n) if B[i][k]),None)
            if p is None:return 0
            B[k],B[p]=B[p],B[k];sign=-sign;pivot=B[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=B[i][j]*pivot-B[i][k]*B[k][j]
                assert num%previous==0
                B[i][j]=num//previous
        for i in range(k+1,n):B[i][k]=0
        previous=pivot
    return sign*B[-1][-1]

def automorphisms(E):
    neighbors=[set() for _ in range(16)]
    for u,v in E:
        neighbors[u].add(v);neighbors[v].add(u)
    maps=[]
    def extend(mapping,used):
        if len(mapping)==16:
            maps.append(tuple(mapping[i] for i in range(16)));return
        unassigned=[i for i in range(16) if i not in mapping]
        u=min(unassigned,key=lambda i:(-len(neighbors[i]&mapping.keys()),i))
        candidates=[v for v in range(16) if v not in used and
          all((j in neighbors[u]) == (mapping[j] in neighbors[v]) for j in mapping)]
        for v in candidates:
            mapping[u]=v;used.add(v)
            extend(mapping,used)
            used.remove(v);del mapping[u]
    extend({},set())
    assert len(maps)==96 and len(set(maps))==96
    return maps

def main():
    E=graph_edges();assert len(E)==24
    family=matchings(E);assert len(family)==11068
    cells=family-{0};bydim=defaultdict(list)
    for s in cells:bydim[s.bit_count()-1].append(s)
    assert tuple(len(bydim[i]) for i in range(8))==(24,228,1096,2826,3816,2444,600,33)

    pending=set(cells);matched={}
    for j in MORSE_VERTEX_ORDER:
        b=1<<j
        for small in sorted(pending):
            big=small|b
            if not small&b and small in pending and big in pending:
                matched[small]=big;pending.remove(small);pending.remove(big)
    assert len(matched)==5525
    critical=defaultdict(list)
    for s in pending:critical[s.bit_count()-1].append(s)
    for vals in critical.values():vals.sort()
    assert {d:len(vals) for d,vals in critical.items()}=={0:1,4:10,5:6}
    all_hasse_acyclic(cells,matched)
    upper=set(matched.values());crit4=critical[4];crit5=critical[5]
    rowno={s:i for i,s in enumerate(crit4)}

    @lru_cache(None)
    def projection(s):
        # Algebraic cancellation on a 4-cell; critical 4-cells form the coordinates.
        if s in pending:return {s:1} if s in rowno else {}
        if s in upper:return {}
        top=matched[s]
        j=(top^s).bit_length()-1
        ans={}
        for t in range(24):
            if not(top>>t&1) or t==j:continue
            cf=-oriented_sign(top,j)*oriented_sign(top,t)
            for r,val in projection(top^(1<<t)).items():
                ans[r]=ans.get(r,0)+cf*val
        return {r:val for r,val in ans.items() if val}

    def project(c):
        out=[0]*10
        for s,a in c.items():
            for u,b in projection(s).items():out[rowno[u]]+=a*b
        return tuple(out)

    def boundary(s):
        ans={}
        for j in range(24):
            if s>>j&1:
                t=s^(1<<j);ans[t]=ans.get(t,0)+oriented_sign(s,j)
        return ans

    matrix=[project(boundary(s)) for s in crit5]
    # This gives two primitive independent boundary columns, hence H_4 = Z^8.
    z=(0,)*10
    col0=(0,0,0,0,0,1,0,1,0,0)
    col3=(0,1,0,1,0,0,0,0,-1,0)
    assert matrix==[col0,z,z,col3,col0,z]

    paths=[];edgepoints=[set(e) for e in E]
    for a,b in combinations(range(24),2):
        if len(edgepoints[a]&edgepoints[b])==1:
            paths.append((a,b,edgepoints[a]|edgepoints[b]))
    assert len(paths)==48
    carriers=[]
    def enumerate_carriers(pos,used,selected):
        if len(selected)==5:
            carriers.append(tuple(selected));return
        for k in range(pos,len(paths)):
            a,b,V=paths[k]
            if not V&used:enumerate_carriers(k+1,used|V,selected+[(a,b)])
    enumerate_carriers(0,set(),[])
    assert len(carriers)==912

    qcoords=[]
    for c in carriers:
        chain={}
        for pick in range(32):
            selected=[pair[(pick>>i)&1] for i,pair in enumerate(c)]
            mask=sum(1<<i for i in selected)
            inversions=sum(selected[i]>selected[j] for i in range(5) for j in range(i+1,5))
            chain[mask]=(-1)**(pick.bit_count()+inversions)
        assert len(chain)==32
        B=defaultdict(int)
        for s,a in chain.items():
            for t,b in boundary(s).items():B[t]+=a*b
        assert all(b==0 for b in B.values())
        v=project(chain)
        # The critical 4-cell lattice modulo the two boundary vectors
        # has this explicit integral coordinate chart of rank 8.
        q=(v[0],v[2],v[3]-v[1],v[4],v[6],v[7]-v[5],v[8]+v[1],v[9])
        assert gcd(*q)==1
        qcoords.append(q)

    indexed={c:i for i,c in enumerate(carriers)}
    eindex={e:j for j,e in enumerate(E)}
    induced=[]
    for phi in automorphisms(E):
        induced.append(tuple(eindex[tuple(sorted((phi[a],phi[b])))] for a,b in E))
    unseen=set(range(912));orbits=[]
    while unseen:
        rep=min(unseen);c=carriers[rep];images=set()
        for action in induced:
            cc=tuple(sorted(tuple(sorted((action[a],action[b]))) for a,b in c))
            images.add(indexed[cc])
        assert rep in images
        orbits.append((rep,tuple(sorted(images))))
        unseen-=images
    assert len(orbits)==10
    got=[]
    for rep,orbit in orbits:
        size,rank,chosen,rows,expected_det=ORBIT_WITNESSES[rep]
        assert len(orbit)==size
        assert exact_rank(qcoords[j] for j in orbit)==rank
        assert all(j in orbit for j in chosen)
        A=[[qcoords[j][i] for j in chosen] for i in rows]
        assert determinant(A)==expected_det
        got.append((rep,size,rank))
    assert [x[0] for x in got]==sorted(ORBIT_WITNESSES)
    assert sorted(rank for _,_,rank in got)==[4,7,7,7,7,7,8,8,8,8]
    print('VERIFY_OK_MOBIUS_KANTOR_SHORTEST_CARRIERS')
    print('F_VECTOR 24 228 1096 2826 3816 2444 600 33')
    print('ACYCLIC_MORSE 5525_PAIRS CRITICAL_1_10_6 H4_Z8')
    print('DISJOINT_TWO_EDGE_PATHS_48 EXACT_OCTAHEDRAL_FOUR_SPHERES_912')
    print('EVERY_ONE_NONZERO_PRIMITIVE AUT_GROUP_96')
    print('ORBIT_REP_SIZE_RANK',got)
    print('FOUR_FULL_RANK_ORBITS_EACH_INTEGRAL_GENERATION')

if __name__=='__main__':main()
