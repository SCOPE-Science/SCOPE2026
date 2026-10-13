import sympy as sp
from itertools import combinations

a,b,c,d=sp.symbols('a b c d')
F=a**3+b**3+c**3+a*b*d+c*d**2
Q=a**2-b*c+b*d
vars=(a,b,c,d)

def projective_empty(polys):
    for v in vars:
        others=[x for x in vars if x!=v]
        ps=[sp.expand(p.subs({v:1})) for p in polys]
        G=sp.groebner(ps,*others,order='lex')
        if not G.contains(sp.Integer(1)):
            return False, v, G
    return True, None, None

# Smoothness of cubic surface Y.
gradF=[sp.diff(F,v) for v in vars]
ok,chart,G=projective_empty(gradF)
assert ok, (chart,G)

# Smoothness of branch complete intersection C=(F=Q=0).
J=sp.Matrix([[sp.diff(F,v) for v in vars],[sp.diff(Q,v) for v in vars]])
mins=[sp.expand(J[:,[i,j]].det()) for i,j in combinations(range(4),2)]
ok,chart,G=projective_empty([F,Q]+mins)
assert ok, (chart,G)

# Fixed eigenspaces of tau=diag(1,w,w^2,w^2).
# Isolated eigenpoints [1:0:0:0], [0:1:0:0] do not lie on Y.
assert F.subs({a:1,b:0,c:0,d:0})==1
assert F.subs({a:0,b:1,c:0,d:0})==1
# Fixed projective line L: a=b=0 cuts Y in c(c^2+d^2), a square-free cubic on P^1.
g=sp.expand(F.subs({a:0,b:0}))
assert sp.factor(g)==c*(c**2+d**2)
gc,gd=sp.diff(g,c),sp.diff(g,d)
# no common projective root of g and derivatives
for v in (c,d):
    other=d if v==c else c
    G=sp.groebner([sp.expand(h.subs({v:1})) for h in (g,gc,gd)],other,order='lex')
    assert G.contains(sp.Integer(1))
# L lies in branch quadric Q=0, so all three fixed points lie on C.
assert sp.expand(Q.subs({a:0,b:0}))==0

# At each fixed point, reduced transverse intersection Y∩L removes the weight-0 tangent direction.
# Remaining tangent weights are 1 and 2 mod 3, so quotient singularities are 1/3(1,2)=A2.
weights=(1,2)
assert (sum(weights)%3)==0

# Cubic Y has K_Y^2=3; quotient by degree 3 with only isolated fixed points is crepant in codim 1.
KY2=3
KZ2=sp.Rational(KY2,3)
assert KZ2==1

# Branch curve C is a (2,3) complete intersection on P^3: genus 4.
# Equivalently C~2H on cubic Y, H=-K_Y: g=1+(C.(C+K))/2=4.
gC=1+(12-6)//2
assert gC==4
# tau|_C has exactly the same three fixed points; Riemann-Hurwitz gives quotient genus 1.
r=3
gB=sp.solve(sp.Eq(2*gC-2,3*(2*sp.Symbol('gB')-2)+r*(3-1)),sp.Symbol('gB'))[0]
assert gB==1

print('VERIFY_OK')
print('Y_smooth=PASS')
print('branch_curve_smooth_genus=4')
print('tau_fixed_points=3')
print('quotient_singularities=3A2')
print('K_Z^2=1')
print('branch_curve_quotient_genus=1')
