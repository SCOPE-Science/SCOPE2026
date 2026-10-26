#!/usr/bin/env python3
"""Independent exact checks of the three-consecutive-pentagonal semigroup theorem.

No external libraries. Dijkstra computes every Apéry representative exactly;
the second route applies the three-generator symmetry criterion to pairs.
"""
import heapq
from math import gcd


def pentagonal(n):
    return n * (3*n - 1) // 2


def triple(n):
    return tuple(pentagonal(j) for j in (n, n+1, n+2))


def coin_member(v, x, y):
    # Exhaustive: every nonnegative representation has 0 <= i <= v//x.
    for i in range(v//x + 1):
        if (v-i*x) % y == 0:
            return True
    return False


def criterion(n):
    a,b,c=triple(n)
    assert gcd(gcd(a,b),c)==1
    # Embedding dimension two: one generator belongs to the other two's monoid.
    if coin_member(c,a,b) or coin_member(b,a,c):
        return True
    # The smaller generator a cannot be made from b,c.
    gens=(a,b,c)
    for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
        d=gcd(gens[i],gens[j])
        if d>1 and coin_member(gens[k], gens[i]//d, gens[j]//d):
            return True
    return False


def apery(n):
    a,b,c=triple(n)
    INF=10**40
    dist=[INF]*a
    dist[0]=0
    heap=[(0,0)]
    while heap:
        val,r=heapq.heappop(heap)
        if val!=dist[r]:
            continue
        for step in (b,c):
            new_r=(r+step)%a
            new_val=val+step
            if new_val<dist[new_r]:
                dist[new_r]=new_val
                heapq.heappush(heap,(new_val,new_r))
    assert INF not in dist
    assert (2*sum(dist)-a*(a-1))%(2*a)==0
    genus=(2*sum(dist)-a*(a-1))//(2*a)
    frob=max(dist)-a
    return genus, frob


def verify():
    candidate=[]
    for n in range(2,100):
        g,f=apery(n)
        sym=2*g==f+1
        assert sym==criterion(n), (n,g,f,sym)
        if sym:
            candidate.append((n,g,f))
    assert candidate==[(2,22,43),(3,67,133),(5,850,1699),(40,129265,258529)], candidate
    # Check the inequalities used for the infinite tail from n=100 onward:
    # a>35(3n+1), c>35(3n+4), c<2a, 2c<3a.
    for n in range(100,3001):
        a,b,c=triple(n)
        assert a>35*(3*n+1)
        assert c>35*(3*n+4)
        assert c<2*a and 2*c<3*a
        assert gcd(a,b)<=2 and gcd(b,c)<=2 and 35%gcd(a,c)==0
        assert not criterion(n), n
    print("VERIFY_OK: n=2..99 independently Apéry/genus and gluing; exceptions: "+repr(candidate)+"; n=100..3000 no gluing, exact inequalities")

if __name__=='__main__':
    verify()
