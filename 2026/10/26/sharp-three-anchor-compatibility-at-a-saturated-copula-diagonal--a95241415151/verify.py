#!/usr/bin/env python3
"""Exact rational verification of three-anchor copula conditional-CDF constructions.

Each row is (latent probability, (F(a), F(b), F(c))). Such rows determine
an explicit checkerboard input copula by assigning conditional response mass
in four successive threshold bins and making it uniform within each bin.
"""
from fractions import Fraction as F
from random import Random


def moment(rows, index, power=1):
    return sum((w * values[index] ** power for w, values in rows), F(0))


def verify(rows, anchors):
    assert sum((w for w, _ in rows), F(0)) == 1
    for w, v in rows:
        assert w >= 0
        assert all(F(0) <= t <= F(1) for t in v)
        assert list(v) == sorted(v)
    assert all(moment(rows, i) == a for i, a in enumerate(anchors))


def endpoints(a, b, c):
    z = F(1) - a
    alpha, gamma = (b-a)/z, (c-a)/z
    lower = [(a, (F(1), F(1), F(1))),
             (z, (F(0), alpha, gamma))]
    upper = [(a, (F(1), F(1), F(1))),
             (z * (1-c)/(1-b), (F(0), alpha, alpha)),
             (z * (c-b)/(1-b), (F(0), alpha, F(1)))]
    return lower, upper


def sharp_range(a, b, c):
    d = a + (b-a)**2/(1-a)
    low = a + (c-a)**2/(1-a)
    high = c-(b-a)*(1-c)/(1-a)
    return d, low, high


def run():
    rng = Random(16318)
    tests = 0
    for _ in range(400):
        n = rng.randrange(5, 61)
        i, j, k = sorted(rng.sample(range(1, n), 3))
        a, b, c = F(i,n), F(j,n), F(k,n)
        d, low, high = sharp_range(a,b,c)
        lower, upper = endpoints(a,b,c)
        for rows, val in ((lower,low),(upper,high)):
            verify(rows, (a,b,c))
            assert (moment(rows,0,2),moment(rows,1,2),moment(rows,2,2)) == (a,d,val)
            tests += 1
        assert high-low == (c-b)*(1-c)/(1-a)
        assert high > low
        t = F(rng.randrange(101),100)
        mix = [(t*w,v) for w,v in upper] + [((1-t)*w,v) for w,v in lower]
        verify(mix,(a,b,c))
        assert moment(mix,2,2) == (1-t)*low+t*high
        tests += 1

    # Fully explicit rational witness for each pair of the incompatible
    # requested triple D(1/4)=1/4, D(1/2)=1/3, D(3/4)=3/4.
    a,b,c = F(1,4), F(1,2), F(3,4)
    dab = [(F(1,4),(F(1),F(1))),
           (F(3,4),(F(0),F(1,3)))]
    dac = [(F(1,4),(F(1),F(1))),
           (F(1,2),(F(0),F(1))),
           (F(1,4),(F(0),F(0)))]
    dbc = [(F(1,4),(F(0),F(0))),
           (F(3,4),(F(2,3),F(1)))]
    for rows, means, seconds in ((dab,(a,b),(a,F(1,3))),
                                  (dac,(a,c),(a,c)),
                                  (dbc,(b,c),(F(1,3),c))):
        verify(rows,means)
        assert tuple(moment(rows,i,2) for i in range(2)) == seconds
        tests += 1
    assert sharp_range(a,b,c) == (F(1,3),F(7,12),F(2,3))
    assert F(3,4)-F(2,3) == F(1,12)
    tests += 1

    # General pairwise-feasible (but globally impossible) triples. For each
    # rational a<b, choose c=r=b^2/d if r<1; then all pair witnesses exist.
    for _ in range(200):
        den=rng.randrange(4,50)
        ia, ib=sorted(rng.sample(range(1,den),2))
        a,b=F(ia,den),F(ib,den)
        d,_,_=sharp_range(a,b,(b+1)/2)
        c=b*b/d
        assert b<c<1
        r,t=c,d/b
        pair_bc=[(r,(t,F(1))), (F(1)-r,(F(0),F(0)))]
        verify(pair_bc,(b,c))
        assert (moment(pair_bc,0,2),moment(pair_bc,1,2)) == (d,c)
        assert c-sharp_range(a,b,c)[2] == (b-a)*(1-c)/(1-a)>0
        tests+=1

    # Stress-test the additional non-sharp stability bound with exact squares.
    # Select arbitrary conditional posterior pairs B<=C off the first saturated cut.
    for _ in range(500):
        a=F(rng.randrange(1,9), 10)
        z=F(1)-a
        vals=[]
        for j in range(4):
            k=rng.randrange(0,21)
            h=rng.randrange(k,21)
            vals.append((F(k,20),F(h,20)))
        alpha=sum((p[0] for p in vals),F(0))/4
        gamma=sum((p[1] for p in vals),F(0))/4
        if not (F(0)<alpha<gamma<F(1)):
            continue
        b=a+z*alpha
        c=a+z*gamma
        dmin,low,high=sharp_range(a,b,c)
        epsilon=z*(sum((p[0]**2 for p in vals),F(0))/4-alpha**2)
        observed=a+z*sum((p[1]**2 for p in vals),F(0))/4
        if observed>high:
            assert (observed-high)**2 <= epsilon*(c-a)*(1-c)/(1-a)
        tests+=1
    print(f'PASS: {tests} exact-rational construction, moment, interval and incompatibility checks')

if __name__ == '__main__':
    run()
