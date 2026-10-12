"""Reconstruct Schur quartic's 64 lines and their exact arithmetic descent.

Requirements: Python 3.10+ and SymPy 1.12+.
Run: python verify_schur_arithmetic.py
Uses exact algebraic expressions; numerical sampling is not used.
"""
from collections import Counter, defaultdict
from itertools import combinations
import sympy as sp

I, r = sp.I, sp.sqrt(3)
zeta = (-1 + I*r)/2
fourth_roots = (sp.S.One, -sp.S.One, I, -I)
cube_roots = (sp.S.One, zeta, zeta**2)
quartic_roots = (sp.S.Zero,) + cube_roots

def exact(v):
    return sp.simplify(sp.expand(sp.radsimp(sp.sympify(v))))

def plucker(v, w):
    minors = tuple(exact(v[j]*w[k] - v[k]*w[j])
                   for j in range(4) for k in range(j+1, 4))
    pivot = next(x for x in minors if x != 0)
    return tuple(exact(x/pivot) for x in minors)

def conjugate(value, sign_i, sign_r):
    return exact(value.subs({I: sign_i*I, r: sign_r*r}, simultaneous=True))

lines = []
for p in quartic_roots:
    for q in quartic_roots:
        lines.append(('L', (p,q), (sp.S.Zero,sp.S.Zero,p,sp.S.One),
                      (q,sp.S.One,sp.S.Zero,sp.S.Zero)))
for a in fourth_roots:
    for b in cube_roots:
        lines.append(('M1', (a,b), (sp.S.One,sp.S.Zero,a,sp.S.Zero),
                      (sp.S.Zero,a**3*b,sp.S.Zero,sp.S.One)))
for k in (2,3,4):
    for a in fourth_roots:
        for b in cube_roots:
            lines.append((f'M{k}', (a,b), (r*a**3*b,sp.S.Zero,b,-2*zeta**(k-2)),
                          (sp.S.Zero,r*a**3*b,-b*zeta**(2-k),-sp.S.One)))
assert len(lines) == 64
pvec = [plucker(v,w) for _,_,v,w in lines]
assert len(set(pvec)) == 64

x = sp.symbols('x0:4'); u,v = sp.symbols('u v')
F = x[0]**4-x[0]*x[1]**3-x[2]**4+x[2]*x[3]**3
for family, parameter, vector1, vector2 in lines:
    substitution = dict(zip(x,(u*a+v*b for a,b in zip(vector1,vector2))))
    assert exact(F.subs(substitution,simultaneous=True)) == 0, (family,parameter)

# Recovery of the field of definition uses the actual fixed Galois subgroup
# of a normalized Plucker coordinate tuple, not merely a field containing
# a chosen pair of spanning vectors.
involutions = ((-1,1),(1,-1),(-1,-1))
image_idx = {p:j for j,p in enumerate(pvec)}
fixed_counts={}; actions={}
for sig in involutions:
    action = tuple(image_idx[tuple(conjugate(co,*sig) for co in p)] for p in pvec)
    assert sorted(action) == list(range(64))
    actions[sig] = action
    fixed_counts[sig] = sum(j == action[j] for j in range(64))
assert fixed_counts == {(-1,1):8,(1,-1):8,(-1,-1):40}

subgroups = {(-1,1):'Q(sqrt(3))',(1,-1):'Q(i)',(-1,-1):'Q(sqrt(-3))'}
field_counts=Counter();family_counts=defaultdict(Counter)
for j,(family,_,_,_) in enumerate(lines):
    fixed_by=[sig for sig in involutions if actions[sig][j] == j]
    field=('Q' if len(fixed_by)==3 else
           'Q(i,sqrt(3))' if len(fixed_by)==0 else subgroups[fixed_by[0]])
    assert len(fixed_by) in (0,1,3)
    field_counts[field]+=1;family_counts[family][field]+=1
assert field_counts == Counter({'Q':6,'Q(i)':2,'Q(sqrt(3))':2,
                               'Q(sqrt(-3))':34,'Q(i,sqrt(3))':20})

orbits=[];remaining=set(range(64))
while remaining:
    j=min(remaining)
    orbit={j} | {actions[sig][j] for sig in involutions}
    assert orbit <= remaining
    remaining-=orbit
    orbits.append(orbit)
assert Counter(map(len,orbits))==Counter({1:6,2:19,4:5})

# The intersection test for two projective lines is the zero
# Klein-quadric polar form on their Plucker six-tuples.
def meet(a,b):
    return exact(a[0]*b[5]-a[1]*b[4]+a[2]*b[3]+
                 a[3]*b[2]-a[4]*b[1]+a[5]*b[0]) == 0
rational = [j for j in range(64) if all(actions[sig][j]==j for sig in involutions)]
assert len(rational)==6
rational_independent=[]
for n in range(1,7):
    members=[choose for choose in combinations(rational,n)
             if all(not meet(pvec[a],pvec[b]) for a,b in combinations(choose,2))]
    if members: rational_independent=members
assert len(rational_independent[0])==4
assert sum(meet(pvec[a],pvec[b]) for a,b in combinations(rational,2)) == 8
# Characteristic zero conjugation fixing i and negating sqrt3 fixes two lines
# over Q(i), while complex conjugation fixes exactly eight real lines.
print('VERIFY_OK lines=64 fields=Q:6,Qi:2,Qsqrt3:2,Qsqrtminus3:34,K:20'
      ' Galois_orbits=1^6,2^19,4^5 real=8 rational=6'
      ' maximal_rational_skew=4')
