"""Independent geometric bracelet-graph construction and metric checks.
Run: python verify_two_token.py
"""
from collections import deque
from math import floor

def pair_verts(n):
    h=(n+2)//3
    return [(a,b) for a in range(n) for b in range(a+1,n) if h<=b-a<=n-h]

def neighbors(v,n,verts):
    a,b=v
    for which in range(2):
        for delta in (-1,1):
            q=[a,b]; q[which]=(q[which]+delta)%n
            w=tuple(sorted(q))
            if w in verts and w != v: yield w

def test(n):
    k=(n-1)//3;h=k+1;v=pair_verts(n)
    assert len(v)==n*k//2,(n,len(v),k)
    allowed=set(v)
    adj={u:set(neighbors(u,n,allowed)) for u in v}
    assert all(u in adj[w] for u in v for w in adj[u])
    assert all(len(ns) in (2,4) for ns in adj.values())
    def circ(x,y):
        d=(x-y)%n;return min(d,n-d)
    def lb(p,q):
        a,b=p;c,d=q
        return min(circ(a,c)+circ(b,d),circ(a,d)+circ(b,c))
    # Certified constructive eccentricity witness for every source.
    q=n//2
    for a,b in v:
        d=(b-a)%n
        x=q//2; y=q-x
        if q%2==1 and d==n-h:
            x=(q+1)//2; y=q-x
        target=tuple(sorted(((a+x)%n,(a+d+y)%n)))
        assert target in allowed,(n,(a,b),target,x,y)
        assert lb((a,b),target)==q,(n,(a,b),target,lb((a,b),target),q)
    for u in v:
        dist={u:0};todo=deque([u])
        while todo:
            w=todo.popleft()
            for x in adj[w]:
                if x not in dist:dist[x]=dist[w]+1;todo.append(x)
        assert len(dist)==len(v),(n,len(dist),len(v))
        assert max(dist.values())==n//2,(n,u,max(dist.values()))
        if n<=25:
            for w,length in dist.items():assert length==lb(u,w),(n,u,w,length,lb(u,w))
    return len(v),sum(map(len,adj.values()))//2, n//2
for k in range(2,21):
    n=3*k+1
    print(n,test(n))
print('TWO_TOKEN_ALL_ECCENTRICITIES_PASS')
