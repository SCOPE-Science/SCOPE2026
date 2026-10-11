#!/usr/bin/env python3
"""Independent finite-field simplicial chain check using recursive vertex matchings."""
from collections import defaultdict
from itertools import combinations

def edges_from_c5_mycielski():
    # Different construction: adjacency-list, then convert to unordered graph edges.
    a={i:set() for i in range(11)}
    def link(x,y): a[x].add(y);a[y].add(x)
    for i in range(5):link(i,(i+1)%5)
    for i in range(5):
        for k in range(5):
            if (i-k)%5 in (1,4):link(i,k+5)
        link(i+5,10)
    return sorted((u,v) for u in a for v in a[u] if u<v)

def faces():
    E=edges_from_c5_mycielski()
    assert len(E)==20
    out=defaultdict(list)
    def visit(s,last,mask):
        if s:out[len(s)].append(s)
        for j in range(last+1,len(E)):
            u,v=E[j]; bits=(1<<u)|(1<<v)
            if not mask&bits:visit(s+(j,),j,mask|bits)
    visit((),-1,0)
    for k in out:out[k].sort()
    return out

def rank_mod_p(F,k,p):
    idx={f:j for j,f in enumerate(F[k-1])}
    basis={}
    for f in F[k]:
        col={idx[f[:j]+f[j+1:]]:(-1 if j%2 else 1)%p for j in range(len(f))}
        col={j:c for j,c in col.items() if c}
        while col:
            lead=max(col)
            if lead not in basis:
                inv=pow(col[lead],-1,p)
                basis[lead]={r:(c*inv)%p for r,c in col.items()}
                break
            factor=col[lead]
            for r,c in basis[lead].items():
                nv=(col.get(r,0)-factor*c)%p
                if nv:col[r]=nv
                else:col.pop(r,None)
    return len(basis)

def main():
    F=faces()
    assert [len(F[k]) for k in range(1,6)]==[20,135,365,360,87]
    for p in (2,3,5):
        ranks=[rank_mod_p(F,k,p) for k in range(2,6)]
        # ranks of boundary: C_1->C_0 through C_4->C_3
        assert ranks==[19,116,249,87],(p,ranks)
        # Non-reduced H_0=1; degree 3 Betti = 360-249-87=24
        print('field',p,'simplicial ranks',ranks,'reduced Betti_3',360-ranks[2]-ranks[3])
    print('independent face enumeration successful')
if __name__=='__main__':main()
