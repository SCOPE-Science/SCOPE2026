"""Exact algebra and finite independent checks for two-sided three-node FSBP."""
from math import sin, cos, sinh, cosh, pi, isclose
import sympy as sp

C, S, k = sp.symbols('C S k', real=True)
T = sp.Matrix([[-(2*C+1), 2*(C+1), -1],
               [-1, 0, 1],
               [1, -2*(C+1), 2*C+1]])
D = k*T/(2*S)
w = S/(k*(1+2*C))
H = sp.diag(w,2*(1+C)*w,w)
B = sp.diag(-1,0,1)
checks=0
for e in H*D+D.T*H-B:
    assert sp.cancel(e)==0
    checks+=1
V=sp.Matrix([[1,C,-S],[1,1,0],[1,C,S]])
assert sp.factor(V.det())==-2*S*(C-1)
checks+=1
Vexp_prime=sp.Matrix([[0,-k*S,k*C],[0,0,k],[0,k*S,k*C]])
Vtrig_prime=sp.Matrix([[0,k*S,k*C],[0,0,k],[0,-k*S,k*C]])
for vp, relation in ((Vexp_prime,C**2-S**2-1), (Vtrig_prime,C**2+S**2-1)):
    for e in D*V-vp:
        numerator,_=sp.fraction(sp.cancel(e))
        assert sp.expand(sp.rem(numerator,relation,C))==0, (e,numerator,relation)
        checks+=1
# Exact normalized-mass comparisons at algebraic frequencies.
for c,svalue,omega,positive in ((sp.Rational(1,2),sp.sqrt(3)/2,sp.pi/3,True),
                                 (sp.Rational(-4,5),-sp.Rational(3,5),sp.pi+sp.asin(sp.Rational(3,5)),True)):
    subs={C:c,S:svalue,k:omega}
    assert all(sp.simplify(e.subs(subs))==0 for e in H*D+D.T*H-B)
    assert (sp.N(w.subs(subs))>0)==positive
    checks+=10
# Stress checks for frequency bands and exact matrix identities.
for j in range(1,270):
    lam=j/65
    cs,ss=cosh(lam),sinh(lam)
    weights=[ss/(lam*(1+2*cs)),2*(1+cs)*ss/(lam*(1+2*cs)),ss/(lam*(1+2*cs))]
    mass=sum(weights)
    assert min(weights)>0 and mass>2 and isclose(max(weights)/min(weights),2*(1+cs),rel_tol=1e-12)
    checks+=3
for j in range(1,950):
    omega=j/101
    if abs(sin(omega))<1e-12 or abs(1+2*cos(omega))<1e-12:
        continue
    theta=omega%(2*pi)
    expected=(0<theta<2*pi/3) or (pi<theta<4*pi/3)
    c,s=cos(omega),sin(omega)
    val=s/(omega*(1+2*c))
    assert (val>0)==expected
    if expected:
        W=[val,2*(1+c)*val,val]
        assert min(W)>0
        assert abs(sum(W)-2*s*(2+c)/(omega*(1+2*c))) < 1e-11
        checks+=2
    checks+=1
print('VERIFICATION_OK',checks,'checks')
