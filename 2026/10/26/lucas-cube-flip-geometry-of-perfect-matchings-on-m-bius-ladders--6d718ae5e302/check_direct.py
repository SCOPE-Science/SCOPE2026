"""Brute-force vertex-first perfect matching and canonical face flip census."""

def edge(a,b): return tuple(sorted((a,b)))

def graph(n):
    assert n >= 4
    e = {edge(i,i+n) for i in range(n)}
    e.update(edge(i,i+1) for i in range(n-1))
    e.update(edge(i+n,i+n+1) for i in range(n-1))
    e.update([edge(n-1,n),edge(2*n-1,0)])
    square=[]
    for i in range(n):
        j=(i+1)%n
        if j:
            horizontal={edge(i,j),edge(i+n,j+n)}
        else:
            horizontal={edge(n-1,n),edge(2*n-1,0)}
        rung={edge(i,i+n),edge(j,j+n)}
        square.append((frozenset(rung),frozenset(horizontal)))
    return e,square

def perfect_matchings(n):
    e,faces=graph(n)
    adj=[[] for _ in range(2*n)]
    for a,b in e:
        adj[a].append(b)
        adj[b].append(a)
    def dfs(free,chosen):
        if not free:
            yield frozenset(chosen)
            return
        v=min(free)
        for w in adj[v]:
            if w in free:
                yield from dfs(free-{v,w}, chosen+[edge(v,w)])
    return list(dfs(set(range(2*n)),[])),faces

def lucas(n):
    out=[]
    for b in range(1<<n):
        if any((b>>i)&(b>>((i+1)%n))&1 for i in range(n)):
            continue
        out.append(b)
    return out

def exercise(n):
    matches,faces=perfect_matchings(n)
    sidx={m:i for i,m in enumerate(matches)}
    assert len(sidx)==len(matches)
    graphs=[set() for _ in matches]
    for i,m in enumerate(matches):
        for r,h in faces:
            if r <= m: other=(m-r)|h
            elif h <= m: other=(m-h)|r
            else: continue
            assert other in sidx
            graphs[i].add(sidx[other])
    assert all(i in graphs[j] for i,G in enumerate(graphs) for j in G)
    edges=sum(map(len,graphs))//2
    sizes=[]; seen=set()
    for i in range(len(matches)):
        if i in seen: continue
        queue=[i]; seen.add(i)
        for k in queue:
            for l in graphs[k]:
                if l not in seen:seen.add(l);queue.append(l)
        sizes.append(len(queue))
    sizes.sort(reverse=True)
    L=lucas(n)
    assert len(matches)==len(L)+(2 if n%2 else 0)
    assert sizes==[len(L)]+([1,1] if n%2 else [])
    assert edges==n*fib(n-1)
    return len(matches),edges,sizes

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

if __name__=='__main__':
    for n in range(4,17):
        v,e,components=exercise(n)
        print(f'n={n:02d} perfect_matchings={v} switches={e} component_sizes={components}')
    print('PASS: all brute-force matchings, square switches, and components agree for n=4..16')
