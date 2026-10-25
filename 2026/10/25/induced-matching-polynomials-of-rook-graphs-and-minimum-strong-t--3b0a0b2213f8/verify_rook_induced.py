#!/usr/bin/env python3
"""Independent graph-level enumeration against the rectangular closed formula."""
from itertools import combinations
from math import factorial

def formula(m,n):
    counts={}
    for h in range(m+1):
        for v in range(n+1):
            if h+2*v>m or 2*h+v>n:continue
            c=factorial(m)*factorial(n)//(factorial(h)*factorial(v)*factorial(m-h-2*v)*factorial(n-2*h-v)*2**(h+v))
            counts[h+v]=counts.get(h+v,0)+c
    return counts

def independently_enumerated(m,n):
    V=list(range(m*n)); edges=[]
    for i,j in combinations(V,2):
        if (i//n==j//n) or (i%n==j%n):edges.append((i,j))
    def conflict(e,f):
        # Selected edges are illegal together if any endpoint of one
        # equals or is adjacent to an endpoint of the other.
        return any(a==b or a//n==b//n or a%n==b%n for a in e for b in f)
    conflicts=[0]*len(edges)
    for i,e in enumerate(edges):
        for j,f in enumerate(edges):
            if conflict(e,f):conflicts[i]|=1<<j
    out={0:1}; maxsize=min(m,n,(m+n)//3)
    for k in range(1,maxsize+1):
        tally=0
        for inds in combinations(range(len(edges)),k):
            if all(((conflicts[a]>>b)&1)==0 for a,b in combinations(inds,2)):
                tally+=1
        out[k]=tally
    return out

def strong_cover_check(m,n):
    V=m*n; edges=[(a,b) for a,b in combinations(range(V),2) if a//n==b//n or a%n==b%n]; E=len(edges)
    allmask=(1<<(V+E))-1
    cover=[1<<i for i in range(V+E)]
    for j,(a,b) in enumerate(edges):
        cover[j+V]|=(1<<a)|(1<<b)
        cover[a]|=1<<(V+j)
        cover[b]|=1<<(V+j)
    target=V-min(m,n,(m+n)//3)
    # Independently excludes every smaller set via monotonicity:
    # every cover of size smaller would extend to a cover of size target-1.
    if target>0:
        for inds in combinations(range(V+E),target-1):
            mask=0
            for j in inds:mask|=cover[j]
            assert mask!=allmask,(m,n,'too small',inds)
    # Check at least one canonical witness at target from direct algorithm.
    H=0; vv=0; t=V-target
    for h in range(t+1):
        v=t-h
        if h+2*v<=m and 2*h+v<=n:H,Vv=h,v;break
    else:raise AssertionError('no packing')
    selected=[]
    for r in range(H):selected.append((r*n+2*r,r*n+2*r+1))
    for c in range(Vv):
        rr=H+2*c; col=2*H+c
        selected.append((rr*n+col,(rr+1)*n+col))
    s=set()
    for a,b in selected:s.update((a,b))
    edgeids={e:i for i,e in enumerate(edges)}
    S=[a for a in range(V) if a not in s]+[V+edgeids[e] for e in selected]
    assert len(S)==target
    mask=0
    for j in S:mask|=cover[j]
    assert mask==allmask
    return target

def main():
    tests=[(m,n) for m in range(2,6) for n in range(m,6) if m*n<=25]
    for m,n in tests:
        f=formula(m,n);e=independently_enumerated(m,n)
        assert f==e,(m,n,f,e)
        assert max(f)==min(m,n,(m+n)//3)
    # finite exhaustive search of all candidate covers below target, within 300s.
    checks=[]
    for m,n in [(2,2),(2,3),(2,4),(3,3)]:
        checks.append((m,n,strong_cover_check(m,n)))
    print('VERIFY_OK exact_induced_polynomials',len(tests),'strong_cover_exhaustive',checks)
if __name__=='__main__':main()
