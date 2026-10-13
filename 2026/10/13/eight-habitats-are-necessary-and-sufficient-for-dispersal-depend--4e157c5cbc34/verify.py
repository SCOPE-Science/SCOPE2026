#!/usr/bin/env python3
"""Exact certificate for edge-correlation ranking on small homogeneous dispersal trees.

Requires Python 3.10+ standard library only. Run: python verify.py
"""
from collections import Counter
from fractions import Fraction
from heapq import heapify, heappop, heappush
from itertools import product

# Polynomials are lists of integer or rational coefficients in ascending order.
def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def mul(a,b):
    q=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):q[i+j]+=x*y
    return trim(q)

def sub(a,b):
    q=[0]*max(len(a),len(b))
    for i,x in enumerate(a):q[i]+=x
    for i,x in enumerate(b):q[i]-=x
    return trim(q)

def sign_uniform(p):
    nonzero=[v for v in p if v]
    return not nonzero or all(v>0 for v in nonzero) or all(v<0 for v in nonzero)

def divide_exact(p,d):
    # Rational long division; None means a nonzero remainder.
    r=list(map(Fraction,p));d=list(map(Fraction,d))
    q=[Fraction(0)]*max(1,len(r)-len(d)+1)
    for k in range(len(r)-len(d),-1,-1):
        v=r[k+len(d)-1]/d[-1]
        q[k]=v
        for j,b in enumerate(d):r[k+j]-=v*b
    if any(r):return None
    return trim(q)


def evaluate(p,t):
    out=0
    for a in reversed(p):out=out*t+a
    return out

def det_bareiss(A):
    # Independent determinant computation over integers.
    A=[r[:] for r in A];n=len(A)
    if n==0:return 1
    sgn=1;previous=1
    for k in range(n-1):
        if A[k][k]==0:
            i=next((j for j in range(k+1,n) if A[j][k]),None)
            if i is None:return 0
            A[k],A[i]=A[i],A[k];sgn=-sgn
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                val=A[i][j]*pivot-A[i][k]*A[k][j]
                assert val%previous==0
                A[i][j]=val//previous
        for i in range(k+1,n):A[i][k]=0
        previous=pivot
    return sgn*A[-1][-1]

def independent_minor_checks(n,edges):
    for rate in (1,3):
        for S in [(v,) for v in range(n)]+list(edges):
            A=[]
            U=[u for u in range(n) if u not in S]
            for u in U:
                A.append([int(u==v)+rate*((sum(u in e for e in edges)) if u==v
                                   else (-1 if (min(u,v),max(u,v)) in edges else 0)) for v in U])
            assert evaluate(forest_minor(n,edges,S),rate)==det_bareiss(A), (n,edges,S,rate)

def prufer_tree(n,seq):
    deg=[1]*n
    for x in seq:deg[x]+=1
    leaves=[x for x in range(n) if deg[x]==1]
    heapify(leaves)
    edges=[]
    for x in seq:
        v=heappop(leaves)
        edges.append((min(v,x),max(v,x)))
        deg[v]-=1;deg[x]-=1
        if deg[x]==1:heappush(leaves,x)
    u=heappop(leaves);v=heappop(leaves)
    edges.append((min(u,v),max(u,v)))
    return tuple(sorted(edges))

