#!/usr/bin/env python3
"""Direct recurrence census for synchronous majority on cliques minus matchings."""
from collections import Counter
from math import comb

def predicted(m,r):
    n=2*m+r
    assert m>=1 and n>=4
    if n%2==0:
        if r==0:
            return (2+2**m,(comb(n,n//2)-2**m)//2)
        return (2,comb(n,n//2)//2)
    if r==1:
        return (2,comb(m,(m+1)//2))
    if n%4==3 and r<=2*m-1:
        return (2,comb(m,(n+1)//4))
    return (2,0)

def transition(m,r):
    n=2*m+r
    nb=[]
    for i in range(n):
        nb.append(sum(1<<j for j in range(n)
                      if j!=i and not (i<2*m and j==(i^1))))
    deg=[v.bit_count() for v in nb]
    def f(x):
        out=0
        for i,b in enumerate(nb):
            c=(x&b).bit_count()
            if c*2>deg[i] or (c*2==deg[i] and (x>>i)&1):
                out|=1<<i
        return out
    return f

def check(m,r):
    n=2*m+r
    f=transition(m,r)
    N=1<<n
    vals=[f(x) for x in range(N)]
    # The only states on an eventual cycle are fixed or in period 2.
    fixed=sum(vals[x]==x for x in range(N))
    periodic2=sum(vals[vals[x]]==x and vals[x]!=x for x in range(N))//2
    actual=(fixed,periodic2)
    expected=predicted(m,r)
    if actual!=expected:
        raise AssertionError((m,r,actual,expected))
    # Exhaustive transient bound: by time 3 state is periodic.
    for x in range(N):
        a=vals[x];b=vals[a];c=vals[b]
        if vals[vals[c]]!=c:
            raise AssertionError(('transient bound',m,r,x))
    return N

def main():
    checks=0; states=0
    for n in range(4,17):
        for m in range(1,n//2+1):
            r=n-2*m
            states+=check(m,r);checks+=1
    assert checks==sum(n//2 for n in range(4,17))
    # Sharp three-update example within the stated m>=4 range.
    f=transition(5,3)
    x=sum(1<<i for i in list(range(6))+[10])
    trace=[x]
    for _ in range(4):
        x=f(x);trace.append(x)
    assert trace[3]==(1<<13)-1 and trace[2]!=trace[3]
    assert trace[4]==trace[3]
    print('Sharp three-step witness for (m,r)=(5,3):',trace)
    print('PASS',checks,'graph parameter pairs;',states,'configurations examined')
    for m,r in [(2,0),(3,0),(4,0),(2,1),(3,1),(4,1),(4,3),(5,3),(4,5),(7,7),(3,9)]:
        if 2*m+r>=4:
            print('K_%d minus %d-edge matching, r=%d: fixed=%d, two-cycle orbits=%d'
                  %(2*m+r,m,r,*predicted(m,r)))
if __name__=='__main__':main()
