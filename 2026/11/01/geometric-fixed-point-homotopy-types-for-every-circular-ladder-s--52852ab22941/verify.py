#!/usr/bin/env python3
"""Independent finite checks for the orbit-conflict fixed-point classification.
Run: python3 verify.py. Standard library only. Finite tests do not prove the theorem.
"""
from collections import Counter
from itertools import combinations
from math import gcd


def graph(edges, vertices):
    vertices=list(vertices)
    A={v:set() for v in vertices}
    for x,y in edges:
        if x==y: raise ValueError('loop')
        A[x].add(y); A[y].add(x)
    return A


def prism(n):
    vs=[(i,j) for i in range(n) for j in range(2)]
    es=[]
    for i in range(n):
        es.append(((i,0),(i,1)))
        for j in range(2): es.append(((i,j),((i+1)%n,j)))
    return graph(es,vs)


def ladder(k):
    vs=[(i,j) for i in range(k) for j in range(2)]
    es=[((i,0),(i,1)) for i in range(k)]
    es += [((i,j),(i+1,j)) for i in range(k-1) for j in range(2)]
    return graph(es,vs)


def mobius(d):
    if d==1: return graph([(0,1)],[0,1])
    return graph([(i,(i+1)%(2*d)) for i in range(2*d)] +
                 [(i,i+d) for i in range(d)],range(2*d))


def circle_ladder(d):
    vs=[(i,j) for i in range(d) for j in range(2)]
    es=[((i,0),(i,1)) for i in range(d)]
    es += [((i,j),((i+1)%d,j)) for i in range(d) for j in range(2)]
    return graph(es,vs)


def quotient(n,a,b,c):
    """g(i,j)=(a+(-1)^b*i,j+c mod2), union graph-orbits."""
    G=prism(n)
    def transform(v):
        i,j=v
        return ((a + (-i if b else i))%n,j^c)
    seen=set();orbits=[]
    for v in G:
        if v not in seen:
            orb=[]; u=v
            while u not in orb:
                orb.append(u)
                u=transform(u)
            assert u==v
            seen.update(orb)
            orbits.append(orb)
    safe=[]
    for o in orbits:
        if all(x not in G[y] for x,y in combinations(o,2)):
            safe.append(o)
    owner={v:i for i,o in enumerate(safe) for v in o}
    Q={i:set() for i in range(len(safe))}
    for v in G:
        for w in G[v]:
            if v in owner and w in owner and owner[v]!=owner[w]:
                Q[owner[v]].add(owner[w])
    return Q


def isomorphic(A,B):
    if len(A)!=len(B):return False
    if sorted(map(len,A.values()))!=sorted(map(len,B.values())):return False
    if not A:return True
    a_keys=list(A);b_keys=list(B)
    def refine_color(G):
        # Exact isomorphism-invariant iterative color refinement.
        col={v:len(G[v]) for v in G}
        while True:
            sig={v:(col[v],tuple(sorted(Counter(col[w] for w in G[v]).items()))) for v in G}
            names={x:i for i,x in enumerate(sorted(set(sig.values())))}
            new={v:names[sig[v]] for v in G}
            if new==col:return col
            col=new
    ac=refine_color(A);bc=refine_color(B)
    if sorted(ac.values())!=sorted(bc.values()): return False
    chosen={};used=set()
    def rec():
        if len(chosen)==len(A):return True
        best=None;best_opts=None
        for x in a_keys:
            if x in chosen:continue
            opts=[y for y in b_keys if y not in used and bc[y]==ac[x] and
                  all((u in A[x])==(chosen[u] in B[y]) for u in chosen)]
            if not opts:return False
            if best_opts is None or len(opts)<len(best_opts):best,best_opts=x,opts
        for y in best_opts:
            chosen[best]=y;used.add(y)
            if rec():return True
            used.remove(y);del chosen[best]
        return False
    return rec()


def expectation(n,a,b,c):
    if not b:
        d=gcd(n,a); order=n//d
        if not c:
            return {} if d==1 else circle_ladder(d)
        if order%2:return {}
        return mobius(d)
    if n%2: return ladder((n-1)//2)
    m=n//2
    return ladder(m+1 if a%2==0 and c==0 else
                  m-2 if a%2==1 and c==0 else
                  m-1 if a%2==0 and c==1 else m)


def f2_homology(G):
    """Reduced mod-two Betti ranks by exact augmented boundary elimination."""
    vs=list(G);n=len(vs);edges={(min(i,j),max(i,j)) for i in range(n)
              for j in range(i+1,n) if vs[j] in G[vs[i]]}
    bysize=[[] for _ in range(n+1)]; bysize[0].append(0)
    for mask in range(1,1<<n):
        indices=[i for i in range(n) if mask & (1<<i)]
        if any((i,j) in edges for i,j in combinations(indices,2)):
            continue
        bysize[len(indices)].append(mask)
    dims=[len(v) for v in bysize]
    rank=[0]*len(dims)
    for k in range(1,len(dims)):
        index={v:i for i,v in enumerate(bysize[k-1])}
        pivots={}
        for face in bysize[k]:
            col=0
            for i in range(n):
                if face>>i&1:
                    col ^= 1<<index[face ^ (1<<i)]
            while col:
                bit=col.bit_length()-1
                if bit not in pivots:
                    pivots[bit]=col
                    break
                col ^= pivots[bit]
        rank[k]=len(pivots)
    return {k-1:dims[k]-rank[k]-rank[k+1] if k+1<len(rank)
            else dims[k]-rank[k] for k in range(1,len(dims))
            if dims[k]-rank[k]-(rank[k+1] if k+1<len(rank) else 0)>0}


def expected_spheres_mobius(d):
    if d==1:return {0:1}
    k=d//4
    if d%4==0:return {2*k-1:1}
    if d%4==2:return {2*k:3}
    return {2*k:1}


def expected_spheres_circle(d):
    k=d//4
    if d%4==0:return {2*k-1:3}
    if d%4==1:return {2*k-1:1}
    if d%4==2:return {2*k:1}
    return {2*k+1:1}


def main():
    checked=0
    for n in range(5,21):
        for a in range(n):
            for b in (0,1):
                for c in (0,1):
                    A=quotient(n,a,b,c)
                    B=expectation(n,a,b,c)
                    assert isomorphic(A,B),(n,a,b,c,len(A),len(B))
                    checked+=1
    lad_checks=0
    for k in range(1,7):
        assert f2_homology(ladder(k))=={(k+1)//2-1:1},k
        lad_checks+=1
    mob_checks=0
    for d in range(1,6):
        assert f2_homology(mobius(d))==expected_spheres_mobius(d),d
        mob_checks+=1
    circ_checks=0
    for d in range(2,6):
        assert f2_homology(circle_ladder(d))==expected_spheres_circle(d),d
        circ_checks+=1
    assert isomorphic(quotient(12,0,1,0),ladder(7))
    assert isomorphic(quotient(12,1,1,0),ladder(4))
    print('VERIFY_OK: orbit_isomorphisms=%d, ladder_mod2=%d, mobius_mod2=%d, circular_mod2=%d' %
          (checked,lad_checks,mob_checks,circ_checks))

if __name__=='__main__':main()