def canonical_tree(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    degrees=[len(ns) for ns in adj]
    alive=[True]*n
    leaves=[v for v in range(n) if degrees[v]<=1]
    remaining=n
    while remaining>2:
        remaining-=len(leaves)
        for v in leaves:alive[v]=False
        nxt=[]
        for v in leaves:
            for u in adj[v]:
                if alive[u]:
                    degrees[u]-=1
                    if degrees[u]==1:nxt.append(u)
        leaves=nxt
    def rooted(v,parent):
        return '('+''.join(sorted(rooted(u,v) for u in adj[v] if u!=parent))+')'
    centers=[v for v in range(n) if alive[v]]
    assert len(centers) in (1,2),(n,centers,degrees)
    if len(centers)==1:return rooted(centers[0],-1)
    a,b=centers
    return '['+''.join(sorted((rooted(a,b),rooted(b,a))))+']'

def forest_minor(n,edges,S):
    # All-minors matrix-forest identity for det((I+tL)[V\\S,V\\S]).
    # Every component must have at most one pinned vertex in S. Components
    # with none have |C| choices of an identity-edge root.
    S=set(S);m=len(edges);out=[0]*(m+1)
    for mask in range(1<<m):
        parent=list(range(n));size=[1]*n;marked=[int(v in S) for v in range(n)]
        k=0;valid=True
        for i,(u,v) in enumerate(edges):
            if not mask&(1<<i):continue
            k+=1
            x=u
            while parent[x]!=x:x=parent[x]
            y=v
            while parent[y]!=y:y=parent[y]
            assert x!=y # subgraphs of a tree have no cycles
            parent[y]=x;size[x]+=size[y];marked[x]+=marked[y]
            if marked[x]>1:valid=False;break
        if not valid:continue
        weight=1
        for v in range(n):
            if parent[v]==v and marked[v]==0:weight*=size[v]
        out[k]+=weight
    return trim(out)

# A positive-leading polynomial with all remaining coefficients negative
# has exactly one positive root by Descartes and an endpoint sign change.
CROSSING_FACTORS=(
    (-1,-5,-5,1),    # t^3-5t^2-5t-1
    (-1,-4,1),       # t^2-4t-1
    (-1,-6,-10,-3,1),
    (-1,-2,1),
    (-1,-4,-3,1),
    (-1,-2,2),
)
assert len(CROSSING_FACTORS)==6
for f in CROSSING_FACTORS:
    assert f[0]<0 and f[-1]>0 and all(c<=0 for c in f[:-1])

def test(n,edges):
    N={v:forest_minor(n,edges,(v,)) for v in range(n)}
    E={e:forest_minor(n,edges,e) for e in edges}
    total=stable=tied=mixed=0
    factors=[]
    for i,e in enumerate(edges):
        for f in edges[:i]:
            total+=1
            # Positive t^2 cancels in the comparison of squared correlations.
            p=sub(mul(mul(E[e],E[e]),mul(N[f[0]],N[f[1]])),
                  mul(mul(E[f],E[f]),mul(N[e[0]],N[e[1]])))
            if p==[0]:tied+=1;continue
            if sign_uniform(p):stable+=1;continue
            mixed+=1
            poss=[]
            for k,q in enumerate(CROSSING_FACTORS):
                quotient=divide_exact(p,q)
                if quotient is not None and sign_uniform(quotient):
                    poss.append(k)
            assert poss,(n,edges,e,f,p)
            factors.append((e,f,poss[0]))
    assert total==stable+tied+mixed
    return total,stable,tied,mixed,factors

def run():
    expected={2:1,3:1,4:2,5:3,6:6,7:11,8:23}
    allcomp=allties=allmixed=0;mix_shapes=[];witnesses=[]
    for n in range(2,9):
        shapes={}
        for seq in product(range(n),repeat=n-2):
            edges=prufer_tree(n,seq)
            typ=canonical_tree(n,edges)
            shapes.setdefault(typ,edges)
        assert len(shapes)==expected[n],(n,len(shapes))
        for typ,edges in sorted(shapes.items()):
            independent_minor_checks(n,edges)
            total,stable,tied,mixed,factors=test(n,edges)
            allcomp+=total;allties+=tied;allmixed+=mixed
            if n<=7:assert mixed==0,(n,typ)
            if mixed:
                assert n==8
                mix_shapes.append(typ)
                witnesses.extend((typ,e,f,j) for e,f,j in factors)
        print('n=%d tree_shapes=%d'% (n,len(shapes)))
    assert len(mix_shapes)==6,(len(mix_shapes),mix_shapes)
    assert len(witnesses)==11,(len(witnesses),witnesses)
    # Distinguished symmetric double-claw with length-three path between hubs.
    W=tuple(sorted(tuple(sorted(e)) for e in
            ((1,0),(1,2),(0,5),(2,3),(2,4),(5,6),(5,7))))
    # Reconstruct and check the displayed witness rational functions exactly.
    N={v:forest_minor(8,W,(v,)) for v in range(8)}
    E={e:forest_minor(8,W,e) for e in W}
    q=[1,4,1]                # t^2 + 4t + 1
    r=[1,6,8,1]              # t^3 + 8t^2 + 6t + 1
    s=[1,7,12,1]             # t^3 + 12t^2 + 7t + 1
    assert mul(mul(E[(0,1)],E[(0,1)]),mul(r,r)) == \
           mul(mul(q,q),mul(N[0],N[1]))
    assert mul(mul(E[(1,2)],E[(1,2)]),mul(q,s)) == \
           mul(r,mul(N[1],N[2]))
    # In the difference of squared correlations, the only positive root
    # comes from q_cross(t)=t^2-4t-1, hence t=2+sqrt(5).
    _,_,_,mix,ff=test(8,W)
    assert mix==2,(mix,ff)
    assert any(set((e,f))==set(((0,1),(1,2))) and j==1 for e,f,j in ff),ff
    print('REVERSAL_SHAPES',len(mix_shapes),'PAIR_COMPARISONS',len(witnesses))
    print('SHAPE_KEYS',' '.join(mix_shapes))
    print('VERIFY_OK shape_counts=1,1,2,3,6,11,23 mixed_shape_count=6 mixed_edge_pairs=11 all_pair_comparisons=%d identically_tied=%d'%(allcomp,allties))

if __name__=='__main__':run()
