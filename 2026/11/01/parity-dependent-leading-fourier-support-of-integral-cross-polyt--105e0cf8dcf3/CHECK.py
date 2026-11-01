"""Exact independent arithmetic residue checker for integer-frequency cross-polytopes.
Standard-library only; execute python CHECK.py.  Finite tests corroborate, not replace, the proof.
"""
from collections import Counter
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product


def multiply(a, b, cap):
    c = [Q(0)] * (cap+1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i+j <= cap:
                c[i+j] += ai*bj
    return c


def residue_polynomial(k):
    """Return P(q)=sum residues exp(qz) z^(n-1)/prod(z²-k_j²), q=2 pi i.
    At integer poles exp(q a)=1; rational coefficients of P in powers of q.
    """
    n = len(k)
    masses = Counter()
    for v in k:
        masses[int(v)] += 1
        masses[-int(v)] += 1
    out = [Q(0)] * (max(masses.values()))
    for a, m in masses.items():
        degree = m-1
        poly = [Q(0)]*(degree+1)
        for j in range(degree+1):
            if j <= n-1:
                poly[j] = Q(comb(n-1,j) * a**(n-1-j))
        for b, mb in masses.items():
            if b == a:
                continue
            d = a-b
            series = [Q((-1)**j*comb(mb+j-1,j),d**(mb+j)) for j in range(degree+1)]
            poly = multiply(poly, series,degree)
        for j in range(degree+1):
            out[degree-j] += poly[j] / factorial(degree-j)
    return tuple(out)


def expected_poly(k):
    n = len(k)
    counts = Counter(map(abs,k))
    target = 2 if n%2 else 3
    pattern = sorted(counts.values(),reverse=True)
    if pattern != [target]+[1]*(n-target) or 0 in counts:
        return None
    a = next(x for x,m in counts.items() if m==target)
    den = 1
    for b,m in counts.items():
        if b != a:
            den *= (a*a-b*b)
    # F(k) = C / q^(n-(target-1)); F=2^n P(q)/q^n.
    # Therefore P(q) = C*q^(target-1)/2^n.
    if n%2:
        val = Q(a**(n-3), 2*den)
    else:
        val = Q(a**(n-4), 8*den)
    return target-1,val


def check():
    tests=0
    cases=[
        (1,1,2),(1,1,2,3,4),(2,2,1,3,5,7,9),
        (1,1,1,2),(1,1,1,2,3,4),
        (2,2,2,1,3,4,5,6),
        (1,2,3),(0,1,2),(0,0,1),(0,0,1,2),
        (1,1,2,2),(1,1,2,2,3,3),(0,0,1,1,2,2),
        (1,2,3,4,5,6),(1,1,2,3,4,5),
    ]
    for k in cases:
        if len(k) < 3: continue
        p=residue_polynomial(k)
        exp=expected_poly(k)
        if exp is not None:
            power, coefficient=exp
            assert len(p)>power and p[power] == coefficient and all(c==0 for i,c in enumerate(p) if i!=power), (k,p,exp)
        elif (len(k)%2 and len(set(map(abs,k)))==len(k)) or (len(k)%2==0 and max(Counter(map(abs,k)).values())<=2):
            assert all(x==0 for x in p),(k,p)
        tests +=1
    for n in (3,4,5,6):
        for k in product(range(3),repeat=n):
            p=residue_polynomial(k)
            counts=Counter(map(abs,k))
            if n%2 and len(counts)==n:
                assert all(x==0 for x in p),(k,p)
            if not n%2 and max(counts.values())<=2:
                assert all(x==0 for x in p),(k,p)
            tests += 1
    print('EXACT_RESIDUE_TESTS_OK',tests)

if __name__ == '__main__': check()
