"""Exact certificates for four-vertex birth--death Moran edge additions.

Requires Python 3 and sympy (tested with sympy 1.13.1).
Run: python verify.py
"""
from itertools import combinations, permutations
from sympy import Matrix, Rational, Symbol, Poly, cancel, factor, fraction, simplify

r = Symbol('r', positive=True)
EDGES = {
    'star': ((0, 3), (1, 3), (2, 3)),
    'path': ((0, 1), (0, 3), (1, 2)),
    'paw': ((0, 3), (1, 2), (1, 3), (2, 3)),
    'cycle': ((0, 1), (0, 3), (1, 2), (2, 3)),
    'diamond': ((0, 1), (0, 2), (0, 3), (1, 2), (2, 3)),
    'complete': tuple(combinations(range(4), 2)),
}
ORDER = ('star', 'path', 'paw', 'cycle', 'diamond', 'complete')


def fixation(n, edges):
    """Solve all finite harmonic equations over rational functions, without simulation."""
    e = {tuple(sorted(edge)) for edge in edges}
    deg = [sum((min(i, j), max(i, j)) in e for j in range(n) if j != i)
           for i in range(n)]
    assert all(deg)
    states = list(range(1, (1 << n)-1))
    row = {mask: i for i, mask in enumerate(states)}
    A = Matrix.zeros(len(states)); b = Matrix.zeros(len(states), 1)
    for mask in states:
        p = row[mask]
        for x, y in permutations(range(n), 2):
            if (min(x, y), max(x, y)) not in e: continue
            if ((mask >> x) & 1) == ((mask >> y) & 1): continue
            rate = (r if (mask >> x) & 1 else Rational(1)) / deg[x]
            nxt = mask ^ (1 << y)
            A[p, p] += rate
            if nxt == (1 << n) - 1: b[p] += rate
            elif nxt: A[p, row[nxt]] -= rate
    u = A.inv() * b
    # Independently check every harmonic equation before extracting singletons.
    assert all(cancel(z)==0 for z in (A*u-b))
    return cancel(sum(u[row[1 << i]] for i in range(n)) / n)


def polynomial(coefficients_descending):
    return Poly.from_list(coefficients_descending, gens=r).as_expr()

Fs = {}
for name in ORDER:
    Fs[name] = fixation(4, EDGES[name])
assert len(Fs) == 6

paw_num = polynomial([45360, 201204, 387108, 479847, 478953,
                      374117, 173451, 31584])
paw_den = polynomial([22680, 123282, 310806, 530223, 751386,
                      866494, 751386, 530223, 310806, 123282, 22680])
dia_num = polynomial([126, 447, 643, 429, 115])
dia_den = polynomial([126, 447, 761, 852, 761, 447, 126])
expected = {
 'star': r**3*(3*r+1)*(3*r+7)/((r+3)*(3*r*r-2*r+3)*(3*r*r+4*r+3)),
 'path': r**3*(8*r*r+16*r+15)/(2*(r+1)*(2*r*r-r+2)*(2*r*r+5*r+6)),
 'paw': r**3*paw_num/(2*paw_den),
 'cycle': r**3/((r+1)*(r*r+1)),
 'diamond': r**3*dia_num/((r+1)*dia_den),
 'complete': r**3/((r+1)*(r*r+1))}
for g in ORDER:
    assert cancel(Fs[g] - expected[g]) == 0, g

# The six edge-addition types are exhaustive, not a random graph sample.
def canonical(n, edges):
    edges = set(tuple(sorted(e)) for e in edges)
    return min(tuple(sorted(tuple(sorted((p[u], p[v]))) for u,v in edges))
               for p in permutations(range(n)))


def connected(n, edges):
    reached={0};edges=set(tuple(sorted(e)) for e in edges)
    while 1:
        new=reached | {v for u,v in edges if u in reached} | {u for u,v in edges if v in reached}
        if reached==new: return len(reached)==n
        reached=new

