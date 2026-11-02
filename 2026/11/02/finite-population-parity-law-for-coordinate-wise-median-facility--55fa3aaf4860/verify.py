"""Exact-rational validation of the finite-size Chebyshev-plane median frontier.

Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import comb
from random import Random


def lower_median(a):
    a = sorted(a)
    return a[(len(a)-1)//2]


def cheb(a,b):
    return max(abs(a[0]-b[0]),abs(a[1]-b[1]))


def costs(points):
    x = lower_median(p[0] for p in points)
    y = lower_median(p[1] for p in points)
    cm = sum(cheb(p,(x,y)) for p in points)
    # 45-degree rotation: max(|a|,|b|) = (|a+b|+|a-b|)/2.
    plus = [p[0]+p[1] for p in points]
    minus = [p[0]-p[1] for p in points]
    mplus = lower_median(plus)
    mminus = lower_median(minus)
    optimum = Q(sum(abs(v-mplus) for v in plus)
                +sum(abs(v-mminus) for v in minus),2)
    return Q(cm),optimum


def bound(n):
    return Q(2) if n%2==0 else Q(2*n,n+1)


def witness(n):
    k=n//2
    return ([(-1,-1)]*(k-1)+[(-1,1)]+[(0,0)]*k
            if n%2==0 else
            [(-1,-1)]*k+[(-1,1)]+[(0,0)]*k)


def main():
    grid=[(x,y) for x in (-1,0,1) for y in (-1,0,1)]
    total=0
    for n in range(2,11):
        exact_max=Q(0)
        for ids in combinations_with_replacement(range(len(grid)),n):
            pts=[grid[i] for i in ids]
            cm,opt=costs(pts)
            if opt:
                assert cm <= bound(n)*opt,(n,pts,cm,opt)
                exact_max=max(exact_max,cm/opt)
            else:
                assert cm==0
            total+=1
        assert exact_max==bound(n),(n,exact_max,bound(n))
        w=witness(n)
        cm,opt=costs(w)
        assert cm==n and opt==(n+1)//2 if n%2 else cm==n and opt==n//2
        assert cm==bound(n)*opt
        print('n',n,'profiles',comb(n+8,8),'sharp_factor',str(bound(n)))
    print('Exhaustive lattice multisets checked:',total)
    rng=Random(20261030)
    trials=7500
    for _ in range(trials):
        n=rng.randrange(2,31)
        pts=[(rng.randrange(-100,101),rng.randrange(-100,101)) for _ in range(n)]
        cm,opt=costs(pts)
        assert opt==0 and cm==0 or cm<=bound(n)*opt
    print('Seeded random integer profiles checked:',trials)
    pairs=0
    for k in range(1,9):
        r=Q(2*k+1,k+1)
        for tt in range(11):
            t=Q(tt,10)
            c=r-1+t
            a=r+(2-r)*t
            b=2*t
            for ix in range(-10,11):
                for iy in range(-10,11):
                    x=Q(ix,5);y=Q(iy,5)
                    f=r*max(abs(x-1),abs(y-t))-max(abs(x),abs(y))
                    assert f >= c-(a if x>0 else 0)-(b if y>0 else 0)
                    pairs+=1
    print('Pointwise dual certificate finite rational checks:',pairs)
    print('ALL CHECKS PASS')

if __name__=='__main__':
    main()
