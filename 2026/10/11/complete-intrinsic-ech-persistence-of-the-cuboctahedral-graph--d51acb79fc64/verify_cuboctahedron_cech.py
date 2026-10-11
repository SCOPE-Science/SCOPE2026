#!/usr/bin/env python3
"""Reproduce intrinsic graph Cech filtration of the cuboctahedron (line graph of 3-cube)."""
import collections,itertools,random

def graph():
    cube_edges=sorted((u, u^(1<<j)) for u in range(8) for j in range(3) if not ((u>>j)&1))
    assert len(cube_edges)==12 and len(set(cube_edges))==12
    adj=[0]*12
    for i,e in enumerate(cube_edges):
        for j,f in enumerate(cube_edges):
            if i!=j and (e[0] in f or e[1] in f):
                adj[i]|=1<<j
    assert all(x.bit_count()==4 for x in adj)
    assert sum(x.bit_count() for x in adj)==48
    ds=[]
    for v in range(12):
        d=[-1]*12;d[v]=0; queue=[v]
        for x in queue:
            for y in range(12):
                if adj[x]>>y&1 and d[y]<0: d[y]=d[x]+1;queue.append(y)
        ds.append(d)
    assert all(sorted(collections.Counter(d).values())==[1,1,4,6] for d in ds)
    assert all(max(d)==3 for d in ds)
    assert all(sum(d[u]==3 for u in range(12))==1 for d in ds)
    assert all(ds[u][v]==ds[v][u] for u in range(12) for v in range(12))
    return cube_edges,adj,ds

def facets(r,adj,ds):
    assert 0<=r<=5
    k=r//2
    if r%2==0:
        return [sum(1<<u for u in range(12) if ds[v][u]<=k) for v in range(12)]
    return [sum(1<<u for u in range(12) if min(ds[v][u],ds[w][u])<=k)
            for v in range(12) for w in range(v+1,12) if adj[v]>>w&1]

def simplices(fac):
    cells=set()
    for f in fac:
        x=f
        while x:
            cells.add(x)
            x=(x-1)&f
    return cells

def matching(S,order):
    remain=set(S); pairs=[]
    for v in order:
        bit=1<<v
        for s in sorted(remain):
            if not s&bit and s|bit in remain:
                t=s|bit
                remain.remove(s);remain.remove(t)
                pairs.append((s,t))
    return pairs,remain

def check_gradient(S,pairs):
    # Downward face arrows reversed only on matched incidence. Other arrows point downward.
    ix={s:i for i,s in enumerate(sorted(S))}
    n=len(ix);succ=[[] for _ in range(n)]; indeg=[0]*n
    upper_to_lower={(t,s) for s,t in pairs}
    count=0
    for t in S:
        for j in range(12):
            if not (t>>j)&1 or t==(1<<j): continue
            s=t^(1<<j)
            assert s in ix
            if (t,s) in upper_to_lower:
                a,b=ix[s],ix[t]
            else:
                a,b=ix[t],ix[s]
            succ[a].append(b);indeg[b]+=1;count+=1
    q=collections.deque(v for v in range(n) if indeg[v]==0)
    reached=0
    while q:
        v=q.popleft();reached+=1
        for w in succ[v]:
            indeg[w]-=1
            if indeg[w]==0:q.append(w)
    assert reached==n,(reached,n)
    return count

def rank_two(S,k):
    faces=sorted(s for s in S if s.bit_count()==k)
    upper=sorted(s for s in S if s.bit_count()==k+1)
    row={v:i for i,v in enumerate(faces)}
    pivots={}
    for t in upper:
        col=0
        for j in range(12):
            if t>>j&1: col ^= 1<<row[t^(1<<j)]
        while col:
            p=col.bit_length()-1
            if p not in pivots:
                pivots[p]=col;break
            col ^= pivots[p]
    return len(pivots)

def compute(r,adj,ds,order=None):
    ff=facets(r,adj,ds);S=simplices(ff)
    counts={k:sum(x.bit_count()==k for x in S) for k in range(1,13)}
    counts={k:v for k,v in counts.items() if v}
    if order is None: return ff,S,counts,None
    pairs,crit=matching(S,order)
    assert 2*len(pairs)+len(crit)==len(S)
    hasse=check_gradient(S,pairs)
    cc=dict(sorted(collections.Counter(s.bit_count()-1 for s in crit).items()))
    return ff,S,counts,(pairs,crit,cc,hasse)

def verify():
    cube_edges, adj, ds=graph()
    assert cube_edges==[(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),
                        (2,6),(3,7),(4,5),(4,6),(5,7),(6,7)]
    orders={2:[7,6,1,11,5,4,0,10,9,8,3,2],
            3:[1,8,2,6,4,11,0,10,5,3,7,9]}
    expected_counts={
        0:{1:12},
        1:{1:12,2:24},
        2:{1:12,2:60,3:104,4:60,5:12},
        3:{1:12,2:66,3:212,4:354,5:300,6:132,7:24},
        4:{k: __import__("math").comb(12,k) for k in range(1,12)},
        5:{k: __import__("math").comb(12,k) for k in range(1,13)}
    }
    for r in range(6):
        ff,S,counts,m=compute(r,adj,ds,orders.get(r))
        assert counts==expected_counts[r],(r,counts)
        assert len(ff)==[12,24,12,24,12,24][r]
        assert [min(f.bit_count() for f in ff),max(f.bit_count() for f in ff)]==[
            [1,1],[2,2],[5,5],[7,7],[11,11],[12,12]][r]
        if r in orders:
            pairs,crit,cc,hasse=m
            assert len(pairs)=={2:120,3:547}[r]
            assert cc=={2:{0:1,2:7},3:{0:1,3:5}}[r]
            assert hasse=={2:732,3:4644}[r]
            ranks={k:rank_two(S,k) for k in range(1,max(counts))}
            assert ranks=={
                2:{1:11,2:49,3:48,4:12},
                3:{1:11,2:55,3:157,4:192,5:108,6:24}}[r]
            # In integral discrete Morse theory, a complex with one 0-cell
            # and only d-cells (d >= 2) is a wedge of d-spheres.
        if r==4:
            assert set(ff)=={((1<<12)-1)^(1<<v) for v in range(12)}
            assert S==set(range(1,(1<<12)-1))
        if r==5:
            assert all(f==(1<<12)-1 for f in ff)
            assert S==set(range(1,(1<<12)))
    print("VERIFY_OK", "scale_2: wedge_7_S2", "scale_3: wedge_5_S3", "scale_4: S10")

if __name__=='__main__':
    verify()
