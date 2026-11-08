#!/usr/bin/env python3
"""Exact rational checks of the three regimes and section return law."""
from fractions import Fraction as Q
from random import Random


def F(d, v):
    x, y = v
    return ((1+y, Q(0)) if x <= 0 else (1+y, -d*x))


def iterate(d,v,n):
    for _ in range(n):
        v=F(d,v)
    return v


def right4(d, u):
    v=(u,Q(0))
    q=[v]
    for _ in range(4):
        v=F(d,v); q.append(v)
    return q


def verify():
    rng=Random(31812)
    steps=0
    for d in [Q(11,10), Q(6,5), Q(3,2), Q(2), Q(7,3), Q(5)]:
        c=(d-1)/d**2
        b=1/d
        star=1/(d+1)
        E=(star,-d*star)
        C=right4(d,Q(1))[:4]
        P=right4(d,star)[:4]
        assert iterate(d,E,1)==E
        assert iterate(d,C[0],4)==C[0]
        assert len(set(C))==4
        assert iterate(d,P[0],4)==P[0]
        assert len(set(P))==4
        assert (1-d,0) in C
        for j in range(80):
            u=Q(rng.randint(1,2000),2000)*b
            if c<u<b:
                path=right4(d,u)
                assert path[2][0]>0 and path[3][0]<0
                assert path[4]==(1-d+d*d*u,Q(0))
                assert c<star<b
            # exact random initial points with bounded rational denominators
            v=(Q(rng.randint(-25,25),rng.randint(1,9)),Q(rng.randint(-25,25),rng.randint(1,9)))
            found=False
            for i in range(500):
                if v in C or v in P or v == E:
                    found=True;break
                v=F(d,v)
            assert found,(d,v)
            steps+=i
        for n in range(8):
            lo=star+d**(-2*n)*(c-star)
            hi=star+d**(-2*n)*(b-star)
            assert hi-lo == d**(-2*n-2)
            for u in (lo,lo+(hi-lo)/Q(5),lo+Q(4)*(hi-lo)/Q(5)):
                v=(u,Q(0))
                for j in range(n):
                    assert c < v[0] < b, (d,n,j,v)
                    v=iterate(d,v,4)
                assert lo <= u <= hi
    for d in [Q(1,2), Q(3,4), Q(9,10)]:
        E=(1/(1+d),-d/(1+d))
        for _ in range(100):
            v=(Q(rng.randint(-200,200),rng.randint(1,15)),Q(rng.randint(-200,200),rng.randint(1,15)))
            for i in range(100):
                x,y=v
                if 0 < x <= 1 and -d <= y <= 0:break
                v=F(d,v)
            else:raise AssertionError(('not in invariant rectangle',d,v))
            assert F(d,E)==E
            steps+=i
    d=Q(1)
    for _ in range(300):
        v=(Q(rng.randint(-500,500),rng.randint(1,15)),Q(rng.randint(-500,500),rng.randint(1,15)))
        for i in range(20):
            x,y=v
            if 0<=x<=1 and -1<=y<=0:break
            v=F(d,v)
        else:raise AssertionError(('not in square',v))
        assert iterate(d,v,2)==(1-v[0],-1-v[1])
        assert iterate(d,v,4)==v
        steps+=i
    print('TRACE_FREE_BORDER_COLLISION_EXACT_CHECK_OK; total_tested=1080; accumulated_steps=',steps)

if __name__=='__main__':verify()
