#!/usr/bin/env python3

def barbell(m,k):
    n=2*m+k
    adj=[[] for _ in range(n)]
    for off in (0,m+k):
        for i in range(off,off+m):
            for j in range(i+1,off+m):
                adj[i].append(j); adj[j].append(i)
    lc,rc=m-1,m+k
    if k==0:
        adj[lc].append(rc); adj[rc].append(lc)
    else:
        adj[lc].append(m); adj[m].append(lc)
        for v in range(m,m+k-1):
            adj[v].append(v+1); adj[v+1].append(v)
        adj[m+k-1].append(rc); adj[rc].append(m+k-1)
    return adj

def stable_depth(adj):
    colors=[0]*len(adj)
    for r in range(len(adj)+3):
        sig=[(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in range(len(adj))]
        names={}
        new=[names.setdefault(s,len(names)) for s in sig]
        # Refinement never merges classes, so equal class counts means equal partitions.
        if len(set(new))==len(set(colors)):
            return r, colors
        colors=new
    raise RuntimeError('no stabilization')

def formula(m,k):
    if m>=4:
        return max(1,(k+1)//2)
    if k==0: return 1
    if k==1: return 2
    if k==2: return 1
    return max(3,(k+1)//2)

dc=0
for m in range(3,21):
    for k in range(0,81):
        s,_=stable_depth(barbell(m,k))
        e=formula(m,k)
        assert s==e,(m,k,s,e)
        dc+=1

# Exceptional B(3,2): at stabilization, six degree-2 vertices share one color.
adj=barbell(3,2)
s,colors=stable_depth(adj)
assert s==1
assert len({colors[v] for v in (0,1,3,4,6,7)})==1
assert colors[2]==colors[5] and colors[2]!=colors[0]
print(f'VERIFY_OK depth_checks={dc} anomaly_checks=1 m=3..20 k=0..80')
