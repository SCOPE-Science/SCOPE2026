#!/usr/bin/env python3
"""Exact standalone volume and convexity checks for complete-multipartite Lipschitz balls.

Requires only the Python standard library. Ehrhart interpolation uses independent
integer-point enumeration of network-difference polyhedra; it does not invoke
the slice-volume decomposition.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, factorial


def volume_formula(parts, t):
    t = Fraction(t)
    N = sum(parts)
    x = t - 1
    v = Fraction(N)
    for s in parts:
        if s < 2:
            continue
        integral = Fraction(0)
        # Substitute r=1+u, 2-r=1-u, then integrate a polynomial.
        for j in range(s - 1):
            for ell in range(N - s + 1):
                integral += Fraction(comb(s - 2, j) * comb(N - s, ell) * (-1)**ell, j + ell + 1) * x**(j + ell + 1)
        v += s * (s - 1) * integral
    return v


def endpoint_formula(parts):
    N = sum(parts)
    v = Fraction(N)
    for s in parts:
        if s > 1:
            v += Fraction(N * sum(comb(N - 1, j) for j in range(s - 1)), comb(N, s))
    return v


def ehrhart_volume(parts, t):
    """Independent exact leading Ehrhart coefficient for a rational metric."""
    t = Fraction(t)
    N = sum(parts)
    d = N - 1
    b = t.denominator
    group = [i for i, a in enumerate(parts) for _ in range(a)]

    def lattice_count(m):
        y = [0] * N
        def go(i):
            if i == N:
                return 1
            low, high = -2*b*m, 2*b*m
            for j in range(i):
                limit = t.numerator*m if group[j] == group[i] else b*m
                low = max(low, y[j]-limit)
                high = min(high, y[j]+limit)
            if low > high:
                return 0
            ans = 0
            for value in range(low, high+1):
                y[i] = value
                ans += go(i+1)
            return ans
        return go(1)

    values = [lattice_count(m) for m in range(d+1)]
    # Every vertex is integral after scaling by b: constraint matrix is
    # a directed-graph incidence matrix, hence totally unimodular.
    leading_difference = sum((-1)**(d-j)*comb(d,j)*values[j] for j in range(d+1))
    return Fraction(leading_difference, factorial(d)*b**d)


def partitions(total, pieces, minimum=1):
    if pieces == 1:
        if total >= minimum:
            yield (total,)
    else:
        for n in range(minimum, total-pieces+2):
            for rest in partitions(total-n, pieces-1, n):
                yield (n,)+rest


def majorizes(x,y):
    a=sorted(x,reverse=True)
    b=sorted(y,reverse=True)
    return a!=b and all(sum(a[:j])>=sum(b[:j]) for j in range(1,len(x)))


def run():
    poly_cases = [
        ((2,2),Fraction(3,2)), ((2,2),Fraction(2)),
        ((3,1,1),Fraction(3,2)), ((3,1,1),Fraction(2)),
        ((2,2,1),Fraction(3,2)), ((2,2,1),Fraction(2)),
        ((3,2),Fraction(3,2)), ((3,2),Fraction(2)),
        ((2,1,1),Fraction(3,2)), ((2,1,1),Fraction(2)),
    ]
    for part,t in poly_cases:
        lhs=ehrhart_volume(part,t)
        rhs=volume_formula(part,t)
        assert lhs==rhs, (part,t,lhs,rhs)
    endpoints=0
    strict_pairs=0
    for N in range(3,15):
        for k in range(2,N+1):
            ps=list(partitions(N,k))
            for p in ps:
                assert volume_formula(p,2)==endpoint_formula(p)
                endpoints+=1
            for p,q in combinations(ps,2):
                if majorizes(p,q):
                    assert volume_formula(p,Fraction(3,2))>volume_formula(q,Fraction(3,2))
                    assert volume_formula(p,2)>volume_formula(q,2)
                    strict_pairs+=1
                elif majorizes(q,p):
                    assert volume_formula(q,Fraction(3,2))>volume_formula(p,Fraction(3,2))
                    assert volume_formula(q,2)>volume_formula(p,2)
                    strict_pairs+=1
    assert volume_formula((1,1,1,1),2)==4
    assert volume_formula((2,2),1)==4
    print(f'EXACT_MULTIPARTITE_VOLUME_PASS ehrhart={len(poly_cases)} endpoints={endpoints} majorization_pairs={strict_pairs}')

if __name__ == '__main__':
    run()
