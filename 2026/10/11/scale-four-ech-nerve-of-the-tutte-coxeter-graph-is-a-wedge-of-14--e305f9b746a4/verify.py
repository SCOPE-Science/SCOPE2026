#!/usr/bin/env python3
"""Reproduce an exact finite homotopy calculation for a symplectic quadrangle incidence graph."""
from itertools import combinations
from collections import Counter, deque


def perpendicular(a, b):
    return (((a & 1) * ((b >> 1) & 1)
             + ((a >> 1) & 1) * (b & 1)
             + ((a >> 2) & 1) * ((b >> 3) & 1)
             + ((a >> 3) & 1) * ((b >> 2) & 1)) % 2 == 0)


def construct():
    points = list(range(1, 16))
    lines = sorted({tuple(sorted((a, b, a ^ b)))
                    for a, b in combinations(points, 2) if perpendicular(a, b)})
    assert len(lines) == 15
    assert all(len(x) == 3 for x in lines)
    adj = [set() for _ in range(30)]
    for j, line in enumerate(lines):
        for a in line:
            adj[a - 1].add(j + 15)
            adj[j + 15].add(a - 1)
    assert all(len(row) == 3 for row in adj)
    assert all((x in adj[y]) == (y in adj[x]) for x in range(30) for y in range(30))
    # Verify GQ(2,2) axioms directly: unique line through perpendicular point pairs
    assert all(sum(a in row and b in row for row in lines) == int(perpendicular(a, b))
               for a,b in combinations(points,2))
    assert all(sum(perpendicular(p, a) for a in L) == 1
               for p in points for L in lines if p not in L)
    distance = []
    for root in range(30):
        d = [-1]*30
        d[root]=0
        q = deque([root])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if d[y] < 0:
                    d[y]=d[x]+1
                    q.append(y)
        assert -1 not in d
        distance.append(d)
    assert max(max(row) for row in distance) == 4
    # Girth 8: brute-force edge removal and shortest alternative paths
    g = 31
    for u in range(30):
        for v in adj[u]:
            if u >= v:
                continue
            d = [-1]*30
            d[u]=0
            q=deque([u])
            while q:
                x=q.popleft()
                for y in adj[x]:
                    if (x==u and y==v) or (x==v and y==u):
                        continue
                    if d[y] < 0:
                        d[y]=d[x]+1
                        q.append(y)
            assert d[v] >= 0
            g=min(g,d[v]+1)
    assert g==8
    return distance


def complexes(distance):
    # At radius 2 on a unit-edge metric graph, any center in an edge has a nearest
    # endpoint a; all graph vertices at distance at most 2 from that center
    # lie in N_2(a). Thus the maximal simplices are among the 30 closed
    # graph-distance-two vertex neighborhoods.
    facets=[sum(1 << i for i in range(30) if distance[z][i] <= 2)
            for z in range(30)]
    assert len(set(facets)) == 30
    assert all(f.bit_count() == 10 for f in facets)
    assert all(not ((a & b) == a) for a,b in combinations(facets,2))
    faces=set()
    for f in facets:
        s=f
        while s:
            faces.add(s)
            s=(s-1)&f
    assert len(faces)==27535
    fvec=[Counter(s.bit_count()-1 for s in faces)[d] for d in range(10)]
    assert fvec==[30,435,2620,5625,7290,6255,3600,1350,300,30], fvec
    return faces, facets, fvec


def matching(faces):
    # Fully specified stage-wise vertex toggle. Later stages operate only on
    # cells untouched in earlier stages; all actual pairs are checked below.
    remaining=set(faces)
    partner={}
    for v in range(30):
        bit=1<<v
        for s in tuple(remaining):
            if s not in remaining or s & bit:
                continue
            t=s | bit
            if t in remaining:
                assert t.bit_count() == s.bit_count()+1
                remaining.remove(s);remaining.remove(t)
                partner[s]=t
                partner[t]=s
    stats=Counter(s.bit_count()-1 for s in remaining)
    assert stats==Counter({0:1,2:144}), stats
    assert len(partner)//2==13695
    assert len(partner)+len(remaining)==len(faces)
    return remaining, partner


def check_acyclic(faces, partner):
    # Forman directed Hasse diagram: unmatched incidences down, paired edges up.
    degree={s:0 for s in faces}
    graph={s:[] for s in faces}
    incidence_count=0
    for s in faces:
        if s.bit_count()==1:
            continue
        t=s
        while t:
            bit=t&-t;t-=bit
            small=s^bit
            assert small in faces
            if partner.get(s)==small:
                src,dst=small,s
            else:
                src,dst=s,small
            graph[src].append(dst)
            degree[dst]+=1
            incidence_count+=1
    q=deque(s for s in faces if degree[s]==0)
    seen=0
    while q:
        s=q.popleft();seen+=1
        for t in graph[s]:
            degree[t]-=1
            if degree[t]==0:
                q.append(t)
    assert seen==len(faces), (seen,len(faces))
    assert incidence_count==sum((d+1)*f for d,f in enumerate(
        [30,435,2620,5625,7290,6255,3600,1350,300,30]) if d)
    return incidence_count


def check_low_degree_homology(faces):
    layers={d: sorted(s for s in faces if s.bit_count()==d+1) for d in range(4)}
    ranks={}
    for d in [1,2,3]:
        lows={s:i for i,s in enumerate(layers[d-1])}
        pivot={}
        for face in layers[d]:
            x=face;vec=0
            while x:
                bit=x&-x;x-=bit
                vec ^= 1<<lows[face^bit]
            while vec:
                bit=vec.bit_length()-1
                if bit in pivot:
                    vec ^= pivot[bit]
                else:
                    pivot[bit]=vec
                    break
        ranks[d]=len(pivot)
    assert ranks=={1:29,2:406,3:2070},ranks
    assert len(layers[2])-ranks[2]-ranks[3]==144
    return ranks


def main():
    D=construct()
    F,facets,fvec=complexes(D)
    crit,partners=matching(F)
    incidence_count=check_acyclic(F,partners)
    ranks=check_low_degree_homology(F)
    chi=sum((-1)**d*f for d,f in enumerate(fvec))
    assert chi==145
    print('VERIFY_OK')
    print('vertices=30 lines=15 girth=8 diameter=4 facets=30')
    print('f_vector='+str(fvec))
    print(f'nonempty_faces={len(F)} matched_pairs={len(partners)//2} Hasse_incidences={incidence_count}')
    print('critical_cells='+str(dict(sorted(Counter(s.bit_count()-1 for s in crit).items()))))
    print('boundary_ranks_mod2='+str(ranks)+' chi='+str(chi))

if __name__=='__main__':
    main()
