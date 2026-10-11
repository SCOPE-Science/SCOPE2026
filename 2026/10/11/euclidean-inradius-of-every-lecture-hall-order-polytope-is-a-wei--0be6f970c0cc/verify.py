#!/usr/bin/env python3
import math

def topo_order(n, covers):
    indeg=[0]*n
    out=[[] for _ in range(n)]
    for u,v in covers:
        out[u].append(v); indeg[v]+=1
    q=[i for i in range(n) if indeg[i]==0]
    order=[]
    while q:
        u=q.pop(0); order.append(u)
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    assert len(order)==n
    return order,out

def analyze(n,s,covers):
    order,out=topo_order(n,covers)
    ins=[[] for _ in range(n)]
    for u,v in covers: ins[v].append(u)
    mins=[i for i in range(n) if not ins[i]]
    maxs=[i for i in range(n) if not out[i]]
    def w(u,v):
        return math.sqrt(1/s[u]**2+1/s[v]**2)

    dm=[-1e100]*n
    for i in mins: dm[i]=1/s[i]
    for u in order:
        for v in out[u]:
            dm[v]=max(dm[v],dm[u]+w(u,v))
    L=max(dm[i]+1/s[i] for i in maxs)

    dp=[-1e100]*n
    for i in maxs: dp[i]=1/s[i]
    for u in reversed(order):
        for v in out[u]:
            dp[u]=max(dp[u],w(u,v)+dp[v])
    assert abs(max(1/s[i]+dp[i] for i in mins)-L)<1e-12

    # Enumerate all augmented maximal chains.
    lengths=[]
    def rec(u,acc):
        if not out[u]:
            lengths.append(acc+1/s[u]); return
        for v in out[u]:
            rec(v,acc+w(u,v))
    for i in mins: rec(i,1/s[i])
    assert abs(max(lengths)-L)<1e-12

    r=1/L
    ym=[r*x for x in dm]
    yp=[1-r*x for x in dp]

    def check(y):
        for i in mins: assert y[i]+1e-12 >= r/s[i]
        for i in maxs: assert 1-y[i]+1e-12 >= r/s[i]
        for u,v in covers: assert y[v]-y[u]+1e-12 >= r*w(u,v)
    check(ym); check(yp)

    unique=all(abs(dm[i]+dp[i]-L)<1e-11 for i in range(n))
    if unique:
        assert max(abs(ym[i]-yp[i]) for i in range(n))<1e-10
    else:
        assert any(abs(ym[i]-yp[i])>1e-9 for i in range(n))
    return L,r,unique,dm,dp,lengths

cases=[
    (4,[1,2,3,4],[(0,1),(1,2),(2,3)]),
    (3,[2,5,3],[(0,2),(1,2)]),
    (4,[1,4,2,7],[(0,1),(0,2),(1,3),(2,3)]),
    (5,[2,3,5,7,11],[(0,1),(1,2),(3,4)]),
    (5,[5,1,4,2,3],[(0,2),(1,2),(2,3),(2,4)]),
]
rows=[analyze(*c) for c in cases]

# Equal weights recover the ordinary order-polytope height formula.
n=5; s=[1]*n; covers=[(0,1),(1,2),(2,3),(3,4)]
L,r,unique,*_=analyze(n,s,covers)
assert abs(L-(2+4*math.sqrt(2)))<1e-12
assert abs(r-1/(2+4*math.sqrt(2)))<1e-12

# The first case is a chain, so its radius equals the closed chain formula.
s=cases[0][1]
chain_L=1/s[0]+sum(math.sqrt(1/s[i]**2+1/s[i+1]**2) for i in range(len(s)-1))+1/s[-1]
assert abs(rows[0][0]-chain_L)<1e-12
assert rows[0][2]

assert any(not row[2] for row in rows)
print("VERIFY_OK lecture-hall-order-inradius cases=%d maximal_paths=%d" %
      (len(rows)+1, sum(len(row[-1]) for row in rows)+1))
