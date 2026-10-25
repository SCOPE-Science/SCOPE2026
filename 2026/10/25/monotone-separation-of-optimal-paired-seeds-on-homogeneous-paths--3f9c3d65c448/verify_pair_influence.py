#!/usr/bin/env python3
"""Exact, self-contained finite checks for two-seed influence on paths."""
import itertools
import json
from fractions import Fraction
from collections import Counter


def add_poly(*polys):
    n = max(map(len, polys))
    return tuple(sum(a[j] if j < len(a) else 0 for a in polys) for j in range(n))


def influence_poly(n, u, v):
    assert 0 <= u < v < n
    c = [0] * n
    for w in range(n):
        du, dv = abs(w-u), abs(w-v)
        c[du] += 1
        c[dv] += 1
        c[max(du,dv)] -= 1  # On a path, the union of the two routes to w has max length.
        # NOTE: For w outside [u,v], union has max length, inside it has v-u.
        if u < w < v:
            c[max(du,dv)] += 1
            c[v-u] -= 1
    return tuple(c)


def gap_poly(n, b):
    assert 1 <= b <= n-1
    tail = n-1-b
    a, c = tail//2, (tail+1)//2
    res = [0]*n
    res[0] = 2
    for j in range(1,a+1): res[j] += 1
    for j in range(1,c+1): res[j] += 1
    for j in range(1,b): res[j] += 2
    res[b] -= (b-1)
    return tuple(res)


def value(coeff, p):
    return sum((c*p**i for i,c in enumerate(coeff)), Fraction(0))


def direct_spread(n, u, v, p):
    E = n-1
    s = Fraction(0)
    for mask in range(1<<E):
        x = mask.bit_count()
        w = p**x*(1-p)**(E-x)
        seen = set((u,v))
        for root in (u,v):
            lo = root
            while lo>0 and (mask>>(lo-1))&1:
                lo -= 1
            hi = root
            while hi<n-1 and (mask>>hi)&1:
                hi += 1
            seen.update(range(lo,hi+1))
        s += w*len(seen)
    return s


def delta_sign(n,b,p):
    h = (n-1-b+1)//2
    return p**b*(1+b*(1-p)) - p**h


def main():
    polynomial_checks = 0
    symmetry_checks = 0
    for n in range(2,25):
        for u,v in itertools.combinations(range(n),2):
            c = influence_poly(n,u,v)
            b = v-u
            balanced = gap_poly(n,b)
            if u == (n-1-b)//2 or u == (n-b)//2:
                assert c == balanced, (n,u,v,c,balanced)
                symmetry_checks += 1
            # Same gap: moving an endpoint tail toward balance cannot lose spread.
            for p in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
                assert value(c,p) <= value(balanced,p)
                polynomial_checks += 1
        for b in range(1,n-1):
            f, g = gap_poly(n,b),gap_poly(n,b+1)
            diff = tuple(g[i]-f[i] for i in range(n))
            expected = [0]*n
            h = (n-b)//2
            expected[b] += b+1
            expected[b+1] -= b
            expected[h] -= 1
            assert diff == tuple(expected), (n,b,diff,expected)
            polynomial_checks += 1
    direct_cases = 0
    for n in range(2,11):
        for u,v in itertools.combinations(range(n),2):
            coeff = influence_poly(n,u,v)
            for p in (Fraction(1,3),Fraction(1,2),Fraction(2,3)):
                assert value(coeff,p) == direct_spread(n,u,v,p),(n,u,v,p)
                direct_cases += 1
    optimal_cases = 0
    transition_checks = 0
    for n in range(2,70):
        N=n-1
        ps=[Fraction(j,20) for j in range(1,20)]+[Fraction(99,100),Fraction(999,1000)]
        last_lower = -1
        for p in ps:
            vs = [value(gap_poly(n,b),p) for b in range(1,n)]
            best=max(vs)
            winners=[b for b,val in enumerate(vs,1) if val==best]
            assert max(winners)-min(winners) <= 1
            assert min(winners)>=last_lower
            last_lower=min(winners)
            for b in range(1,n-1):
                gap_difference=vs[b]-vs[b-1]
                assert gap_difference == delta_sign(n,b,p)
                transition_checks += 1
            optimal_cases += 1
    # Fully explicit n=4 transition and source sets.
    assert gap_poly(4,2) == (2,3,-1,0)
    assert gap_poly(4,3) == (2,2,2,-2)
    assert value(gap_poly(4,2),Fraction(1,4)) > value(gap_poly(4,3),Fraction(1,4))
    assert value(gap_poly(4,2),Fraction(1,2)) == value(gap_poly(4,3),Fraction(1,2))
    assert value(gap_poly(4,2),Fraction(3,4)) < value(gap_poly(4,3),Fraction(3,4))
    result = {
        'status':'PASS',
        'path_orders_checked':list(range(2,70)),
        'exact_direct_edge_state_checks':direct_cases,
        'balanced_polynomial_identity_cases':symmetry_checks,
        'fixed_gap_balancing_comparisons':polynomial_checks,
        'optimal_gap_rational_cases':optimal_cases,
        'adjacent_gap_exact_rational_checks':transition_checks,
        'smallest_switching_path_vertices':4,
        'four_vertex_interior_threshold':'1/2',
        'method':'exact rational arithmetic and exhaustive Bernoulli edge-state enumeration; unrestricted proof is algebraic'
    }
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__': main()
