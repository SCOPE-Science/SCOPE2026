"""Exact integer verification for degree ratios of odd biisotropic Grassmannians.
Run: python3 verify.py. Uses only the Python standard library.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial


def add(P, Q):
    R = defaultdict(int, P)
    for mon, c in Q.items():
        R[mon] += c
    return {m: c for m, c in R.items() if c}


def mul(P, Q):
    R = defaultdict(int)
    for m, c in P.items():
        for n, d in Q.items():
            R[tuple(m[i] + n[i] for i in range(3))] += c*d
    return {m: c for m, c in R.items() if c}


one = {(0, 0, 0): 1}
x = {(1, 0, 0): 1}
y = {(0, 1, 0): 1}
z = {(0, 0, 1): 1}
H = add(add(x, y), z)
P = one
for pair in (add(x, y), add(x, z), add(y, z)):
    P = mul(P, mul(pair, pair))
Vand = mul(mul(add(x, {k: -v for k, v in y.items()}),
               add(x, {k: -v for k, v in z.items()})),
           add(y, {k: -v for k, v in z.items()}))


def schur_ssyt(shape):
    cells = [(r, c) for r in range(3) for c in range(shape[r])]
    out = defaultdict(int)
    for vals in product((1, 2, 3), repeat=len(cells)):
        a = dict(zip(cells, vals))
        if any((c > 0 and a[r, c-1] > a[r, c]) or
               (r > 0 and (r-1, c) in a and a[r-1, c] >= a[r, c])
               for r, c in cells):
            continue
        counts = tuple(vals.count(i) for i in (1, 2, 3))
        out[counts] += 1
    return dict(out)


parts = ((4,2,0), (4,1,1), (3,3,0), (3,2,1), (2,2,2))
coefficients = (1,1,1,2,1)
SchurP = {}
for shape, c in zip(parts, coefficients):
    SchurP = add(SchurP, {m: c*v for m,v in schur_ssyt(shape).items()})
assert P == SchurP, 'Schur expansion failed'


def f_standard(rows):
    if any(q < 0 for q in rows):
        return 0
    assert rows[0] >= rows[1] >= rows[2]
    N = sum(rows)
    num = factorial(N)
    for i in range(3):
        for j in range(i+1, 3):
            num *= rows[i] - rows[j] + j-i
    den = factorial(rows[0]+2)*factorial(rows[1]+1)*factorial(rows[2])
    assert num % den == 0
    return num // den


def degree_coefficient(n):
    R = 2*n-2
    d = 6*(n-2)
    target = (R+2,R+1,R)
    T = mul(P,Vand)
    result = 0
    for mon,c in T.items():
        a = tuple(target[i] - mon[i] for i in range(3))
        if min(a) < 0 or sum(a) != d:
            continue
        result += c*factorial(d)//(factorial(a[0])*factorial(a[1])*factorial(a[2]))
    return result


def degree_schur(n):
    R = 2*n-2
    G = f_standard((R-2,R-2,R-2))
    X = sum(c*f_standard((R-part[2],R-part[1],R-part[0]))
            for part,c in zip(parts,coefficients))
    return X,G


def ratio_closed(n):
    R = 2*n-2
    return Fraction(8*(8*R**3-24*R**2+10*R+15), R*(R+1)*(R+2))


for n in range(3,13):
    D,G = degree_schur(n)
    assert D == degree_coefficient(n), (n,D,degree_coefficient(n))
    assert Fraction(D,G) == ratio_closed(n), n
    assert 1 < Fraction(D,G) < 64 <= 2**(6*(n-2))
    print(f'n={n}, complex_dimension={6*(n-2)}, degree_X={D}, degree_Y={G}, ratio={Fraction(D,G)}')
print('PASS: Schur identity, two independent degree methods, closed rational ratio and obstruction inequalities')

# Polynomial identities, checked coefficient by coefficient for every R.
# Lists encode polynomials in R in ascending degree, without CAS packages.
def polyadd(*polys):
    z = [0]*max(map(len, polys))
    for p in polys:
        for i, v in enumerate(p):
            z[i] += v
    while len(z) > 1 and z[-1] == 0:
        z.pop()
    return z


def polyk(p, k):
    return [k*v for v in p]


def polymul(*polys):
    z = [1]
    for p in polys:
        w = [0]*(len(z)+len(p)-1)
        for i, x in enumerate(z):
            for j, y in enumerate(p):
                w[i+j] += x*y
        z = w
    return z


r = [0, 1]
r1, r2, rm1, rm2, rm3 = [1, 1], [2, 1], [-1, 1], [-2, 1], [-3, 1]
den = polymul(r, r1, r2)
num_from_schur = polyadd(
    polyk(polymul(r, rm3, rm2), 27),
    polyk(polymul(r2, rm3, rm2), 10),
    polyk(polymul(r, rm2, rm1), 10),
    polyk(polymul(r, r2, rm2), 16),
    den,
)
num_closed = polyk([15,10,-24,8], 8)
assert num_from_schur == num_closed, (num_from_schur, num_closed)
assert polyadd(num_closed, polyk(den, -1)) == polymul([3], rm2, [-5,3], [4,7])
assert polyadd(polyk(den, 64), polyk(num_closed, -1)) == polyk(polymul([-1,2], [5,8]), 24)
print('PASS: exact rational identity and both strict bounds certified as polynomial identities')
