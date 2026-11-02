"""Direct certificate for the 4,8 general-position coloring on a three-arm spider."""
from itertools import combinations,product
from collections import Counter

def graph(L=4,r=3):
    n=1+r*L
    adj=[[] for _ in range(n)]
    for a in range(r):
        for t in range(1,L+1):
            u=1+a*L+t-1
            v=0 if t==1 else u-1
            adj[u].append(v);adj[v].append(u)
    return adj

def path(adj,s,t):
    parent={s:None}; todo=[s]
    for x in todo:
        if x==t: break
        for y in adj[x]:
            if y not in parent: parent[y]=x;todo.append(y)
    p=[];y=t
    while y is not None:p.append(y);y=parent[y]
    return tuple(p)

def data(L=4,r=3,d=8,k=4):
    adj=graph(L,r); n=len(adj)
    ps={tuple(sorted(path(adj,u,v))) for u in range(n) for v in range(u,n) if len(path(adj,u,v))-1<=d}
    bad=set(combinations(range(n),k))
    for p in ps:
        if len(p)>=k:bad.difference_update(combinations(sorted(p),k))
    # bad is k-subsets not on any shortest path; clique iff every k-subset is absent from bad
    best=0
    for m in range(1<<n):
        if m.bit_count()<=best:continue
        s={i for i in range(n) if m>>i&1}
        if all(not set(t)<=s for t in bad):best=len(s)
    return adj,tuple(sorted(ps,key=lambda t:(-len(t),t))),best

def valid(colors,paths,k):
    return all(max(Counter(colors[i] for i in p).values())<k for p in paths)

if __name__=='__main__':
    adj,paths,omega=data()
    assert omega==9
    # Count all color assignments of the 4 arm vertices, with central color fixed to 0.
    # The path between the leaf vertices of each arm pair is checked directly.
    diam=[p for p in paths if len(p)==9]
    assert len(diam)==3
    num=0
    for arms in product(range(3),repeat=12):
        colors=(0,)+arms
        if all(max(Counter(colors[i] for i in p).values())<4 for p in diam):
            num+=1
            assert valid(colors,paths,4)
    assert num==0
    print('THREE_COLOR_EXHAUSTIVE_FAIL_FIXED_CENTER',3**12,'assignments',len(diam),'diameter_paths')
    colors=(0,)+tuple(t%4 for _a in range(3) for t in range(1,5))
    assert valid(colors,paths,4)
    print('FOUR_COLOR_PATH_EXHAUSTIVE_OK',len(paths),'geodesics','omega',omega)
    print('VERIFY_OK')
