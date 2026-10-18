#!/usr/bin/env python3
"""Exact upper-triangular matrix census and degree-profile fiber checks."""
from functools import lru_cache
from collections import defaultdict
from math import comb

@lru_cache(None)
def compositions(s, k):
    if k == 1:
        return ((s,),)
    return tuple((x,) + suffix for x in range(s + 1)
                 for suffix in compositions(s-x, k-1))

def fishburn_matrices(n):
    for k in range(1, n+1):
        def extend(i, left, rows, covered):
            if i == k:
                if left == 0 and covered == (1 << k)-1:
                    yield rows
                return
            for weight in range(1, left-(k-i-1)+1):
                for tail in compositions(weight,k-i):
                    new_covered = covered
                    for j,val in enumerate(tail, i):
                        if val:
                            new_covered |= 1 << j
                    # No later row can fill columns 0 through i.
                    if (new_covered & ((1 << (i+1))-1)) != ((1 << (i+1))-1):
                        continue
                    row = (0,)*i + tail
                    yield from extend(i+1,left-weight,rows+(row,),new_covered)
        yield from extend(0,n,(),0)

def profiles(M):
    k=len(M)
    entries=[(i,j,M[i][j]) for i in range(k) for j in range(i,k) if M[i][j]]
    paired=[]
    for i,j,v in entries:
        below=sum(w for a,b,w in entries if b<i)
        above=sum(w for a,b,w in entries if a>j)
        paired.extend([(below,above)]*v)
    return tuple(sorted(paired)),tuple(sorted((b for a,b in paired),reverse=True))

def staircase_profiles(n):
    def walk(i, ceiling, chosen):
        if i==n:
            yield chosen
            return
        for d in range(min(ceiling, n-i-1)+1):
            yield from walk(i+1,d,chosen+(d,))
    yield from walk(0,n-1,())

def margin_count(r,c):
    k=len(r)
    @lru_cache(None)
    def dfs(i,rem):
        if i==k:
            return int(all(x==0 for x in rem))
        ans=0
        def row(j,free,cols):
            nonlocal ans
            if j==k:
                if free==0:
                    ans+=dfs(i+1,tuple(cols))
                return
            if j<i:
                row(j+1,free,cols)
                return
            for a in range(min(free,cols[j])+1):
                nxt=list(cols);nxt[j]-=a
                row(j+1,free-a,nxt)
        row(0,r[i],list(rem))
        return ans
    return dfs(0,tuple(c))

def extracted_margins(out):
    distinct=[];mult=[]
    for d in out:
        if not distinct or distinct[-1]!=d:
            distinct.append(d);mult.append(1)
        else:mult[-1]+=1
    n=len(out)
    r=(n-distinct[0],)+tuple(distinct[i-1]-distinct[i] for i in range(1,len(distinct)))
    return r,tuple(mult)

if __name__=='__main__':
    for n in range(1,10):
        out_groups=defaultdict(int);paired_groups={};allcount=0
        for mat in fishburn_matrices(n):
            allcount+=1
            paired,out=profiles(mat)
            assert paired not in paired_groups, (n,paired)
            paired_groups[paired]=mat
            out_groups[out]+=1
        expected=comb(2*n,n)//(n+1)
        assert len(out_groups)==expected
        assert set(out_groups)==set(staircase_profiles(n))
        assert allcount==len(paired_groups)
        for out,count in out_groups.items():
            assert all(out[i]>=out[i+1] for i in range(n-1))
            assert all(v<=n-i-1 for i,v in enumerate(out))
            if n<=8:
                r,c=extracted_margins(out)
                assert margin_count(r,c)==count, (n,out,r,c,count)
        print(f'n={n} interval_orders={allcount} one_sided_signatures={len(out_groups)} unique_fibers={sum(v==1 for v in out_groups.values())} maximum_fiber={max(out_groups.values())}')
    print('VERIFY_FISHBURN_PASS')
