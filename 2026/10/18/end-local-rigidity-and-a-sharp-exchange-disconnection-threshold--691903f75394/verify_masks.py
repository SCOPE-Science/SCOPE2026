#!/usr/bin/env python3
"""Independent bit-mask verifier for ordinary zero forcing and token jumps."""
from itertools import combinations

def model(n):
    # Vertex labels: three row blocks of n, unlike column-major checker.
    adj=[0]*(3*n)
    for r in range(3):
        for c in range(n):
            v=r*n+c
            for s,d in ((r-1,c),(r+1,c),(r,c-1),(r,c+1)):
                if 0<=s<3 and 0<=d<n:adj[v]|=1<<(s*n+d)
    return adj

def force(mask, adj):
    goal=(1<<len(adj))-1
    while True:
        future=0
        v=mask
        while v:
            bit=v&-v;v-=bit;i=bit.bit_length()-1
            unseen=adj[i]&(~mask)&goal
            if unseen and (unseen&(unseen-1))==0:future|=unseen
        future &= ~mask
        if not future: return mask==goal
        mask|=future

def all_bases(n):
    adj=model(n)
    out=set()
    for triple in combinations(range(3*n),3):
        mask=sum(1<<v for v in triple)
        if force(mask,adj):out.add(mask)
    return out

def exchange_graph(bases, n):
    bases=list(bases); table={m:i for i,m in enumerate(bases)}
    links=[set() for _ in bases]
    for i,m in enumerate(bases):
        for j in range(3*n):
            if not (m>>j&1):continue
            for k in range(3*n):
                if m>>k&1:continue
                z=m^(1<<j)^(1<<k)
                if z in table: links[i].add(table[z])
    assert all(i in links[j] for i,L in enumerate(links) for j in L)
    components=[];seen=set()
    for u in range(len(bases)):
        if u in seen:continue
        reach={u}; stack=[u];seen.add(u)
        while stack:
            v=stack.pop()
            for w in links[v]:
                if w not in seen:seen.add(w);reach.add(w);stack.append(w)
        components.append(reach)
    lengths=[]
    for part in components:
        distances=[]
        for src in part:
            q=[src]; dis={src:0}
            for v in q:
                for w in links[v]:
                    if w not in dis:dis[w]=dis[v]+1;q.append(w)
            assert len(dis)==len(part)
            distances.append(max(dis.values()))
        lengths.append((max(distances),min(distances)))
    return sum(map(len,links))//2,sorted(map(len,components)),sorted(lengths)

for n in range(3,11):
    adj=model(n)
    for k in [1,2]:
        assert not any(force(sum(1<<v for v in S),adj) for S in combinations(range(3*n),k)),('lower bound',n,k)
    bases=all_bases(n)
    e,components,ext=exchange_graph(bases,n)
    if n==3: expected=(20,44,[20],[(4,3)])
    elif n==4:expected=(26,56,[26],[(6,4)])
    else:expected=(26,48,[13,13],[(5,3),(5,3)])
    assert (len(bases),e,components,ext)==expected,(n,len(bases),e,components,ext)
    if n>=5:
        # Any successful triple is supported entirely in one end 3-column strip.
        for s in bases:
            cols={j%n for j in range(3*n) if (s>>j)&1}
            assert max(cols)<=2 or min(cols)>=n-3
    print(f'n={n} zero_forcing_number=3 bases={len(bases)} edges={e} comp={components} (dia,rad)={ext}')
print('VERIFY_OK')
