#!/usr/bin/env python3
"""Finite checks for two labeled particles on complete graphs with all vertices sinks.

The proof for all m>=4 is independent of the bounded checks in this file.
Use Python 3.9+; no third-party packages needed.
"""
import itertools
import json
import math


def rank_mod_p(rows, ncol, p):
    a = [[x % p for x in row] for row in rows]
    rank = 0
    for col in range(ncol):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(inv * x) % p for x in a[rank]]
        for r in range(rank + 1, len(a)):
            fac = a[r][col]
            if fac:
                a[r] = [(x - fac * y) % p for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def setup(m):
    verts = list(range(m))
    edges = list(itertools.combinations(verts, 2))
    E = len(edges)
    eidx = {e: i for i, e in enumerate(edges)}
    c0 = list(itertools.product(verts, repeat=2))
    c1 = [(0, e, v) for e in edges for v in verts]
    c1 += [(1, e, v) for e in edges for v in verts]
    c2 = [(e, f) for e in edges for f in edges if e != f]
    c0_idx = {v: i for i, v in enumerate(c0)}
    c1_idx = {v: i for i, v in enumerate(c1)}
    c2_idx = {v: i for i, v in enumerate(c2)}
    rows1 = [[0] * len(c1) for _ in c0]
    for j, (axis, (a, b), v) in enumerate(c1):
        if axis == 0:
            rows1[c0_idx[(b, v)]][j] += 1
            rows1[c0_idx[(a, v)]][j] -= 1
        else:
            rows1[c0_idx[(v, b)]][j] += 1
            rows1[c0_idx[(v, a)]][j] -= 1
    rows2 = [[0] * len(c2) for _ in c1]
    for j, (e, f) in enumerate(c2):
        a, b = e; c, d = f
        for cell, sign in [((1, f, b), 1), ((1, f, a), -1),
                           ((0, e, d), -1), ((0, e, c), 1)]:
            rows2[c1_idx[cell]][j] += sign
    # Check ∂_1∂_2 by sparse incidence of each face, without matrix multiplication.
    for e, f in c2:
        a,b=e; c,d=f
        bdry=[((1, f, b), 1), ((1,f,a),-1), ((0,e,d),-1), ((0,e,c),1)]
        bd={}
        for (axis,(x,y),v),co in bdry:
            v0=(x,v) if axis==0 else (v,x)
            v1=(y,v) if axis==0 else (v,y)
            bd[v0]=bd.get(v0,0)-co
            bd[v1]=bd.get(v1,0)+co
        assert all(co==0 for co in bd.values())
    return edges, c0, c1, c2, rows1, rows2


def cycle(m, nodes, edges):
    idx={e:i for i,e in enumerate(edges)}
    z=[0]*len(edges)
    for a,b in zip(nodes,nodes[1:]+nodes[:1]):
        k=tuple(sorted((a,b)))
        z[idx[k]] += (1 if (a,b)==k else -1)
    assert all(abs(x)<=1 for x in z)
    return z


def triangle_units(m, edges):
    for a,b in edges:
        others=[v for v in range(m) if v not in (a,b)]
        c,d=others[:2]
        x=cycle(m,[a,b,c],edges)
        y=cycle(m,[a,b,d],edges)
        z=[u*v for u,v in zip(x,y)]
        assert sum(t!=0 for t in z)==1
        assert z[edges.index((a,b))] in [-1,1]


def action_on_edge(pi, edge):
    a,b=edge
    u,v=pi[a],pi[b]
    return tuple(sorted((u,v))), (1 if u<v else -1)


def traces(pi, swap, m, edges, c0, c1, c2):
    t0=t1=t2=0
    for a,b in c0:
        dest=(pi[b],pi[a]) if swap else (pi[a],pi[b])
        if dest==(a,b):t0+=1
    for axis,e,v in c1:
        e2,sgn=action_on_edge(pi,e)
        dest=(1-axis,e2,pi[v]) if swap else (axis,e2,pi[v])
        if dest==(axis,e,v):t1+=sgn
    for e,f in c2:
        e2,s=action_on_edge(pi,e)
        f2,t=action_on_edge(pi,f)
        dest=(f2,e2) if swap else (e2,f2)
        if dest==(e,f):t2+=s*t*(-1 if swap else 1)
    return (t0,t1,t2)


def formulas(pi):
    m=len(pi)
    f=sum(pi[i]==i for i in range(m))
    t=sum(pi[i]==j and pi[j]==i for i in range(m) for j in range(i+1,m))
    F=f*(f-1)//2+t
    h=f*(f-1)//2-t-f+1
    pp=[pi[pi[i]] for i in range(m)]
    fp=sum(pp[i]==i for i in range(m))
    tp=sum(pp[i]==j and pp[j]==i for i in range(m) for j in range(i+1,m))
    h2=fp*(fp-1)//2-tp-fp+1
    return h,F,h2


def verify(m):
    edges,c0,c1,c2,d1,d2=setup(m)
    triangle_units(m,edges)
    b=len(edges)-m+1
    expected={0:1,1:2*b,2:b*b-len(edges)}
    assert expected[2]>=0
    rankchecks={}
    for p in (2,3,5,7):
        r1=rank_mod_p(d1,len(c1),p)
        r2=rank_mod_p(d2,len(c2),p)
        betti={0:len(c0)-r1,1:len(c1)-r1-r2,2:len(c2)-r2}
        assert betti==expected,(m,p,betti,expected)
        rankchecks[str(p)]=[r1,r2]
    checked=0
    characteristic={}
    for pi in itertools.permutations(range(m)):
        h,F,h2=formulas(pi)
        for swap in (False,True):
            t0,t1,t2=traces(pi,swap,m,edges,c0,c1,c2)
            L=t0-t1+t2
            ch1=0 if swap else 2*h
            ch2=(F-h2) if swap else (h*h-F)
            assert L==1-ch1+ch2,(m,pi,swap,L,ch1,ch2)
            checked+=1
            if tuple(pi)==tuple(range(m)):
                characteristic['identity_swap' if swap else 'identity']={
                    'trace_H1':ch1,'trace_H2':ch2,'cellular_Lefschetz':L}
    return {'vertices':m,'edges':len(edges),'first_betti_graph':b,
            'cells':[len(c0),len(c1),len(c2)],
            'betti':[expected[i] for i in range(3)],
            'boundary_ranks_mod_primes':rankchecks,
            'verified_symmetries':checked,'selected_characters':characteristic}


def main():
    data={'proof_scope':'all integers m>=4 (symbolic argument)',
          'finite_checks':[verify(m) for m in (4,5,6)]}
    print(json.dumps(data,sort_keys=True,indent=2))

if __name__=='__main__': main()
