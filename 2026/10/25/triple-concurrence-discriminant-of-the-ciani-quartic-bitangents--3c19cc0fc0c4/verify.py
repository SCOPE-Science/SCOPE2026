"""Exact incidence check for bitangents of the Ciani quartic pencil.

Run with Python 3 and SymPy. All arithmetic is over Q[t] or Q[lambda].
No floating-point approximation is used; every one of the 3276 unordered
three-line determinants is checked. A nonzero determinant vanishes at a
special parameter precisely when its irreducible factor does.
"""

from collections import Counter, defaultdict
from itertools import combinations
import sympy as S

t, lam = S.symbols('t lam')
D = t*t + 1
A = t*t - 1
C = []

# Four tetrahedral bitangents, represented by integral polynomial triples.
for sign_y in (1, -1):
    for sign_z in (1, -1):
        C.append((D, sign_y*D, sign_z*D))

# Twelve coordinate-pair bitangents (three pairs and four slopes each).
for i, j in combinations(range(3), 2):
    for vi, vj in ((1, t), (1, -t), (t, 1), (t, -1)):
        v = [S.Integer(0)]*3
        v[i], v[j] = vi, vj
        C.append(tuple(v))

# Twelve further bitangents from quadratic square restrictions.
for i in range(3):
    j, k = [h for h in range(3) if h != i]
    for eps in (1, -1):
        for eta in (1, -1):
            v = [S.Integer(0)]*3
            v[i], v[j], v[k] = eta*A, D, eps*D
            C.append(tuple(v))
assert len(C) == 28

param = -2*(t**4+1)/(t*t+1)**2
alpha = A/D
assert S.cancel(param + 1 + alpha**2) == 0
assert S.cancel(param*(t*t+1)**2 + 2*(t**4+1)) == 0

# Check the common four-line bitangent factorization.
x, y, z = S.symbols('x y z')
F = x**4 + y**4 + z**4 + lam*(x*x*y*y + x*x*z*z + y*y*z*z)
P = -(x**4+y**4+z**4) + 2*(x*x*y*y+x*x*z*z+y*y*z*z)
assert S.expand(F - (lam+2)*(x*x+y*y+z*z)**2/4 - (lam-2)*P/4) == 0

# On y = -x-u z, the quartic is even in x+u z/2. Its square condition.
u = S.symbols('u')
R = S.Poly(S.expand(F.subs({x:S.symbols('w')-u/2,
                                  y:-S.symbols('w')-u/2,z:1}, simultaneous=True)),
           S.symbols('w'))
w = S.symbols('w')
r4,r2,r0 = [R.coeff_monomial(w**j) for j in (4,2,0)]
assert S.factor(4*r4*r0-r2*r2 - 4*(lam-2)*(u*u-1)*(lam+u*u+1)) == 0


def determinant(i,j,k):
    a,b,c=C[i],C[j],C[k]
    return S.Poly(S.expand(a[0]*(b[1]*c[2]-b[2]*c[1])-
                           a[1]*(b[0]*c[2]-b[2]*c[0])+
                           a[2]*(b[0]*c[1]-b[1]*c[0])), t)

zero_triples = set()
factors = defaultdict(set)
for ijk in combinations(range(28),3):
    q = determinant(*ijk)
    if q.is_zero:
        zero_triples.add(ijk)
    else:
        for ff, power in S.factor_list(q.as_expr(),t)[1]:
            p = S.Poly(ff,t).monic()
            factors[tuple(p.all_coeffs())].add(ijk)
assert len(zero_triples) == 36
assert len(factors) == 45
assert len(zero_triples) + 3240 == 3276


def incidence(triples):
    """Find all intersection points as maximal sets of incident lines."""
    points=set()
    for i,j in combinations(range(28),2):
        point=frozenset((i,j)) | frozenset(k for k in range(28)
                         if k not in (i,j) and tuple(sorted((i,j,k))) in triples)
        points.add(point)
    assert sum(len(p)*(len(p)-1)//2 for p in points) == 378
    return Counter(map(len,points))

assert incidence(zero_triples) == {2:324,4:9}

# Each factor in Q[t] maps to a unique irreducible factor in Q[lambda].
rel = lam*D**2 + 2*(t**4+1)
parameter_groups = defaultdict(list)
for key, extra in factors.items():
    f = S.Poly.from_list(list(key),gens=t).monic()
    res = S.resultant(f.as_expr(),rel,t)
    nonconstant = [S.Poly(g,lam).monic() for g,_ in S.factor_list(res,lam)[1]]
    if not nonconstant:
        assert S.expand(f.as_expr() - (t*t+1)) == 0
        continue
    assert len(nonconstant) == 1
    parameter_groups[tuple(nonconstant[0].all_coeffs())].append((f,extra))
assert len(parameter_groups) == 16

P4 = [lam+5]
P12 = [25*lam+34, lam+10, lam**2-lam+2,
       lam**3+2*lam**2+4*lam+4,
       lam**3-4*lam**2+13*lam+34]
P24 = [5*lam+6, lam**2+3*lam+6,
       lam**3+13*lam**2+64*lam+68,
       lam**3-2*lam**2+60*lam+72,
       lam**4-lam**3+10*lam**2+4*lam+8]
P0=[lam]
P21=[lam**2+3*lam+18]
Psingular=[lam+2,lam+1,lam-2]

expected={}
for polynomials, counts in [
    (P4,{2:312,3:4,4:9}),
    (P12,{2:288,3:12,4:9}),
    (P24,{2:252,3:24,4:9}),
    (P0,{2:288,4:15}),
    (P21,{2:252,4:21}),
    (Psingular,None),
]:
    for p in polynomials:
        key=tuple(S.Poly(p,lam).monic().all_coeffs())
        assert key not in expected
        expected[key]=counts
assert set(expected)==set(parameter_groups)

smooth_polynomials=P4+P12+P24+P0+P21
assert sum(S.degree(p,lam) for p in smooth_polynomials)==27
for p in smooth_polynomials:
    assert S.gcd(S.Poly(p,lam),S.Poly(S.diff(p,lam),lam)).degree() == 0
    assert S.gcd(S.Poly(p,lam),S.Poly((lam+2)*(lam+1)*(lam-2),lam)).degree()==0
for p,q in combinations(smooth_polynomials,2):
    assert S.gcd(S.Poly(p,lam),S.Poly(q,lam)).degree()==0

for pkey, values in parameter_groups.items():
    target=expected[pkey]
    if target is None:
        continue
    # All conjugate parametrizations are checked, not only one representative.
    for f,extra in values:
        all_triples=zero_triples | extra
        actual=dict(incidence(all_triples))
        assert actual == target, (pkey,f,actual,target)
        assert sum(actual.get(m,0)*m*(m-1)//2 for m in (2,3,4))==378

print('VERIFY_OK: 28 bitangents, 3276 triple determinants, 16 parameter strata, 27 smooth exceptional parameters')
