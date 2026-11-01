"""Reproduce algebraic resonance and Jacobian checks for the reciprocal-sine map.

Requires Python 3 and SymPy. The universal statements rely on the proof in RESULT.md.
"""
import math
import random
import sympy as sp

w, a, b, c = sp.symbols('w a b c', real=True, nonzero=True)
t = sp.symbols('t', real=True, nonzero=True)
x, y, z = sp.symbols('x y z', real=True, nonzero=True)
U = lambda t: sp.sin(b/t)
V = lambda t: sp.sin(c/t)
F1 = sp.sin(a/x)*U(y)*V(z)
F2 = U(y)*V(z)
F3 = V(y)*U(z)
assert sp.trigsimp((F2-F3).subs(c,b)) == 0
assert sp.trigsimp((F2-F3).subs(c,-b)) == 0

Up = sp.diff(U(t), t)
Vp = sp.diff(V(t), t)
A = Up*V(t)
B = U(t)*Vp
D2 = sp.expand(A*A-B*B)
# Laurent coefficients at large equal positive coordinates.
assert sp.simplify(sp.series((A-B).subs(t,1/w),w,0,6).removeO().coeff(w,5)- b*c*(b*b-c*c)/3)==0
assert sp.simplify(sp.series((A+B).subs(t,1/w),w,0,4).removeO().coeff(w,3)+2*b*c)==0
D2_8 = sp.series(D2.subs(t,1/w), w, 0, 9).removeO().coeff(w,8)
assert sp.simplify(D2_8+sp.Rational(2,3)*b*b*c*c*(b*b-c*c))==0
# The first column of the full Jacobian has zeros in its bottom two rows.
J1 = sp.diff(F1,x)
leading = sp.series(J1.subs({x:1/w,y:1/w,z:1/w}) * (D2_8*w**8),w,0,13).removeO().coeff(w,12)
expected=sp.Rational(2,3)*a*b**3*c**3*(b*b-c*c)
assert sp.simplify(leading-expected)==0

rng=random.Random(20210917)
for sigma in (-1,1):
    aa,bb,cc=1.3,0.9,0.9*sigma
    for i in range(100):
        x0=rng.uniform(0.15,1.0)*rng.choice((-1,1))
        y0=rng.uniform(0.15,1.0)*rng.choice((-1,1))
        z0=rng.uniform(0.15,1.0)*rng.choice((-1,1))
        yp=math.sin(bb/y0)*math.sin(cc/z0)
        zp=math.sin(cc/y0)*math.sin(bb/z0)
        assert abs(yp-zp)<2e-14
    for t0 in (0.21,0.45,-0.66):
        xp=math.sin(aa/0.4)*math.sin(bb/t0)*math.sin(cc/t0)
        tp=sigma*math.sin(bb/t0)**2
        assert abs(xp-math.sin(aa/0.4)*tp)<2e-14
def bisect(f,lo,hi,steps=90):
    f_lo=f(lo)
    assert f_lo*f(hi)<0
    for _ in range(steps):
        mid=(lo+hi)/2
        if f(lo)*f(mid)>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

fixed_count=0
for sigma in (-1,1):
    aa,bb,cc=1.0,1.0,float(sigma)
    for k in range(15,21):
        r=bisect(lambda r:r-math.sin(bb/r)**2,bb/((k+.5)*math.pi),bb/(k*math.pi))
        t0=sigma*r
        m=60 if sigma==1 else 61
        x0=bisect(lambda xx:sigma*r*math.sin(aa/xx)-xx,aa/((m+.5)*math.pi),aa/(m*math.pi))
        xp=math.sin(aa/x0)*math.sin(bb/t0)*math.sin(cc/t0)
        yp=math.sin(bb/t0)*math.sin(cc/t0)
        zp=math.sin(cc/t0)*math.sin(bb/t0)
        assert abs(xp-x0)<2e-12 and abs(yp-t0)<2e-12 and abs(zp-t0)<2e-12
        fixed_count+=1
assert fixed_count==12
print('VERIFICATION_OK: exact collapse identities and determinant; 200 resonance points; 12 nonzero fixed-point witnesses')
