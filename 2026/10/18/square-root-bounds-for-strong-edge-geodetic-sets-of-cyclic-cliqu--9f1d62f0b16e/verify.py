#!/usr/bin/env python3
"""Standalone finite checks for square-root strong edge-geodetic bounds on cycle-clique products.
Requires Python >=3.9; standard library only. Mathematical proof covers all parameters.
"""
from math import isqrt
from itertools import combinations

def ceil_root(n):
    k=isqrt(n)
    return k+(k*k<n)

def anchors(n):
    s=min(n,2*ceil_root(n)+6)
    return tuple((i*n)//s for i in range(s))

def directed_arc(n,a,b,direction):
    p=[a];x=a
    while x!=b:
        x=(x+direction)%n
        p.append(x)
        assert len(p)<=n+1
    return p

def rung_candidates(n,T,r):
    s=len(T)
    assert s<n
    h=s//2-2
    # Sorted positive distances from the target rung, on both sides.
    left=sorted(((r-x)%n,x) for x in T if x!=r)
    right=sorted(((x-r)%n,x) for x in T if x!=r)
    assert len(left)>=h-1 and len(right)>=h-1
    opts=[]
    for i in range(1,h):
        for j in range(1,h-i+1):
            dl,x=left[i-1];dr,y=right[j-1]
            assert dl+dr<=n//2,(n,r,i,j,dl,dr,s)
            opts.append((x,y,1))
            opts.append((y,x,-1))
    assert len(opts)==h*(h-1) and len({(x,y) for x,y,_ in opts})==len(opts)
    assert len(opts)>=n,(n,s,h,len(opts))
    return opts

def construct(n,m):
    T=anchors(n);s=len(T)
    assert n>=3 and m>=2 and s>=3
    paths={}
    def record(path):
        key=frozenset((path[0],path[-1]))
        assert len(key)==2
        assert key not in paths,('duplicate endpoints',n,m,key)
        paths[key]=tuple(path)
    if s==n:
        # All vertices selected: the length-one geodesic for every edge.
        for j in range(m):
            for r in range(n):record([(r,j),((r+1)%n,j)])
        for p,q in combinations(range(m),2):
            for r in range(n):record([(r,p),(r,q)])
        return {(r,j) for r in T for j in range(m)},paths
    # Every horizontal rim is covered by geodesics in its layer.
    for j in range(m):
        for a,b in zip(T,T[1:]+T[:1]):
            arc=directed_arc(n,a,b,1)
            assert len(arc)-1<=n/2
            record([(x,j) for x in arc])
    # Match n cross-layer pairs to n rungs, greedily; n candidates for each rung.
    rung_map={}; used=set()
    for r in range(n):
        a,b,d=next((a,b,d) for a,b,d in rung_candidates(n,T,r) if (a,b) not in used)
        used.add((a,b));rung_map[r]=(a,b,d)
    assert len(used)==n
    for p,q in combinations(range(m),2):
        for r,(a,b,d) in rung_map.items():
            first=directed_arc(n,a,r,d)
            second=directed_arc(n,r,b,d)
            path=[(x,p) for x in first]+[(x,q) for x in second]
            assert len(path)-1==min((b-a)%n,(a-b)%n)+1
            record(path)
    return {(r,j) for r in T for j in range(m)},paths

def square_construction(k,m):
    """A sharp strong edge-geodetic witness for C_(k*k) box K_m, k>=3."""
    assert k>=3 and m>=2
    n=k*k
    T=tuple(range(0,n,k))
    paths={}
    def record(path):
        pair=frozenset((path[0],path[-1]))
        assert len(pair)==2 and pair not in paths
        paths[pair]=tuple(path)
    for j in range(m):
        for i in range(k):
            a=i*k;b=((i+1)%k)*k
            arc=directed_arc(n,a,b,1)
            assert len(arc)-1==k<=n//2
            record([(r,j) for r in arc])
    for p,q in combinations(range(m),2):
        rungs=set()
        for i in range(k):
            a=i*k
            for d in range(k):
                b=((i+d)%k)*k
                if d==0:
                    r=a; direction=1
                elif d<=k//2:
                    r=a+d;direction=1
                else:
                    r=(((i-1)%k)*k+d)%n;direction=-1
                assert r not in rungs,(k,r,i,d)
                rungs.add(r)
                arca=directed_arc(n,a,r,direction)
                arcb=directed_arc(n,r,b,direction)
                path=[(x,p) for x in arca]+[(x,q) for x in arcb]
                assert len(path)-1==min((b-a)%n,(a-b)%n)+1
                record(path)
        assert len(rungs)==n
    return {(r,j) for r in T for j in range(m)},paths

def check_square(k,m):
    n=k*k
    S,paths=square_construction(k,m)
    assert len(S)==m*k
    edges=set()
    for j in range(m):
        for r in range(n):edges.add(frozenset(((r,j),((r+1)%n,j))))
    for p,q in combinations(range(m),2):
        for r in range(n):edges.add(frozenset(((r,p),(r,q))))
    covered=set()
    for pair,path in paths.items():
        assert pair==frozenset((path[0],path[-1]))
        assert path[0] in S and path[-1] in S
        a,j=path[0];b,l=path[-1]
        assert len(path)-1==min((b-a)%n,(a-b)%n)+(j!=l)
        for v,w in zip(path,path[1:]):
            e=frozenset((v,w));assert e in edges
            covered.add(e)
    assert covered==edges,(k,m,len(edges-covered))
    return len(edges)

def check(n,m):
    S,paths=construct(n,m)
    nverts=len(S);s=len(anchors(n))
    assert nverts==m*s
    all_edges=set()
    for j in range(m):
        for r in range(n):
            all_edges.add(frozenset(((r,j),((r+1)%n,j))))
    for p,q in combinations(range(m),2):
        for r in range(n):all_edges.add(frozenset(((r,p),(r,q))))
    union=set()
    for key,path in paths.items():
        assert path[0] in S and path[-1] in S
        assert key==frozenset((path[0],path[-1]))
        assert len(path)==len(set(path))
        for u,v in zip(path,path[1:]):
            e=frozenset((u,v));assert e in all_edges
            union.add(e)
        a,alpha=path[0];b,beta=path[-1]
        assert len(path)-1==min((b-a)%n,(a-b)%n)+(alpha!=beta)
    assert union==all_edges, ('uncovered',n,m,len(all_edges-union))
    return len(paths),len(all_edges)

def main():
    cases=0;maxn=0;sumedges=0
    for n in list(range(3,81))+[85,93,97,100,121,144,169,196,225,256,300]:
        for m in (2,3,4) if n<=100 else (2,3):
            a,b=check(n,m);cases+=1;maxn=max(n,maxn);sumedges+=b
    # Confirm balanced-circle interval counts on smaller instances independently.
    checks=0
    for n in range(3,89):
        T=set(anchors(n));s=len(T)
        for L in range(0,n+1):
            q=(s*L)//n
            for start in range(n):
                count=sum(((start+j)%n) in T for j in range(L))
                assert count>=q,(n,L,start,count,q)
                checks+=1
    sharp_cases=0;sharp_edges=0
    for k in range(3,21):
        for m in (2,3,4):
            sharp_edges+=check_square(k,m);sharp_cases+=1
    print('VERIFY_OK')
    print('covered_graph_cases',cases)
    print('exact_square_graph_cases',sharp_cases)
    print('exact_square_edge_coverage_checks',sharp_edges)
    print('largest_graph_order_n',maxn)
    print('total_edge_coverage_checks',sumedges)
    print('balanced_interval_checks',checks)
    print('lower_bound_and_all_parameter_claim_justified_by_written_proof_not_by_finite_tests')
if __name__=='__main__':main()
