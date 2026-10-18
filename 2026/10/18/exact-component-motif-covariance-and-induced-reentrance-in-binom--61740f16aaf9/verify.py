"""Exact finite checks for covariance of connected-component and connected-motif counts.
Run: python verify.py
"""
from itertools import combinations, permutations
from fractions import Fraction
from math import comb

# Graphs on canonical vertex sets are encoded as bitsets of unordered pairs.
def pairs(n): return list(combinations(range(n), 2))
def bit_graph(n, edges):
    ed = {tuple(sorted(x)) for x in edges}
    return sum(1 << i for i, e in enumerate(pairs(n)) if e in ed)

def patterns(n, template):
    es = pairs(n); edge_set = set(template)
    result = set()
    for pm in permutations(range(n)):
        result.add(sum(1 << idx for idx, (i,j) in enumerate(es)
                       if tuple(sorted((pm[i],pm[j]))) in edge_set))
    return result

def label_patterns(n, edges):
    return patterns(n, {tuple(sorted(e)) for e in edges})

def edge_induced(mask, n, subset):
    all_edges = pairs(n)
    sub_edges = pairs(len(subset))
    loc = {v:i for i,v in enumerate(subset)}
    sub_map = {frozenset(pair):i for i,pair in enumerate(sub_edges)}
    result = 0
    for idx,(a,b) in enumerate(all_edges):
        if (mask >> idx)&1 and a in loc and b in loc:
            result |= 1 << sub_map[frozenset((loc[a],loc[b]))]
    return result

def graph_components(mask,n):
    adj = [set() for _ in range(n)]
    for idx,(a,b) in enumerate(pairs(n)):
        if (mask >> idx)&1:
            adj[a].add(b);adj[b].add(a)
    unseen = set(range(n)); comps=[]
    while unseen:
        seed=next(iter(unseen)); seen={seed};todo=[seed]; unseen.remove(seed)
        while todo:
            v=todo.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w);unseen.remove(w);todo.append(w)
        comps.append(tuple(sorted(seen)))
    return comps

# Selected connected types, enough to exercise varying order, edge count, and induced/noninduced motifs.
T = {
'K2':(2,[(0,1)]),
'P3':(3,[(0,1),(1,2)]),
'K3':(3,[(0,1),(1,2),(0,2)]),
'P4':(4,[(0,1),(1,2),(2,3)]),
'C4':(4,[(0,1),(1,2),(2,3),(3,0)]),
'K4':(4,list(pairs(4))),
}
P = {key:label_patterns(*v) for key,v in T.items()}

def a_count(H,F,induced):
    h,edges=T[H]; f,_=T[F]
    if f>h:return 0
    g=bit_graph(h,edges)
    return sum((int(edge_induced(g,h,S) in P[F]) if induced else
               sum((edge_induced(g,h,S)&v)==v for v in P[F]))
               for S in combinations(range(h),f))

def count_motifs(mask,n,F,induced):
    f,_=T[F]
    if f>n:return 0
    return sum((int(edge_induced(mask,n,S) in P[F]) if induced else
               sum((edge_induced(mask,n,S)&v)==v for v in P[F]))
               for S in combinations(range(n),f))

def counts(mask,n):
    c=graph_components(mask,n)
    return {H:sum(len(S)==T[H][0] and edge_induced(mask,n,S) in P[H] for S in c)
            for H in T if T[H][0]<=n}

def formula(n,H,F,p,induced):
    h,He=T[H]; f,Fe=T[F]
    cF=len(P[F]); e=len(Fe); nonedge=comb(f,2)-e
    B=cF*(comb(n,f)-(comb(n-h,f) if n-h>=f else 0))
    a=a_count(H,F,induced)
    psi=p**e*((1-p)**nonedge if induced else 1)
    cH=len(P[H]); eh=len(He)
    EnH=(Fraction(comb(n,h)*cH,1)*p**eh
         *(1-p)**(comb(h,2)-eh+h*(n-h)))
    return EnH*(a-B*psi)

def test():
    assertions=0
    choices=[Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(3,4)]
    for n in range(2,6):
        M=comb(n,2)
        cells=[]
        for bits in range(1<<M):
            hm=counts(bits,n)
            fm={(F,ind):count_motifs(bits,n,F,ind)
                for F in T if T[F][0]<=n for ind in (False,True)}
            cells.append((bits.bit_count(),hm,fm))
        for H in T:
            if T[H][0]>n:continue
            for F in T:
                if T[F][0]>n:continue
                for induced in (False,True):
                    for p in choices:
                        d=p.denominator;r=p.numerator
                        Z=d**M
                        E1=E2=E12=0
                        for nume,hm,fm in cells:
                            w=r**nume*(d-r)**(M-nume)
                            a=hm[H];b=fm[(F,induced)]
                            E1+=w*a;E2+=w*b;E12+=w*a*b
                        actual=Fraction(E12,Z)-Fraction(E1*E2,Z*Z)
                        expected=formula(n,H,F,p,induced)
                        assert actual==expected,(n,H,F,induced,p,actual,expected)
                        assertions+=1
    n=4;p=Fraction(1,2)
    actual=formula(n,'P3','P3',p,True)
    assert actual==-Fraction(3,32), actual
    assertions+=1
    # Two strict transitions: the signed covariance factor is 1-12p^2(1-p).
    assert 1-12*Fraction(1,4)**2*(1-Fraction(1,4))>0
    assert 1-12*Fraction(1,2)**2*(1-Fraction(1,2))<0
    assert 1-12*Fraction(9,10)**2*(1-Fraction(9,10))>0
    assertions+=3
    print(f'PASS {assertions} exact-rational covariance and phase checks, exhaustive all graphs n=2..5')
if __name__=='__main__':test()
