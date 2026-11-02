"""Independent incidence-and-bitset certificate for PG(2,3) oval exchanges.
Nine affine points, four directions at infinity and thirteen explicit lines.
Run: python3 affine_check.py (Python standard library only).
"""
from itertools import combinations
from collections import Counter, deque

# Label affine (x,y) by 3*x+y, infinity points for slopes 0,1,2,vertical by 9..12.
lines=[]
for m in (0,1,2):
    for b in (0,1,2):
        pts=[3*x+((m*x+b)%3) for x in range(3)] + [9+m]
        lines.append(sum(1<<i for i in pts))
for x in range(3):
    lines.append(sum(1<<(3*x+y) for y in range(3)) | (1<<12))
lines.append(sum(1<<i for i in range(9,13)))
assert len(lines)==13 and len(set(lines))==13
assert all(L.bit_count()==4 for L in lines)
for x,y in combinations(range(13),2):
    assert sum(bool((L & (1<<x)) and (L & (1<<y))) for L in lines)==1

config=[]
for pts in combinations(range(13),4):
    m=sum(1<<i for i in pts)
    if all((m & L).bit_count() <= 2 for L in lines):
        config.append(m)
assert len(config)==234
index={m:i for i,m in enumerate(config)}
links=[]
for m in config:
    neigh=set()
    for old in range(13):
        if not (m>>old)&1: continue
        for new in range(13):
            if (m>>new)&1: continue
            n=m^(1<<old)^(1<<new)
            if n in index: neigh.add(index[n])
    links.append(neigh)
assert all(len(s)==12 for s in links)
assert all(i in links[j] for j,nb in enumerate(links) for i in nb)

joint=Counter()
for i,a in enumerate(config):
    dist=[-1]*len(config)
    dist[i]=0
    q=deque([i])
    while q:
        v=q.popleft()
        for w in links[v]:
            if dist[w]<0:
                dist[w]=dist[v]+1
                q.append(w)
    assert Counter(dist)=={0:1,1:12,2:60,3:114,4:47}
    anomalous_pairs={}
    anomalous_singles=Counter()
    for j,b in enumerate(config):
        if j==i:continue
        common=a&b
        r=common.bit_count()
        deviation=dist[j]-(4-r)
        assert deviation in (0,1)
        U=a|b
        nontrivial=all(U & L for L in lines) and all((U&L)!=L for L in lines)
        assert bool(deviation)==bool(nontrivial)
        if r==2 and deviation:
            anomalous_pairs[common]=anomalous_pairs.get(common,0)+1
        if r==1 and deviation:
            anomalous_singles[common]+=1
        if i<j: joint[(r,dist[j])]+=1
    assert len(anomalous_pairs)==6 and set(anomalous_pairs.values())=={1}
    assert len(anomalous_singles)==4 and set(anomalous_singles.values())=={2}

assert joint=={(3,1):1404,(2,2):7020,(2,3):702,(1,3):12636,(1,4):936,(0,4):4563}
print('AFFINE_INCIDENCE_BITSET_ALL_PAIRS_PASS')
print('arcs=234 edges=1404 diameter=4 degree=12')
print('nontrivial_blocking_exactly_matches_extra_exchange')
print('six_one_per_common_pair_eight_two_per_common_point')
