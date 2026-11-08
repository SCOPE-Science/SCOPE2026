"""Independent exhaustive bitmask check for the two-layer two-set Kneser prism, n=3,4,5."""
from itertools import combinations
from collections import Counter, deque

def audit(n, expectation):
    labels=list(combinations(range(n),2)); q=len(labels); V=2*q
    forb=[0]*V
    for a in range(V):
        layer=a//q; pair=set(labels[a%q]);
        for b in range(V):
            if a==b:continue
            if layer==b//q and pair.isdisjoint(labels[b%q]) or b==a+q or a==b+q:
                forb[a]|=1<<b
    sets=[]
    opt=expectation[0]
    for bitset in range(1<<V):
        if bitset.bit_count()!=opt:continue
        good=True
        for a in range(V):
            if bitset>>a&1 and bitset&forb[a]:good=False;break
        if good:sets.append(bitset)
    assert len(sets)==expectation[1], (n,len(sets))
    known=set(sets)
    AD={m:[] for m in sets}
    for m in sets:
        for a in range(V):
            if m>>a&1:
                for b in range(V):
                    if not(m>>b&1):
                        nxt=m^(1<<a)^(1<<b)
                        if nxt in known:AD[m].append(nxt)
        assert len(AD[m])==len(set(AD[m]))
        for nxt in AD[m]:
            moved=m & ~nxt; added=nxt & ~m
            assert (forb[moved.bit_length()-1]>> (added.bit_length()-1))&1
    seen=set();sizes=[]
    for v in sets:
        if v in seen:continue
        seen.add(v);Q=[v]
        for u in Q:
            for w in AD[u]:
                if w not in seen:seen.add(w);Q.append(w)
        sizes.append(len(Q))
    assert Counter(sizes)==Counter(expectation[2])
    assert sorted(Counter(map(len,AD.values())).items())==sorted(expectation[3].items())
    total_edges=sum(map(len,AD.values()))//2
    assert total_edges==expectation[4]
    dia=None
    if len(sizes)==1:
        dia=0
        for v in sets:
            dist={v:0};Q=deque([v])
            while Q:
                w=Q.popleft()
                for z in AD[w]:
                    if z not in dist:dist[z]=dist[w]+1;Q.append(z)
            dia=max(dia,max(dist.values()))
    assert dia==expectation[5]
    print('PASS direct n=',n,'states=',len(sets),'edges=',total_edges,'components=',Counter(sizes),'degrees=',Counter(map(len,AD.values())),'diam=',dia)

for n,e in [(3,(3,8,[8],{3:8},12,3)),(4,(6,8,[1]*8,{0:8},0,None)),(5,(7,80,[80],{3:40,4:40},140,9))]: audit(n,e)
