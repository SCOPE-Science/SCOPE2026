#!/usr/bin/env python3
"""Exact finite Morse verification for one-edge-deleted three-row grids.

Run: python3 verify_grid_edge_defects.py
Uses only Python standard library. Coordinates are zero-based (row, column).
"""
import collections
import itertools
import functools


def grid_edges(n):
    edges = []
    for y in range(3):
        for x in range(n):
            u = y*n+x
            if x+1 < n: edges.append((u, u+1))
            if y+1 < 3: edges.append((u, u+n))
    return edges


def all_matchings(edges):
    edge_bits=[(1<<u)|(1<<v) for u,v in edges]
    out=[]
    def recurse(i, used, face):
        if i==len(edges):
            out.append(face)
            return
        recurse(i+1, used, face)
        if (used & edge_bits[i])==0:
            recurse(i+1, used|edge_bits[i], face|(1<<i))
    recurse(0,0,0)
    return set(out)



def alternating_matching_count_by_vertices(edges, vertex_count):
    """Independent deletion/cover recursion for the matching polynomial at -1."""
    neighbors=[0]*vertex_count
    for u,v in edges:
        neighbors[u]|=1<<v
        neighbors[v]|=1<<u
    @functools.lru_cache(None)
    def f(vertices):
        if not vertices:return 1
        bit=vertices&-vertices
        u=bit.bit_length()-1
        rest=vertices^bit
        answer=f(rest)
        possible=neighbors[u]&rest
        while possible:
            vbit=possible&-possible
            answer-=f(rest^vbit)
            possible-=vbit
        return answer
    return f((1<<vertex_count)-1)

def morse_match(faces, order):
    remaining=set(faces)
    lower_upper={}
    for v in order:
        bit=1<<v
        for a in tuple(remaining):
            b=a|bit
            if not a&bit and b in remaining:
                remaining.remove(a)
                remaining.remove(b)
                lower_upper[a]=b
    return remaining,lower_upper


def validate_directed_hasse(faces,pairs):
    """Exhaustively check no closed gradient path, using directed Kahn sorting."""
    degree={a:0 for a in faces}
    edges=0
    for b in faces:
        x=b
        while x:
            bit=x&-x
            a=b^bit
            if pairs.get(a)==b:
                degree[b]+=1
            else:
                degree[a]+=1
            edges+=1
            x-=bit
    waiting=collections.deque(a for a,d in degree.items() if d==0)
    visited=0
    while waiting:
        b=waiting.popleft()
        visited+=1
        x=b
        while x:
            bit=x&-x
            a=b^bit
            if pairs.get(a)!=b:
                degree[a]-=1
                if degree[a]==0:waiting.append(a)
            x-=bit
        if b in pairs:
            c=pairs[b]
            degree[c]-=1
            if degree[c]==0:waiting.append(c)
    assert visited==len(faces),('cycle',visited,len(faces))
    return edges


# Each pair (n,index) is independently determined from its full face enumeration.
# Values are the critical top-cell counts for the finite classification.
EXPECTED={
    5:[12,10,12,12,12,12,12,12,10,14,10,14,12,14,12,14,12,10,12,12,12,12],
    6:[24,21,22,25,28,23,22,23,24,25,21,26,21,28,25,27,23,28,23,26,25,21,24,22,28,22,24]
}

# Explicit vertex processing order for each graph (per deletion), exported in
# a separate JSON-like data file below. It is intentionally only a compact
# certificate; enumeration and checks above are independently implemented.
ORDERS = {}

