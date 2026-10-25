#!/usr/bin/env python3
"""Exact finite tests for face-boundary join generators of robust clique complexes.

Only standard-library arithmetic is required. This checks finite instances;
proof for all rectangular grids is contained in RESULT.md.
"""
from itertools import combinations
from collections import defaultdict


def boundary(s):
    return {s[:j] + s[j+1:]: (-1)**j for j in range(len(s))}


def alternating_sum(entries):
    out = defaultdict(int)
    for simplex, coeff in entries.items():
        for sub, sg in boundary(simplex).items():
            out[sub] += coeff*sg
    return {k:v for k,v in out.items() if v}


def wedge(p, q):
    out = defaultdict(int)
    for a, ca in p.items():
        for b, cb in q.items():
            s = a+b
            if len(set(s)) != len(s):
                continue
            swaps = sum(s[i]>s[j] for i in range(len(s)) for j in range(i+1,len(s)))
            out[tuple(sorted(s))] += ca*cb*(-1 if swaps%2 else 1)
    return {k:v for k,v in out.items() if v}


def grid(m, n):
    verts = [(i, j) for i in range(m) for j in range(n)]
    num = {a:i for i,a in enumerate(verts)}
    edges = {tuple(sorted((num[(i,j)],num[(a,b)])))
             for i,j in verts for a,b in verts if abs(i-a)+abs(j-b)==1}
    sqs = []
    for i in range(m-1):
        for j in range(n-1):
            a, b, c, d = [num[z] for z in ((i,j),(i,j+1),(i+1,j+1),(i+1,j))]
            cir = defaultdict(int)
            for u,v in ((a,b),(b,c),(c,d),(d,a)):
                cir[tuple(sorted((u,v)))] += 1 if u<v else -1
            sqs.append({z:t for z,t in cir.items() if t})
    return verts, num, edges, sqs


def is_tetrahedron(tet, edges):
    for a,b in combinations(tet, 2):
        if (a,b) in edges:
            rest=tuple(z for z in tet if z!=a and z!=b)
            if rest in edges:
                return True
    return False


def rank_sparse(cols, p):
    basis={}
    for col in cols:
        v={k:c%p for k,c in col.items() if c%p}
        while v:
            pivot=min(v)
            if pivot not in basis:
                c=v[pivot]
                basis[pivot]={k:(val*pow(c,-1,p))%p for k,val in v.items()}
                break
            factor=v[pivot]
            v={k:(v.get(k,0)-factor*basis[pivot].get(k,0))%p
               for k in v.keys() | basis[pivot].keys()}
            v={k:c for k,c in v.items() if c}
    return len(basis)


def signed_action(chain, permutation):
    out=defaultdict(int)
    for tet,coeff in chain.items():
        t=tuple(permutation[x] for x in tet)
        inv=sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
        out[tuple(sorted(t))]+=coeff*(-1 if inv%2 else 1)
    return {k:v for k,v in out.items() if v}


def run_case(m, n):
    verts, num, edges, cycles=grid(m,n)
    F=len(cycles)
    assert all(not alternating_sum(z) for z in cycles)
    assert all(set(z).issubset(edges) for z in cycles)
    pairs=list(combinations(range(F),2))
    products=[wedge(cycles[i],cycles[j]) for i,j in pairs]
    assert all(not alternating_sum(z) for z in products)
    assert all(all(is_tetrahedron(t,edges) for t in z) for z in products)
    for p in (2,3,5):
        assert rank_sparse(products,p)==len(pairs), (m,n,p)
    symmetries=[lambda x:x,
                lambda x:(m-1-x[0],x[1]),
                lambda x:(x[0],n-1-x[1]),
                lambda x:(m-1-x[0],n-1-x[1])]
    if m==n:
        symmetries += [lambda x:(x[1],x[0]),lambda x:(x[1],n-1-x[0])]
    fcs=[(i,j) for i in range(m-1) for j in range(n-1)]
    corners=lambda i,j:{(i,j),(i,j+1),(i+1,j),(i+1,j+1)}
    for trans in symmetries:
        perm={num[p]:num[trans(p)] for p in verts}
        faceperm={i:next(j for j,t in enumerate(fcs)
                         if {trans(x) for x in corners(*f)}==corners(*t))
                  for i,f in enumerate(fcs)}
        for (a,b),cycle in zip(pairs,products):
            tgt=tuple(sorted((faceperm[a],faceperm[b])))
            assert signed_action(cycle,perm)==products[pairs.index(tgt)],(m,n,a,b)
    return F, len(pairs), len({tet for c in products for tet in c}), len(symmetries)


def actual_top_kernel(m,n):
    verts, num, edges, cycles=grid(m,n)
    tets=[s for s in combinations(range(len(verts)),4) if is_tetrahedron(s,edges)]
    bound_cols=[boundary(t) for t in tets]
    r=rank_sparse(bound_cols,3)
    return len(tets)-r, len(cycles)*(len(cycles)-1)//2


def main():
    checks=0
    for m in range(2,6):
        for n in range(m,6):
            faces,pairs,tets,acts=run_case(m,n)
            print(f'grid {m}x{n}: faces={faces}, independent join cycles={pairs}, distinct support tetrahedra={tets}, symmetry maps={acts}')
            checks+=1
    for m,n in ((2,3),(2,5),(3,3),(3,4),(4,4)):
        actual,expected=actual_top_kernel(m,n)
        assert actual==expected,(m,n,actual,expected)
        print(f'exact mod-3 direct top kernel {m}x{n}: {actual}')
    print(f'PASS: {checks} grids, all signed joins/relations, ranks in characteristics 2,3,5 and symmetry actions; 5 direct top-kernel checks.')

if __name__=='__main__':
    main()
