#!/usr/bin/env python3
"""Exact integer-lattice verification of a one-cross-edge metric deformation.

Run: python3 research23_volume_check.py
No external libraries. Computes Ehrhart leading coefficients by integer
range-state enumeration; this does not replace the analytic all-size proof.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, factorial

@lru_cache(None)
def extrema_states(num, radius):
    c = Counter()
    for vals in product(range(-radius, radius+1), repeat=num):
        c[min(vals), max(vals)] += 1
    return c

def lattice_count(p, q, h, radius):
    assert p >= 2 and q >= 2 and h in (1,2,3)
    us = extrema_states(p-1,radius)
    vs = extrema_states(q-1,radius)
    ans = 0
    for (umin,umax), n in us.items():
        for (vmin,vmax), m in vs.items():
            lo = max(-h*radius, vmax-umin-radius)
            hi = min(h*radius, vmin-umax+radius)
            if lo <= hi:
                ans += n*m*(hi-lo+1)
    return ans

def predicted_volume(p,q,h):
    d = p+q-1
    return Fraction(2**d*factorial(p-1)*factorial(q-1)*p*q,
                    factorial(d)) + Fraction(2*factorial(p-1)*factorial(q-1),factorial(d))*(2**d-(3-h)**d)

def ehrhart_volume(p,q,h):
    d=p+q-1
    values=[lattice_count(p,q,h,k) for k in range(d+1)]
    leading = sum((-1)**(d-k)*comb(d,k)*v for k,v in enumerate(values))
    return Fraction(leading, factorial(d)),values

def main():
    checks=0
    for p,q in [(2,2),(2,3),(3,2),(2,4),(3,3),(3,4),(4,3),(4,4),(3,5),(5,3),(5,4)]:
        for h in (1,2,3):
            v,seq=ehrhart_volume(p,q,h)
            expected=predicted_volume(p,q,h)
            assert v==expected,(p,q,h,v,expected,seq)
            checks+=1
    print(f'PASS exact Ehrhart-leading-coefficient checks: {checks}')
    for p,q in [(2,2),(3,4),(4,4),(5,3)]:
        print(f'p={p} q={q}: volumes h=1,2,3: '+', '.join(str(predicted_volume(p,q,h)) for h in (1,2,3)))
    print('PASS all checks')

if __name__ == '__main__':
    main()

def rational_height_check(p,q,s,r):
    """Lattice dilation by s clears the rational exceptional edge r/s."""
    assert s >= 1 and s <= r <= 3*s
    d=p+q-1
    totals=[]
    for k in range(d+1):
        radius=s*k
        us=extrema_states(p-1,radius)
        vs=extrema_states(q-1,radius)
        ans=0
        for (umin,umax),nu in us.items():
            for (vmin,vmax),nv in vs.items():
                lo=max(-r*k,vmax-umin-radius)
                hi=min(r*k,vmin-umax+radius)
                if lo<=hi:ans+=nu*nv*(hi-lo+1)
        totals.append(ans)
    lead=sum((-1)**(d-k)*comb(d,k)*v for k,v in enumerate(totals))
    actual=Fraction(lead,s**d*factorial(d))
    expected=predicted_volume(p,q,Fraction(r,s))
    assert actual==expected,(p,q,s,r,actual,expected)
    return (p,q,Fraction(r,s),actual)

if __name__=='__main__':
    cases=[(2,2,2,3),(2,3,2,3),(3,2,2,5),(3,3,2,5),(2,4,2,5),(3,4,2,3)]
    for case in cases:
        print('rational height PASS',rational_height_check(*case))
