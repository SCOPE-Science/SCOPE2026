#!/usr/bin/env python3
"""Exact-rational independent finite checks of a claimed continuous wheel diameter law.
This is a finite test, not the proof of the all-n, all-s theorem.
Uses only the Python standard library.
"""
from fractions import Fraction as Q
from itertools import combinations


def build_wheel(n, spoke):
    spoke = Q(spoke)
    edges = [(i, (i + 1) % n, Q(1)) for i in range(n)]
    edges += [(n, i, spoke) for i in range(n)]
    vertdist = [[Q(0) if i == j else None for j in range(n + 1)] for i in range(n + 1)]
    for a, b, length in edges:
        vertdist[a][b] = vertdist[b][a] = length
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if vertdist[i][k] is None or vertdist[k][j] is None:
                    continue
                d = vertdist[i][k] + vertdist[k][j]
                if vertdist[i][j] is None or d < vertdist[i][j]:
                    vertdist[i][j] = d
    return edges, vertdist


def pair_maximum(edge1, edge2, distances, same):
    u,v,L = edge1
    w,z,M = edge2
    # Every function is (A,B,C), representing A*x+B*y+C.
    pieces = []
    for a, i in ((u, 0), (v, 1)):
        for b, j in ((w, 0), (z, 1)):
            pieces.append((Q(1) if i == 0 else Q(-1),
                           Q(1) if j == 0 else Q(-1),
                           distances[a][b] + (L if i else 0) + (M if j else 0)))

    def intersect(e1, e2):
        a,b,c = e1
        d,e,f = e2
        det = a*e-b*d
        if det == 0:
            return None
        return ((b*f-c*e)/det, (c*d-a*f)/det)

    best = Q(-1)
    for sign in ((1,-1) if same else (0,)):
        pp = pieces + ([(Q(sign),Q(-sign),Q(0))] if same else [])
        lines = [(Q(1),Q(0),Q(0)),(Q(1),Q(0),-L),
                 (Q(0),Q(1),Q(0)),(Q(0),Q(1),-M)]
        if same:
            lines.append((Q(1),Q(-1),Q(0)))
        for (a,b,c),(d,e,f) in combinations(pp,2):
            # Equality of two competing path-length planes.
            if (a,b)!=(d,e):
                lines.append((a-d,b-e,c-f))
        for line1,line2 in combinations(lines,2):
            pos=intersect(line1,line2)
            if pos is None:continue
            x,y=pos
            if not (0<=x<=L and 0<=y<=M):continue
            if same and sign*(x-y)<0:continue
            val=min(a*x+b*y+c for a,b,c in pp)
            if val>best:best=val
    return best


def exact_diameter(n,spoke):
    edges,dist=build_wheel(n,spoke)
    # Rotational symmetry allows one representative of each of three edge-pair types.
    best=Q(-1)
    for k in range(n):
        for i,j in ((0,k),(0,n+k),(n,n+k)):
            candidate=pair_maximum(edges[i],edges[j],dist,i==j)
            best=max(best,candidate)
    return best


def claimed_diameter(n,s):
    s=Q(s);m=n//2; M=(n+1)//2
    rr = min(Q(n,2),2*s+1) if n%2==0 else min(Q(n,2),2*s+1,s+Q(m+1,2))
    rs = min(2*s+Q(1,2),s+Q(M,2))
    return max(rr,rs)


def claimed_peak(n):
    if n==3:return Q(1,3),None
    if n%2==0:return Q(2,n+2),Q(n-2,4)
    return Q(2*(n-1),n*(n+1)),Q(n-3,4)


def main():
    cases=0
    for n in range(3,12):
        sample=[Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(3,2),Q(2),Q(3)]
        peak,witness=claimed_peak(n)
        if witness is not None:
            sample.extend([witness,Q(witness+Q(1,8))])
        for spoke in sorted(set(sample)):
            actual=exact_diameter(n,spoke)
            expected=claimed_diameter(n,spoke)
            assert actual==expected, (n,spoke,actual,expected)
            assert expected / (n*(1+spoke)) <=peak,(n,spoke)
            cases+=1
        if witness is not None:
            assert claimed_diameter(n,witness) / (n*(1+witness)) ==peak
        else:
            for spoke in sample:
                assert claimed_diameter(n,spoke)/(n*(1+spoke))==peak
    print('PASS: %d exactly enumerated parameter cases (n=3,...,11), independent path-pair maximization.'%cases)
    print('PASS: claimed sharp normalized peaks and equality witnesses.')
    print('LIMIT: finite cases are NOT an infinite proof; see the analytical argument.')

if __name__=='__main__':main()
