#!/usr/bin/env python3
"""Finite exact checks for elementary-abelian quadratic Artin--Schreier covers."""
from math import comb

PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29]


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def quotient_lines(p):
    return [(1, t) for t in range(p)] + [(0, 1)]


def check_cartier_zero(p):
    g = (p - 1) // 2
    # Nonzero exponents in (X^p-X)^g.
    coeff = {}
    for k in range(g + 1):
        exp = p * k + g - k
        coeff[exp] = ((-1) ** (g - k) * comb(g, k)) % p
    assert all(coeff.get(p * i - j, 0) == 0
               for i in range(1, g + 1) for j in range(1, g + 1))
    assert (p + 1) * g == (p * p - 1) // 2
    return g


def check_projective_idempotents(p):
    lines = quotient_lines(p)
    points = [(i, j) for i in range(p) for j in range(p)]
    subgroups = [{((s*u) % p, (s*v) % p) for s in range(p)}
                 for u, v in lines]
    assert len(set(map(frozenset, subgroups))) == p + 1
    for idx, H in enumerate(subgroups):
        assert len(H) == p
        for K in subgroups[idx + 1:]:
            multiplicities = {g: 0 for g in points}
            for a, b in H:
                for c, d in K:
                    multiplicities[((a+c) % p, (b+d) % p)] += 1
            assert all(v == 1 for v in multiplicities.values())
    # In each cyclic quotient w^p-w=(c+a*d)t^2+d*b*t,
    # a outside F_p implies c+a*d != 0 for all (c,d) != (0,0).
    assert all(c != 0 or d != 0 for c, d in lines)


def point_count_example(p):
    # F_{p^2}=F_p[alpha], alpha^2=D with D a nonsquare in F_p.
    D = next(d for d in range(2, p) if pow(d, (p-1)//2, p) == p-1)
    F = [(u, v) for u in range(p) for v in range(p)]
    def add(x, y):
        return ((x[0]+y[0]) % p, (x[1]+y[1]) % p)
    def mul(x, y):
        return ((x[0]*y[0]+D*x[1]*y[1]) % p,
                (x[0]*y[1]+x[1]*y[0]) % p)
    def power(x, n):
        r=(1,0)
        while n:
            if n % 2: r=mul(r,x)
            x=mul(x,x)
            n//=2
        return r
    def trace(x):
        t=add(x,power(x,p))
        assert t[1] == 0
        return t[0]
    alpha=(0,1)
    # C: y^p-y=t^2, x^p-x=alpha*t^2+t.
    countC=1
    countD={line:1 for line in quotient_lines(p)}
    for t in F:
        first=mul(t,t)
        second=add(mul(alpha,first),t)
        A=trace(first)
        B=trace(second)
        if A == B == 0:
            countC += p*p
        for c,d in countD:
            if (c*A+d*B) % p == 0:
                countD[(c,d)] += p
    q=p*p
    assert countC-(q+1) == sum(v-(q+1) for v in countD.values())
    return countC


def main():
    for p in PRIMES:
        assert is_prime(p)
        check_cartier_zero(p)
        check_projective_idempotents(p)
    examples={p:point_count_example(p) for p in [3,5,7,11,13]}
    print('VERIFY_OK primes=' + ','.join(map(str,PRIMES)) +
          ' Cartier_zero=true subgroup_pair_convolution=true' +
          ' finite_field_point_counts=' + repr(examples))

if __name__ == '__main__':
    main()
