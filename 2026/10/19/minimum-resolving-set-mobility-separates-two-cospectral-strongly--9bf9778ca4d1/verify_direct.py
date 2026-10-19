"""Exhaustive distance-signature verifier for two 16-vertex graphs.
Standard library only. Execute: python3 verify_direct.py.
"""
from itertools import combinations
from collections import Counter, deque

N = 16
XY = [(x,y) for x in range(4) for y in range(4)]
SH_STEPS = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}

def distances(kind):
    d = [[0]*N for _ in range(N)]
    for i,(x,y) in enumerate(XY):
        for j,(u,v) in enumerate(XY):
            if i == j: continue
            if kind=='rook':
                d[i][j] = 1 if x==u or y==v else 2
            else:
                d[i][j] = 1 if ((x-u)%4,(y-v)%4) in SH_STEPS else 2
    for i in range(N):
        assert sum(d[i][j]==1 for j in range(N))==6
        for j in range(N): assert d[i][j]==d[j][i]
    for i in range(N):
        for j in range(i+1,N):
            common=sum(d[i][w]==1 and d[j][w]==1 for w in range(N))
            assert common==2
    return d

def resolving(d,verts):
    return len({tuple(d[v][s] for s in verts) for v in range(N)}) == N

def bases_by_size(d,k):
    return {tuple(s) for s in combinations(range(N),k) if resolving(d,s)}

def components(adj):
    remain=set(range(len(adj)))
    comps=[]
    while remain:
        start=min(remain); remain.remove(start)
        found={start};queue=deque([start])
        while queue:
            x=queue.popleft()
            for y in adj[x]:
                if y not in found:
                    found.add(y);remain.remove(y);queue.append(y)
        comps.append(found)
    return comps

def reconfig(d,bases,local):
    seq=sorted(bases);lookup={s:i for i,s in enumerate(seq)}
    adj=[set() for _ in seq]
    for i,b in enumerate(seq):
        inside=set(b)
        for a in b:
            for z in range(N):
                if z in inside or (local and d[a][z]!=1):continue
                new=tuple(sorted((inside-{a})|{z}))
                j=lookup.get(new)
                if j is not None: adj[i].add(j)
    for i,nei in enumerate(adj):
        for j in nei:assert i in adj[j]
    return seq,adj

def main():
    for kind in ('rook','shrikhande'):
        d=distances(kind)
        smaller=[len(bases_by_size(d,k)) for k in range(1,4)]
        B=bases_by_size(d,4)
        print(kind, 'k1-k3', smaller, 'basis4',len(B))
        assert smaller==[0,0,0]
        assert len(B)==(144 if kind=='rook' else 48)
        full=None
        for local in (False,True):
            seq,adj=reconfig(d,B,local)
            comps=components(adj)
            edges=sum(map(len,adj))//2
            cs=Counter(map(len,comps))
            ds=Counter(map(len,adj))
            print('move',('slide' if local else 'jump'),'edges',edges,'components',dict(sorted(cs.items())),'degrees',dict(sorted(ds.items())))
            if kind=='rook':
                assert edges==288 and cs=={9:16} and ds=={4:144}
                for C in comps:
                    assert len(C)==9
                    assert sum(len(adj[x]&C) for x in C)==36
                    # Check that every non-neighbor lies at distance exactly 2.
                    for x in C:
                        within={x}|adj[x]|set().union(*(adj[y] for y in adj[x]))
                        assert within==C
            else:
                assert edges==0 and cs=={1:48} and ds=={0:48}
            e_set={(min(i,j),max(i,j)) for i in range(len(adj)) for j in adj[i]}
            if full is None:full=e_set
            else:assert e_set==full
        if kind=='rook':
            # Each component is the 3-by-3 rook graph, verified via its two parameters.
            seq,adj=reconfig(d,B,False)
            for C in components(adj):
                for i,j in combinations(sorted(C),2):
                    common=len(adj[i]&adj[j])
                    assert common==(1 if j in adj[i] else 2)
        # Exactly-two-landmark exchange graph: a 4-move add-add-remove-remove
        # sequence realizes each edge with a capacity of six sensors.
        seq=sorted(B)
        A2=[set() for _ in seq]
        for i in range(len(seq)):
            si=set(seq[i])
            for j in range(i+1,len(seq)):
                if len(si.intersection(seq[j]))==2:
                    A2[i].add(j);A2[j].add(i)
        c2=components(A2)
        assert len(c2)==1
        assert {len(a) for a in A2}==({26} if kind=='rook' else {10})
        ecc=[]
        for src in range(len(seq)):
            distance={src:0}; q=deque([src])
            while q:
                v=q.popleft()
                for w in A2[v]:
                    if w not in distance:
                        distance[w]=distance[v]+1; q.append(w)
            assert len(distance)==len(seq)
            ecc.append(max(distance.values()))
        assert set(ecc)=={3}
        print('two-exchange edges',sum(map(len,A2))//2, 'connected',True,'diameter',max(ecc))
        print('CHECK_OK',kind)
    print('VERIFY_OK')
if __name__=='__main__':main()
