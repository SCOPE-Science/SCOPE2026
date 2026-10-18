#!/usr/bin/env python3
"""Exhaustive edge-mask verification for GP(8,3) six-cycle matching flips."""
import collections
import hashlib
import json
from pathlib import Path

N = 8
V = 2*N
edges = sorted({tuple(sorted((a,b))) for i in range(N) for a,b in
                [(i,(i+1)%N),(i,N+i),(N+i,N+(i+3)%N)]})
assert len(edges)==24
idx = {e:k for k,e in enumerate(edges)}
neigh=[[] for _ in range(V)]
for k,(u,v) in enumerate(edges):
    neigh[u].append((v,k));neigh[v].append((u,k))
for row in neigh:row.sort()

matchings=[]
def match_rec(rem,mask):
    if not rem:
        matchings.append(mask)
        return
    v=(rem&-rem).bit_length()-1
    for w,j in neigh[v]:
        if rem>>w&1:
            match_rec(rem & ~(1<<v) & ~(1<<w),mask | 1<<j)
match_rec((1<<V)-1,0)
matchings=sorted(matchings)
assert len(matchings)==33 and len(set(matchings))==33

cycles=set()
def walk(path):
    s=path[0]
    if len(path)==6:
        if s in [w for w,j in neigh[path[-1]]]:
            path_edges=[tuple(sorted((path[i],path[(i+1)%6]))) for i in range(6)]
            cycles.add(sum(1<<idx[e] for e in path_edges))
        return
    for w,j in neigh[path[-1]]:
        if w >= s and w not in path:
            walk(path+[w])
for root in range(V):walk([root])
cycles=sorted(cycles)
assert len(cycles)==24
index={m:i for i,m in enumerate(matchings)}
links=[set() for _ in matchings]
flip_count=collections.Counter()
for i,m in enumerate(matchings):
    for c in cycles:
        if (m&c).bit_count()==3:
            other=m^c
            if other in index:
                j=index[other]
                links[i].add(j)
                flip_count[c]+=1
assert all(i not in row for i,row in enumerate(links))
assert all(i in links[j] for i,row in enumerate(links) for j in row)
assert sum(map(len,links))==192
assert len(flip_count)==24 and set(flip_count.values())=={8}

color={0:0};queue=[0]
for u in queue:
    for v,j in neigh[u]:
        if v not in color:
            color[v]=1-color[u];queue.append(v)
        else:assert color[v]!=color[u]
left=sorted(x for x in color if color[x]==0)
right=sorted(x for x in color if color[x]==1)
assert len(left)==len(right)==8
rindex={v:i for i,v in enumerate(right)}
signs=[]
for m in matchings:
    perm=[]
    for u in left:
        ws=[v for v,j in neigh[u] if m>>j&1]
        assert len(ws)==1
        perm.append(rindex[ws[0]])
    assert len(set(perm))==8
    inversions=sum(perm[i]>perm[j] for i in range(8) for j in range(i+1,8))
    signs.append(1 if inversions%2==0 else -1)
assert collections.Counter(signs)=={1:3,-1:30}
assert all(signs[i]==signs[j] for i,row in enumerate(links) for j in row)

components=[];leftover=set(range(len(matchings)))
while leftover:
    start=min(leftover);seen={start};work=[start]
    for i in work:
        for j in links[i]:
            if j not in seen:seen.add(j);work.append(j)
    leftover-=seen
    components.append(sorted(seen))
components.sort(key=lambda c:(-len(c),c[0]))
assert [len(c) for c in components]==[30,1,1,1]
assert all(signs[x]==-1 for x in components[0])
assert all(signs[c[0]]==1 and not links[c[0]] for c in components[1:])
assert collections.Counter(len(links[x]) for x in components[0])=={6:24,8:6}

# The isolated matchings form a one-factorization of the entire edge set.
iso=[matchings[c[0]] for c in components[1:]]
assert iso[0]&iso[1]==iso[0]&iso[2]==iso[1]&iso[2]==0
assert iso[0]|iso[1]|iso[2]==(1<<len(edges))-1

all_d=[]
for s in components[0]:
    d={s:0};todo=[s]
    for v in todo:
        for u in links[v]:
            if u not in d:d[u]=d[v]+1;todo.append(u)
    assert len(d)==30
    all_d.extend(d.values())
assert max(all_d)==4
assert sum(len(row) for row in links)//2==96

certificate={
    'graph':'GP(8,3)','edge_order':[list(e) for e in edges],
    'left_order':left,'right_order':right,
    'matching_masks':[f'{m:06x}' for m in matchings],
    'six_cycle_masks':[f'{c:06x}' for c in cycles],
    'flip_adjacency':[sorted(row) for row in links],
    'bipartite_signs':signs,
    'components':components,
    'positive_isolated_matching_masks':[f'{x:06x}' for x in sorted(iso)],
    'long_component_diameter':4,
}
if __name__=='__main__':
    import sys
    if len(sys.argv)>1:
        target=Path(sys.argv[1]);got=json.loads(target.read_text(encoding='utf-8'))
        assert got==certificate, 'full certificate disagrees with enumeration'
        print('CERTIFICATE_REPLAY_OK entries=33 cycles=24 adjacency_rows=33 exact=true')
    else:
        Path(__file__).with_name('hexagon_flip_certificate.json').write_text(
            json.dumps(certificate,sort_keys=True,separators=(',',':'),ensure_ascii=False)+'\n',encoding='utf-8')
    print('MASK_VERIFY_OK vertices=16 edges=24 matchings=33 hexagons=24 flip_edges=96')
    print('MASK_VERIFY_OK sign_classes=30+3 nontrivial_component=30 singletons=3 diameter=4')
    print('MASK_VERIFY_OK degrees=6x24+8x6 isolated_matchings_partition_edges=true')
