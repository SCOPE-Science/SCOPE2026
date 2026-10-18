"""Exact, independent checks for facet and symmetry-orbit formulas."""
from itertools import combinations, permutations, product
from math import comb

def data(n):
    es=list(combinations(range(n),2)); q={e:n+i for i,e in enumerate(es)}
    N=n+len(es)
    edges=[(u,q[u,v]) for u,v in es]+[(v,q[u,v]) for u,v in es]
    adj=[[] for _ in range(N)]
    for u,v in edges: adj[u].append(v);adj[v].append(u)
    seen={0}; queue=[0];tree=[]
    for u in queue:
        for v in adj[u]:
            if v not in seen:
                seen.add(v);queue.append(v);tree.append((u,v))
    assert len(tree)==N-1
    return es,q,N,edges,tree

def brute_facets(n):
    es,q,N,edges,tree=data(n)
    out=[]
    for signs in product((-1,1),repeat=N-1):
        h=[0]*N
        for (u,v),s in zip(tree,signs): h[v]=h[u]+s
        if all(abs(h[u]-h[v])==1 for u,v in edges):out.append(tuple(h))
    return out

def exact_formula(n):
    m=comb(n,2)
    return 2**m+sum(comb(n,k)*2**(comb(k,2)+comb(n-k,2)) for k in range(1,n))

def graph_type_count(j):
    pairs=list(combinations(range(j),2));M=len(pairs)
    actions=[]
    for p in permutations(range(j)):
        actions.append([pairs.index(tuple(sorted((p[u],p[v])))) for u,v in pairs])
    seen=set();groups=[]
    for mask in range(1<<M):
        if mask in seen:continue
        orb=set()
        for a in actions:
            mm=0
            for i,k in enumerate(a):
                if mask>>i&1:mm|=1<<k
            orb.add(mm)
        groups.append(orb);seen.update(orb)
    index={m:i for i,g in enumerate(groups) for m in g}
    complementation_orbits=set()
    for i,g in enumerate(groups):complementation_orbits.add(tuple(sorted((i,index[(1<<M)-1-next(iter(g))]))))
    return len(groups),len(complementation_orbits)

def orbit_count_formula(n):
    a={j:graph_type_count(j)[0] for j in range(1,n+1)}
    b=graph_type_count(n)[1]
    s=b+sum(a[k]*a[n-k] for k in range(1,(n+1)//2))
    if n%2==0:s+=a[n//2]*(a[n//2]+1)//2
    return s

def brute_orbit_count(n,pts):
    es,q,N,edges,tree=data(n)
    assert n>=4
    esidx={e:i for i,e in enumerate(es)}
    acts=[]
    for p in permutations(range(n)):
        newindex=tuple(p[i] for i in range(n))+tuple(n+esidx[tuple(sorted((p[u],p[v])))] for u,v in es)
        acts.append(newindex)
    allp=set(pts);orbits=0;size_hist={}
    while allp:
        v=allp.pop();orbit=set()
        for newindex in acts:
            w=[0]*N
            for i,j in enumerate(newindex): w[j]=v[i]
            d=w[0]
            canon=tuple(t-d for t in w)
            orbit.add(canon)
            orbit.add(tuple(-t for t in canon))
        assert orbit <= set(pts)
        allp.difference_update(orbit)
        orbits+=1;size_hist[len(orbit)]=size_hist.get(len(orbit),0)+1
    return orbits,size_hist

def test():
    for n in range(2,7):
        pts=brute_facets(n)
        assert len(pts)==exact_formula(n),(n,len(pts),exact_formula(n))
        print('facet',n,len(pts))
        if n in (4,5):
            a,st=brute_orbit_count(n,pts)
            f=orbit_count_formula(n)
            assert a==f,(n,a,f)
            print('orbits',n,a,st)
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':test()
