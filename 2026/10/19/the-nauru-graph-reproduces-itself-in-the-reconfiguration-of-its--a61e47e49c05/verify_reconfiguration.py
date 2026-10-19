#!/usr/bin/env python3
"""Direct enumeration of every optimal strong resolver and every token-jump move."""
import itertools,collections,hashlib,json
N=24
adj=[set() for i in range(N)]
for i in range(12):
    for a,b in ((i,(i+1)%12),(i,12+i),(12+i,12+(i+5)%12)):
        adj[a].add(b);adj[b].add(a)
D=[]
for s in range(N):
    d=[99]*N;d[s]=0;front=[s]
    for u in front:
        for v in adj[u]:
            if d[v]>d[u]+1:d[v]=d[u]+1;front.append(v)
    D.append(d)

# Independent derivation: a strong resolving set meets every mutually maximally
# distant pair. Compute the graph by the definition, without reading any certificate.
far={(u,v) for u in range(N) for v in range(u+1,N) if
    all(D[x][v]<=D[u][v] for x in adj[u]) and
    all(D[y][u]<=D[u][v] for y in adj[v])}
assert len(far)==60

# Exhaustive independent-set enumeration within each bipartition of GP(12,5).
parts=[tuple(x for x in range(N) if (x%12)%2==(0 if x<12 else 1)),
       tuple(x for x in range(N) if (x%12)%2==(1 if x<12 else 0))]
assert len(parts[0])==len(parts[1])==12
sets=[]
for P in parts:
    groups=[]
    for mask in range(1<<12):
        chosen=tuple(P[j] for j in range(12) if mask>>j&1)
        if all((min(a,b),max(a,b))not in far for a,b in itertools.combinations(chosen,2)):
            groups.append(chosen)
    count=collections.Counter(map(len,groups))
    assert count=={0:1,1:12,2:36,3:24}, count
    sets.append([s for s in groups if len(s)==3])
    assert len(sets[-1])==24
allv=set(range(N))
bases=[tuple(sorted(allv-set(a)-set(b))) for a in sets[0]for b in sets[1]]
assert len(bases)==576 and len(set(bases))==576

# Verify every one of the 576 bases directly from shortest-path definition.
for S in bases:
    assert len(S)==18
    for u in range(N):
        for v in range(u+1,N):
            assert any(D[s][u]==D[s][v]+D[v][u] or D[s][v]==D[s][u]+D[u][v] for s in S)
# Conversely any strong resolver meets all 60 far pairs, hence at least 9 vertices
# of each component: maximum independent size in each 12-vertex SR component = 3.

A=[set() for _ in bases]
for i,S in enumerate(bases):
    si=set(S)
    for j in range(i+1,len(bases)):
        if len(si.difference(bases[j]))==1:
            A[i].add(j);A[j].add(i)
assert len(bases)==576 and all(len(v)==6 for v in A)
assert sum(len(x)for x in A)//2==1728
profile=(1,6,21,54,100,138,141,90,25)
for start in range(len(bases)):
    d=[-1]*len(bases);d[start]=0;Q=collections.deque([start])
    while Q:
        u=Q.popleft()
        for v in A[u]:
            if d[v]<0:d[v]=d[u]+1;Q.append(v)
    hist=tuple(collections.Counter(d)[k] for k in range(9))
    assert hist==profile, (start,hist)

with open('bases_certificate.json','w',encoding='utf8')as f:
    json.dump({'basis_masks':[hex(sum(1<<i for i in B))for B in bases],
               'exchange_edges':[[i,j]for i in range(len(bases))for j in sorted(A[i])if i<j],
               'distance_profile':profile},f,sort_keys=True,separators=(',',':'));f.write('\n')
print('DIRECT_STRONG_OK: all 576 size-18 sets resolve every vertex pair; 17 impossible.')
print('EXCHANGE_OK: 576 vertices, 1728 edges, connected six-regular, radius=diameter=8.')
print('DISTANCE_OK:',profile)
print('BASES_CERT_SHA256:',hashlib.sha256(open('bases_certificate.json','rb').read()).hexdigest())
