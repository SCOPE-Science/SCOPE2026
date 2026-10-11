#!/usr/bin/env python3
"""Finite independent consistency checks for Boolean rank-span-two complexes."""
from collections import Counter
from itertools import permutations
from math import comb, factorial


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    for a in range(min(n, n if maximum is None else maximum), 0, -1):
        for tail in partitions(n-a, a):
            yield (a,) + tail


def cycle_representative(parts):
    p = []
    offset = 0
    for d in parts:
        for j in range(d):
            p.append(offset + (j+1) % d)
        offset += d
    return tuple(p)


def cycle_signature(perm):
    seen = set()
    lengths = []
    for i in range(len(perm)):
        if i not in seen:
            d = 0
            j = i
            while j not in seen:
                seen.add(j)
                d += 1
                j = perm[j]
            lengths.append(d)
    return len(lengths), lengths.count(1), lengths.count(2)


def character_formula(c, fixed1, cycles2):
    pair_term = (comb(fixed1, 2) * (2**(c-2)-2)) if fixed1 >= 2 else 0
    return 2**c-3-(fixed1+cycles2)*(2**(c-1)-2)+pair_term


def build(n):
    nodes = list(range(1, (1<<n)-1))
    edges = []
    triangles = []
    for a in nodes:
        rem = [j for j in range(n) if not (a>>j)&1]
        for (j,) in __import__('itertools').combinations(rem, 1):
            b = a | (1 << j)
            if b != (1<<n)-1:
                edges.append((a,b))
        for j,k in __import__('itertools').combinations(rem, 2):
            b = a | (1<<j) | (1<<k)
            if b != (1<<n)-1:
                edges.append((a,b))
                triangles.append((a,a|(1<<j),b))
                triangles.append((a,a|(1<<k),b))
    edges.sort()
    triangles.sort()
    return nodes, edges, triangles


def rank_f2(n, edges, triangles):
    ind = {e:i for i,e in enumerate(edges)}
    pivots={}
    dependent=0
    for a,b,c in triangles:
        vector=(1<<ind[(a,b)])^(1<<ind[(b,c)])^(1<<ind[(a,c)])
        while vector:
            lead=vector.bit_length()-1
            if lead in pivots:
                vector ^= pivots[lead]
            else:
                pivots[lead]=vector
                break
        else:
            dependent+=1
    return len(pivots),dependent


def fixed_by_perm(mask,perm):
    image=0
    for j,dest in enumerate(perm):
        if (mask>>j)&1:
            image |= 1<<dest
    return image==mask


def direct_character(nodes,edges,triangles,perm):
    invariant={v for v in nodes if fixed_by_perm(v,perm)}
    v = len(invariant)
    e = sum(a in invariant and b in invariant for a,b in edges)
    t = sum(a in invariant and b in invariant and c in invariant
            for a,b,c in triangles)
    return v-e+t-1


def orbit_cell_counts(n):
    orbit_vertices = sum(comb(n,a) for a in range(1,n))
    orbit_edges=0
    orbit_triangles=0
    for a in range(1,n):
        for d in (1,2):
            if a+d <= n-1:
                orbit_edges += factorial(n)//(factorial(a)*factorial(d)*factorial(n-a-d))
                if d==2:
                    orbit_triangles += factorial(n)//(factorial(a)*factorial(n-a-2))
    return orbit_vertices,orbit_edges,orbit_triangles


def main():
    classes = 0
    mod2_cases = 0
    enumerated_simplices = 0
    for n in range(4,9):
        nodes,edges,triangles=build(n)
        enumerated_simplices += len(nodes)+len(edges)+len(triangles)
        assert len(nodes)==2**n-2
        assert len(edges)==n*2**(n-1)-2*n + comb(n,2)*(2**(n-2)-2)
        assert len(triangles)==2*comb(n,2)*(2**(n-2)-2)
        assert (len(nodes),len(edges),len(triangles))==orbit_cell_counts(n)
        for parts in partitions(n):
            perm=cycle_representative(parts)
            c,f,t=cycle_signature(perm)
            exact=direct_character(nodes,edges,triangles,perm)
            predicted=character_formula(c,f,t)
            assert exact==predicted,(n,parts,exact,predicted)
            classes += 1
        if n <= 8:
            rank2, dependent=rank_f2(n,edges,triangles)
            beta=2**(n-3)*(n*n-5*n+8)-n*n+3*n-3
            assert rank2==len(edges)-len(nodes)+1
            assert dependent==beta
            print(f'n={n}: (f0,f1,f2)=({len(nodes)},{len(edges)},{len(triangles)}), '
                  f'rank(d2)={rank2}, beta2_F2={dependent}, S_n classes={len(list(partitions(n)))}')
            mod2_cases+=1
    print(f'VERIFY_OK n_cases={mod2_cases} conjugacy_classes={classes} enumerated_faces={enumerated_simplices}')

if __name__=='__main__':main()
