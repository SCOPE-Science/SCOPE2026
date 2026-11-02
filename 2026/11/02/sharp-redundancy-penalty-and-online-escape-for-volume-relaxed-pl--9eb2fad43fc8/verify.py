"""Exact-rational supplementary checks for planar block-projection geometry.

Run: python3 verify.py. No external dependencies. The infinite-configuration
claim follows from the proof, not from these finite checks.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def unit(t):
    t = F(t)
    return ((1-t*t)/(1+t*t), 2*t/(1+t*t))


def cross2(u,v):
    return u[0]*v[1]-u[1]*v[0]


def sqdist(u,v):
    return sum((a-b)**2 for a,b in zip(u,v))


def q_data(parameters):
    rows = [unit(t) for t in parameters]
    weights = [cross2(u,v)**2 for u,v in combinations(rows,2)]
    assert min(weights)>0
    peak = max(weights)
    c = len(weights)
    q = sum((F(1)-w/peak for w in weights),F(0))/c
    # The chord embedding identifies 4 times each determinant squared.
    chords = [unit(0)] # placeholder replaced immediately
    chords = [((u[0]*u[0]-u[1]*u[1]), 2*u[0]*u[1]) for u in rows]
    assert [sqdist(u,v) for u,v in combinations(chords,2)] == [4*w for w in weights]
    assert F(0)<=q<F(len(rows)-2,len(rows)-1)
    return q,weights


def invert_two(A):
    a,b=A
    det=cross2(a,b)
    return ((b[1]/det,-a[1]/det),(-b[0]/det,a[0]/det))


def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def main():
    rng=Random(0xC0A5)
    trials=0
    for m in range(3,13):
        for _ in range(150):
            nums=rng.sample(range(-300,301),m)
            params=[F(n,997) for n in nums]
            q_data(params)
            trials+=1
        # Endpoints near opposite phases, other rows concentrated at midpoint.
        for scale in [30,100,1000,10000]:
            t=F(1,scale)
            params=[-t,t]+[F(j,1)*t*t for j in range(1,m-1)]
            q,weights=q_data(params)
            assert weights[0]==max(weights) and weights.count(max(weights))==1
            bound=F(m-2,m-1)
            assert q<bound
            if scale==10000:
                assert bound-q < F(1,1000)
            trials+=1
    # Every full-rank two-row projector equals identity exactly.
    identity=((F(1),F(0)),(F(0),F(1)))
    for _ in range(500):
        a,b=rng.sample(range(-200,201),2)
        A=(unit(F(a,389)),unit(F(b,389)))
        assert matmul(invert_two(A),A)==identity
    # For a 3-row symmetric example, the sharp upper envelope is 1/2.
    q,_=q_data([-F(1,10000),F(0),F(1,10000)])
    assert F(49,100)<q<F(1,2)
    print(f"PASS: {trials} exact-rational geometries, 500 exact inverse tests")
    print("PASS: sharp near-extremizers for every row count 3..12")
    print("PASS: three-row near-extremizer and unique largest-volume pair")

if __name__=='__main__':
    main()
