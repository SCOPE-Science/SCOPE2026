"""Exact algebraic and finite-field certificate for the decagonal 61-line divisor.

Python 3, standard library only. Every incidence is recomputed from ten
conic tangents, without data tables of precomputed lines or points.
"""
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
from collections import Counter, defaultdict
from math import gcd, lcm, comb

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
ZETA = (0, 1, 0, 0)

def add(a, b): return tuple(x + y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def sub(a, b): return tuple(x - y for x, y in zip(a, b))
def mul(a, b):
    c = [0] * 7
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): c[i + j] += x * y
    for k in range(6, 3, -1):
        t = c[k]
        if t:
            for j in range(1, 5): c[k - j] -= t
    return tuple(c[:4])
def power(a, e):
    res = ONE
    while e:
        if e & 1: res = mul(res, a)
        a = mul(a, a)
        e >>= 1
    return res

def cross(a, b):
    return (sub(mul(a[1], b[2]), mul(a[2], b[1])),
            sub(mul(a[2], b[0]), mul(a[0], b[2])),
            sub(mul(a[0], b[1]), mul(a[1], b[0])))
def dot(a, b):
    return add(add(mul(a[0], b[0]), mul(a[1], b[1])), mul(a[2], b[2]))

@lru_cache(None)
def inverse(a):
    assert a != ZERO
    columns = [mul(a, tuple(int(i == j) for i in range(4))) for j in range(4)]
    mat = [[Fraction(columns[j][i]) for j in range(4)] +
           [Fraction(int(i == 0))] for i in range(4)]
    for j in range(4):
        r = next(k for k in range(j, 4) if mat[k][j])
        mat[j], mat[r] = mat[r], mat[j]
        d = mat[j][j]
        mat[j] = [v / d for v in mat[j]]
        for k in range(4):
            if k != j:
                d = mat[k][j]
                mat[k] = [x - d * y for x, y in zip(mat[k], mat[j])]
    return tuple(mat[i][4] for i in range(4))

@lru_cache(None)
def normalize(v):
    assert any(a != ZERO for a in v)
    j = next(j for j, a in enumerate(v) if a != ZERO)
    u = inverse(v[j])
    return tuple(mul(a, u) for a in v)

