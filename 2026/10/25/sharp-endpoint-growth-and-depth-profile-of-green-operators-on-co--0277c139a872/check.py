#!/usr/bin/env python3
"""Exact rational checks for endpoint norms of hierarchical tree Green operators."""
from fractions import Fraction as Q
from itertools import product

def test(b,h):
    paths=[p for j in range(h+1) for p in product(range(b),repeat=j)]
    n=len(paths); index={p:i for i,p in enumerate(paths)}
    D=b**(h+1)-1
    sizes=[0]+[(b**(h-l+1)-1)//(b-1) for l in range(1,h+1)]
    f=[Q(0)]
    for l in range(1,h+1): f.append(f[-1]+Q(sizes[l],n))
    H=sum((b**j*f[j] for j in range(h+1)),Q(0))/n
    def meet(x,y):
        t=0
        for a,c in zip(x,y):
            if a!=c: break
            t+=1
        return t
    g=[[Q(meet(x,y))+H-f[len(x)]-f[len(y)] for y in paths] for x in paths]
    checks=0
    for i,x in enumerate(paths):
        assert sum(g[i])==0; checks+=1
        for j,y in enumerate(paths):
            assert g[i][j]==g[j][i]; checks+=1
            neigh=([x[:-1]] if x else [])+([x+(a,) for a in range(b)] if len(x)<h else [])
            lhs=len(neigh)*g[i][j]-sum(g[index[t]][j] for t in neigh)
            assert lhs==Q(int(i==j))-Q(1,n), (b,h,i,j,lhs)
            checks+=1
    q1=Q(sizes[1],n)
    delta=f[h]-H
    assert delta==sum((Q(sizes[l],n)*Q(b**l-1,D) for l in range(1,h+1)),Q(0));checks+=1
    assert delta>=0 and delta<=Q(h*b**(h+1),D**2);checks+=1
    rs=[]
    for k in range(h+1):
        i=index[(0,)*k]
        r=sum(abs(x) for x in g[i])/n
        rs.append(r)
        target=2*f[k]*(1-q1) if k else Q(0)
        assert abs(r-target)<=2*delta,(b,h,k,r,target,delta)
        checks+=1
    leaf=paths[index[(0,)*h]]
    for y in paths:
        entry=g[index[leaf]][index[y]]
        assert (entry>0) == (meet(leaf,y)>=1), (b,h,y,entry)
        checks+=1
    explicit_leaf=Q(2,b)*(Q((b-1)*n+1)*f[h]-H)
    assert sum(abs(e) for e in g[index[leaf]])==explicit_leaf
    checks+=1
    assert max(rs)==max(sum(abs(z) for z in row)/n for row in g);checks+=1
    assert abs(max(rs)-2*f[h]*(1-q1))<=2*delta;checks+=1
    return checks, n, list(map(float,rs))

if __name__=='__main__':
    c=0
    for b,h in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(4,1),(4,2),(5,1),(5,2)]:
        a,n,rs=test(b,h);c+=a
        print('b,h,N',b,h,n,'radii',*[round(v,8) for v in rs]);
    print('PASS',c,'exact rational assertions')
