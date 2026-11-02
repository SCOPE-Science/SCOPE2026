#!/usr/bin/env python3
"""Independent geometric chord-reachability test and exhaustive support census."""
from itertools import combinations
from math import comb

def crossing(a,b,c,d):
    if a>b:a,b=b,a
    if c>d:c,d=d,c
    return (a<c<b<d) or (c<a<d<b)

def fvector(n):
    edges=list(combinations(range(n),2));m=len(edges)
    adj=[0]*m;incident=[0]*n
    for i,(a,b) in enumerate(edges):
        incident[a]|=1<<i
        incident[b]|=1<<i
        for j,(c,d) in enumerate(edges[:i]):
            if len({a,b,c,d})<4 or crossing(a,b,c,d):
                adj[i]|=1<<j
                adj[j]|=1<<i
    def good(S):
        rem=S
        while rem:
            bit=rem&-rem;rem^=bit
            i=bit.bit_length()-1
            T=S^bit
            a,b=edges[i]
            queue=T&incident[a]
            target=T&incident[b]
            seen=queue
            while queue and not (seen & target):
                cur=queue&-queue;queue^=cur
                e=cur.bit_length()-1
                new=adj[e]&T&~seen
                seen|=new
                queue|=new
            if seen&target:return False
        return True
    result=[]
    for k in range(n):
        z=0
        for ii in combinations(range(m),k):
            S=sum(1<<j for j in ii)
            if good(S):z+=1
        result.append(z)
        print('GEOMETRIC_SUPPORT_CENSUS_PASS',n,k,z,flush=True)
    return result

if __name__=='__main__':
    expected={4:[1,6,15,12],5:[1,10,45,90,55],6:[1,15,105,375,588,273],7:[1,21,210,1155,3276,3990,1428],8:[1,28,378,2940,12929,28980,27492,7752]}
    import sys
    for n in (list(map(int,sys.argv[1:])) if len(sys.argv)>1 else [4,5,6,7,8]):
        vals=fvector(n)
        assert vals==expected[n]
        assert vals[-1]==comb(3*(n-1),n-1)//(2*n-1)
    print('ALL_GEOMETRIC_CENSUSES_PASS')
