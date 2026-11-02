"""Independent finite-field interpolation checks for the double Eckardt scheme.

Run: python3 verify.py. The infinite theorem is proved by ideal identities
and the uniform-matroid Cohen--Macaulay property; these tests do not replace it.
"""
from itertools import combinations
from collections import defaultdict


def exponents(d):
    return [(a, b, c, d-a-b-c)
            for a in range(d+1) for b in range(d-a+1)
            for c in range(d-a-b+1)]


def rank(rows, p):
    pivots = {}
    for raw in rows:
        v = [x % p for x in raw]
        while True:
            z = next((j for j, x in enumerate(v) if x), None)
            if z is None:
                break
            if z not in pivots:
                k = pow(v[z], -1, p)
                pivots[z] = [(x*k) % p for x in v]
                break
            w = pivots[z]
            c = v[z]
            v[z:] = [(u-c*x) % p for u, x in zip(v[z:], w[z:])]
    return len(pivots)


def multiply(f, g, p):
    h = defaultdict(int)
    for a, c in f.items():
        for b, d in g.items():
            h[tuple(x+y for x,y in zip(a,b))] += c*d
    return {e: v % p for e, v in h.items() if v % p}


def ideal_rows(gens, d, monomials, p):
    for g in gens:
        gd = sum(next(iter(g)))
        if d < gd:
            continue
        for shift in exponents(d-gd):
            yield [g.get(tuple(x-y for x,y in zip(e,shift)),0)
                   if all(x>=y for x,y in zip(e,shift)) else 0
                   for e in monomials]


def first_jets(points, monomials, p):
    # Four first partials plus values; including values handles degrees divisible by p.
    for point in points:
        for variable in range(5):
            out=[]
            for e in monomials:
                if variable < 4 and e[variable] == 0:
                    out.append(0)
                    continue
                v = e[variable] if variable < 4 else 1
                for j in range(4):
                    z = e[j] - (j == variable)
                    v = v * pow(point[j], z, p) % p
                out.append(v)
            yield out


def run_prime(p):
    assert p > 3 and p % 3 == 1
    roots=[r for r in range(p) if (r**3+1) % p == 0]
    assert len(roots)==3
    points=[]
    for i,j in combinations(range(4),2):
        for r in roots:
            v=[0]*4; v[i]=1;v[j]=r
            points.append(tuple(v))
    assert len(points)==18 and len(set(points))==18
    F={tuple(3*(j==i) for j in range(4)):1 for i in range(4)}
    J=[{tuple(int(j!=i) for j in range(4)):1} for i in range(4)]
    G=[F]+J
    Q={(1,1,1,1):1}
    I2=[multiply(g,h,p) for k,g in enumerate(G) for h in G[k:]]
    target=[1,4,10,20,34,52,65,72,72]
    print(f'prime={p}; roots={roots}; geometric Eckardt points={len(points)}')
    for degree in range(4,9):
        mon=exponents(degree)
        n=len(mon)
        symbolic=n-rank(first_jets(points,mon,p),p)
        constructed=rank(ideal_rows(I2+[Q],degree,mon,p),p)
        expected=n-target[degree]
        assert symbolic==constructed==expected, (p,degree,symbolic,constructed,expected)
        if degree==6:
            ordinary=rank(ideal_rows(I2,degree,mon,p),p)
            assert ordinary==15
            assert constructed==19
        print(f'  degree={degree}; symbolic dimension={symbolic}; generated dimension={constructed}; quotient Hilbert={n-symbolic}')
    print('  VERIFIED')


for p in (7,13,19):
    run_prime(p)
print('VERIFY_OK')
