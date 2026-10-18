"""Exact finite certificate for sharp three-phase tree surveillance; standard library only.
Run: python3 verify_three_sentinel_winners.py
"""
from collections import defaultdict, deque, Counter
from itertools import accumulate

WITNESS = [(1,0),(1,2),(0,5),(2,3),(3,4),(5,6),(6,7),(6,8)]


def adjacency(n, edges):
    a = [[] for _ in range(n)]
    for u,v in edges:
        a[u].append(v); a[v].append(u)
    return a


def canonical(n,edges):
    a=adjacency(n,edges)
    deg=[len(x) for x in a]
    leaves=[i for i in range(n) if deg[i]<=1]
    remaining=n
    while remaining>2:
        remaining-=len(leaves)
        new=[]
        for v in leaves:
            for w in a[v]:
                deg[w]-=1
                if deg[w]==1:new.append(w)
            deg[v]=0
        leaves=new
    def rooted(u, parent):
        return '('+''.join(sorted(rooted(w,u) for w in a[u] if w!=parent))+')'
    return min(rooted(v,-1) for v in leaves)


def profiles(n,edges):
    a=adjacency(n,edges)
    out=[]
    for v in range(n):
        ds=[-1]*n;ds[v]=0;q=deque([v])
        while q:
            u=q.popleft()
            for w in a[u]:
                if ds[w]<0:ds[w]=ds[u]+1;q.append(w)
        assert all(k>=0 for k in ds)
        counts=tuple(sum(x==j for x in ds) for j in range(1,n))
        assert sum(counts)==n-1
        out.append(counts)
    return out


def pareto(profiles):
    uniq=set(profiles)
    cumul={s:tuple(accumulate(s)) for s in uniq}
    return sorted([s for s in uniq if not any(t!=s and all(x>=y for x,y in zip(cumul[t],cumul[s])) for t in uniq)])


def polynomial_mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return tuple(o)


def assert_poly_diff(x,y,factors):
    product=(1,)
    for f in factors:product=polynomial_mul(product,f)
    given=tuple(a-b for a,b in zip((0,)+x,(0,)+y))
    n=max(len(given),len(product)); assert given+(0,)*(n-len(given))==product+(0,)*(n-len(product)),(given,product)


def small_census():
    trees={canonical(1,[]):[]}
    expected={1:1,2:1,3:1,4:2,5:3,6:6,7:11,8:23}
    for n in range(1,9):
        assert len(trees)==expected[n],(n,len(trees))
        mx=0;exception=0
        for edges in trees.values():
            profiles_here=profiles(n,edges)
            frontier=pareto(profiles_here)
            mx=max(mx,len(frontier))
            if n<=7:assert len(frontier)<=2,(n,edges,frontier)
            if n==8 and len(frontier)==3:
                exception+=1
                # Exactly one otherwise Pareto-undominated pair has a
                # strictly positive difference p^2(1-p)^2 on 0<p<1.
                assert any(
                    (lambda x,y: (len(x)>=4 and len(y)>=4 and
                      tuple(a-b for a,b in zip(x,y))[:4]==(0,1,-2,1) and
                      all(a==b for a,b in zip(x[4:],y[4:]))))(x,y)
                    for x in frontier for y in frontier if x!=y
                ),('missing n8 exact dominance certificate',edges,frontier)
            else:
                assert n!=8 or len(frontier)<=2
        if n==8: assert exception==1,(exception,mx)
        print('n=',n,'trees=',len(trees),'max nondominated profiles=',mx,'exceptional trees=',exception)
        if n<8:
            nxt={}
            for es in trees.values():
                for v in range(n):
                    new_es=es+[(v,n)]
                    nxt.setdefault(canonical(n+1,new_es),new_es)
            trees=nxt


def witness_checks():
    n=9; d=profiles(n,WITNESS)
    f=pareto(d)
    assert len(f)==3 and set(f)=={d[v] for v in (0,5,6)}
    # Distances and candidate scores.
    assert d[0][:5]==(2,2,3,1,0)
    assert d[5][:5]==(2,3,1,1,1)
    assert d[6][:6]==(3,1,1,1,1,1)
    # Exact algebra C_6-C_5 = p(1-p)(1-p-p^2-p^3-p^4)
    assert_poly_diff(d[6],d[5],[(0,1),(1,-1),(1,-1,-1,-1,-1)])
    # C_5-C_0 = p^2(1-p)(1-p-p^2)
    assert_poly_diff(d[5],d[0],[(0,0,1),(1,-1),(1,-1,-1)])
    # Other vertices are strictly dominated for all 0<p<1 by a winner candidate.
    cumul={v:tuple(accumulate(d[v])) for v in range(n)}
    for v in range(n):
        if v in (0,5,6):continue
        assert any(all(x>=y for x,y in zip(cumul[w],cumul[v]))
                   and cumul[w]!=cumul[v] for w in (0,5,6)),v
    # Strictly increasing root polynomials in (0,1), root q4 before root q2.
    def q4(x):return x**4+x**3+x**2+x-1
    def q2(x):return x**2+x-1
    a,b=0.,1.
    for _ in range(70):
        m=(a+b)/2
        if q4(m)<0:a=m
        else:b=m
    r=(a+b)/2
    a,b=0.,1.
    for _ in range(70):
        m=(a+b)/2
        if q2(m)<0:a=m
        else:b=m
    s=(a+b)/2
    assert 0<r<s<1
    print('n9 witness edges:',WITNESS)
    print('n9 unique winners in order: 6, 5, 0')
    print('n9 transitions:',format(r,'.15f'),format(s,'.15f'))


if __name__=='__main__':
    small_census()
    witness_checks()
    print('PASS: exact exhaustive small-tree certificate and analytical witness identities')
