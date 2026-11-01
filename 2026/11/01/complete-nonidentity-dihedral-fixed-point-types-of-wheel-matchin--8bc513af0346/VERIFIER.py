"""Exact finite verification of wheel-matching fixed-space orbit complexes.

Requires Python 3.9 or later; uses only the standard library. Infinite-family
claims rely on the separate mathematical proof, not finite tests.
"""
from math import gcd


def edges(n):
    return [('S',i) for i in range(n)] + [('R',i) for i in range(n)]


def endpoints(e,n):
    kind,i=e
    return {-1,i} if kind=='S' else {i,(i+1)%n}


def action(e,n,a,refl):
    kind,i=e
    if kind=='S':return ('S',(a-i if refl else a+i)%n)
    return ('R',(a-i-1 if refl else a+i)%n)


def orbit_graph(n,a,refl):
    remaining=set(edges(n)); admissible=[]
    while remaining:
        start=min(remaining); orb=[]; item=start
        while item not in orb:
            orb.append(item)
            item=action(item,n,a,refl)
        assert item==start
        remaining.difference_update(orb)
        used=set(); ok=True
        for e in orb:
            ep=endpoints(e,n)
            if used&ep:ok=False
            used.update(ep)
        if ok:admissible.append(tuple(orb))
    conflict=set()
    for i in range(len(admissible)):
        for j in range(i+1,len(admissible)):
            if any(endpoints(e,n)&endpoints(f,n)
                   for e in admissible[i] for f in admissible[j]):
                conflict.add((i,j))
    return admissible,conflict


def components(vcount,conflict):
    adj=[set() for _ in range(vcount)]
    for i,j in conflict:adj[i].add(j);adj[j].add(i)
    unseen=set(range(vcount));result=[]
    while unseen:
        seed=min(unseen);stack=[seed];seen={seed};unseen.remove(seed)
        while stack:
            v=stack.pop()
            for w in adj[v]:
                if w in unseen:
                    unseen.remove(w);seen.add(w);stack.append(w)
        result.append((len(seen),sum(len(adj[v]) for v in seen)//2,
                       max(len(adj[v]) for v in seen)))
    return sorted(result)


def path_signature(k):
    return (k, max(0,k-1), 0 if k==1 else 1 if k==2 else 2)


def cycle_signature(k):
    return (k,k,2)


def test_graph_reductions():
    total=0
    for n in range(5,65):
        for a in range(n):
            for refl in (False,True):
                if a==0 and not refl:continue
                orbs,conf=orbit_graph(n,a,refl)
                actual=components(len(orbs),conf)
                if not refl:
                    g=gcd(n,a)
                    target=[] if g==1 else [path_signature(2) if g==2 else cycle_signature(g)]
                elif n%2:
                    target=sorted([path_signature((n-1)//2),path_signature(1)])
                elif a%2:
                    target=[path_signature(n//2+1)]
                else:
                    target=sorted([path_signature(2),path_signature(n//2-2)])
                assert actual==target,(n,a,refl,actual,target)
                total+=1
    print('PASS:',total,'nonidentity dihedral orbit graphs match all four families')


def all_matching_sets(n):
    es=edges(n);result=set()
    def backtrack(i,used,chosen):
        if i==len(es):result.add(frozenset(chosen));return
        backtrack(i+1,used,chosen)
        ep=endpoints(es[i],n)
        if not used&ep:
            chosen.append(es[i]);backtrack(i+1,used|ep,chosen);chosen.pop()
    backtrack(0,set(),[])
    return result


def independence_faces(vcount,conflict):
    adjacent=[0]*vcount
    for i,j in conflict:
        adjacent[i]|=1<<j;adjacent[j]|=1<<i
    faces=[]
    def rec(i,mask):
        if i==vcount:faces.append(mask);return
        rec(i+1,mask)
        if not (adjacent[i]&mask):rec(i+1,mask|(1<<i))
    rec(0,0);return faces


def test_direct_fixed_matchings():
    count=0
    for n in range(5,12):
        full=all_matching_sets(n)
        for a in range(n):
            for refl in (False,True):
                if a==0 and not refl:continue
                fixed={match for match in full
                       if {action(e,n,a,refl) for e in match}==set(match)}
                orbs,conf=orbit_graph(n,a,refl)
                faces=independence_faces(len(orbs),conf)
                rebuilt={frozenset(e for i in range(len(orbs)) if mask>>i&1
                                      for e in orbs[i]) for mask in faces}
                assert fixed==rebuilt,(n,a,refl)
                count+=1
    print('PASS:',count,'independently enumerated fixed-matching face sets')


def homology_mod2(vcount,conflict):
    masks=independence_faces(vcount,conflict)
    degrees={}
    for mask in masks:
        k=mask.bit_count()
        if k:degrees.setdefault(k-1,[]).append(mask)
    ranks={}
    for d in range(1,max(degrees,default=-1)+1):
        rows={s:i for i,s in enumerate(degrees[d-1])}
        basis={}
        for simplex in degrees[d]:
            col=0; bits=simplex
            while bits:
                b=bits&-bits;bits-=b
                col^=1<<rows[simplex^b]
            while col:
                pivot=col.bit_length()-1
                if pivot in basis:col^=basis[pivot]
                else:basis[pivot]=col;break
        ranks[d]=len(basis)
    return {d:(len(s)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0))
            for d,s in degrees.items() if len(s)-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)}


def test_template_homology():
    checks=0
    for t in range(1,16):
        path_edges={(i,i+1) for i in range(t-1)}
        actual=homology_mod2(t,path_edges)
        if t%3==1: expected={}
        elif t%3==0:expected={t//3-1:1}
        else:expected={(t-2)//3:1}
        assert actual==expected,('path',t,actual,expected)
        checks+=1
    for t in range(3,16):
        cyc_edges={(i,i+1) for i in range(t-1)}|{(0,t-1)}
        actual=homology_mod2(t,cyc_edges)
        if t%3==0:expected={t//3-1:2}
        elif t%3==1:expected={(t-4)//3:1}
        else:expected={(t-2)//3:1}
        assert actual==expected,('cycle',t,actual,expected)
        checks+=1
    print('PASS:',checks,'template mod-2 boundary-rank tests')


if __name__=='__main__':
    test_graph_reductions()
    test_direct_fixed_matchings()
    test_template_homology()
