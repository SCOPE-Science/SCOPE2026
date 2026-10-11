#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict

RAW = [
"014","018","023","027","036","049","056","05b","07a","08a","09b",
"125","126","137","139","147","15a","16b","18b","19a","23b","248",
"24a","258","269","279","2ab","345","34b","35a","367","389","38a",
"459","46a","46b","478","568","579","57b","67a","689","78b","9ab"]
lab={str(i):i for i in range(10)}; lab.update({'a':10,'b':11})
F={tuple(sorted(lab[c] for c in s)) for s in RAW}
V=tuple(range(12))
def faces(k): return {tuple(sorted(c)) for f in F for c in combinations(f,k)}
E=sorted(faces(2)); assert len(F)==44 and len(E)==66 and set(E)==set(combinations(V,2))
# closed surface local incidence
edeg=Counter(e for t in F for e in combinations(t,2)); assert set(edeg.values())=={2}
assert 12-66+44==-10 # chi=2-2g => g=6
Ei={e:i for i,e in enumerate(E)}
def evec(edges):
    x=0
    for e in edges: x ^= 1<<Ei[tuple(sorted(e))]
    return x
def tri_bd(t): return evec(combinations(t,2))
def rref(rows):
    B={}
    for x in rows:
        y=x
        for p in sorted(B,reverse=True):
            if (y>>p)&1:y^=B[p]
        if not y: continue
        p=y.bit_length()-1
        for q in list(B):
            if (B[q]>>p)&1:B[q]^=y
        B[p]=y
    return dict(sorted(B.items(),reverse=True))
def red(x,B):
    y=x
    for p,r in B.items():
        if (y>>p)&1:y^=r
    return y
B=rref([tri_bd(t) for t in F]); assert len(B)==43
assert len(E)-(len(V)-1)-len(B)==12
alltri=set(combinations(V,3)); missing=sorted(alltri-F); assert len(missing)==176
cls=defaultdict(list)
for t in missing:
    c=red(tri_bd(t),B); assert c!=0; cls[c].append(t)
assert len(cls)==110
mult=Counter(len(v) for v in cls.values()); assert mult==Counter({1:56,2:48,4:6})
# Full automorphism group. Any automorphism is determined by image of vertex 0 and an isomorphism
# from its link cycle to the target vertex link cycle. Enumerate all such dihedral link maps.
def link_cycle(v):
    adj=defaultdict(list)
    for t in F:
        if v in t:
            a,b=[x for x in t if x!=v]
            adj[a].append(b); adj[b].append(a)
    assert set(adj)==set(V)-{v} and all(len(adj[x])==2 for x in adj)
    start=min(adj); n1=min(adj[start]); cyc=[start,n1]
    prev,start2=start,n1
    while True:
        nxt=adj[start2][0] if adj[start2][1]==prev else adj[start2][1]
        if nxt==cyc[0]: break
        cyc.append(nxt); prev,start2=start2,nxt
    assert len(cyc)==11
    return tuple(cyc)
links={v:link_cycle(v) for v in V}
def preserves(p):
    return {tuple(sorted(p[x] for x in t)) for t in F}==F
AUT=[]
source=links[0]
for target in V:
    tc=links[target]
    for shift in range(11):
        for sign in (1,-1):
            p={0:target}
            for i,x in enumerate(source): p[x]=tc[(shift+sign*i)%11]
            if len(set(p.values()))==12 and preserves(p): AUT.append(p)
# unique mappings
uniq={tuple(p[i] for i in V):p for p in AUT}; AUT=list(uniq.values())
assert len(AUT)==12
# Missing support orbits
def imt(t,p): return tuple(sorted(p[x] for x in t))
unseen=set(missing); supp_orb=[]
while unseen:
    t=min(unseen); O={imt(t,p) for p in AUT}; assert O<=set(missing); supp_orb.append((len(O),t)); unseen-=O
assert sorted(n for n,_ in supp_orb)==[4,4]+[12]*14
# Homology class action and orbits. use any representative triangle from class.
def class_action(c,p):
    t=cls[c][0]
    return red(tri_bd(imt(t,p)),B)
unseen=set(cls); corbs=[]
while unseen:
    c=next(iter(unseen)); O={class_action(c,p) for p in AUT}; assert O<=set(cls)
    m=len(cls[c]); assert all(len(cls[x])==m for x in O)
    corbs.append((len(O),m)); unseen-=O
prof=Counter(corbs)
assert prof==Counter({(12,1):4,(4,1):2,(12,2):3,(6,2):2,(6,4):1})
# multiplicity-4 classes one orbit of six classes, 24 supports
quad=[c for c in cls if len(cls[c])==4]; assert len(quad)==6
O={class_action(quad[0],p) for p in AUT}; assert set(quad)==O
# every missing triangle is a simple length-3 nonzero H1 class; no shorter simple cycles exist.
print('VERIFY_OK f=12,66,44 chi=-10 genus=6 H1_F2_dim=12 missing3=176 all_missing3_nonzero=yes '
      'triangular_classes=110 multiplicities=1:56,2:48,4:6 aut=12 '
      'support_orbits=4,4,' + ','.join(['12']*14) + ' '
      'class_orbits=(12,1)x4,(4,1)x2,(12,2)x3,(6,2)x2,(6,4)x1 quadruple_classes_one_orbit=yes')
