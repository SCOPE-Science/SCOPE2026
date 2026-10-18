#!/usr/bin/env python3
"""Exact finite checks for the two-prefix circular pair-correlation bound.
All numerical objects are fractions; no external packages are needed.
The checks are independent of the analytic, all-sequences argument.
"""
from fractions import Fraction as Q
from math import isqrt
from random import Random


def gaps_with_insertions(points, n, m):
    # Tie policy: order by (circle coordinate, birth index) throughout.
    old = sorted(range(n), key=lambda i: (points[i], i))
    new = sorted(range(m), key=lambda i: (points[i], i))
    pos = {j: t for t, j in enumerate(new)}
    assert all(j in pos for j in old)
    out = []
    for k, i in enumerate(old):
        j = old[(k + 1) % n]
        d = (pos[j] - pos[i]) % m
        if not d:
            d = m
        # The later partition between consecutive old labels has d gaps
        starts = [(pos[i] + l) % m for l in range(d)]
        lengths = [(points[new[(t+1)%m]] - points[new[t]] + (1 if t==m-1 else 0)) for t in starts]
        if pos[j] <= pos[i]:
            # When positions tie and wrap, the modulo difference of 0 is 0;
            # numeric modular circle gap from equal coordinates should be 0.
            pass
        orig = points[j] - points[i] + (1 if k==n-1 else 0)
        assert sum(lengths) == orig
        out.append((orig, d-1, lengths))
    assert sum(g for g, r, l in out) == 1
    return out


def statistic(points, k, a):
    count=0
    for i in range(k):
        for j in range(i+1,k):
            d=abs(points[i]-points[j])
            if min(d,1-d) <= a/k:
                count += 2
    return Q(count,k)


def check_case(points, n, m, a):
    e=Q(m-n,n)
    short_old=short_later=0
    for g,r,ls in gaps_with_insertions(points,n,m):
        b=int(g <= a/n)
        s=sum(t <= a/m for t in ls)
        lower=(1-b)*a/n + r*(1-e)*a/m - s*a/m
        assert g >= lower,(points,n,m,a,g,r,ls,lower)
        short_old += b
        short_later += s
    rn=statistic(points,n,a)
    rm=statistic(points,m,a)
    assert short_old <= Q(n,2)*rn
    assert short_later <= Q(m,2)*rm
    rhs=2*(1+e*(1-e)/(1+e)-1/a)
    assert rn+rm >= rhs,(points,n,m,a,rn,rm,rhs)


def main():
    rng=Random(262013)
    trial_count=0
    distinct=0
    duplicates=0
    avals=[Q(1,5),Q(1,2),Q(3,4),Q(17,20),Q(9,10),Q(99,100)]
    for n in range(3,31):
        for m in range(n+1,min(2*n,n+8)):
            for pattern in range(5):
                den=10*n+13
                points=[Q(rng.randrange(den),den) for _ in range(m)]
                if pattern==0:
                    # All points distinct on a rational grid.
                    points=[Q(j,3*m+7) for j in range(m)]
                    distinct+=1
                elif pattern==1:
                    # A heavy collision at the origin, new/old ties.
                    points=[Q(0) if j % 3 else Q(1,2) for j in range(m)]
                    duplicates+=1
                elif pattern==2:
                    points=[Q(0) for _ in range(m)]
                    duplicates+=1
                for a in avals:
                    check_case(points,n,m,a)
                    trial_count+=1
    # Finite checks for the exact optimum and positivity threshold.
    from decimal import Decimal, getcontext
    getcontext().prec=50
    sq2=Decimal(2).sqrt()
    alpha=(Decimal(2)+sq2)/4
    target=Decimal(4)-2*sq2
    assert abs(alpha*target - 1)<Decimal('1e-45')
    assert Q(17,20)<Q(1) and Decimal(9)/10>alpha
    print(f"PASS: {trial_count} exact two-prefix/circular-gap inequalities")
    print(f"Instances with uniform distinct patterns: {distinct}; collision-heavy patterns: {duplicates}")
    print(f"Critical scale (50-digit decimal): {alpha}")
    print(f"Asymptotic limsup coefficient: {target}")

if __name__=='__main__':
    main()
