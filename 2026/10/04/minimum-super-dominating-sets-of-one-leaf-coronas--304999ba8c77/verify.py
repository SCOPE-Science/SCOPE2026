from itertools import combinations

def components(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    seen=set(); comps=[]
    for s in range(n):
        if s in seen: continue
        stack=[s]; seen.add(s); comp=[]
        while stack:
            u=stack.pop(); comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); stack.append(v)
        comps.append(set(comp))
    return comps,adj

def corona_k1(n, edges):
    # supports 0..n-1, leaves n..2n-1; leaf n+i adjacent only to i
    N=2*n
    adj=[set() for _ in range(N)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    for i in range(n):
        adj[i].add(n+i); adj[n+i].add(i)
    return adj

def is_super_dom(adj,mask):
    N=len(adj)
    outside=[u for u in range(N) if not ((mask>>u)&1)]
    outset=set(outside)
    for u in outside:
        ok=False
        for v in adj[u]:
            if ((mask>>v)&1) and (adj[v] & outset)=={u}:
                ok=True; break
        if not ok: return False
    return True

def predicted_min_sets(n, comps):
    out=set()
    for cmask in range(1<<len(comps)):
        X=set()
        for j,C in enumerate(comps):
            if (cmask>>j)&1: X |= C
        m=0
        for i in range(n):
            # support outside iff component selected into X, so leaf selected
            if i in X: m |= 1<<(n+i)
            else: m |= 1<<i
        out.add(m)
    return out

graphs=subsets=minsets=0
for n in range(1,6):
    pairs=list(combinations(range(n),2))
    for emask in range(1<<len(pairs)):
        edges=[pairs[j] for j in range(len(pairs)) if (emask>>j)&1]
        comps,_=components(n,edges)
        adj=corona_k1(n,edges)
        N=2*n
        # minimum cannot be below n; verify all subsets of size <=n explicitly.
        actual=set()
        for k in range(n+1):
            for S in combinations(range(N),k):
                subsets += 1
                mask=sum(1<<x for x in S)
                ok=is_super_dom(adj,mask)
                if k<n:
                    assert not ok,(n,edges,k,S)
                elif ok:
                    actual.add(mask)
        expected=predicted_min_sets(n,comps)
        assert actual==expected,(n,edges,len(comps),len(actual),len(expected))
        assert len(actual)==2**len(comps)
        minsets += len(actual)
        graphs += 1

print('VERIFY_OK')
print('base_graphs_checked =',graphs)
print('vertex_subsets_checked =',subsets)
print('minimum_super_dominating_sets_checked =',minsets)
print('all labeled simple base graphs on n = 1..5')
print('all corona minima have size n')
print('all minimum sets correspond exactly to unions of base components')
print('all minimum-set counts equal 2^c(H)')