for n, desired in [(2,1), (3,2), (4,6)]:
    pairs = list(combinations(range(n), 2))
    connected_canon=set()
    for bits in range(1<<len(pairs)):
        ed=[e for k,e in enumerate(pairs) if (bits>>k)&1]
        if connected(n,ed): connected_canon.add(canonical(n, ed))
    assert len(connected_canon)==desired

mapped={canonical(4, EDGES[name]): name for name in ORDER}
assert len(mapped)==6
transitions=set()
for name, edges in EDGES.items():
    e={tuple(sorted(x)) for x in edges}
    for add in combinations(range(4), 2):
        if add not in e:
            dest=mapped[canonical(4,e|{add})]
            transitions.add((name,dest))
assert transitions=={
 ('star','paw'),('path','paw'),('path','cycle'),
 ('paw','diamond'),('cycle','diamond'),('diamond','complete')
}

# Exact sign identities; numerators and denominators factor over the integers.
# All denominators of the six differences are strictly positive for r>1.
positive_polynomials = {
 ('star','paw'): polynomial([145260, 609597, 1436700, 2571333,
                                 3156548, 2773983, 1926516, 907119, 178416]),
 ('paw','diamond'): polynomial([1156680, 10173546, 36750645, 74738010,
 100287210, 104456627, 100009239, 88915844, 63095328, 30846837, 9098658, 1236816]),
 ('cycle','diamond'): 8*r**3+32*r**2+29*r+11,
 ('diamond','complete'): 8*r**3+32*r**2+29*r+11,
 ('path','cycle'): r+9,
}
critical=polynomial([12780,14805,-177144,-665280,-1193573,-1412701,
                     -1179232,-667896,-206727,-19404])
assert Poly(critical,r).count_roots(1, 100) == 1  # exact rational root count
assert critical.subs(r,Rational(4887,1000))<0
assert critical.subs(r,Rational(4888,1000))>0
# Descartes: exactly one sign change of coefficients, so exactly one positive root.
cs=Poly(critical,r).all_coeffs()
assert sum((cs[k]>0)!=(cs[k+1]>0) for k in range(len(cs)-1))==1

for g,h in sorted(transitions):
    diff=cancel(Fs[h]-Fs[g])
    num,den=fraction(factor(diff))
    target=critical if (g,h)==('path','paw') else positive_polynomials[g,h]
    signed = {('star','paw'):-1,('path','paw'):1,('path','cycle'):-1,
              ('paw','diamond'):-1,('cycle','diamond'):1,('diamond','complete'):-1}[(g,h)]
    factor_extra = 3*(r+1) if (g,h)==('star','paw') else Rational(1)
    target_num=signed*r**3*(r-1)*factor_extra*target
    assert cancel(num-target_num)==0,(g,h)
    assert Poly(den,r).eval(2)>0
    # Every multiplicative factor in each reported denominator is positive at r>1.
    for fac,_ in Poly(den,r).factor_list()[1]:
        assert all(x>=0 for x in Poly(fac.as_expr().subs(r,r+1),r).all_coeffs()) and fac.eval(1)>0,(g,h,fac)

# Minimality: on three nodes adding the only missing edge reduces fixation for r>1.
f3p=fixation(3, ((0,1),(1,2)))
f3k=fixation(3, tuple(combinations(range(3),2)))
assert cancel(f3k-f3p + r**2*(r-1)/((r+2)*(r**2+r+1)*(2*r**2+r+2)))==0
assert fixation(2, ((0,1),))==r/(r+1)
print('PASS: six exact 4-vertex fixation functions and all harmonic equations')
print('PASS: graph-isomorphism enumeration of every 2-, 3-, and 4-vertex type')
print('PASS: complete six-edge-addition sign certificates')
print('PASS: unique positive fitness crossover r in (4.887, 4.888)')
print('PASS: three-vertex minimality proof identity')
