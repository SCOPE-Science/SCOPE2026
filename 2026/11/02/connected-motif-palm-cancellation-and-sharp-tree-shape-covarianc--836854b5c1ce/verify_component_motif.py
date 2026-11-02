#!/usr/bin/env python3
"""Exact, independent exhaustive G(n,p) verification of component--connected-subgraph covariances.
Pure Python standard library. Run python3 check_component_motif.py.
"""
from itertools import combinations, permutations
from math import comb, factorial
from fractions import Fraction

GRAPHS = {
 'K2': (2, ((0,1),)),
 'P3': (3, ((0,1),(1,2))),
 'K3': (3, ((0,1),(0,2),(1,2))),
 'P4': (4, ((0,1),(1,2),(2,3))),
 'S4': (4, ((0,1),(0,2),(0,3))),
 'C4': (4, ((0,1),(1,2),(2,3),(3,0))),
 'K4': (4, tuple(combinations(range(4),2))),
}
def canonical_patterns(n, pattern):
    v, ed=GRAPHS[pattern]
    if n<v:return []
    inst=set()
    for inds in combinations(range(n),v):
        for order in permutations(inds):
            inst.add(frozenset(tuple(sorted((order[i],order[j]))) for i,j in ed))
    # Distinct edge sets are distinct copies for connected patterns with at least 2 vertices.
    return list(inst)

def matches_component(comp, edges, H):
    h,hed=GRAPHS[H]
    if len(comp)!=h:return False
    base=frozenset(edges)
    for order in permutations(comp):
        candidate=frozenset(tuple(sorted((order[i],order[j]))) for i,j in hed)
        if candidate==base:return True
    return False

def comp_count(n, edges, H):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for u,v in edges:parent[find(u)]=find(v)
    blocks={}
    for i in range(n):blocks.setdefault(find(i),[]).append(i)
    return sum(matches_component(block,[e for e in edges if e[0] in block],H) for block in blocks.values())

def universal_count(n,h,F):
    f,_=GRAPHS[F]
    return len(canonical_patterns(n,F))-len(canonical_patterns(n-h,F))

def direct(n,p,H,F,induced=False):
    E=list(combinations(range(n),2));N=len(E)
    motifs=[]
    for instance in canonical_patterns(n,F):
        present=sum(1<<E.index(edge) for edge in instance)
        verts=sorted({v for edge in instance for v in edge})
        forbidden=sum(1<<E.index(edge) for edge in combinations(verts,2) if edge not in instance) if induced else 0
        motifs.append((present,forbidden))
    a,b=p.numerator,p.denominator
    norm=b**N
    ec=ex=ecx=0
    from collections import Counter
    moments=Counter()
    for mask in range(1<<N):
        edges=[edge for i,edge in enumerate(E) if mask&(1<<i)]
        c=comp_count(n,edges,H)
        x=sum((mask&yes)==yes and (mask&no)==0 for yes,no in motifs)
        w=a**len(edges)*(b-a)**(N-len(edges))
        ec+=w*c;ex+=w*x;ecx+=w*c*x
    actual=Fraction(ecx,norm)-Fraction(ec*ex,norm**2)
    h,_=GRAPHS[H];f,fe=GRAPHS[F]
    inside=len(canonical_patterns(h,F))
    # Internal motifs in H, not in complete graph
    h_edges=frozenset(tuple(sorted(x)) for x in GRAPHS[H][1]);E_H=list(combinations(range(h),2))
    instances=canonical_patterns(h,F)
    t=sum(1 for edges in instances if (edges==frozenset(e for e in h_edges if set(e).issubset({u for edge in edges for u in edge})) if induced else edges.issubset(h_edges)))
    q=universal_count(n,h,F)
    miss=comb(f,2)-len(fe) if induced else 0
    expected=Fraction(ec,norm)*(t-q*p**len(fe)*(1-p)**miss)
    assert actual==expected,(n,p,H,F,induced,actual,expected,t,q)
    return (n,str(p),H,F,'induced' if induced else 'noninduced',t,q,str(actual))

if __name__=='__main__':
    cases=[(4,'K2','K2'),(4,'P3','K2'),(4,'K3','K3'),(4,'K3','K2'),
           (5,'K2','K2'),(5,'P3','K2'),(5,'K3','K3'),(5,'K3','P3'),
           (5,'P4','K2'),(5,'P4','P3'),(5,'S4','P3'),(5,'S4','K2'),(5,'C4','P3'),(5,'C4','K3'),
           (5,'K4','K3')]
    hits=0
    for n,H,F in cases:
        for p in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
            result=direct(n,p,H,F);hits+=1
            result2=direct(n,p,H,F,induced=True);hits+=1
            if p==Fraction(1,2):print(*result,sep=' | ')
    for H in ('P4','S4'):
        result=direct(5,Fraction(7,25),H,'P3');hits+=1
        print('transition example',*result,sep=' | ')
    for H in ('P4','S4'):
        result=direct(5,Fraction(1,3),H,'P3',induced=True);hits+=1
        print('induced motif',*result,sep=' | ')
    print('PASS',hits,'independent exhaustive probability identities; no sampling')
