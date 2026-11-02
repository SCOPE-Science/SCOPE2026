"""Standalone science reproducibility: brute force original graph vs independent edge-process recurrence."""
import math
from collections import Counter
from functools import lru_cache

def recurrence(n):
    a={(0,0):1}
    for nn in range(1,n+1):
        for kk in range(1,nn):
            a[(nn,kk)]= nn*(nn-1)*a.get((nn-1,kk-1),0)+ math.comb(nn,2)*a.get((nn-2,kk-1),0)
    return {nn-1+k:math.factorial(n)*math.comb(nn-1+k,nn-1)*a.get((n,k),0) for nn in [n] for k in range((n+1)//2,n)}

def brute_original(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    N=n+len(edges)
    nbr=[0]*N
    for idx,(i,j) in enumerate(edges,n):
        for i0 in (i,j):
            nbr[idx]|=1<<i0
            nbr[i0]|=1<<idx
    all_mask=(1<<N)-1
    @lru_cache(maxsize=None)
    def f(used):
        covered=0
        m=used
        while m:
            bit=m&-m; u=bit.bit_length()-1; covered|=nbr[u];m-=bit
        if covered==all_mask:return ((0,1),)
        cnt=Counter()
        for u in range(N):
            if ((used>>u)&1)==0 and nbr[u]&~covered:
                for extra,value in f(used|(1<<u)):
                    cnt[extra+1]+=value
        return tuple(sorted(cnt.items()))
    out=dict(f(0))
    return out,f.cache_info()

if __name__=='__main__':
    for n in range(2,6):
        a=brute_original(n); b=recurrence(n)
        print(n,'original',a[0],'recurrence',b,'states',a[1])
        assert a[0]==b,(n,a,b)
        assert sorted(b)==list(range(n-1+(n+1)//2,2*n-1))
        if n%2==0:
            assert b[n-1+n//2]==math.factorial(n)*math.comb(n-1+n//2,n-1)*math.factorial(n)//2**(n//2)
        if n%2:
            r=(n-1)//2
            assert b[n-1+(n+1)//2]==math.factorial(n)*math.comb(n-1+(n+1)//2,n-1)*math.factorial(n)*r*(r+1)//(2**r)
        assert b[2*n-2]==math.factorial(n)*math.comb(2*n-2,n-1)*math.comb(n,2)*math.factorial(n-1)*math.factorial(n-2)
    print('PASS: independent exhaustive graph validation and extremal formulas')
