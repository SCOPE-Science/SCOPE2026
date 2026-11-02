#!/usr/bin/env python3
"""Check exact two-extension witness spectra of orthogonal-array graphs.
All mathematical input is explicitly constructed here; no external packages.
"""
from collections import defaultdict

FIELDS={3:(3,[0,1]),4:(2,[1,1,1]),5:(5,[0,1]),7:(7,[0,1]),8:(2,[1,1,0,1]),9:(3,[1,0,1]),11:(11,[0,1])}

def field(n):
    p,poly=FIELDS[n]; deg=len(poly)-1
    assert p**deg==n and poly[-1]==1
    def digits(x):
        a=[]
        for _ in range(deg):a.append(x%p);x//=p
        return a
    def number(a): return sum(v*(p**i) for i,v in enumerate(a))
    def add(x,y):return number([(a+b)%p for a,b in zip(digits(x),digits(y))])
    def mul(x,y):
        a,b=digits(x),digits(y); c=[0]*(2*deg-1)
        for i in range(deg):
            for j in range(deg):c[i+j]=(c[i+j]+a[i]*b[j])%p
        for z in range(2*deg-2,deg-1,-1):
            w=c[z]
            for i in range(deg):c[z-deg+i]=(c[z-deg+i]-w*poly[i])%p
        return number(c[:deg])
    assert all(len({mul(a,b) for b in range(1,n)})==n-1 for a in range(1,n))
    return add,mul

def params(n,t):
    k=t*(n-1)
    la=n-2+(t-1)*(t-2)
    mu=t*(t-1)
    return {
        'adj11':la,'adj10':k-la-1,'adj01':k-la-1,
        'adj00':n*n-2*k+la,
        'non11':mu,'non10':k-mu,'non01':k-mu,
        'non00':n*n-2-2*k+mu}

def graph(n,t):
    add,mul=field(n)
    points=[(x,y) for x in range(n) for y in range(n)]
    coord=[]
    for x,y in points:
        full=[x,y]+[add(x,mul(s,y)) for s in range(1,n)]
        coord.append(full[:t])
    assert len(coord[0])==t and len(set(tuple(x) for x in coord))==n*n
    for i in range(t):
        for j in range(i):assert len(set((c[i],c[j]) for c in coord))==n*n
    adj=[]
    for u,a in enumerate(coord):
        adj.append(sum(1<<v for v,b in enumerate(coord) if v!=u and any(a[z]==b[z] for z in range(t))))
    return adj

def measured(n,t):
    adj=graph(n,t); v=n*n; allmask=(1<<v)-1
    expected=params(n,t)
    minima=[]; sample=None; minval=10**10
    for u in range(v):
        for w in range(u+1,v):
            m=allmask^(1<<u)^(1<<w)
            x=adj[u]&m;y=adj[w]&m
            c={ '11':(x&y).bit_count(), '10':(x&~y).bit_count(),
                '01':(~x&y&m).bit_count(), '00':(~x&~y&m).bit_count()}
            prefix='adj' if ((adj[u]>>w)&1) else 'non'
            for label,z in c.items():
                assert z==expected[prefix+label],(n,t,u,w,prefix,label,z,expected)
                if z<minval:sample=(u,w,prefix,label,z);minval=z
    assert all(z>0 for z in expected.values())
    assert minval==min(expected.values())
    return adj,sample,minval

def check_radius(adj,sample,minval):
    v=len(adj); full=(1<<v)-1
    u,w,prefix,label,count=sample
    pattern=int(label[0]),int(label[1])
    ws=[z for z in range(v) if z not in (u,w) and ((adj[u]>>z)&1)==pattern[0] and ((adj[w]>>z)&1)==pattern[1]]
    assert len(ws)==count==minval
    deleted=set(ws)
    assert u not in deleted and w not in deleted
    residual=[z for z in range(v) if z not in deleted]
    assert not any(((adj[u]>>z)&1)==pattern[0] and ((adj[w]>>z)&1)==pattern[1] for z in residual if z not in (u,w))
    return tuple(ws[:10])

def optimum(n):
    h=n//2
    if n%2==0:return h*(h-1),[h,h+1]
    return h*(h+1)-1,[h+1]

if __name__=='__main__':
    for n in FIELDS:
        outs=[]
        for t in range(2,n):
            adj,sample,m=measured(n,t)
            deleted=check_radius(adj,sample,m)
            outs.append((t,m))
        best=max(m for t,m in outs)
        maximizers=[t for t,m in outs if m==best]
        assert (best,maximizers)==optimum(n),(n,best,maximizers,optimum(n))
        print(f'n={n} min_witness_by_t={outs}; max={best} achieved_at={maximizers}; all_pairs_and_sharp_deletions=PASS')
    for n in range(3,300):
        vals=[(t,min(params(n,t).values())) for t in range(2,n)]
        best=max(m for _,m in vals)
        assert (best,[t for t,m in vals if m==best])==optimum(n),(n,best,vals)
    print('symbolic-parameter optimization checked n=3..299: PASS')
    print('RESULT PASS')
