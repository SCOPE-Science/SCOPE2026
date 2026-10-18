"""Exact small-field checks for gcd-degree statistics of polynomial product collisions.
Run: python3 checker.py. Requires only the Python standard library.
The field with four elements is represented by F_2[z]/(z^2+z+1).
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product


def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def mul_scalar(x, y, q):
    if q != 4:
        return x * y % q
    res = 0
    for i in range(2):
        if (y >> i) & 1:
            res ^= x << i
    if res & 8:
        res ^= 9
    if res & 4:
        res ^= 7
    return res


def neg(x, q):
    return x if q == 4 else (-x) % q


def inv(x, q):
    if q == 4:
        return {1: 1, 2: 3, 3: 2}[x]
    return pow(x, -1, q)


def trim(f):
    while len(f) > 1 and f[-1] == 0:
        f = f[:-1]
    return tuple(f)


def poly_mul(f, g, q):
    ans = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            ans[i+j] = add(ans[i+j], mul_scalar(x,y,q), q)
    return trim(ans)


def rem(f, g, q):
    f = list(f)
    inverse = inv(g[-1],q)
    while len(f) >= len(g):
        z = mul_scalar(f[-1], inverse, q)
        shift = len(f) - len(g)
        for j, y in enumerate(g):
            f[shift+j] = add(f[shift+j], neg(mul_scalar(z,y,q),q), q)
        while f and f[-1] == 0:
            f.pop()
    return tuple(f) if f else (0,)


def gcd(f, g, q):
    while g != (0,):
        f,g = g, rem(f,g,q)
    inverse = inv(f[-1],q)
    return tuple(mul_scalar(x,inverse,q) for x in f)


def polys(q,d):
    return [tuple(cs)+(1,) for m in range(d+1) for cs in product(range(q),repeat=m)]


def exhaustive(q,d):
    P=polys(q,d)
    prod_groups=defaultdict(list)
    for f in P:
        for g in P:
            prod_groups[poly_mul(f,g,q)].append((f,g))
    H=Counter()
    for group in prod_groups.values():
        for f1,f2 in group:
            for f3,f4 in group:
                a=len(gcd(f1,f3,q))-1
                b=len(gcd(f2,f4,q))-1
                H[a,b] += 1
    for a in range(d+1):
        for b in range(d+1):
            expected=(q**(2*d+1-abs(a-b))-q**(a+b))//(q-1)
            assert H[a,b] == expected, (q,d,a,b,H[a,b],expected)
    total=sum(H.values())
    numer=(d+1)*(q*q-1)*q**(2*d+1)-3*q**(2*d+2)+4*q**(d+1)-1
    assert total*(q-1)**3 == numer, (q,d,total)
    print('EXHAUSTIVE_OK q=%d d=%d tuples=%d monic_polys=%d'%(q,d,total,len(P)))


def total_variation(q,d):
    total=sum((q**(2*d+1-abs(a-b))-q**(a+b))//(q-1)
              for a in range(d+1) for b in range(d+1))
    c=Fraction(q-1,q+1)
    observed=Fraction(0)
    for a in range(d+1):
        for b in range(d+1):
            n=(q**(2*d+1-abs(a-b))-q**(a+b))//(q-1)
            observed += abs(Fraction(n,total) - c/Fraction((d+1)*q**abs(a-b)))
    omitted_mass=Fraction(0)
    for a in range(d+1):
        omitted_mass += c*(Fraction(1,q**a)+Fraction(1,q**(d-a)))/Fraction((d+1)*(q-1))
    return (observed+omitted_mass)/2


def crosschecks():
    cases=[(2,0),(2,1),(2,2),(2,3),(2,4),
           (3,0),(3,1),(3,2),(3,3),
           (4,0),(4,1),(4,2),
           (5,0),(5,1),(5,2)]
    for q,d in cases:
        exhaustive(q,d)
    for q in [2,3,4,5,7]:
        for d in [0,1,2,3,5,10,20]:
            tv=total_variation(q,d)
            bound=Fraction(3*q,(q*q-1)*(d+1))
            assert tv<=bound,(q,d,tv,bound)
        print('TV_BOUND_OK q=%d degrees=0,1,2,3,5,10,20'%q)
    for q in [2,3,4,5,7]:
        for d in [5,10,50,100]:
            numerator=(d+1)*(q*q-1)*q**(2*d+1)-3*q**(2*d+2)+4*q**(d+1)-1
            E=numerator//(q-1)**3
            assert numerator%(q-1)**3==0
            computed=sum((q**(2*d+1-abs(a-b))-q**(a+b))//(q-1)
                         for a in range(d+1) for b in range(d+1))
            assert E==computed
    print('ALL_EXACT_CHECKS_PASSED')

if __name__ == '__main__':
    crosschecks()
