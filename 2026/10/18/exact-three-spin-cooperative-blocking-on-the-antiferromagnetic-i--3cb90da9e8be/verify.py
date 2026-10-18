"""Finite checks of the exact cooperative-metastability census of an antiferromagnetic Ising wheel.
Run with Python 3, no external dependencies. Finite checks corroborate the separate all-size proof.
"""
from itertools import combinations, product
from collections import Counter
from math import comb, isclose, log


def energy(s):
    hub, rim = s[0], s[1:]
    n = len(rim)
    return sum(rim[i] * rim[(i + 1) % n] for i in range(n)) + hub * sum(rim)


def min_flip_cost(s, max_size):
    base = energy(s)
    worst = 10**10
    for k in range(1, max_size + 1):
        for vertices in combinations(range(len(s)), k):
            flipped = list(s)
            for v in vertices:
                flipped[v] = -flipped[v]
            worst = min(worst, energy(flipped) - base)
    return worst


def predicted(s):
    h, x = s[0], s[1:]
    n = len(x)
    if any(x[i] == h and (x[(i - 1) % n] == h or x[(i + 1) % n] == h)
           for i in range(n)):
        return False, False
    if any(x[(i - 1) % n] == x[i] == x[(i + 1) % n] == -h
           for i in range(n)):
        return False, False
    obstruction = any(x[(i - 2) % n] == x[(i - 1) % n] == -h
                      and x[i] == h
                      and x[(i + 1) % n] == x[(i + 2) % n] == -h
                      for i in range(n))
    return True, not obstruction


def formula(n, order):
    pol = Counter()
    for m in range((n + 2) // 3, n // 2 + 1):
        j = n - 2*m
        if order == 3:
            if 2*j > m:
                continue
            top = 2*n*comb(m-j, j)
            den = m-j
        else:
            top = 2*n*comb(m,j)
            den = m
        assert top % den == 0
        pol[m] += top // den
    return +pol


def from_rational_generator(nmax, order):
    # Expand 2(2*y*z^2 + 3*y*z^3)/(1-y*z^2-y*z^3)
    # or 2(2*y*z^2 + 5*y^2*z^5)/(1-y*z^2-y^2*z^5).
    if order == 3:
        steps = ((2, 1), (5, 2))
    else:
        steps = ((2, 1), (3, 1))
    den_inverse = [Counter() for _ in range(nmax+1)]
    den_inverse[0][0] = 1
    for n in range(1, nmax+1):
        for shift, degree in steps:
            if n >= shift:
                for m, a in den_inverse[n-shift].items():
                    den_inverse[n][m+degree] += a
    out = [Counter() for _ in range(nmax+1)]
    for n in range(1, nmax+1):
        for shift, degree in steps:
            if n>=shift:
                for m, a in den_inverse[n-shift].items():
                    out[n][m+degree] += 2*shift*a
    return out


def root_of(characteristic):
    lo, hi = 1.0, 2.0
    for _ in range(90):
        mid = (lo+hi)/2
        if characteristic(mid)<0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def main():
    checks=0
    for n in range(5,13):
        direct1, direct2, direct3 = Counter(),Counter(),Counter()
        for s in product((-1,1),repeat=n+1):
            p1,p3=predicted(s)
            c1=min_flip_cost(s,1)>=0
            c2=min_flip_cost(s,2)>=0
            c3=min_flip_cost(s,3)>=0
            assert p1==c1 and c2==c1 and p3==c3, (n,s,p1,p3,c1,c2,c3)
            m=sum(v==s[0] for v in s[1:])
            if c1: direct1[m]+=1
            if c2: direct2[m]+=1
            if c3: direct3[m]+=1
            checks+=3
        assert direct1==formula(n,1)==direct2
        assert direct3==formula(n,3)
        print('n',n,'one/two',sum(direct1.values()),'three',sum(direct3.values()),'three-polynomial',dict(sorted(direct3.items())))
    for order in (1,3):
        generators=from_rational_generator(150,order)
        for n in range(5,151):
            assert generators[n]==formula(n,order), (n,order)
            checks+=1
    a=root_of(lambda x:x**3-x-1)
    b=root_of(lambda x:x**5-x**3-1)
    assert 1<a<2 and 1<b<a
    assert abs(a**3-a-1)<1e-12
    assert abs(b**5-b**3-1)<1e-12
    print('growth bases',f'{a:.15f}',f'{b:.15f}')
    print('entropy densities',f'{log(a):.15f}',f'{log(b):.15f}')
    print('entropy gap',f'{log(a/b):.15f}')
    print('checked direct configurations and rational-coefficient identities:',checks)


if __name__ == '__main__':
    main()
