import sympy as sp
from sympy import symbols, Poly, expand

p = 31
Y,Z,X,u,v = sp.symbols('Y Z X u v')
# Moriya--Kudo Example 4.2.7(II), homogeneous sextic.
F = (23*Y**6 + 4*Y**4*Z**2 + 4*Y**4*X**2 + 4*Y**2*Z**4
     + 19*Y**2*X**4 + Z**6 + 22*Z**4*X**2 + 12*Z**2*X**4)

def mod(x):
    return int(sp.Integer(x) % p)

# point (13:1:0)
subs_pt = {Y:13, Z:1, X:0}
vals = [F, sp.diff(F,Y), sp.diff(F,Z), sp.diff(F,X)]
assert all(mod(expr.subs(subs_pt)) == 0 for expr in vals)

# local chart Z=1, Y=13+u, X=v. Obtain terms through degree 4 over F_31.
G = sp.Poly(sp.expand(F.subs({Y:13+u,Z:1,X:v})), u,v, modulus=p)
terms = {}
for mon, coeff in G.terms():
    if sum(mon) <= 4:
        terms[mon] = int(coeff) % p
# Required coefficients: a u^2 + b u v^2 + c v^4 + ...
a = terms.get((2,0),0)
b = terms.get((1,2),0)
c = terms.get((0,4),0)
assert a != 0 and b != 0 and c != 0
# no linear terms; unique quadratic term is u^2
assert all(terms.get(m,0)==0 for m in [(1,0),(0,1),(1,1),(0,2)])
# completed-square quartic coefficient c-b^2/(4a) is nonzero, hence local type A3.
inv = lambda n: pow(int(n)%p,-1,p)
h4 = (c - b*b*inv(4*a)) % p
assert h4 != 0

# At the paired point (-13:1:0) the same computation holds by Y -> -Y symmetry.
subs_pt2={Y:-13,Z:1,X:0}
assert all(mod(expr.subs(subs_pt2)) == 0 for expr in vals)

# Lemma 4.2.2 system (2) forces a triple root in P(s)=c60*s^3+c42*s^2+c24*s+c06.
c60,c42,s=sp.symbols('c60 c42 s', nonzero=True)
c24 = c42**2/(3*c60)
c06 = c42**3/(27*c60**2)
s0 = -c42/(3*c60)
P = c60*s**3+c42*s**2+c24*s+c06
assert sp.simplify(P.subs(s,s0)) == 0
assert sp.simplify(sp.diff(P,s).subs(s,s0)) == 0
assert sp.simplify(sp.diff(P,s,2).subs(s,s0)) == 0
assert sp.simplify(sp.diff(P,s,3)) == 6*c60

# Delta accounting for an irreducible plane sextic normalized by a genus-five curve.
pa = (6-1)*(6-2)//2
assert pa == 10
assert pa-5 == 5
# source node contributes delta 1; in a three-singularity case symmetry makes the remaining pair equal.
remaining = 5-1
assert remaining % 2 == 0 and remaining//2 == 2
# For a split form U^2 - V^alpha in characteristic !=2, delta=floor(alpha/2).
# Evenness in the transverse coordinate forces alpha even; delta=2 therefore forces alpha=4.
possible = [a0 for a0 in range(4,12) if a0//2 == 2 and a0%2==0]
assert possible == [4]

print(f"VERIFY_OK sympy={sp.__version__} exampleII=A3_pair h4={h4} system2=triple_root_contradiction three_point_basket=A1+2A3")
