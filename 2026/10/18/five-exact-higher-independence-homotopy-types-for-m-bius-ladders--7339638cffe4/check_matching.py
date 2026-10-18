#!/usr/bin/env python3
"""Reconstruct five finite two-independence complexes and certify acyclic matchings."""
from collections import Counter, defaultdict, deque

ORDERS = {
 4: [7,2,3,6,4,0,5,1],
 5: [6,0,4,8,2,5,1,7,9,3],
 6: [7,8,3,1,4,10,6,11,2,9,0,5],
 7: [0,2,10,12,8,4,1,11,5,3,6,13,7,9],
 8: [10,3,5,2,4,15,11,12,0,1,6,7,14,9,13,8],
}
EXPECTED = {4:(2,1), 5:(3,9), 6:(3,6), 7:(4,1), 8:(5,31)}

def faces(n):
    N=2*n
    edges={tuple(sorted((i,(i+1)%N))) for i in range(N)}
    edges.update((i,i+n) for i in range(n))
    adj=[0]*N
    for a,b in edges:
        adj[a]|=1<<b;adj[b]|=1<<a
    ans={}
    for face in range(1,1<<N):
        good=True
        for v in range(N):
            if face & (1<<v) and (adj[v]&face).bit_count()>=2:
                good=False
                break
        if good: ans[face]=face.bit_count()-1
    return ans

def matching(faces,order):
    left=set(faces)
    pairs=[]
    for v in order:
        toggle=1<<v
        changes=[]
        for f in sorted(left):
            if f&toggle==0 and f|toggle in left:
                changes.append((f,f|toggle))
        flat=[x for pair in changes for x in pair]
        assert len(set(flat))==len(flat)
        assert set(flat)<=left
        left.difference_update(flat)
        pairs.extend(changes)
    return pairs,left

def directed_poset_dag(faces,pairs):
    vertex_set=set(faces)
    ascending=set(pairs)
    deg={f:0 for f in vertex_set}
    adj=defaultdict(list)
    cover_count=0
    for high in sorted(vertex_set):
        x=high
        while x:
            b=x&-x; x-=b
            low=high^b
            if low not in vertex_set:continue
            cover_count+=1
            if (low,high) in ascending:src,dst=low,high
            else:src,dst=high,low
            adj[src].append(dst)
            deg[dst]+=1
    queue=deque(x for x in vertex_set if deg[x]==0)
    visited=0
    while queue:
        u=queue.popleft();visited+=1
        for v in adj[u]:
            deg[v]-=1
            if deg[v]==0:queue.append(v)
    assert visited==len(vertex_set), 'directed-cycle detected'
    return cover_count,visited

def main():
    for n,order in ORDERS.items():
        fc=faces(n)
        pairs,crit=matching(fc,order)
        graph_covers,visited=directed_poset_dag(fc,pairs)
        signature=Counter(fc[x] for x in crit)
        d,b=EXPECTED[n]
        assert signature=={0:1,d:b},(n,signature)
        assert len(fc)==2*len(pairs)+len(crit)
        fvec=[sum(dim==k for dim in fc.values()) for k in range(max(fc.values())+1)]
        print(f'n={n} vertices={2*n} f_vector={fvec} nonempty_faces={len(fc)} matched_pairs={len(pairs)} hasse_covers={graph_covers} dag_visited={visited} critical={dict(sorted(signature.items()))}')
    print('ALL_ACYCLIC_MATCHING_CERTIFICATES_PASSED')
if __name__=='__main__':main()
