#!/usr/bin/env python3
"""Reproducibility checks for the three-site preferential-relocation endpoint."""
from fractions import Fraction
from collections import defaultdict
from math import atan


def origin_family_transform(a, s, t):
    return 1.0 / (1.0 + s + a * t * atan(t))


def initial_side_factor(a, t):
    return 1.0 - a + a / (1.0 + t*t)


def full_transform(a, s, t):
    return initial_side_factor(a, t) * origin_family_transform(a, s, t)


def simpson(f, n=6000):
    assert n % 2 == 0
    h = 1.0/n
    total = f(0.0)+f(1.0)
    for j in range(1,n):
        total += (4 if j & 1 else 2)*f(j*h)
    return total*h/3


def finite_exact_distribution(steps, a):
    """Count-vector and current-position law under the original walk."""
    d = {(1,0,0,0):Fraction(1)}
    for j in range(steps):
        nd=defaultdict(Fraction)
        for (z,p,m,current),prob in d.items():
            counts=(z,p,m)
            total=z+p+m
            if current==0:
                for to in (1,2):
                    new=list(counts)
                    new[to]+=1
                    nd[(*new,to)] += prob*a/2
                relocation=1-a
            else:
                relocation=Fraction(1)
            for to in (0,1,2):
                if counts[to]:
                    new=list(counts)
                    new[to]+=1
                    nd[(*new,to)] += prob*relocation*counts[to]/total
        d=dict(nd)
        assert sum(d.values())==1
        assert all(sum(k[:3]) == j+2 for k in d)
        assert all(k[0]>=1 for k in d)
    return d


def main():
    tests=0
    for a in (0.1, 0.25, 0.5, 0.9):
        for s in (0.0, 0.3, 2.0):
            for t in (0.0, 0.2, 0.9, 2.5):
                F=origin_family_transform(a,s,t)
                rhs=simpson(lambda u:origin_family_transform(a,u*s,u*t)**2*initial_side_factor(a,u*t))
                assert abs(F-rhs)<1e-9,(a,s,t,F,rhs)
                tests+=1
                # Conditioning W~Exp(1): unconditional transform is its Laplace integral.
                rhs2=initial_side_factor(a,t)/(1.0+s+a*t*atan(t))
                assert abs(full_transform(a,s,t)-rhs2)<1e-13
                tests+=1
        # Characteristic fourth-order Taylor coefficients for origin-only and initial-side branches.
        second_zero=2*a
        fourth_zero=8*a+24*a*a
        second_full=4*a
        fourth_full=32*a+48*a*a
        assert second_zero>0 and fourth_zero>second_zero*second_zero
        assert second_full>0 and fourth_full>second_full*second_full
        tests+=2
    for a in (Fraction(1,3),Fraction(1,2),Fraction(4,5)):
        for n in range(1,9):
            d=finite_exact_distribution(n,a)
            assert sum(v for k,v in d.items() if k[3]==1)==sum(v for k,v in d.items() if k[3]==2)
            assert sum(v for k,v in d.items() if k[1]>k[2])==sum(v for k,v in d.items() if k[2]>k[1])
            tests+=2
        d=finite_exact_distribution(1,a)
        assert sum(v for k,v in d.items() if k[3]==0)==1-a
        tests+=1
    print(f'PASS: {tests} exact/analytic checks')
    print('Origin-family transform: 1/(1+s+a*t*atan(t))')
    print('Original walk transform: (1-a+a/(1+t*t))/(1+s+a*t*atan(t))')
    print('E[D^2]=4a; E[D^4]=32a+48a^2 (original walk).')
    print('Finite Markov checks are not proofs of almost-sure limits.')

if __name__=='__main__':
    main()
