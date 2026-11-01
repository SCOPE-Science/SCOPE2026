#!/usr/bin/env python3
"""Exact finite matching-complex and integral Morse calculations for cyclic ladders.

Only Python's standard library is required. Every nonempty face is enumerated.
The matching and its directed-Hasse acyclicity are independently checked.
"""
from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import prod


def edge_table(n):
    # Bottom vertices 0,...,n-1; top vertices n,...,2n-1.
    e = set()
    for i in range(n):
        e.add(tuple(sorted((i, (i+1) % n))))
        e.add(tuple(sorted((n+i, n+(i+1) % n))))
        e.add((i, n+i))
    return sorted(e)


def valid_faces(n, edges):
    masks = [(1 << u) | (1 << v) for u, v in edges]
    out = set()
    def walk(i, used_vertices, used_edges):
        if i == len(edges):
            if used_edges:
                out.add(used_edges)
            return
        walk(i+1, used_vertices, used_edges)
        if not used_vertices & masks[i]:
            walk(i+1, used_vertices | masks[i], used_edges | (1 << i))
    walk(0, 0, 0)
    return out


def independent_second_enumeration(n, edges):
    # Different implementation: exhaust all edge subsets and inspect endpoints.
    vertex_masks = [(1<<u)|(1<<v) for u,v in edges]
    faces = set()
    for mask in range(1, 1 << len(edges)):
        used = 0
        x = mask
        while x:
            t = x & -x
            x -= t
            endpoint = vertex_masks[t.bit_length()-1]
            if used & endpoint:
                break
            used |= endpoint
        else:
            faces.add(mask)
    return faces


def greedy_pairs(faces, m):
    residual = faces.copy()
    pairs = []
    for j in range(m):
        bit = 1<<j
        for lower in sorted(residual):
            if lower & bit:
                continue
            upper = lower | bit
            if upper in residual:
                residual.remove(lower)
                residual.remove(upper)
                pairs.append((lower, upper))
    return pairs, residual


def boundary(face):
    # Orient the vertices of a simplex by increasing edge index.
    x = face
    out = []
    j = 0
    while x:
        t = x & -x
        x -= t
        if face != t:
            out.append((face ^ t, -1 if j % 2 else 1))
        j += 1
    return out


def validate_matching(faces, pairs, critical):
    seen = set(critical)
    assert len(critical) + 2*len(pairs) == len(faces)
    assert critical <= faces
    for lower, upper in pairs:
        assert lower in faces and upper in faces
        assert upper.bit_count() == lower.bit_count()+1
        assert (upper & lower) == lower
        assert lower not in seen and upper not in seen
        seen.update((lower,upper))
    assert seen == faces
    # Construct and completely topologically sort the directed Hasse diagram.
    # Unmatched incidences point downward; a matched incidence points upward.
    higher = {upper:lower for lower,upper in pairs}
    lower = {lower:upper for lower,upper in pairs}
    indeg = {f:0 for f in faces}
    adj = defaultdict(list)
    incidences = 0
    for upper in faces:
        for sub,_ in boundary(upper):
            incidences += 1
            if higher.get(upper) == sub:
                src,dst = sub,upper
            else:
                src,dst = upper,sub
            adj[src].append(dst)
            indeg[dst] += 1
    work = deque(f for f in faces if indeg[f]==0)
    visited = 0
    while work:
        u=work.popleft()
        visited+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                work.append(v)
    assert visited == len(faces), 'a directed Morse cycle exists'
    return incidences


def chain_ranks_mod2(faces):
    max_dim = max(f.bit_count()-1 for f in faces)
    layers = [[f for f in faces if f.bit_count()==d+1] for d in range(max_dim+1)]
    ranks = []
    for d in range(1,max_dim+1):
        low_index = {f:i for i,f in enumerate(sorted(layers[d-1]))}
        pivot = {}
        for face in layers[d]:
            x=0
            for sub,_ in boundary(face):
                x ^= 1<<low_index[sub]
            while x:
                k=x.bit_length()-1
                if k in pivot:
                    x ^= pivot[k]
                else:
                    pivot[k]=x
                    break
        ranks.append(len(pivot))
    fvector = [len(layer) for layer in layers]
    betti = [fvector[i] - (ranks[i] if i<len(ranks) else 0) -
             (ranks[i-1] if i else 0) for i in range(len(fvector))]
    return fvector, ranks, betti


