#!/usr/bin/env python3
"""Exhaustive maximal-clique enumeration for finite Brandt semigroups."""
from itertools import permutations, product
from collections import Counter
from math import comb

def groups():
    yield 'trivial', [(0,)]
    yield 'C2', [(0,1),(1,0)]
    yield 'C3', list(range(3))
    yield 'S3', list(permutations(range(3)))
    yield 'D8', [(a,b) for a in range(4) for b in range(2)]

def group_mult(name, elems):
    if name=='D8':
        return [[elems.index(((x[0]+(1 if x[1]==0 else -1)*y[0])%4,(x[1]+y[1])%2)) for y in elems] for x in elems]
    if name[0]=='C':
        q=len(elems)
        return [[(i+j)%q for j in range(q)] for i in range(q)]
    return [[elems.index(tuple(elems[i][elems[j][k]] for k in range(len(elems[i])))) for j in range(len(elems))] for i in range(len(elems))]

def max_abelian_sets(table):
    q=len(table)
    comm=lambda a,b:table[a][b]==table[b][a]
    sets=[]
    for mask in range(1,1<<q):
        a=[i for i in range(q) if mask>>i&1]
        if all(comm(x,y) for x in a for y in a) and all(any(not comm(x,b) for x in a) for b in range(q) if not (mask>>b&1)):
            sets.append(frozenset(a))
    return sets

def maximal_cliques(adj):
    n=len(adj); all_bits=(1<<n)-1; out=[]
    def bk(R,P,X):
        if not(P or X):
            out.append(frozenset(i for i in range(n) if R>>i&1)); return
        pivots=P|X
        if pivots:
            u=max((i for i in range(n) if pivots>>i&1),key=lambda i:(P&adj[i]).bit_count())
            candidates=P&~adj[u]
        else:candidates=P
        while candidates:
            vb=candidates&-candidates; v=vb.bit_length()-1
            bk(R|vb,P&adj[v],X&adj[v]); P&=~vb; X|=vb; candidates&=~vb
    bk(0,all_bits,0)
    return set(out)

def check(name, elems, n):
    tab=group_mult(name,elems)
    q=len(elems); M=max_abelian_sets(tab)
    V=[(i,g,j) for i in range(n) for j in range(n) for g in range(q)]
    indexes={v:a for a,v in enumerate(V)}
    def mul(x,y):
        return None if x is None or y is None or x[2]!=y[0] else (x[0],tab[x[1]][y[1]],y[2])
    adj=[]
    for x in V:
        bits=0
        for k,y in enumerate(V):
            if x!=y and mul(x,y)==mul(y,x):bits |= 1<<k
        adj.append(bits)
    found=maximal_cliques(adj)
    expected=set()
    for colors in product(range(3),repeat=n):
        S={i for i,c in enumerate(colors) if c==1}
        T={i for i,c in enumerate(colors) if c==2}
        if bool(S)!=bool(T):continue
        U={i for i,c in enumerate(colors) if c==0}
        if not S and not T: # only all diag
            for choices in product(M,repeat=n):
                expected.add(frozenset(indexes[(i,g,i)] for i in range(n) for g in choices[i]))
        else:
            for choices in product(M,repeat=len(U)):
                edges={(i,g,j) for i in S for j in T for g in range(q)}
                for i,A in zip(sorted(U),choices):edges|={(i,g,i) for g in A}
                expected.add(frozenset(indexes[x] for x in edges))
    predicted=(len(M)+2)**n-2*(len(M)+1)**n+2*len(M)**n
    assert found==expected,(name,n,len(found),len(expected),list(found-expected)[:2],list(expected-found)[:2])
    assert len(found)==predicted
    actual=Counter(map(len,found)); predicted_size=Counter(map(len,expected)); assert actual==predicted_size
    for clique in found:
        elements=[V[i] for i in clique]
        for x in elements:
            for y in elements:
                z=mul(x,y)
                assert z is None or z in elements,(name,n,x,y,z)
    print('OK',name,'n=',n,'group_size=',q,'max_abelian=',len(M),'cliques=',len(found),'size_spectrum=',dict(sorted(actual.items())))

if __name__=='__main__':
    for name, elems in groups():
        for n in ([2,3,4] if name not in ('S3','D8') else [2,3,4] if name=='S3' else [2,3]):
            check(name,elems,n)
