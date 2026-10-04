#!/usr/bin/env python3
from itertools import combinations

def span_add(S, x):
    return frozenset(S | {x ^ s for s in S})

def all_subspaces(n):
    levels=[{frozenset([0])}]
    V=range(1<<n)
    for d in range(n):
        nxt=set()
        for S in levels[-1]:
            for x in V:
                if x not in S:
                    nxt.add(span_add(S,x))
        levels.append(nxt)
    return levels

def basis_of(S,n):
    rows=[x for x in S if x]
    basis=[]
    # Gaussian elimination, high bits first
    for col in range(n-1,-1,-1):
        piv=next((x for x in rows if (x>>col)&1),None)
        if piv is None: continue
        basis.append(piv)
        rows=[x ^ piv if ((x>>col)&1) else x for x in rows if x!=piv]
    return basis

def rank_bits(rows, m):
    rows=list(rows)
    r=0
    for col in range(m-1,-1,-1):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>col)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(len(rows)):
            if i!=r and ((rows[i]>>col)&1): rows[i]^=rows[r]
        r+=1
    return r

def lcd(S,n):
    B=basis_of(S,n); k=len(B)
    gram=[]
    for a in B:
        row=0
        for j,b in enumerate(B):
            if ((a & b).bit_count() & 1): row |= 1<<j
        gram.append(row)
    return rank_bits(gram,k)==k

def verify_n(n):
    levels=all_subspaces(n)
    for k in range(1,n):
        verts=[S for S in levels[k] if lcd(S,n)]
        idx={S:i for i,S in enumerate(verts)}
        adj=[set() for _ in verts]
        for i in range(len(verts)):
            A=verts[i]
            for j in range(i+1,len(verts)):
                B=verts[j]
                if len(A & B)==(1<<(k-1)):
                    adj[i].add(j); adj[j].add(i)
        deg=(2**k-1)*(2**(n-k)-1)
        lam=2**k+2**(n-k)-4
        assert all(len(x)==deg for x in adj),(n,k,'degree',sorted(set(map(len,adj))),deg)
        for i in range(len(verts)):
            for j in adj[i]:
                if i<j:
                    c=len(adj[i] & adj[j])
                    assert c==lam,(n,k,'lambda',i,j,c,lam)
        tri=sum(len(adj[i] & adj[j]) for i in range(len(verts)) for j in adj[i] if i<j)//3
        expected=len(verts)*deg*lam//6
        assert tri==expected,(n,k,tri,expected)
        print(f'n={n} k={k} vertices={len(verts)} degree={deg} lambda={lam} triangles={tri}')

def main():
    for n in range(2,7): verify_n(n)
    print('VERIFY_OK')

if __name__=='__main__': main()
