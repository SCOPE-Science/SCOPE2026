"""Exact finite verification of common-noise affine coalescence for several bases.

The all-time theorem is proved analytically; finite checks are diagnostic only.
Run: python verify.py
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def update(x, branch, base):
    if branch == 0:
        return (base * x) % 1
    return (x + branch - 1) / base


def exact_first_hit(x, y, base, p, horizon):
    q = 1 - p
    active = {(x, y): Fraction(1)}
    hits = []
    for _ in range(1, horizon + 1):
        new = defaultdict(Fraction)
        hit = Fraction(0)
        for (a, b), weight in active.items():
            for branch in range(base + 1):
                prob = p if branch == 0 else q / base
                aa = update(a, branch, base)
                bb = update(b, branch, base)
                if aa == bb:
                    hit += weight * prob
                else:
                    new[(aa, bb)] += weight * prob
        hits.append(hit)
        active = new
    return hits


def ballot(k, n, p):
    if n < k or (n-k) % 2:
        return Fraction(0)
    u = (n+k)//2
    return Fraction(k, n) * comb(n, u) * p**u * (1-p)**(n-u)


def run():
    count = 0
    for base in (2, 3, 4, 6):
        horizon = 7 if base < 4 else (6 if base == 4 else 5)
        for x in (Fraction(1,7),Fraction(3,11)):
            for k in (1,2,3):
                y = x + Fraction(1,base**k)
                assert y < 1
                for p in (Fraction(2,5),Fraction(1,2),Fraction(3,5)):
                    got = exact_first_hit(x, y, base, p, horizon)
                    for n, val in enumerate(got, 1):
                        expected = ballot(k,n,p)
                        assert val == expected,(base,x,k,p,n,val,expected)
                        count+=1
        # A reduced denominator not dividing a power of the base cannot coalesce.
        forbidden_denom = 5 if base == 6 else 7
        x=Fraction(1,9)
        y=x+Fraction(1,forbidden_denom)
        assert y<1
        for p in (Fraction(2,5),Fraction(3,5)):
            assert all(h == 0 for h in exact_first_hit(x,y,base,p,min(horizon,6)))
            count+=min(horizon,6)
    # Composite base: 1/2 has minimal 6-adic depth one, not a power-of-6 denominator.
    for p in (Fraction(2,5), Fraction(1,2), Fraction(3,5)):
        got=exact_first_hit(Fraction(1,7),Fraction(1,7)+Fraction(1,2),6,p,5)
        for n,val in enumerate(got,1):
            assert val == ballot(1,n,p)
            count+=1
    print(f'PASS: {count} exact rational comparisons across bases 2, 3, 4, and 6.')

if __name__ == '__main__':
    run()
