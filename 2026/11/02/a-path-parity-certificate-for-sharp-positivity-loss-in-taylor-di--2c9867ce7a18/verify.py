"""Exact rational checks for the sharp graph-Taylor positivity theorem.

Usage: python verify.py
Standard-library only. Finite tests illustrate, but do not replace, the general proof.
"""
from fractions import Fraction as F
from math import factorial
from collections import deque


def zero(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def ident(n):
    out = zero(n)
    for i in range(n):
        out[i][i] = F(1)
    return out


def mul(a, b):
    n = len(a)
    out = zero(n)
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    if b[k][j]:
                        out[i][j] += a[i][k] * b[k][j]
    return out


def add_scaled(a, b, c):
    return [[a[i][j] + c*b[i][j] for j in range(len(a))]
            for i in range(len(a))]


def cycle(n, rate=F(1)):
    a = zero(n)
    for i in range(n):
        a[i][(i+1) % n] += rate
        a[i][(i-1) % n] += rate
    return a


def directed_cycle(n, rate=F(1)):
    a = zero(n)
    for i in range(n):
        a[i][(i+1) % n] += rate
    return a


def cube(rates):
    n = 1 << len(rates)
    a = zero(n)
    for i in range(n):
        for b, rate in enumerate(rates):
            a[i][i^(1 << b)] = F(rate)
    return a


def biclique(n):
    a = zero(2*n)
    for i in range(n):
        for j in range(n,2*n):
            a[i][j] = a[j][i] = F(1)
    return a


def taylor_update(a, s, h):
    n = len(a)
    d = sum(a[0])
    assert d > 0 and all(sum(row)==d for row in a)
    q = [[a[i][j] - (d if i==j else F(0)) for j in range(n)] for i in range(n)]
    power = ident(n)
    out = zero(n)
    for k in range(s+1):
        out = add_scaled(out,power,h**k/F(factorial(k)))
        power=mul(power,q)
    return out


def shortest_path_distance(a, src, dst):
    seen={src}
    q=deque([(src,0)])
    while q:
        u,r=q.popleft()
        if u==dst:
            return r
        for v,x in enumerate(a[u]):
            if x>0 and v not in seen:
                seen.add(v)
                q.append((v,r+1))
    return None


def verify_one(label,a,s):
    n=len(a)
    d=sum(a[0])
    assert all(sum(row)==d for row in a)
    # The bipartite examples have a pair at directed/undirected distance s-1.
    pair=next(((i,j) for i in range(n) for j in range(n)
               if shortest_path_distance(a,i,j)==s-1),None)
    assert pair is not None, (label,s)
    i,j=pair
    powers=[ident(n)]
    for _ in range(s):
        powers.append(mul(powers[-1],a))
    assert all(powers[k][i][j]==0 for k in range(s-1))
    assert powers[s-1][i][j]>0
    assert powers[s][i][j]==0
    checks=0
    for x in [F(0),F(1,8),F(1,2),F(3,4),F(1)]:
        p=taylor_update(a,s,x/d)
        assert all(v>=0 for row in p for v in row), (label,s,x)
        assert all(sum(row)==1 for row in p), (label,s,x)
        assert p[i][j]==(x/d)**(s-1)*powers[s-1][i][j]/factorial(s-1)*(1-x)
        checks+=3
    for x in [F(101,100),F(6,5),F(2)]:
        p=taylor_update(a,s,x/d)
        assert p[i][j]<0, (label,s,x)
        assert all(sum(row)==1 for row in p)
        assert p[i][j]==(x/d)**(s-1)*powers[s-1][i][j]/factorial(s-1)*(1-x)
        checks+=3
    return checks


def main():
    graphs=[
        ('cycle-8',cycle(8)),('cycle-10',cycle(10)),
        ('cycle-12',cycle(12)),('cycle-8-weighted',cycle(8,F(3,7))),
        ('bipartite-3-3',biclique(3)),
        ('cube-4',cube([F(1,2),F(2,3),F(3,4),F(5,6)])),
        ('directed-cycle-8',directed_cycle(8,F(3,5))),
    ]
    total=0;cases=0
    for name,a in graphs:
        n=len(a)
        dist=max(shortest_path_distance(a,i,j) or 0 for i in range(n) for j in range(n))
        for s in range(2,min(dist+2,7)):
            total+=verify_one(name,a,s)
            cases+=1
    # Dimension gap: K2 has no pair at distance 3 and RK4 exceeds Euler's CFL.
    a=cycle(2) if False else [[F(0),F(1)],[F(1),F(0)]]
    p=taylor_update(a,4,F(6,5))
    assert all(v>=0 for row in p for v in row)
    assert all(sum(row)==1 for row in p)
    total+=2
    print(f'VERIFY_OK cases={cases} exact_assertion_groups={total}')

if __name__=='__main__':
    main()
