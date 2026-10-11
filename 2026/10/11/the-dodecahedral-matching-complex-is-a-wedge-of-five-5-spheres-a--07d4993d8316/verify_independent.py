#!/usr/bin/env python3
"""Independent matching-polynomial recurrence and simplicial F2 homology."""
from functools import lru_cache
from collections import defaultdict

def main():
    n=20
    graph=[0]*n
    def edge(x,y):
        assert x!=y
        graph[x]|=1<<y;graph[y]|=1<<x
    for i in range(10):
        edge(i,(i+1)%10)
        edge(i,10+i)
        edge(10+i,10+(i+2)%10)
    assert all(a.bit_count()==3 for a in graph)
    @lru_cache(maxsize=None)
    def poly(vertices):
        if not vertices:return (1,)
        bit=vertices&-vertices;v=bit.bit_length()-1
        base=vertices^bit
        ans=list(poly(base))
        neighbors=graph[v]&base
        while neighbors:
            b=neighbors&-neighbors;neighbors^=b
            p=poly(base^b)
            if len(ans)<len(p)+1:ans.extend([0]*(len(p)+1-len(ans)))
            for j,x in enumerate(p):ans[j+1]+=x
        return tuple(ans)
    values=poly((1<<n)-1)
    target=(1,30,375,2540,10155,24474,34805,27300,10260,1400,36)
    assert values==target
    print('COUNT_OK',values,'recurrence_states',poly.cache_info().currsize,flush=True)
    # Construct the line graph independently from original adjacency: its vertices are graph edges.
    edges=[]
    for u in range(n):
        for v in range(u+1,n):
            if graph[u] & (1<<v):edges.append((u,v))
    assert len(edges)==30
    conflict=[sum((1<<j) for j,(a,b) in enumerate(edges) if u in (a,b) or v in (a,b)) for u,v in edges]
    sizefaces=[[0]]+[[] for _ in range(10)]
    for vertex in range(30):
        bit=1<<vertex
        for j in range(9,-1,-1):
            sizefaces[j+1].extend([f|bit for f in sizefaces[j] if not f&conflict[vertex]])
    assert tuple(len(a) for a in sizefaces)==target
    print('enumeration_independent_OK',flush=True)
    ranks=[]
    for j in range(1,11):
        if not sizefaces[j]:continue
        rows={s:i for i,s in enumerate(sizefaces[j-1])}
        pivot={}
        for c in sizefaces[j]:
            v=0;x=c
            while x:
                b=x&-x;x^=b
                v^=1<<rows[c^b]
            while v:
                k=v.bit_length()-1
                p=pivot.get(k)
                if p is None:
                    pivot[k]=v;break
                v^=p
        ranks.append(len(pivot))
        print('rank_boundary_from_size',j,'=',len(pivot),'rows',len(rows),'cols',len(sizefaces[j]),flush=True)
    # Includes augmentation from 0-faces to empty face: rank=1.
    assert tuple(ranks)==(1,29,346,2194,7961,16513,18287,8896,1364,36),tuple(ranks)
    # Reduced homology dimensions: dim k has chain size k+1
    betti={k:len(sizefaces[k+1])-ranks[k]-ranks[k+1] for k in range(9)}
    assert betti=={0:0,1:0,2:0,3:0,4:0,5:5,6:117,7:0,8:0}
    print('HOMOLOGY_F2_OK',betti)
if __name__=='__main__':main()
