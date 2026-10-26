"""Exact finite-tree verification of branch geometry and eventual diameter excess.

The finite tests do not prove the almost-sure or infinite-tail assertions.
Run with Python 3.10+: python verify_diameter.py
"""
from itertools import product
from collections import deque


def diameter(adj):
    def farthest(start):
        dist=[-1]*len(adj); dist[start]=0
        queue=deque([start]); end=start
        while queue:
            u=queue.popleft()
            if dist[u]>dist[end]: end=u
            for v in adj[u]:
                if dist[v]<0:
                    dist[v]=dist[u]+1;queue.append(v)
        return end,dist[end]
    u,_=farthest(0)
    _,d=farthest(u)
    return d


def inspect(prefix):
    # The infinite attachment sequence is the given finite prefix followed
    # by "last vertex" attachments forever.  A finite 12-step continuation
    # is sufficient to locate the infinite ray and compute its finite bushes.
    nbits=len(prefix)
    choices=list(prefix)+[1]*12
    N=len(choices)+1
    parent=[-1,0]
    adjacency=[[1],[0]]
    height=[0,1]
    for i,bit in enumerate(choices,start=2):
        par=i-1 if bit else i-2
        parent.append(par)
        height.append(height[par]+1)
        adjacency.append([par])
        adjacency[par].append(i)
    ray=[]
    node=N
    while node>=0:
        ray.append(node)
        node=parent[node]
    ray=list(reversed(ray))
    ray_index={v:i for i,v in enumerate(ray)}
    excess=0
    for idx,spine_vertex in enumerate(ray):
        # One child is next ray vertex, any other child is a finite chain.
        children=[v for v in adjacency[spine_vertex] if v>spine_vertex]
        next_vertex=ray[idx+1] if idx+1<len(ray) else None
        side_children=[v for v in children if v!=next_vertex]
        assert len(side_children)<=1
        length=0
        if side_children:
            v=side_children[0]; length=1
            while True:
                below=[w for w in adjacency[v] if w>v]
                assert len(below)<=1
                if not below:break
                v=below[0];length+=1
        # Consecutive second-last choices immediately after this ray site.
        # b_0 is a deterministic first choice.
        b=(1 if spine_vertex==0 or spine_vertex>len(choices) else choices[spine_vertex-1])
        if b==0:
            predicted=0
        else:
            run=0
            for t in range(spine_vertex+1,len(choices)+1):
                if choices[t-1]: break
                run+=1
            predicted=(run+1)//2
        # Past the tested random prefix the continuation is all 1.
        assert length==predicted,(prefix,spine_vertex,length,predicted)
        excess=max(excess,length-idx)
    D=diameter(adjacency)
    H=max(height)
    assert H==height[-1]
    assert D-H==excess,(prefix,D,H,excess)
    return excess


def main():
    tested=0; positive=0; max_excess=0
    for n in range(0,12):
        for bits in product((0,1),repeat=n):
            gap=inspect(bits)
            max_excess=max(max_excess,gap)
            positive+=gap>0
            tested+=1
    assert tested==4095
    print(f'PASS: {tested} exhaustive eventual-tail finite trees, '
          f'{positive} with positive excess; largest excess {max_excess}')


if __name__=='__main__':main()
