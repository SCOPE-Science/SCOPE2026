#!/usr/bin/env python3
"""Exact finite checks for orthogonal complete-graph cographic polytopes.

Enumerate balanced trinary flows and identify polar vertices by the
forest criterion. This is a finite check, not the proof for all orders.
"""
from collections import Counter
from fractions import Fraction


def check(n):
    edges = [(i,j) for i in range(n) for j in range(i+1,n)]
    E=len(edges)
    # Exact orthogonal projection onto the circulation space of K_n.
    inc=[]
    for i,j in edges:
        col=[0]*n
        col[i]=-1
        col[j]=1
        inc.append(col)
    proj=[[Fraction(int(a==b),1)-Fraction(sum(inc[a][v]*inc[b][v] for v in range(n)),n)
           for b in range(E)] for a in range(E)]
    assert all(sum(proj[a][k]*proj[k][b] for k in range(E))==proj[a][b]
               for a in range(E) for b in range(E))
    assert all(sum(proj[a][b]*inc[b][v] for b in range(E))==0
               for a in range(E) for v in range(n))
    assert all(proj[a][a]==Fraction(n-2,n) for a in range(E))
    future=[[0]*n for _ in range(E+1)]
    for k in range(E-1,-1,-1):
        future[k]=future[k+1][:]
        i,j=edges[k]
        future[k][i]+=1
        future[k][j]+=1
    degree=[0]*n
    zero=[]
    stats=Counter()
    witnesses={}
    checks=0
    # Any balanced integral flow in [-1,1]^E is trinary.
    def rec(k,weight):
        nonlocal checks
        if any(abs(degree[v])>future[k][v] for v in range(n)):
            return
        if k==E:
            checks+=1
            if any(degree):
                return
            # Polar vertex iff its set of unsaturated (zero) edges is a forest.
            parent=list(range(n))
            def root(x):
                while parent[x]!=x:
                    x=parent[x]
                return x
            for idx in zero:
                i,j=edges[idx]
                ri,rj=root(i),root(j)
                if ri==rj:
                    return
                parent[ri]=rj
            stats[weight]+=1
            if weight not in witnesses:
                witnesses[weight]=tuple(zero)
            return
        i,j=edges[k]
        zero.append(k)
        rec(k+1,weight)
        zero.pop()
        degree[i]+=1
        degree[j]-=1
        rec(k+1,weight+1)
        degree[i]-=2
        degree[j]+=2
        rec(k+1,weight+1)
        degree[i]+=1
        degree[j]-=1
    rec(0,0)
    assert stats
    m=max(stats)
    expected=E if n%2 else E-n//2
    assert m==expected, (n,m,expected)
    assert (len(stats)==1)==(n%2==1), (n,stats)
    if n%2==0:
        assert all(len(witnesses[m])==n//2 for _ in [0])
        # n/2 zero edges imply a perfect matching, because every vertex
        # must have odd zero-degree.
        assert len(stats)>=2
    d=(n-1)*(n-2)//2
    R2=Fraction(n-2,n)
    r2=Fraction(1,m)
    assert R2*E==d
    assert r2== (Fraction(2,n*(n-1)) if n%2 else Fraction(2,n*(n-2)))
    return {"n":n,"cycle_rank":d,"edges":E,"polar_vertex_count":sum(stats.values()),"squared_norm_spectrum":dict(sorted(stats.items())),"R_squared":str(R2),"r_squared":str(r2),"trinary_flow_checks":checks}

if __name__=='__main__':
    import json
    print(json.dumps([check(n) for n in [4,5,6]],indent=2))
    print('VERIFY_OK cographic_complete_graph_parity n=4,5,6 polar_vertices=all_balanced_trinary_forest_flows=yes contact_parity=yes exact_projection_idempotence=yes')
