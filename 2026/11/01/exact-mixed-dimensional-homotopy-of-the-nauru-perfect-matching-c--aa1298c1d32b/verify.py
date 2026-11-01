#!/usr/bin/env python3
"""Reproduce the finite Nauru perfect-matching-complex computation using Python 3 only.

Run: python3 verify.py
The adjacent certificate.json is an independent, byte-level target for the two
integer Morse matrices, not merely a saved summary of their ranks.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import json


def graph():
    n, k = 12, 5
    edges = sorted({tuple(sorted(z)) for i in range(n) for z in
                    [(i, (i+1) % n), (i, i+n), (i+n, n+(i+k) % n)]})
    assert len(edges) == 36 and all(sum(v in e for e in edges) == 3 for v in range(24))
    return edges


def perfect_matchings(edges, largest=False):
    adj = [[] for _ in range(24)]
    for j, (a, b) in enumerate(edges):
        adj[a].append((b, j)); adj[b].append((a, j))
    @lru_cache(None)
    def rec(remaining):
        if not remaining:
            return (0,)
        v = remaining.bit_length()-1 if largest else (remaining & -remaining).bit_length()-1
        out = []
        for w, j in adj[v]:
            if (remaining >> w) & 1:
                out.extend(m | (1 << j) for m in
                           rec(remaining ^ (1 << v) ^ (1 << w)))
        return tuple(out)
    return sorted(set(rec((1 << 24)-1)))


def all_faces(facets):
    faces = {0}
    for facet in facets:
        subsets = [0]
        x = facet
        while x:
            bit = x & -x; x ^= bit
            subsets.extend(v | bit for v in subsets[:])
        assert len(subsets) == (1 << 12)
        faces.update(subsets)
    return faces


def toggling(faces, reverse=False):
    rem = set(faces); pair = {}
    for i in (range(35,-1,-1) if reverse else range(36)):
        bit = 1 << i
        lows = [s for s in rem if not (s & bit) and (s | bit) in rem]
        for s in lows:
            rem.remove(s); rem.remove(s | bit); pair[s] = s | bit
    assert 2*len(pair)+len(rem) == len(faces)
    return pair, rem


def acyclic(faces, pair):
    # Every codimension-one incidence is directed downwards except matched
    # incidences, which point upwards. Kahn's algorithm must exhaust the Hasse DAG.
    indeg = dict.fromkeys(faces, 0)
    incidences = 0
    for upper in faces:
        lowerbits = upper
        while lowerbits:
            bit = lowerbits & -lowerbits; lowerbits ^= bit
            lower = upper ^ bit; incidences += 1
            if pair.get(lower) == upper:
                indeg[upper] += 1
            else:
                indeg[lower] += 1
    q = deque(s for s in indeg if indeg[s] == 0)
    visited = 0
    while q:
        s = q.popleft(); visited += 1
        if s in pair:
            u = pair[s]; indeg[u] -= 1
            if not indeg[u]:q.append(u)
        sub = s
        while sub:
            bit = sub & -sub; sub ^= bit; low = s ^ bit
            if pair.get(low) != s:
                indeg[low] -= 1
                if not indeg[low]:q.append(low)
    assert visited == len(faces)
    return incidences


def oriented_boundary(s):
    pos=0; remaining=s
    while remaining:
        bit = remaining & -remaining; remaining ^= bit
        yield s ^ bit, (-1 if pos % 2 else 1)
        pos += 1


def matrix(pair, critical, k, modulus=None):
    rowcells = sorted(s for s in critical if s.bit_count()-1 == k-1)
    colcells = sorted(s for s in critical if s.bit_count()-1 == k)
    idx={s:i for i,s in enumerate(rowcells)}
    up = set(pair.values())
    @lru_cache(None)
    def projection(y):
        if y in idx:return {idx[y]:1}
        if y in up:return {}
        if y not in pair:return {}
        upper = pair[y]
        sign = next(s for z,s in oriented_boundary(upper) if z==y)
        result=defaultdict(int)
        for z,sgn in oriented_boundary(upper):
            if z == y: continue
            for i,v in projection(z).items():
                result[i] -= sign*sgn*v
        if modulus is not None:
            return {i:v%modulus for i,v in result.items() if v%modulus}
        return {i:v for i,v in result.items() if v}
    M = [[0]*len(colcells) for _ in rowcells]
    for j,c in enumerate(colcells):
        for z,sign in oriented_boundary(c):
            for i,v in projection(z).items():M[i][j] += sign*v
    if modulus is not None:
        M = [[x%modulus for x in row] for row in M]
    return rowcells,colcells,M


def rank_q(A):
    if not A:return 0
    M = [[Fraction(v) for v in row] for row in A]
    nrow,ncol=len(M),len(M[0]); r=0
    for col in range(ncol):
        pivot = next((i for i in range(r,nrow) if M[i][col]),None)
        if pivot is None:continue
        M[r],M[pivot]=M[pivot],M[r]
        p=M[r][col]
        for i in range(r+1,nrow):
            if M[i][col]:
                a=M[i][col]/p
                for j in range(col,ncol):M[i][j] -= a*M[r][j]
        r += 1
        if r==nrow:break
    return r


def det_bareiss(A):
    X=[row[:] for row in A]; n=len(X)
    if not n:return 1
    sign=1; prev=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if X[i][k]),None)
        if pivot is None:return 0
        if pivot!=k:
            X[k],X[pivot]=X[pivot],X[k];sign=-sign
        q=X[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = q*X[i][j]-X[i][k]*X[k][j]
                assert num % prev == 0
                X[i][j] = num // prev
            X[i][k] = 0
        prev=q
    return sign*X[-1][-1]


def rank_f2(M):
    basis={}
    for j in range(len(M[0]) if M else 0):
        v=sum((M[i][j]%2)<<i for i in range(len(M)))
        while v:
            p=v.bit_length()-1
            if p in basis:v ^= basis[p]
            else:
                basis[p]=v;break
    return len(basis)


def main():
    cert=json.loads((Path(__file__).resolve().parent/'certificate.json').read_text('utf-8'))
    edges=graph()
    pm=perfect_matchings(edges)
    assert pm==perfect_matchings(edges,largest=True)
    faces=all_faces(pm)
    fv={str(k):v for k,v in sorted(Counter(s.bit_count()-1 for s in faces).items())}
    assert len(pm)==120 and len(faces)==346822
    assert edges==[tuple(v) for v in cert['edges']]
    assert pm==cert['perfect_matching_masks']
    assert fv==cert['f_vector']
    pair,critical=toggling(faces)
    assert len(pair)==173357 and len(critical)==108
    assert {str(k):v for k,v in sorted(Counter(s.bit_count()-1 for s in critical).items())}=={'3':22,'4':67,'5':19}
    incidences=acyclic(faces,pair)
    assert incidences==cert['hasse_incidences']
    assert sorted(critical)==cert['critical_masks']
    mats={}
    for k in (4,5):
        rows,cols,M=matrix(pair,critical,k)
        dat=cert['morse_boundaries'][str(k)]
        assert rows==dat['row_masks'] and cols==dat['column_masks'] and M==dat['matrix']
        r=rank_q(M)
        p=dat['minor_rows'];q=dat['minor_columns']
        d=det_bareiss([[M[i][j] for j in q] for i in p])
        assert r==dat['rank'] and r==len(p)==len(q)
        assert d==dat['minor_determinant'] and abs(d)==1
        mats[k]=M
    assert all(sum(mats[4][i][k]*mats[5][k][j] for k in range(67))==0
               for i in range(22) for j in range(19))
    # Independent checker: reverse the 36 pivot stages; calculate boundaries mod 2.
    reverse_pair,reverse_critical=toggling(faces,reverse=True)
    assert len(reverse_pair)==(len(faces)-len(reverse_critical))//2
    assert acyclic(faces,reverse_pair)==incidences
    r3,c4,B4=matrix(reverse_pair,reverse_critical,4,modulus=2)
    r4,c5,B5=matrix(reverse_pair,reverse_critical,5,modulus=2)
    assert len(r3)==11 and len(c4)==len(r4)==55 and len(c5)==18
    assert rank_f2(B4)==5 and rank_f2(B5)==18
    assert (len(r3)-5,len(r4)-5-18,len(c5)-18)==(6,32,0)
    euler=sum(((-1)**(s.bit_count()-1)) for s in critical)
    assert euler==26
    print('Nauru GP(12,5): vertices=24 edges=36 perfect_matchings=120')
    print('Faces including empty=346822; Morse pairs=173357; critical dimensions: 3:22 4:67 5:19')
    print('Complete directed Hasse acyclicity=PASS, incidences='+str(incidences))
    print('Morse boundary ranks over Q: degree 4=16, degree 5=19')
    print('Unimodular maximal-rank minors: degree 4=+1, degree 5=-1')
    print('Morse boundary composition zero=PASS; Euler=26')
    print('Independent reverse toggles: mod-2 ranks degree 4=5, degree 5=18')
    print('Reduced integral homology ranks: degree 3=6, degree 4=32; torsion-free')
    print('Wedge homotopy result: six 3-spheres and thirty-two 4-spheres')
    print('NAURU_PERFECT_MATCHING_WEDGE_EXACT_VERIFIED')

if __name__=='__main__': main()