def morse_boundaries(critical, pairs):
    lower_to_upper = dict(pairs)
    upper_to_lower = {b:a for a,b in pairs}

    @lru_cache(None)
    def project(face):
        if face in critical:
            return {face:1}
        if face in upper_to_lower:
            return {}
        upper = lower_to_upper[face]
        missing = upper ^ face
        inc = -1 if (upper & (missing-1)).bit_count()%2 else 1
        result = defaultdict(int)
        for other, coeff in boundary(upper):
            if other == face:continue
            for c,a in project(other).items():
                result[c] -= inc*coeff*a
        return {c:a for c,a in result.items() if a}

    result = {}
    dimensions = sorted(set(f.bit_count()-1 for f in critical))
    for d in dimensions:
        if d <= 0:continue
        ups = sorted(f for f in critical if f.bit_count()==d+1)
        lows = sorted(f for f in critical if f.bit_count()==d)
        matrix = []
        for upper in ups:
            coeffs = defaultdict(int)
            for f,coeff in boundary(upper):
                for c,a in project(f).items():
                    coeffs[c]+=coeff*a
            matrix.append([coeffs[f] for f in lows])
        result[d]=(ups,lows,matrix)
    return result


def matrix_rank_rational(matrix):
    if not matrix or not matrix[0]:return 0
    a=[[Fraction(v) for v in row] for row in matrix]
    nr,nc=len(a),len(a[0]);rank=0
    for c in range(nc):
        pivot=next((r for r in range(rank,nr) if a[r][c]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        v=a[rank][c]
        for j in range(c,nc):a[rank][j]/=v
        for r in range(nr):
            if r != rank:
                v=a[r][c]
                if v:
                    for j in range(c,nc):a[r][j]-=v*a[rank][j]
        rank+=1
        if rank==nr:break
    return rank


def det(a):
    if len(a)==1:return a[0][0]
    if len(a)==2:return a[0][0]*a[1][1]-a[0][1]*a[1][0]
    return sum(((-1)**j)*v*det([row[:j]+row[j+1:] for row in a[1:]])
               for j,v in enumerate(a[0]))


def unit_maximal_minor(matrix, rank):
    if rank == 0:return True,None
    for rset in combinations(range(len(matrix)),rank):
        for cset in combinations(range(len(matrix[0])),rank):
            val=det([[matrix[i][j] for j in cset] for i in rset])
            if abs(val)==1:return True,(rset,cset,val)
    return False,None


EXPECTED = {
 3: {'f':(9,18,4),'r':(8,4),'b':(1,6,0),'critical':{0:1,1:6},'pairs':12,'ranks':{}},
 4: {'f':(12,42,44,9),'r':(11,31,9),'b':(1,0,4,0),'critical':{0:1,2:4},'pairs':51,'ranks':{}},
 5: {'f':(15,75,145,95,11),'r':(14,61,82,11),'b':(1,0,2,2,0),'critical':{0:1,2:5,3:5},'pairs':165,'ranks':{3:3}},
 6: {'f':(18,117,336,420,192,20),'r':(17,100,236,172,20),'b':(1,0,0,12,0,0),'critical':{0:1,3:13,4:1},'pairs':544,'ranks':{4:1}},
}

def main():
    for n in EXPECTED:
        exp=EXPECTED[n]
        edges=edge_table(n)
        assert len(edges)==3*n
        faces=valid_faces(n,edges)
        assert faces==independent_second_enumeration(n,edges)
        fv,ranks,betti=chain_ranks_mod2(faces)
        assert tuple(fv)==exp['f'] and tuple(ranks)==exp['r']
        assert tuple(betti)==exp['b']
        assert all(all((f^t) in faces for t in [1<<j for j in range(len(edges)) if f&(1<<j)])
                   for f in faces if f.bit_count()>1)
        pairs,critical=greedy_pairs(faces,len(edges))
        assert len(pairs)==exp['pairs']
        assert dict(Counter(f.bit_count()-1 for f in critical))==exp['critical']
        incidence_count=validate_matching(faces,pairs,critical)
        mats=morse_boundaries(critical,pairs)
        rank_by_degree={}
        for d,(upper,lower,mat) in mats.items():
            rank=matrix_rank_rational(mat)
            if rank:
                assert len(lower)>0
                good,witness=unit_maximal_minor(mat,rank)
                assert good, 'Morse differential not unit-saturated'
                rank_by_degree[d]=rank
                print('n=',n,'Morse degree',d,'rows',upper,'columns',lower,'matrix',mat,'unit_minor',witness)
        assert rank_by_degree==exp['ranks']
        morse_fv=Counter(f.bit_count()-1 for f in critical)
        morse_betti=[morse_fv.get(d,0)-rank_by_degree.get(d,0)-rank_by_degree.get(d+1,0)
                     for d in range(len(fv))]
        assert morse_betti==betti
        euler = sum((-1)**d*c for d,c in enumerate(fv))
        assert euler == sum((-1)**d*c for d,c in morse_fv.items())
        print(f'n={n} edges={len(edges)} faces={len(faces)} fvector={fv} ' +
              f'boundary_ranks_F2={ranks} betti={betti} Morse_pairs={len(pairs)} ' +
              f'critical={dict(sorted(morse_fv.items()))} incidences={incidence_count} Euler={euler} OK')
    print('CYCLIC_LADDER_MATCHING_INTEGRAL_MORSE_VERIFIED')

if __name__=='__main__':main()
