#!/usr/bin/env python3
"""Direct finite verification of diamond closure-map classification and pairwise commutation."""
from itertools import product
from math import comb

def verify(n):
    k=n+2
    zero=0;top=k-1;atoms=range(1,top)
    def le(i,j): return (i==0) or (i==j) or (j==top)
    # Enumerate ALL extensive selfmaps, then test monotonicity and idempotence.
    good=[]
    for x0 in range(k):
        for choices in product((False,True),repeat=n):
            f=(x0,)+tuple(a if fixed else top for a,fixed in zip(atoms,choices))+(top,)
            if all(le(f[i],f[j]) for i in range(k) for j in range(k) if le(i,j)) and all(f[f[i]]==f[i] for i in range(k)):
                good.append(f)
    def A(mask):
        return (0,)+tuple(i if mask & (1 << (i-1)) else top for i in atoms)+(top,)
    def B(i):
        return (i,)+tuple(j if j==i else top for j in atoms)+(top,)
    C=(top,)*k
    expected={A(mask) for mask in range(1<<n)}|{B(i) for i in atoms}|{C}
    assert set(good)==expected,(n,len(good),len(expected))
    def compose(f,g):return tuple(f[g[i]] for i in range(k))
    def commute(f,g):return compose(f,g)==compose(g,f)
    count=sum(commute(f,g) for f in good for g in good)
    assert count==4**n+(n+2)*2**n+(n+1)**2,(n,count)
    assert sum(not commute(A(mask),B(i)) for mask in range(1<<n) for i in atoms)==n*2**(n-1)
    fs=[]
    for subset in range(1<<n):
        F={A(mask) for mask in range(1<<n) if (mask & subset)==subset}|{B(i) for i in atoms if subset&(1<<(i-1))}|{C}
        assert all(commute(f,g) for f in F for g in F)
        assert all(any(not commute(x,f) for f in F) for x in expected-F)
        fs.append(frozenset(F))
    assert len(set(fs))==(1<<n)
    return n,len(good),count,len(fs),max(map(len,fs))

if __name__=='__main__':
    for n in range(2,9):
        print(*verify(n))
    print('VERIFY_OK')

# Supplementary independent verification of all-arity enumerator; the
# identity below uses the exact combinatorial inclusion-exclusion formula.
def tuple_count_formula(n, k):
    from math import comb
    return sum(comb(n,h)*sum((-1)**(h-j)*comb(h,j)*(2**(n-h)+1+j)**k
                             for j in range(h+1)) for h in range(n+1))

def tuple_count_direct(n,k):
    top=n+1
    def A(mask): return (0,)+tuple(i if (mask>>(i-1))&1 else top for i in range(1,top))+(top,)
    def B(i): return (i,)+tuple(j if j==i else top for j in range(1,top))+(top,)
    C=(top,)*(n+2)
    fs=list({A(mask) for mask in range(1<<n)}|{B(i) for i in range(1,top)}|{C})
    good=[[all(f[g[j]]==g[f[j]] for j in range(n+2)) for g in fs] for f in fs]
    count=0
    def dfs(depth,compatible):
        if depth==k:return 1
        return sum(dfs(depth+1,tuple(j for j in compatible if good[i][j])) for i in compatible)
    return dfs(0, tuple(range(len(fs))))

if __name__=='__main__':
    for n,k in [(2,0),(2,3),(2,4),(3,3),(3,4),(4,3),(4,4),(5,3),(6,3)]:
        x=tuple_count_formula(n,k); y=tuple_count_direct(n,k)
        assert x==y,(n,k,x,y)
        print('tuples',n,k,x)
    print('TUPLES_VERIFY_OK')
