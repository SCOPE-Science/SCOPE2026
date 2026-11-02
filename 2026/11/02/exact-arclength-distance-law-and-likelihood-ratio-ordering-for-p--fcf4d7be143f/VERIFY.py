#!/usr/bin/env python3
"""Exact-rational finite checks for the intrinsic metric of projective-plane incidence networks."""
from collections import Counter, deque
from fractions import Fraction as F
from itertools import product
from math import gcd


def normalize(v,p):
    i=next(k for k,x in enumerate(v) if x%p)
    inv=pow(v[i],-1,p)
    return tuple((x*inv)%p for x in v)


def plane(p):
    assert p>=2 and all(p%d for d in range(2,int(p**0.5)+1))
    triples=sorted({normalize(v,p) for v in product(range(p),repeat=3) if any(v)})
    n=len(triples)
    assert n==p*p+p+1
    graph=[[] for _ in range(2*n)]
    edges=[]
    for i,v in enumerate(triples):
        for j,l in enumerate(triples):
            if sum(a*b for a,b in zip(v,l))%p==0:
                e=(i,n+j)
                edges.append(e)
                graph[i].append(n+j)
                graph[n+j].append(i)
    assert len(edges)==(p+1)*n
    assert all(len(a)==p+1 for a in graph)
    dist=[]
    for v in range(2*n):
        d=[None]*(2*n)
        d[v]=0
        q=deque([v])
        while q:
            u=q.popleft()
            for w in graph[u]:
                if d[w] is None:
                    d[w]=d[u]+1
                    q.append(w)
        assert max(d)==3
        dist.append(d)
    return edges,dist


def kind(e,f,dist):
    if e==f: return 0
    if len(set(e)&set(f))==1: return 1
    cross=sum(dist[a][b]==1 for a,b in ((e[0],f[1]),(e[1],f[0])))
    assert cross in (0,1)
    return 2 if cross else 3


def shortest(e,f,dist,x,y):
    if e==f: return abs(x-y)
    (a,b),(c,d)=e,f
    return min(x+y+dist[a][c],x+(1-y)+dist[a][d],
               (1-x)+y+dist[b][c],(1-x)+(1-y)+dist[b][d])


def predicted(k,e,f,dist,x,y):
    if k==0:return abs(x-y)
    if k==1:
        common=(set(e)&set(f)).pop()
        xe=x if e[0]==common else 1-x
        yf=y if f[0]==common else 1-y
        return xe+yf
    if k==2:
        if dist[e[0]][f[1]]==1:
            return 2+x-y
        assert dist[e[1]][f[0]]==1
        return 2-x+y
    assert k==3
    return 3-abs(x+y-1)


def run(p,grid=(F(0),F(1,5),F(1,2),F(4,5),F(1))):
    edges,dist=plane(p)
    m=len(edges)
    counts=Counter()
    validations=0
    for ei,e in enumerate(edges):
        c=Counter()
        for f in edges:
            k=kind(e,f,dist)
            c[k]+=1
            for x in grid:
                for y in grid:
                    actual=shortest(e,f,dist,x,y)
                    model=predicted(k,e,f,dist,x,y)
                    assert actual==model,(p,ei,e,f,k,x,y,actual,model)
                    validations+=1
        assert [c[i] for i in range(4)]==[1,2*p,2*p*p,p**3]
        counts.update(c)
    print('q=',p,'edges=',m,'ordered pair classes=',[counts[i] for i in range(4)],'evaluations=',validations)
    return m,validations

if __name__=='__main__':
    total=0
    for p in (2,3,5):
        m,n=run(p)
        total+=n
    # Check the universal moment and derivative identities as polynomial identities,
    # using only integer arithmetic; this is not a numerical interpolation.
    def padd(a,b):
        return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]
    def pmul(a,b):
        z=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): z[i+j]+=x*y
        return z
    def pscale(a,k):return [k*x for x in a]
    def psub(a,b):return padd(a,pscale(b,-1))
    def ppow(a,n):
        r=[1]
        for _ in range(n):r=pmul(r,a)
        return r
    m=[1,2,2,1]
    mprime=[2,4,3]
    assert ppow([1,2],3)==[1,6,12,8]
    assert psub(pscale(m,6),pmul([1,2],mprime))==[4,4,1,0]
    second_numerator=[1,14,50,43]
    variance_lhs=psub(pscale(pmul(second_numerator,m),3),pscale(ppow([1,2],6),2))
    variance_rhs=pmul([1,4,1],[1,20,39,20,1])
    assert variance_lhs==variance_rhs
    print('symbolic mean/second/variance/monotonicity polynomial identities verified; exact endpoint evaluations=',total)
