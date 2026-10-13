import sympy as sp

a,b,t,x,y,z,p,q,r = sp.symbols('a b t x y z p q r')
F = x**4 + y**4 + x*z**3

# Affine chart z=1. Tangent direction (F_y,-F_x).
A = 4*a**3 + 1
B = 4*b**3
T = sp.expand((a+B*t)**4 + (b-A*t)**4 + (a+B*t))
assert sp.expand(T.coeff(t,0)) == a**4+a+b**4
assert sp.expand(T.coeff(t,1)) == 0
c2 = sp.factor(T.coeff(t,2))
c3 = sp.factor(T.coeff(t,3))
assert c2 == 6*b**2*(16*a**6 + 8*a**3 + 16*a**2*b**4 + 1)
assert c3 == -4*b*(64*a**9 + 48*a**6 + 12*a**3 - 64*a*b**8 + 1)

# If b != 0, use b^4=-a^4-a. The t^2 coefficient forces 8a^3=1,
# but the remaining t^3 factor is then -27/4, so no hyperflex occurs.
q4 = -a**4-a
E2 = sp.expand((16*a**6+8*a**3+16*a**2*b**4+1).subs(b**4,q4))
E3 = sp.expand((64*a**9+48*a**6+12*a**3-64*a*b**8+1).subs(b**8,q4**2))
assert sp.expand(E2-(1-8*a**3)) == 0
rem = sp.rem(sp.Poly(E3,a), sp.Poly(8*a**3-1,a)).as_expr()
assert sp.factor(rem) == -sp.Rational(27,4)

# Thus affine hyperflexes have b=0 and a(a^3+1)=0.
h = sp.factor(a**4+a)
assert h == a*(a+1)*(a**2-a+1)
# On x=a z, restriction is y^4 for each root a^4+a=0.
restricted = sp.expand(F.subs(x,a*z))
assert sp.rem(sp.Poly(restricted-y**4,a), sp.Poly(a**4+a,a)).as_expr() == 0

# At infinity x=1, C is 1+u^4+v^3=0. Its tangent at (u,v)=(c,0), c^4=-1,
# is u=c and has intersection v^3: flex order 3, not hyperflex.
u,v,c = sp.symbols('u v c')
Finf = 1+u**4+v**3
assert sp.expand(Finf.subs(u,c)).subs(c**4,-1) == v**3

# Equianharmonic cross-ratio of roots {0,-1,alpha,beta}; beta=1-alpha.
alpha = sp.symbols('alpha')
beta = 1-alpha
cr = sp.cancel((0-alpha)*(-1-beta)/((0-beta)*(-1-alpha)))
num = sp.together(cr-alpha).as_numer_denom()[0]
assert sp.rem(sp.Poly(num,alpha),sp.Poly(alpha**2-alpha+1,alpha)).as_expr() == 0

# Kernel of action on the hyperflex divisor. A projective map fixing y=0 pointwise
# has [x:y:z] -> [x+p y:q y:z+r y]. Compare F after substitution.
Fm = sp.Poly(sp.expand(F.subs({x:x+p*y,y:q*y,z:z+r*y}, simultaneous=True) - F), x,y,z)
coeff = {mon:co for mon,co in Fm.terms()}
# x^3 y coefficient forces p=0.
assert sp.factor(coeff[(3,1,0)]) == 4*p
# after p=0, x z^2 y coefficient forces r=0.
Fm_p0 = sp.Poly(sp.expand(Fm.as_expr().subs(p,0)),x,y,z)
assert sp.factor(dict(Fm_p0.terms())[(1,1,2)]) == 3*r
# then preservation is exactly q^4=1.
Fm_pr0 = sp.factor(Fm.as_expr().subs({p:0,r:0}))
assert sp.expand(Fm_pr0-y**4*(q**4-1)) == 0

print('VERIFY_OK hyperflexes=4 collinear=y=0 tangents=4_concurrent equianharmonic=A4 kernel=C4')
