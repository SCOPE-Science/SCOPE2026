#!/usr/bin/env python3
"""Exact finite verification of the two-agent binary-approval multiplicity law.

Run: python3 verify.py
No third-party packages required. All items have distinct labels.
"""
from collections import Counter
from itertools import product
from math import comb, erf, sqrt
from fractions import Fraction


def formula_count(a, b, c):
    successes = sum(comb(c, t) for t in range(c+1)
                    if abs(a-b-c+2*t) <= 1)
    return successes + (1 if abs(a-b)>c+1 else 0)


def direct_count(profile):
    # Nonshared approved goods have forced destinations; check every split of shared goods.
    a = profile.count(1)
    b = profile.count(2)
    c = profile.count(3)
    scores = []
    for assign in product((0,1), repeat=c):
        k = sum(assign)
        u1, u2 = a+k, b+c-k
        scores.append((min(u1,u2), max(u1,u2)))
    optimal = max(scores)
    return sum(score == optimal for score in scores)



def brute_full_market(profile):
    """Independently try every unassigned/agent-one/agent-two choice for each good."""
    eligible=[]
    for allocations in product((0,1,2), repeat=len(profile)):
        # Code 0=unassigned, 1=agent one, 2=agent two.
        if any((typ==0 and dest!=0) or
               (typ!=0 and dest==0) or
               (dest==1 and not (typ&1)) or
               (dest==2 and not (typ&2))
               for typ,dest in zip(profile,allocations)):
            continue
        u1=sum(dest==1 for dest in allocations)
        u2=sum(dest==2 for dest in allocations)
        eligible.append((min(u1,u2),max(u1,u2)))
    assert eligible
    best=max(eligible)
    return sum(score==best for score in eligible)


def coeff_near_center(m, p):
    # Coefficient sum of z^(-1), z^0, and z^1 in
    # ((1-p)^2+p(z+z^(-1)))^m, with exact rational arithmetic.
    d = (1-p)**2
    f = {0: Fraction(1)}
    for _ in range(m):
        g = {}
        for j, val in f.items():
            for step, weight in ((0,d), (1,p), (-1,p)):
                g[j+step] = g.get(j+step, Fraction())+val*weight
        f = g
    return sum(f.get(j,Fraction()) for j in (-1,0,1))


def exhaustive(m, p):
    weights = ((1-p)**2,p*(1-p),p*(1-p),p*p)
    n_profiles = 0
    total_k = Fraction()
    total_tail = Fraction()
    total_multi = Fraction()
    distribution = Counter()
    for profile in product(range(4),repeat=m):
        a,b,c = profile.count(1),profile.count(2),profile.count(3)
        k = direct_count(profile)
        assert k == formula_count(a,b,c), (m,profile,k,formula_count(a,b,c))
        if m<=4:
            assert brute_full_market(profile)==k, (m,profile,k)
        assert (k>1) == (abs(a-b)<c), (m,profile,k,a,b,c)
        prob = Fraction(1)
        for item in profile:
            prob *= weights[item]
        n_profiles += 1
        distribution[k] += 1
        total_k += k*prob
        total_tail += (abs(a-b)>c+1)*prob
        total_multi += (k>1)*prob
    assert total_k == coeff_near_center(m,p)+total_tail
    assert n_profiles == 4**m
    return n_profiles, total_k, total_multi, distribution


def main():
    p=Fraction(1,2)
    total=0
    for m in range(0,8):
        size, mean, multi, dist = exhaustive(m,p)
        total += size
        print(f'm={m}: {size} profiles; E[K]={mean}; P(K>1)={multi}; multiplicities={dict(sorted(dist.items()))}')
    assert total == sum(4**m for m in range(8)) == 21845
    print(f'Exact direct counts compared to formula on {total} profiles; all passed.')
    print('Additional full-market ternary-allocation enumeration passed on 341 profiles (m<=4).')
    for lam in (Fraction(1,2),Fraction(1),Fraction(2)):
        xf=float(lam)**1.5/2
        print(f'critical lambda={lam}: asymptotic multiple-optimum probability erf({xf:.9g})={erf(xf):.12f}')
    print('PASS')


if __name__=='__main__':
    main()
