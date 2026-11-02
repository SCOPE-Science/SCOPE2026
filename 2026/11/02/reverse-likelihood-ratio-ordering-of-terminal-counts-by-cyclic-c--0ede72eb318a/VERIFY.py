"""Exact arithmetic checks for cyclic-core/terminal-count likelihood-ratio ordering.

Run: python VERIFY.py
The infinite theorem depends on its paper proof, not on this finite test.
"""
from collections import Counter
from itertools import product
from math import comb, factorial

checks = 0

def assert_equal(a,b):
    global checks
    assert a == b, (a,b)
    checks += 1

def assert_true(a, details=''):
    global checks
    assert a, details
    checks += 1


def stir(N, r, q, memo={}):
    if q<r or q>N or r<0: return 0
    if N==r: return int(q==r)
    if N==0: return int(q==0)
    key=N,r,q
    if key not in memo:
        memo[key]=q*stir(N-1,r,q)+stir(N-1,r,q-1)
    return memo[key]

def ncounts(n,m):
    t=n-m
    if t==0:return {0:1}
    return {z:factorial(t)//factorial(z)*stir(n-1,m,n-z) for z in range(1,t+1)}

# Verify normalized conditional law, deletion formula and row log-concavity.
for n in range(2,39):
    for m in range(1,n+1):
        t=n-m
        zlaw=ncounts(n,m)
        assert_equal(sum(zlaw.values()),n**max(t-1,0))
        if t:
            for z in range(1,t+1):
                iz=comb(t,z)*sum((-1)**j*comb(t-z,j)*(n-z-j)**(t-1)
                                   for j in range(t-z+1))
                assert_equal(zlaw[z],iz)
        if m>=2 and t>=1:
            for q in range(m,n):
                assert_equal(stir(n-1,m,q),
                             stir(n-1,m-1,q)-(m-1)*stir(n-2,m-1,q))
    for r in range(1,n):
        N=n-1
        for q in range(r+1,N):
            assert_true(stir(N,r,q)**2 >= stir(N,r,q-1)*stir(N,r,q+1))
    # Every reverse 2x2 minor of the conditional law, including support zeros.
    cs={k:ncounts(n,k) for k in range(1,n+1)}
    for k in range(1,n):
        for z in range(0,n-1):
            a=cs[k].get(z,0)
            b=cs[k].get(z+1,0)
            c=cs[k+1].get(z,0)
            d=cs[k+1].get(z+1,0)
            # if k rises, Z shifts down: a*d <= b*c
            assert_true(a*d <= b*c,(n,k,z,a,b,c,d))

# All separated two-by-two minors, not only adjacent ones.
for n in range(2,18):
    count_rows={m:ncounts(n,m) for m in range(1,n+1)}
    for low in range(1,n):
        for high in range(low+1,n+1):
            for z1 in range(0,n):
                for z2 in range(z1+1,n):
                    aa=count_rows[low].get(z1,0)
                    bb=count_rows[low].get(z2,0)
                    cc=count_rows[high].get(z1,0)
                    dd=count_rows[high].get(z2,0)
                    assert_true(aa*dd <= bb*cc,(n,low,high,z1,z2))

# Enumerate all maps independently through n=6, identify directed cyclic vertices.
def cyc_count(mp):
    cyc=set()
    for start in range(len(mp)):
        position={}
        v=start
        while v not in position:
            position[v]=len(position)
            v=mp[v]
        cyc.update([w for w,p in position.items() if p>=position[v]])
    return len(cyc)

for n in range(2,7):
    table=Counter()
    for mp in product(range(n),repeat=n):
        indeg=[0]*n
        for j in mp: indeg[j]+=1
        table[cyc_count(mp),indeg.count(0)]+=1
    for m in range(1,n+1):
        t=n-m
        c=ncounts(n,m)
        # total mappings with cyclic vertex set size m is (n)_m * m / n^{m+1} * n^n.
        total=m*factorial(n)//factorial(n-m)*n**(n-m-1) if m<n else factorial(n)
        if m==n: total=factorial(n)
        assert_equal(sum(table[m,z] for z in range(n+1)),total)
        if m<n:
            assert_equal(total % n**(t-1),0)
            scale=total//n**(t-1)
        else:scale=total
        for z in range(n+1):
            assert_equal(table[m,z],scale*c.get(z,0))

print('PASS: %d exact checks; mapping enumeration through n=6; adjacent reverse-TP2 through n=38, all minors through n=17.'%checks)