ORDERS['5:0'] = [13, 3, 5, 19, 17, 14, 1, 6, 20, 10, 0, 16, 15, 9, 12, 18, 2, 11, 7, 8, 4]
ORDERS['5:1'] = [19, 17, 18, 13, 10, 12, 3, 0, 8, 5, 11, 20, 15, 1, 6, 14, 4, 16, 7, 2, 9]
ORDERS['5:2'] = [11, 4, 9, 19, 20, 0, 15, 8, 2, 7, 13, 5, 16, 14, 18, 6, 12, 3, 10, 1, 17]
ORDERS['5:3'] = [12, 1, 9, 10, 11, 2, 17, 16, 7, 13, 5, 3, 8, 19, 14, 20, 4, 0, 18, 15, 6]
ORDERS['5:4'] = [1, 16, 20, 8, 2, 5, 3, 19, 14, 6, 13, 9, 10, 4, 18, 12, 0, 11, 17, 7, 15]
ORDERS['5:5'] = [5, 14, 17, 12, 3, 13, 16, 7, 10, 4, 8, 20, 1, 15, 18, 9, 11, 2, 19, 0, 6]
ORDERS['5:6'] = [13, 15, 12, 11, 5, 1, 19, 8, 16, 7, 4, 10, 3, 18, 14, 6, 9, 20, 0, 2, 17]
ORDERS['5:7'] = [6, 7, 11, 14, 4, 9, 18, 13, 15, 10, 12, 17, 16, 1, 3, 19, 2, 5, 8, 20, 0]
ORDERS['5:8'] = [7, 8, 5, 17, 14, 16, 6, 11, 19, 2, 9, 10, 20, 3, 13, 4, 18, 15, 12, 1, 0]
ORDERS['5:9'] = [3, 10, 16, 12, 0, 9, 15, 6, 8, 18, 2, 1, 19, 13, 14, 5, 7, 20, 17, 11, 4]
ORDERS['5:10'] = [12, 6, 13, 19, 4, 17, 5, 14, 11, 2, 0, 20, 3, 8, 18, 1, 7, 9, 15, 16, 10]
ORDERS['5:11'] = [12, 6, 4, 9, 0, 7, 8, 17, 11, 10, 18, 5, 14, 13, 2, 16, 20, 15, 3, 19, 1]
ORDERS['5:12'] = [1, 8, 13, 6, 4, 9, 20, 15, 7, 11, 2, 5, 14, 10, 0, 3, 12, 19, 18, 17, 16]
ORDERS['5:13'] = [10, 0, 4, 1, 17, 13, 20, 3, 7, 18, 19, 15, 2, 6, 14, 5, 8, 16, 9, 12, 11]
ORDERS['5:14'] = [4, 12, 20, 6, 3, 17, 10, 19, 9, 0, 7, 18, 2, 1, 11, 16, 5, 14, 15, 8, 13]
ORDERS['5:15'] = [13, 17, 9, 1, 4, 20, 2, 7, 3, 11, 18, 6, 19, 8, 16, 12, 0, 14, 10, 5, 15]
ORDERS['5:16'] = [18, 11, 20, 2, 19, 6, 4, 12, 10, 5, 17, 15, 1, 13, 3, 9, 0, 8, 16, 7, 14]
ORDERS['5:17'] = [7, 11, 0, 10, 12, 20, 2, 1, 15, 8, 9, 5, 14, 19, 16, 18, 17, 4, 3, 13, 6]
ORDERS['5:18'] = [6, 3, 18, 16, 20, 10, 0, 13, 5, 12, 2, 9, 7, 11, 14, 19, 15, 8, 4, 17, 1]
ORDERS['5:19'] = [8, 13, 15, 3, 11, 19, 20, 14, 17, 5, 10, 2, 18, 7, 6, 1, 9, 12, 0, 4, 16]
ORDERS['5:20'] = [9, 0, 12, 8, 6, 10, 5, 15, 13, 4, 14, 16, 17, 19, 2, 1, 11, 20, 7, 3, 18]
ORDERS['5:21'] = [14, 4, 10, 1, 9, 12, 5, 6, 8, 18, 20, 19, 11, 15, 17, 0, 16, 2, 3, 7, 13]
ORDERS['6:0'] = [0, 12, 11, 1, 2, 18, 14, 10, 5, 20, 7, 15, 17, 9, 8, 19, 6, 21, 24, 25, 22, 13, 3, 23, 4, 16]
ORDERS['6:1'] = [15, 2, 5, 3, 22, 23, 24, 17, 6, 7, 8, 12, 19, 20, 0, 9, 11, 13, 14, 16, 10, 25, 1, 21, 18, 4]
ORDERS['6:2'] = [6, 23, 17, 20, 4, 3, 24, 21, 25, 5, 9, 2, 1, 8, 0, 15, 14, 7, 13, 22, 18, 12, 10, 11, 16, 19]
ORDERS['6:3'] = [8, 14, 1, 11, 23, 0, 9, 19, 5, 21, 13, 20, 7, 25, 17, 3, 2, 18, 12, 24, 15, 22, 4, 10, 16, 6]
ORDERS['6:4'] = [21, 11, 18, 3, 0, 23, 2, 14, 10, 7, 6, 24, 25, 4, 8, 19, 13, 12, 16, 17, 20, 1, 22, 15, 9, 5]
ORDERS['6:5'] = [23, 16, 20, 21, 19, 22, 13, 1, 9, 11, 8, 5, 25, 10, 3, 18, 2, 7, 24, 14, 6, 0, 15, 4, 17, 12]
ORDERS['6:6'] = [23, 1, 4, 22, 6, 13, 12, 17, 25, 2, 20, 24, 16, 19, 0, 3, 10, 9, 18, 8, 11, 14, 5, 15, 7, 21]
ORDERS['6:7'] = [2, 1, 6, 14, 17, 7, 16, 0, 19, 22, 5, 11, 8, 4, 25, 23, 13, 15, 20, 9, 24, 3, 21, 10, 18, 12]
ORDERS['6:8'] = [22, 19, 7, 17, 6, 2, 10, 1, 12, 14, 20, 8, 24, 16, 9, 5, 21, 4, 25, 15, 11, 0, 3, 13, 23, 18]
ORDERS['6:9'] = [9, 16, 8, 1, 11, 14, 6, 10, 5, 23, 19, 0, 13, 4, 22, 2, 7, 25, 20, 15, 12, 24, 21, 18, 17, 3]
ORDERS['6:10'] = [8, 21, 14, 0, 24, 12, 23, 16, 25, 6, 17, 20, 2, 7, 5, 9, 3, 10, 18, 1, 11, 22, 13, 4, 15, 19]
ORDERS['6:11'] = [23, 15, 12, 8, 4, 5, 13, 17, 9, 22, 24, 0, 19, 7, 2, 14, 6, 10, 21, 3, 20, 18, 16, 25, 11, 1]
ORDERS['6:12'] = [4, 9, 6, 23, 19, 13, 14, 15, 10, 8, 20, 21, 7, 5, 2, 11, 0, 1, 3, 12, 24, 18, 17, 16, 25, 22]
ORDERS['6:13'] = [1, 24, 9, 21, 3, 2, 15, 22, 17, 0, 23, 12, 8, 16, 7, 13, 6, 10, 5, 20, 11, 14, 25, 18, 19, 4]
ORDERS['6:14'] = [12, 20, 14, 22, 6, 24, 3, 16, 25, 13, 11, 9, 8, 18, 23, 19, 17, 15, 2, 5, 4, 0, 10, 7, 1, 21]
ORDERS['6:15'] = [10, 14, 20, 9, 24, 16, 23, 6, 0, 3, 13, 5, 19, 2, 21, 1, 18, 17, 12, 8, 7, 11, 25, 4, 22, 15]
ORDERS['6:16'] = [0, 12, 6, 8, 2, 24, 16, 1, 23, 19, 11, 4, 22, 25, 20, 13, 10, 21, 14, 17, 3, 18, 5, 15, 7, 9]
ORDERS['6:17'] = [1, 5, 20, 17, 16, 22, 24, 8, 21, 15, 7, 10, 25, 9, 13, 18, 2, 23, 19, 14, 3, 11, 6, 0, 12, 4]
ORDERS['6:18'] = [20, 18, 0, 15, 13, 22, 24, 2, 14, 1, 8, 16, 11, 23, 5, 21, 10, 9, 25, 12, 4, 3, 6, 17, 19, 7]
ORDERS['6:19'] = [13, 8, 17, 21, 22, 2, 16, 10, 20, 9, 25, 7, 24, 6, 5, 12, 4, 23, 18, 1, 11, 0, 15, 14, 3, 19]
ORDERS['6:20'] = [8, 17, 0, 16, 9, 12, 6, 15, 25, 23, 10, 4, 2, 13, 19, 14, 24, 5, 1, 11, 21, 7, 20, 3, 22, 18]
ORDERS['6:21'] = [6, 22, 11, 17, 18, 14, 7, 19, 8, 25, 13, 1, 10, 9, 20, 24, 23, 4, 2, 15, 3, 0, 12, 5, 16, 21]
ORDERS['6:22'] = [18, 2, 16, 8, 17, 12, 19, 1, 3, 25, 0, 15, 20, 13, 22, 6, 5, 21, 24, 7, 4, 14, 23, 11, 9, 10]
ORDERS['6:23'] = [19, 23, 8, 22, 17, 14, 5, 16, 7, 6, 1, 15, 21, 9, 25, 24, 4, 11, 2, 13, 18, 3, 0, 20, 12, 10]
ORDERS['6:24'] = [23, 10, 13, 15, 12, 9, 18, 16, 2, 22, 1, 8, 3, 7, 21, 17, 14, 25, 20, 24, 19, 5, 4, 0, 11, 6]
ORDERS['6:25'] = [3, 10, 8, 16, 20, 25, 0, 6, 19, 12, 2, 7, 14, 11, 22, 5, 18, 4, 15, 1, 23, 21, 13, 24, 17, 9]
ORDERS['6:26'] = [18, 9, 4, 8, 12, 3, 10, 21, 24, 0, 5, 2, 22, 20, 1, 6, 25, 13, 17, 14, 19, 7, 23, 11, 15, 16]

def run():
    cases=0
    total_simplices=0
    total_incidences=0
    total_pairs=0
    for n in [5,6]:
        base=grid_edges(n)
        for k,edge in enumerate(base):
            graph=base[:k]+base[k+1:]
            faces=all_matchings(graph)
            order=ORDERS[f'{n}:{k}']
            assert sorted(order)==list(range(len(graph)))
            remain,pairs=morse_match(faces,order)
            assert len(pairs)*2+len(remain)==len(faces)
            crit=collections.Counter(x.bit_count()-1 for x in remain)
            target=EXPECTED[n][k]
            assert crit=={n-1:target},(n,k,crit,target)
            euler=sum((-1)**(x.bit_count()-1) for x in faces)
            assert euler==(-1)**(n-1)*target,(n,k,euler,target)
            assert -alternating_matching_count_by_vertices(graph,3*n)==euler
            inc=validate_directed_hasse(faces,pairs)
            cases+=1
            total_simplices+=len(faces)
            total_incidences+=inc
            total_pairs+=len(pairs)
    print('PASS',cases,'edge-deletion graphs;',total_simplices,'augmented faces;',total_incidences,'directed cover incidences;',total_pairs,'Morse pairs')

if __name__=='__main__':run()
