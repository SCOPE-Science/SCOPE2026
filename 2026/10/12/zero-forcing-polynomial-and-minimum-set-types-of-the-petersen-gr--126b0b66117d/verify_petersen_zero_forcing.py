from itertools import combinations, permutations
from collections import Counter

V = tuple(range(10))  # 0..4=u_i; 5..9=v_i
adj = {v:set() for v in V}
def add(a,b):
    adj[a].add(b); adj[b].add(a)
for i in range(5):
    add(i,(i+1)%5)
    add(i,5+i)
    add(5+i,5+((i+2)%5))

assert all(len(adj[v])==3 for v in V)
assert sum(map(len,adj.values()))//2==15

def closure(S):
    blue=set(S)
    while True:
        forced=set()
        for u in tuple(blue):
            w=[v for v in adj[u] if v not in blue]
            if len(w)==1:
                forced.add(w[0])
        if not forced:
            return frozenset(blue)
        blue.update(forced)

def zf(S): return len(closure(S))==10

def edges_on(S):
    S=set(S)
    return {(min(a,b),max(a,b)) for a in S for b in adj[a] if b in S and a<b}

patterns={
 'C5': {(0,1),(1,2),(2,3),(3,4),(0,4)},
 'P5': {(0,1),(1,2),(2,3),(3,4)},
 'P4+K1': {(0,1),(1,2),(2,3)},
 'FORK': {(0,1),(1,2),(1,3),(3,4)},
 'P3+2K1': {(0,1),(1,2)},
 '2K2+K1': {(0,1),(2,3)},
}

def iso_type(S):
    s=tuple(S); E=edges_on(s)
    for name,P in patterns.items():
        for perm in permutations(range(5)):
            mp={s[i]:perm[i] for i in range(5)}
            im={(min(mp[a],mp[b]),max(mp[a],mp[b])) for a,b in E}
            if im==P:
                return name
    return 'OTHER'

counts=Counter()
type_total=Counter(); type_zf=Counter()
for r in range(11):
    for S in combinations(V,r):
        if zf(S): counts[r]+=1
        if r==5:
            t=iso_type(S); type_total[t]+=1
            if zf(S): type_zf[t]+=1

expected={5:132,6:190,7:120,8:45,9:10,10:1}
assert dict(counts)==expected, (counts,expected)
assert sum(counts.values())==498
assert type_total==Counter({'P4+K1':60,'FORK':60,'P5':60,'P3+2K1':30,'2K2+K1':30,'C5':12}), type_total
assert type_zf==Counter({'P4+K1':60,'P5':60,'C5':12}), type_zf
assert all(not zf(S) for r in range(5) for S in combinations(V,r))
assert all(zf(S) == (iso_type(S) in {'C5','P5','P4+K1'}) for S in combinations(V,5))
print('VERIFY_OK subsets=1024 zf_total=498 coefficients=5:132,6:190,7:120,8:45,9:10,10:1 min_types=C5:12,P5:60,P4+K1:60 nonforcing5=120')
