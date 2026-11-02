"""Exact symbolic checks for two-bounce spectra of a convex eye-shaped billiard.

Requires Python 3 and SymPy. All infinite conclusions in the accompanying
proof are analytic, not inferred from this finite checker.
"""
import sympy as S
u,e=S.symbols('u e',real=True)
t=S.symbols('t',real=True)
r=S.Matrix([S.cos(t),e*S.sin(t)*(1+S.sin(t)**2)])
rp=r.diff(t); rpp=rp.diff(t)
normal=(r.dot(rp)).expand().trigsimp()
expected=S.sin(t)*S.cos(t)*(-1+e**2*(1+S.sin(t)**2)*(1+3*S.sin(t)**2))
assert S.trigsimp(normal-expected)==0
curvature_numer=S.expand_trig(rp[0]*rpp[1]-rp[1]*rpp[0]).trigsimp()
assert S.trigsimp(curvature_numer-e*(1-3*S.sin(t)**2+6*S.sin(t)**4))==0
H=1+3*u-2*u**2
D=(1+3*u)*H
Q=1-3*u+6*u*u
K=2*(1+u)*Q/D
assert S.simplify(D-(1+u)*Q-4*u*(1-u)*(3*u+2))==0
assert S.simplify(K-1-(18*u**3-u**2-10*u+1)/D)==0
assert S.simplify(K.diff(u)-8*(15*u**4+12*u**3+17*u**2-2*u-2)/((1+3*u)**2*(2*u**2-3*u-1)**2))==0
# The one-collision optical matrix has determinant one, trace 2(1-K).
k,L=S.symbols('k L')
flight=S.Matrix([[1,L],[0,1]])
reflection=S.Matrix([[1,0],[-2*k,1]])
M=reflection*flight
assert M.det()==1
assert S.expand(S.trace(M**2)-(4*(1-L*k)**2-2))==0
assert (M**2+S.eye(2)).subs(k,1/L)==S.zeros(2)
# Strict positivity of Q via its negative discriminant; D positive
assert S.discriminant(Q,u)<0
# Two resonance roots separated by rational sign-change brackets.
f=18*u**3-u**2-10*u+1
assert f.subs(u,S.Rational(1,10))>0 and f.subs(u,S.Rational(11,100))<0
assert f.subs(u,S.Rational(7,10))<0 and f.subs(u,S.Rational(3,4))>0
assert f.subs(u,0)>0 and f.subs(u,S.Rational(1,2))<0 and f.subs(u,1)>0
critical=(1+S.sqrt(541))/54
assert critical>0 and critical<1
assert S.simplify(f.diff(u).subs(u,critical))==0
roots=sorted([float(S.re(rt)) for rt in S.nroots(f,n=30)
              if abs(float(S.im(rt)))<1e-20 and 0<float(S.re(rt))<1])
assert len(roots)==2
for x in roots:
    eps=1/(((1+x)*(1+3*x))**0.5)
    assert 1/(2*2**0.5)<eps<1
    assert abs(float(K.subs(u,x))-1)<1e-12
for v in [S.Rational(i,1000) for i in range(1,1000)]:
    z=K.subs(u,v)
    assert 0<z<2
    tr=4*(1-z)**2-2
    assert -2<=tr<2
# Explicit axial diagnostics from original source under any interior epsilon
for eps in [S.Rational(2,5), S.Rational(1,2), S.Rational(3,4), S.Rational(9,10)]:
    vertical=4*(1-16*eps**2)**2-2
    horizontal=4*(2/eps**2-1)**2-2
    assert vertical>2 and horizontal>2
print('PASS: symbolic geometry, trace, sharp positivity, resonance count/brackets, and 1,003 finite checks.')
print('resonance u roots:',roots)
print('resonance epsilon values:',[1/(((1+x)*(1+3*x))**0.5) for x in roots])
