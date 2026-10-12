#!/usr/bin/env python3
"""Exact independent checks for connected domination in rectangular rook graphs."""
from math import comb
from functools import lru_cache
from collections import defaultdict


def polyadd(dst, p, scalar=1):
    for i, x in enumerate(p):
        if i >= len(dst):
            dst += [0] * (i + 1 - len(dst))
        dst[i] += scalar * x


def polymul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                if b:
                    r[i+j] += a*b
    return r


@lru_cache(None)
def all_bipartite(a, b):
    return [comb(a*b,k) for k in range(a*b+1)]


@lru_cache(None)
def conn_bipartite(a, b):
    """Root-component decomposition of all labeled bipartite graphs."""
    assert a >= 1 and b >= 1
    ans = all_bipartite(a,b).copy()
    for ra in range(1, a+1):
        for rb in range(0, b+1):
            if (ra, rb) == (a,b):
                continue
            if rb == 0:
                if ra != 1:
                    continue
                c = [1]
            else:
                c = conn_bipartite(ra,rb)
            rem = all_bipartite(a-ra,b-rb)
            polyadd(ans,polymul(c,rem),-comb(a-1,ra-1)*comb(b,rb))
    assert ans[0] == 0
    assert all(i>=a+b-1 or coeff==0 for i, coeff in enumerate(ans))
    assert all(x>=0 for x in ans)
    return ans


@lru_cache(None)
def stirling2(n,k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return stirling2(n-1,k-1)+k*stirling2(n-1,k)


def predicted(m,n):
    full=[0]*(m*n+1)
    for b in range(1,n+1):
        polyadd(full,conn_bipartite(m,b),comb(n,b))
    for a in range(1,m+1):
        polyadd(full,conn_bipartite(a,n),comb(m,a))
    polyadd(full,conn_bipartite(m,n),-1)
    minimal=[0]*(m*n+1)
    for b in range(1,min(m,n)):
        minimal[m+b-1]+=comb(n,b)*m**(b-1)*__import__('math').factorial(b)*stirling2(m-1,b)
    for a in range(1,min(m,n)):
        minimal[n+a-1]+=comb(m,a)*n**(a-1)*__import__('math').factorial(a)*stirling2(n-1,a)
    return full,minimal


def brute(m,n):
    N=m*n
    adj=[0]*N
    for i in range(N):
        for j in range(N):
            if i!=j and (i//n==j//n or i%n==j%n):
                adj[i]|=1<<j
    def connected_dominates(mask):
        if not mask:
            return False
        dominated=mask
        chosen=[]
        bits=mask
        while bits:
            bit=bits&-bits
            i=bit.bit_length()-1
            chosen.append(i)
            dominated|=adj[i]
            bits-=bit
        if dominated!=(1<<N)-1:
            return False
        reached=1<<chosen[0]
        frontier=reached
        while frontier:
            next_frontier=0
            bits=frontier
            while bits:
                bit=bits&-bits
                i=bit.bit_length()-1
                next_frontier|=adj[i]&mask&~reached
                bits-=bit
            frontier=next_frontier
            reached|=frontier
        return reached==mask
    def structural(mask):
        # This implementation uses bipartite incidence components rather than rook adjacency.
        rows=set();cols=set();parent=list(range(m+n));degree=[0]*(m+n)
        def root(i):
            while parent[i]!=i:
                i=parent[i]
            return i
        bits=mask
        while bits:
            bit=bits&-bits
            i=bit.bit_length()-1
            row,col=divmod(i,n)
            rows.add(row);cols.add(col);degree[row]+=1;degree[m+col]+=1
            parent[root(row)]=root(m+col)
            bits-=bit
        if not (len(rows)==m or len(cols)==n):
            return False, False
        if len({root(v) for v in rows}|{root(m+v) for v in cols})!=1:
            return False, False
        edgecount=mask.bit_count()
        tree=edgecount==len(rows)+len(cols)-1
        if not tree:
            return True,False
        min_struct=(len(rows)==m and len(cols)<n and all(degree[m+c]>=2 for c in cols)) or (len(cols)==n and len(rows)<m and all(degree[r]>=2 for r in rows))
        return True, min_struct
    full=[0]*(N+1);minimal=[0]*(N+1)
    total=0;min_total=0
    for mask in range(1,1<<N):
        real=connected_dominates(mask)
        structural_member,structural_minimal=structural(mask)
        assert real==structural_member,(m,n,mask,'connectivity')
        if not real:
            continue
        total+=1
        full[mask.bit_count()]+=1
        minimally_all=True
        bits=mask
        while bits:
            bit=bits&-bits
            if connected_dominates(mask^bit):
                minimally_all=False
                break
            bits-=bit
        assert minimally_all==structural_minimal,(m,n,mask,'minimal classification')
        if minimally_all:
            min_total+=1
            minimal[mask.bit_count()]+=1
    return full,minimal,total,min_total


def main():
    checks=[(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(2,8),(3,3),(3,4),(3,5),(4,4)]
    visits=0;cds=0;minimal_count=0
    for m,n in checks:
        p,q=predicted(m,n)
        bp,bq,c,d=brute(m,n)
        assert p==bp,(m,n,'full',p,bp)
        assert q==bq,(m,n,'minimal',q,bq)
        allowed=[i for i,x in enumerate(q) if x>0]
        assert allowed[0]==min(m,n)
        assert allowed[-1]==m+n-2
        visits+=(1<<(m*n))-1
        cds+=c;minimal_count+=d
        print(f'CASE_OK {m}x{n} connected={c} minimal={d} min_spectrum={allowed}')
    p,q=predicted(3,3)
    print('FULL_3x3', [(i,c) for i,c in enumerate(p) if c])
    print('MINIMAL_3x3',[(i,c) for i,c in enumerate(q) if c])
    print(f'VERIFY_OK boards={len(checks)} subset_checks={visits} connected_sets={cds} minimal_sets={minimal_count}')

if __name__=='__main__':
    main()
