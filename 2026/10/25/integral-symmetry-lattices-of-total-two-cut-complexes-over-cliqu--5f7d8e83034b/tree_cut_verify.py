#!/usr/bin/env python3
"""Standalone signed-Lefschetz checks for tree-indexed total 2-cut complexes.

Only elementary graph adjacency, subset enumeration and signed permutations are used.
Run: python3 tree_cut_verify.py
"""
from itertools import permutations
from math import factorial

def permutation_sign(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def tree_automorphisms(n, edges):
    E={frozenset(e) for e in edges}
    return [p for p in permutations(range(n)) if {frozenset((p[u],p[v])) for u,v in edges}==E]

def color_tree(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    col=[None]*n;col[0]=0;stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if col[v] is None:col[v]=1-col[u];stack.append(v)
            else:assert col[v]!=col[u]
    assert None not in col
    return col

def vertex_permutation(m,n,rows,a):
    # (column,row) coordinate
    return tuple(a[v]*m+rows[i] for v in range(n) for i in range(m))

def complex_faces(m,n,edges):
    N=m*n
    E={frozenset((v*m+i,v*m+j)) for v in range(n) for i in range(m) for j in range(i+1,m)}
    E.update(frozenset((u*m+i,v*m+i)) for u,v in edges for i in range(m))
    # S belongs to the 2-cut complex iff its complement contains a nonedge.
    faces=[]
    for mask in range(1,1<<N):
        complement=[j for j in range(N) if not(mask>>j)&1]
        if any(frozenset((u,v)) not in E for k,u in enumerate(complement) for v in complement[k+1:]):
            faces.append(mask)
    return faces

def signed_lefschetz(faces,p):
    signed_sum=0
    for mask in faces:
        elems=[k for k in range(len(p)) if (mask>>k)&1]
        permuted=[p[k] for k in elems]
        if set(permuted)!=set(elems):continue
        inv=sum(permuted[i]>permuted[j] for i in range(len(permuted)) for j in range(i+1,len(permuted)))
        val=(-1 if (len(elems)-1+inv)%2 else 1)
        signed_sum+=val
    return signed_sum-1  # reduced Lefschetz

def reduced_betti_mod2(faces):
    """Exact augmented simplicial chain ranks over F_2 (small cases)."""
    bydim={}
    for mask in faces:
        d=mask.bit_count()-1
        bydim.setdefault(d,[]).append(mask)
    top=max(bydim)
    ranks={0:0,top+1:0}
    for d in range(1,top+1):
        row={mask:i for i,mask in enumerate(bydim[d-1])}
        pivots={}
        for f in bydim[d]:
            b=0
            rest=f
            while rest:
                v=rest&-rest; rest-=v
                b^=1<<row[f-v]
            while b:
                pivot=b.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot]=b
                    break
                b^=pivots[pivot]
        ranks[d]=len(pivots)
    return {d:len(fs)-ranks[d]-ranks.get(d+1,0)-(1 if d==0 else 0)
            for d,fs in bydim.items()}

def run():
    # includes both path and branching tree; m=2,3,4 and up to 12 vertices.
    examples=[(2,2,[(0,1)]),(3,2,[(0,1)]),(4,2,[(0,1)]),
              (2,3,[(0,1),(1,2)]),(3,3,[(0,1),(1,2)]),(4,3,[(0,1),(1,2)]),
              (2,4,[(0,1),(1,2),(2,3)]),(3,4,[(0,1),(1,2),(2,3)]),
              (2,4,[(0,1),(0,2),(0,3)]),(3,4,[(0,1),(0,2),(0,3)])]
    checked=0
    for m,n,edges in examples:
        color=color_tree(n,edges)
        faces=complex_faces(m,n,edges)
        if m*n<=9:
            bettis=reduced_betti_mod2(faces)
            expected_degree=m*n-4
            assert bettis=={d:((m-1)*(n-1) if d==expected_degree else 0) for d in bettis}, (m,n,edges,bettis)
        automs=tree_automorphisms(n,edges)
        for a in automs:
            chi=1 if color[0]==color[a[0]] else -1
            efixed=sum(frozenset((a[u],a[v]))==frozenset((u,v)) for u,v in edges)
            for sig in permutations(range(m)):
                p=vertex_permutation(m,n,sig,a)
                trace=(permutation_sign(sig)**n)*(permutation_sign(a)**m)*chi*(sum(sig[i]==i for i in range(m))-1)*efixed
                expected=(-1)**(m*n-4)*trace
                actual=signed_lefschetz(faces,p)
                if actual!=expected:
                    raise AssertionError((m,n,edges,a,sig,actual,expected))
                checked+=1
        print('OK m=%d tree_vertices=%d degrees=%s faces=%d group_elements=%d rank=%d' %
              (m,n,sorted([sum(u in e for e in edges) for u in range(n)]),len(faces),len(automs)*factorial(m),(m-1)*len(edges)))
    print('PASS signed Lefschetz checks:',checked)
if __name__=='__main__':run()
