"""Independent verification: fixed-cardinality combinations and pairwise set comparison.
Run: python3 verify_b.py (Python standard library only).
"""
from collections import Counter, deque
from itertools import combinations
n=24; step=(12,7,-7)
E=set()
for i in range(n):
    E.add(frozenset((i,(i+1)%n)))
    E.add(frozenset((i,(i+step[i%3])%n)))
assert len(E)==36
edge_masks=[sum(1<<v for v in e) for e in E]
sets={}
for k in (9,10):
    good=[]
    for combo in combinations(range(n),k):
        mask=sum(1<<v for v in combo)
        if not any((mask&e)==e for e in edge_masks):good.append(mask)
    sets[k]=good
assert len(sets[9])==424 and len(sets[10])==8
# An independent 11-set would contain an independent 10-subset.
for s in sets[10]:
    for v in range(n):
        if not s>>v & 1:
            assert any(v in e and any((s>>u)&1 for u in e if u != v) for e in E)
def stats(k, sliding):
    S=sets[k]; A=[[] for _ in S]
    for i in range(len(S)):
        for j in range(i):
            d=S[i]^S[j]
            if d.bit_count()!=2:continue
            if sliding and frozenset(u for u in range(n) if d>>u&1) not in E:continue
            A[i].append(j);A[j].append(i)
    unseen=set(range(len(S))); sizes=[]; ecc=[]
    while unseen:
        root=next(iter(unseen));component={root};todo=[root];unseen.remove(root)
        for v in todo:
            for w in A[v]:
                if w not in component:component.add(w);unseen.remove(w);todo.append(w)
        sizes.append(len(component))
        for source in component:
            d={source:0};q=deque([source])
            while q:
                v=q.popleft()
                for w in A[v]:
                    if w not in d:d[w]=d[v]+1;q.append(w)
            ecc.append(max(d.values()))
    print(f'k={k} model={"TS" if sliding else "TJ"} states={len(S)} edges={sum(map(len,A))//2} component_sizes={sorted(sizes)} eccentricities={sorted(Counter(ecc).items())}')
    return sorted(sizes)
assert stats(9,False)==[424]
assert stats(9,True)==[2,2,2,2,416]
assert stats(10,False)==[4,4]
assert stats(10,True)==[4,4]
print('EXHAUSTIVE COMBINATIONS PASSED')
