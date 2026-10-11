#!/usr/bin/env python3
"""Exact checks of Steinberg-projector endpoint formulas (standard Python only)."""
from fractions import Fraction
from itertools import product


def irred_counts(q, n):
    # Counts all monic irreducibles of degree d (including the polynomial X at d=1).
    v = {}
    for d in range(1, n + 1):
        v[d] = (q ** d - sum(e * v[e] for e in range(1, d) if d % e == 0)) // d
    if n >= 1:
        v[1] -= 1
    return v


def independent_class_sum(q, n):
    # Sum class contributions using semisimple rational canonical types;
    # coefficients are exact fractions. Each irreducible polynomial is a factor.
    coeff = [Fraction(1)] + [Fraction(0)] * n
    for d, num in irred_counts(q, n).items():
        local = [Fraction(0)] * (n + 1)
        local[0] = Fraction(1)
        w = Fraction(1)
        for m in range(1, n // d + 1):
            w /= q ** (d * m) - 1
            local[d * m] = w
        for _ in range(num):
            coeff = [sum(coeff[k] * local[s-k] for k in range(s+1)) for s in range(n+1)]
    return coeff[n]


def formula(q, n):
    coeff = Fraction(1)
    total = coeff
    for j in range(1, n // 2 + 1):
        coeff *= Fraction(q ** (2*j-2) - q, q ** (2*j) - 1)
        total += coeff
    return total


def normalize(v, p):
    for t in v:
        if t % p:
            m = pow(t, -1, p)
            return tuple(x*m % p for x in v)
    raise ValueError('zero vector')


def is_invertible(g, p, d):
    a = [list(g[i*d:(i+1)*d]) for i in range(d)]
    for i in range(d):
        pivot = next((j for j in range(i, d) if a[j][i] % p), None)
        if pivot is None:
            return False
        a[i], a[pivot] = a[pivot], a[i]
        inv = pow(a[i][i], -1, p)
        for j in range(i+1, d):
            factor = a[j][i]*inv % p
            for k in range(i, d):
                a[j][k] = (a[j][k] - factor*a[i][k]) % p
    return True


def explicit_flags(q, d):
    assert d in (2,3) and q in (2,3)
    points = sorted({normalize(v, q) for v in product(range(q), repeat=d) if any(v)})
    planes = points if d == 3 else []
    flags = [(x,f) for x in points for f in planes if sum(a*b for a,b in zip(x,f)) % q == 0]
    sg = 0
    total = 0
    hist = {}
    for g in product(range(q), repeat=d*d):
        if not is_invertible(g, q, d):
            continue
        total += 1
        # Left-action on point columns and right-action on dual row vectors.
        lp = {v for v in points if normalize(tuple(sum(g[i*d+j]*v[j] for j in range(d))%q for i in range(d)),q) == v}
        if d == 2:
            st = len(lp)-1
        else:
            pf = {f for f in planes if normalize(tuple(sum(f[i]*g[i*d+j] for i in range(d))%q for j in range(d)),q) == f}
            st = 1 - len(lp) - len(pf) + sum(1 for x,f in flags if x in lp and f in pf)
        hist[st] = hist.get(st,0)+1
        sg += abs(st)
    avg = Fraction(sg, total)
    return avg,total,hist


def check():
    count=0
    for q in (2,3,4,5):
        for n in range(0,9):
            a,b=independent_class_sum(q,n),formula(q,n)
            assert a==b,(q,n,a,b)
            count+=1
    explicit=[]
    for q,d in ((2,2),(3,2),(2,3),(3,3)):
        a,g,h=explicit_flags(q,d)
        assert a==formula(q,d),(q,d,a,formula(q,d))
        explicit.append((q,d,g,str(a),h))
    print('VERIFY_OK class_sum_parameters=%d explicit_GL=%s'%(count,str(explicit)))


if __name__=='__main__':check()
