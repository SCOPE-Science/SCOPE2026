#!/usr/bin/env python3
"""Exact enumeration and algebra for regular edge-colorings and matching moments."""
from fractions import Fraction as F
from itertools import combinations
from math import prod
from collections import Counter

def matchings(vs):
    if not vs:
        yield ()
        return
    v=vs[0]
    for i in range(1,len(vs)):
        w=vs[i]
        for rem in matchings(vs[1:i]+vs[i+1:]):
            yield ((v,w),)+rem

def check(n, color):
    N=2*n
    edges={(i,j):color(i,j) for i in range(N) for j in range(i+1,N)}
    colors=sorted(set(edges.values()))
    deg={c:[0]*N for c in colors}
    for (u,v),c in edges.items():
        deg[c][u]+=1;deg[c][v]+=1
    assert all(len(set(deg[c]))==1 for c in colors)
    d={c:deg[c][0] for c in colors}
    assert sum(d.values())==N-1
    triangles=Counter()
    for x,y,z in combinations(range(N),3):
        cc=tuple(sorted([edges[x,y],edges[x,z],edges[y,z]]))
        if len(set(cc))==3:triangles[cc]+=1
    samples=Counter()
    for mt in matchings(tuple(range(N))):
        cnt=Counter(edges[e] for e in mt)
        samples[tuple(cnt.get(c,0) for c in colors)]+=1
    t=sum(samples.values())
    assert t==prod(range(1,N,2))
    mean={};pair={};trip={}
    for i in colors:
        mean[i]=F(sum(weight*vec[colors.index(i)] for vec,weight in samples.items()),t)
        assert mean[i]==F(n*d[i],N-1)
    A=F(2*n*(n-1),(N-1)*(N-3))
    for i,j in combinations(colors,2):
        ex=F(sum(weight*vec[colors.index(i)]*vec[colors.index(j)] for vec,weight in samples.items()),t)
        cov=ex-mean[i]*mean[j]
        assert ex==F(n*(n-2)*d[i]*d[j],(N-1)*(N-3)),(n,i,j,ex)
        assert cov==-A*F(d[i]*d[j],N-1),(n,i,j,cov)
    for i in colors:
        ex=F(sum(weight*vec[colors.index(i)]**2 for vec,weight in samples.items()),t)
        assert ex-mean[i]**2==A*(d[i]-F(d[i]*d[i],N-1))
    pos={c:i for i,c in enumerate(colors)}
    poscount=negcount=0
    for i,j,k in combinations(colors,3):
        e3=F(sum(weight*vec[pos[i]]*vec[pos[j]]*vec[pos[k]] for vec,weight in samples.items()),t)
        tv=triangles[i,j,k]
        assert e3==F(n*(n*n-6*n+10)*d[i]*d[j]*d[k]-tv,(N-1)*(N-3)*(N-5)),(n,i,j,k,e3,tv)
        eij=F(n*(n-2)*d[i]*d[j],(N-1)*(N-3))
        eik=F(n*(n-2)*d[i]*d[k],(N-1)*(N-3))
        ejk=F(n*(n-2)*d[j]*d[k],(N-1)*(N-3))
        cumul=e3-eij*mean[k]-eik*mean[j]-ejk*mean[i]+2*mean[i]*mean[j]*mean[k]
        expected=F(2*n*(4*n*n-8*n+5)*d[i]*d[j]*d[k],(N-5)*(N-3)*(N-1)**3)-F(tv,(N-1)*(N-3)*(N-5))
        assert cumul==expected,(n,(i,j,k),cumul,expected)
        poscount+=cumul>0
        negcount+=cumul<0
        if n==4 and len(colors)==7:
            assert (tv==8)==(i^j^k==0)
            assert tv in (0,8)
            if tv==8:
                assert cumul==F(-32,1715)
                assert e3==0
            else:
                assert cumul==F(296,5145)
                assert e3==F(8,105)
    return n,len(colors),t,len(list(combinations(colors,3))),poscount,negcount

if __name__=='__main__':
    r=[]
    for n in (3,4,5,6):
        r.append(check(n,lambda i,j,N=2*n: min((j-i)%N,(i-j)%N)))
    r.append(check(4,lambda i,j: i^j))
    r.append(check(4,lambda i,j: 0 if i^j in (1,2) else 1 if i^j in (3,4) else 2))
    for row in r:print('PASS n/colors/matchings/third/pos/neg',row)
    print('PASS exact complete-matching and rainbow-triangle moment certificates')