def integral(v):
    flat = [c for a in v for c in a]
    d = lcm(*(c.denominator for c in flat))
    a = [int(c * d) for c in flat]
    g = gcd(*a)
    a = [c // g for c in a]
    return tuple(tuple(a[i:i+4]) for i in (0, 4, 8))

AUT = {k: [power(ZETA, (k * i) % 5) for i in range(4)] for k in range(1, 5)}
def galois(a, k):
    out = ZERO
    for i, v in enumerate(a):
        if v: out = add(out, tuple(v * z for z in AUT[k][i]))
    return out
@lru_cache(None)
def number_norm(a):
    out = ONE
    for k in (1, 2, 3, 4): out = mul(out, galois(a, k))
    assert out[1:] == (0, 0, 0)
    return abs(int(out[0]))

def prime_factors(n):
    out = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.add(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: out.add(n)
    return out

# The regular decagon's side lines are tangents to its incircle.
# A projective diagonal change places those tangents at the tenth roots
# of unity on the rational Veronese conic.
t = neg(power(ZETA, 3))
assert power(t, 10) == ONE
T = [power(t, j) for j in range(10)]
seeds = [(ONE, mul(u, u), neg(mul((2, 0, 0, 0), u))) for u in T]
base_points = {normalize(cross(seeds[i], seeds[j]))
               for i, j in combinations(range(10), 2)}
assert len(base_points) == 45
base_points = sorted(base_points)
secants = {normalize(cross(base_points[i], base_points[j]))
           for i, j in combinations(range(45), 2)}
assert len(secants) == 481
lines = sorted(l for l in secants
               if sum(dot(l, P) == ZERO for P in base_points) >= 3)
assert len(lines) == 61
assert all(normalize(s) in lines for s in seeds)
line_supports = [sum(dot(l, P) == ZERO for P in base_points) for l in lines]
assert Counter(line_supports) == {3: 40, 4: 5, 5: 6, 9: 10}

points = defaultdict(set)
for i, j in combinations(range(61), 2):
    P = normalize(cross(lines[i], lines[j]))
    points[P].update((i, j))
assert len(points) == 551
assert Counter(map(len, points.values())) == {2:335, 3:140, 5:70, 10:1, 12:5}
assert sum(comb(len(v), 2) for v in points.values()) == comb(61, 2)

def conjugate_point(P, k): return normalize(tuple(galois(a, k) for a in P))
pset = set(points)
for k in (1, 2, 3, 4):
    assert {conjugate_point(P, k) for P in pset} == pset
fixed = {k: sum(conjugate_point(P, k) == P for P in pset) for k in (1, 2, 3, 4)}
assert fixed == {1: 551, 2: 7, 3: 7, 4: 27}
orbit_degree = Counter(len({conjugate_point(P, k) for k in (1, 2, 3, 4)}) for P in pset)
assert orbit_degree == {1: 7, 2: 20, 4: 524}
rational_points = {tuple(P[i][0] for i in range(3)):len(v)
                   for P, v in points.items() if all(a[1:] == (0,0,0) for a in P)}
assert rational_points == {
    (1,1,-1):2, (1,1,0):2, (1,1,1):2,
    (1,1,Fraction(-1,2)):5, (1,1,Fraction(1,2)):5,
    (0,0,1):10, (1,-1,0):12}

# Primitive integral cyclotomic representatives and all 35,990 triple
# determinants. Their nonzero algebraic norms control every reduction.
L = [integral(v) for v in lines]
assert all(gcd(*(number_norm(a) for a in line if a != ZERO)) == 1 for line in L)
dnorm = Counter()
num_zero = 0
for i, j, k in combinations(range(61), 3):
    d = dot(L[i], cross(L[j], L[k]))
    if d == ZERO: num_zero += 1
    else: dnorm[number_norm(d)] += 1
assert num_zero == 2060
assert sum(dnorm.values()) == 33930
assert dnorm == {
    1:220, 5:1220, 16:3375, 80:13480, 256:1320,
    400:1160, 1280:5200, 1296:440, 1936:560,
    2000:3680, 4096:105, 5776:120, 6400:80,
    6480:1280, 9680:1160, 10000:40, 20480:200,
    20736:10, 28880:180, 32000:80, 50000:20}
assert set().union(*(prime_factors(n) for n in dnorm)) == {2,3,5,11,19}

# Exceptional specializations: the defining polynomial for the image
# of zeta_5 is irreducible of the indicated degree (except p=5,
# where its sole geometric root is 1). All geometric intersection
# points are computed from pairs of *distinct* reduced lines.
POLYS = {
 2:(1,1,1,1,1), 3:(1,1,1,1,1), 5:(4,1),
 7:(1,1,1,1,1), 11:(8,1), 19:(1,5,1),
 29:(1,6,1), 31:(15,1)}

def finite_census(p):
    coeff = POLYS[p]
    d = len(coeff)-1
    q = p**d
    zero = (0,)*d
    one = (1,)+(0,)*(d-1)
    def addf(a,b): return tuple((x+y)%p for x,y in zip(a,b))
    def subf(a,b): return tuple((x-y)%p for x,y in zip(a,b))
    def mulf(a,b):
        c=[0]*(2*d-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
        for k in range(2*d-2,d-1,-1):
            r=c[k]
            if r:
                for j in range(d): c[k-d+j]=(c[k-d+j]-r*coeff[j])%p
        return tuple(c[:d])
    def powf(a,e):
        out=one
        while e:
            if e&1:out=mulf(out,a)
            a=mulf(a,a)
            e>>=1
        return out
    z=(0,1)+(0,)*(d-2) if d>1 else ((-coeff[0])%p,)
    def evalf(a):
        v=zero
        w=one
        for c in a:
            v=addf(v,mulf((c%p,)+(0,)*(d-1),w))
            w=mulf(w,z)
        return v
    def normf(v):
        ix=next(i for i in range(3) if v[i]!=zero)
        w=powf(v[ix],q-2)
        return tuple(mulf(a,w) for a in v)
    def crossf(a,b):
        return (subf(mulf(a[1],b[2]),mulf(a[2],b[1])),
                subf(mulf(a[2],b[0]),mulf(a[0],b[2])),
                subf(mulf(a[0],b[1]),mulf(a[1],b[0])))
    ls=[]
    for line in L:
        v=tuple(evalf(a) for a in line)
        assert v!=(zero,zero,zero)
        ls.append(normf(v))
    ls=set(ls)
    pts=defaultdict(set)
    for a,b in combinations(ls,2): pts[normf(crossf(a,b))].update((a,b))
    hist=Counter(map(len,pts.values()))
    assert sum(comb(m,2)*c for m,c in hist.items())==comb(len(ls),2)
    rational=sum(normf(tuple(powf(a,p) for a in point))==point for point in pts)
    return len(ls),len(pts),dict(hist),rational

EXCEPT={
 2:(6,6,{2:5,5:1},2),
 3:(51,91,{2:5,5:40,6:40,10:6},5),
 5:(7,7,{2:6,6:1},7),
 11:(61,131,{2:5,5:70,6:50,10:1,12:5},131),
 19:(61,341,{2:65,3:170,4:30,5:70,10:1,12:5},21)}
for p,expect in EXCEPT.items(): assert finite_census(p)==expect,(p,finite_census(p))
for p,nrat in ((7,7),(29,27),(31,551)):
    line_n,geom_n,hist,rational=finite_census(p)
    assert (line_n,geom_n,rational)==(61,551,nrat)
    assert hist == {2:335,3:140,5:70,10:1,12:5}

if __name__=='__main__':
    print('VERIFY_OK: 61 lines, 551 points; 35,990 exact determinant norms; Galois and all exceptional prime profiles')
