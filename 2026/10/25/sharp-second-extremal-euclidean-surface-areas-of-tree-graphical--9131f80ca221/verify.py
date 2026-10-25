"""Independent finite checks of geometric tree-zonotope surface identities.
Pure Python 3 standard library. This is not a proof for all n.
"""
import itertools
import math


def edges_from_prufer(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq: deg[x]+=1
    edges=[]
    for x in seq:
        leaf=next(i for i in range(n) if deg[i]==1)
        edges.append((leaf,x)); deg[leaf]-=1; deg[x]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    return edges+[(u,v)]


def cut_products(edges,n):
    out=[]
    for u,v in edges:
        adj=[[] for _ in range(n)]
        for x,y in edges:
            if (x,y)==(u,v): continue
            adj[x].append(y); adj[y].append(x)
        seen={u}; stk=[u]
        while stk:
            for y in adj[stk.pop()]:
                if y not in seen: seen.add(y);stk.append(y)
        s=len(seen)
        out.append(s*(n-s))
    return out


def det_bareiss(mat):
    a=[row[:] for row in mat]; n=len(a)
    if n==0:return 1
    sign=1;last=1
    for k in range(n-1):
        if a[k][k]==0:
            pivot=next((i for i in range(k+1,n) if a[i][k]!=0),None)
            if pivot is None: return 0
            a[k],a[pivot]=a[pivot],a[k];sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*v-a[i][k]*a[k][j]
                assert z%last==0
                a[i][j]=z//last
        for i in range(k+1,n): a[i][k]=0
        last=v
    return sign*a[-1][-1]


def gram_det(edges,n):
    m=len(edges)
    B=[[0]*m for _ in range(n)]
    for j,(u,v) in enumerate(edges): B[u][j]=1; B[v][j]=-1
    A=[[sum(B[k][i]*B[k][j] for k in range(n)) for j in range(m)] for i in range(m)]
    return det_bareiss(A)


def canon(edges,n):
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    def rootcode(u,parent):
        return '('+''.join(sorted(rootcode(v,u) for v in adj[u] if v!=parent))+')'
    return min(rootcode(v,-1) for v in range(n))


def star(n): return [(0,i) for i in range(1,n)]
def path(n): return [(i,i+1) for i in range(n-1)]
def nearstar(n):
    return [(0,i) for i in range(1,n-1)]+[(n-2,n-1)]
def nearpath(n):
    return [(i,i+1) for i in range(n-2)]+[(1,n-1)]

checks=0
for n in range(4,8):
    f1=math.sqrt(n-1)
    f2=math.sqrt(2*(n-2))
    low=2*(n-1)*f1
    high=2*sum(math.sqrt(k*(n-k)) for k in range(1,n))
    gap=2*(f2-f1)
    shapes={'min':canon(star(n),n),'max':canon(path(n),n),
            'second_min':canon(nearstar(n),n),'second_max':canon(nearpath(n),n)}
    seen=set()
    for seq in itertools.product(range(n),repeat=n-2):
        edges=edges_from_prufer(seq)
        typ=canon(edges,n)
        if typ in seen: continue
        seen.add(typ)
        q=cut_products(edges,n)
        area=2*sum(math.sqrt(p) for p in q)
        assert low-1e-10<=area<=high+1e-10
        assert (abs(area-low)<1e-10)==(typ==shapes['min'])
        assert (abs(area-high)<1e-10)==(typ==shapes['max'])
        if typ!=shapes['min']:
            assert area>=low+gap-1e-10
            assert (abs(area-(low+gap))<1e-10)==(typ==shapes['second_min'])
        if typ!=shapes['max']:
            assert area<=high-gap+1e-10
            assert (abs(area-(high-gap))<1e-10)==(typ==shapes['second_max'])
        # Forest-incidence Gram minors independently give face areas.
        assert gram_det(edges,n)==n
        for j in range(n-1):
            other=edges[:j]+edges[j+1:]
            assert gram_det(other,n)==q[j]
            checks+=1
        checks+=1
    print('n',n,'unlabeled',len(seen),'face-and-extreme-checks',checks)
assert checks>100
print('VERIFY_OK',checks,'exact_Gram_and_extremality_checks')
