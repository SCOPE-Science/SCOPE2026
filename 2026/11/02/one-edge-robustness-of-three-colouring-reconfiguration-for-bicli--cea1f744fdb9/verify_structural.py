"""Independent constructive check: hypercubes with six four-cycle ears.
Does not enumerate 3^(m+n) input colourings; constructs every state by pieces.
"""
from itertools import product
from collections import deque, Counter

def structural(m,n):
    cubes=[]
    for color in range(3):
        allowed=tuple(t for t in range(3) if t!=color)
        cubes.append([(color,)*m+v for v in product(allowed,repeat=n)])
    for color in range(3):
        allowed=tuple(t for t in range(3) if t!=color)
        cubes.append([v+(color,)*n for v in product(allowed,repeat=m)])
    verts=set().union(*map(set,cubes));adj={v:set() for v in verts}
    for cube in cubes:
        for a in cube:
            for b in cube:
                if sum(u!=v for u,v in zip(a,b))==1:
                    adj[a].add(b)
    old=set(verts)
    for shared in range(3):
        rest=tuple(t for t in range(3) if t!=shared)
        for left_color,right_color in [(rest[0],rest[1]),(rest[1],rest[0])]:
            ear=(shared,)+(left_color,)*(m-1)+(shared,)+(right_color,)*(n-1)
            u=(left_color,)*m+(shared,)+(right_color,)*(n-1)
            v=(shared,)+(left_color,)*(m-1)+(right_color,)*n
            assert ear not in verts and u in verts and v in verts
            verts.add(ear);adj[ear]={u,v};adj[u].add(ear);adj[v].add(ear)
    return verts,adj,old

def direct_neighbors(state,m,n):
    good=[]
    for i in range(m+n):
        for c in range(3):
            if c==state[i]:continue
            cand=state[:i]+(c,)+state[i+1:]
            if all(cand[a]!=cand[m+b] for a in range(m) for b in range(n) if (a,b)!=(0,0)):
                good.append(cand)
    return set(good)

def maxdist(adj,v):
    d={v:0};q=deque([v]);
    while q:
        x=q.popleft()
        for y in adj[x]:
            if y not in d:d[y]=d[x]+1;q.append(y)
    assert len(d)==len(adj)
    return max(d.values())

def main():
    for m,n in [(2,2),(2,3),(2,6),(3,3),(3,4),(4,4),(5,5)]:
        states,adj,old=structural(m,n)
        assert len(states)==3*(2**m+2**n)
        assert len(old)==3*(2**m+2**n)-6
        assert all(adj[s]==direct_neighbors(s,m,n) for s in states)
        degree=Counter(map(len,adj.values()))
        assert sum(degree.values())==len(states)
        assert all(maxdist(adj,s)==3*(m+n)//2 for s in states)
        print('STRUCTURAL_PASS',m,n,len(states),degree)
    print('STRUCTURAL_ALL_PASS')

if __name__=='__main__':main()
