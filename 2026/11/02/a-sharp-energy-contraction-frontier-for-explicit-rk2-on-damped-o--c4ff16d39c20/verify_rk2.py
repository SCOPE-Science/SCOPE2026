"""Exact symbolic and numerical checks for the two-stage order-two stability polynomial.
Standalone research reproducibility aid; requires sympy and numpy.
"""
import math
import numpy as np
import sympy as S

x, a, v, s = S.symbols('x a v s', positive=True, real=True)
I = S.eye(2)
L = S.Matrix([[0,-a],[a,-1]])
R = I+x*L+S.Rational(1,2)*x*x*L*L
B = S.simplify(I-R.T*R)
expected11=a*a*x**3*(4-(1+a*a)*x)/4
expectedDet=a*a*x**4*(a*a*x-2)*(x*((a*a*x-1)**2+3)-8)/16
assert S.simplify(B[0,0]-expected11)==0
assert S.simplify(S.factor(B.det()-expectedDet))==0
assert S.factor(S.diff(x*((v*x-1)**2+3)-8,x))==3*v*v*x*x-4*v*x+4
assert S.simplify((4-s)*((s-1)**2+3)-8-(2-s)**3)==0
z_s=8/((s-1)**2+3)
v_s=S.factor(s/z_s)
assert S.simplify(v_s.subs(s,2)-1)==0
assert S.simplify(v_s.subs(s,1)-S.Rational(3,8))==0
assert S.simplify(z_s.subs(s,1)-S.Rational(8,3))==0
assert S.simplify(S.diff(v_s,s)-(3*s*s-4*s+4)/8)==0
assert S.simplify(S.diff(z_s,s)+16*(s-1)/((s-1)**2+3)**2)==0

Ropt = S.simplify(R.subs({a:S.sqrt(S.Rational(3,8)),x:S.Rational(8,3)}))
assert Ropt==S.Matrix([[-S.Rational(1,3),2*S.sqrt(6)/9],[-2*S.sqrt(6)/9,S.Rational(5,9)]])
assert sorted(Ropt.eigenvals().keys(), key=S.default_sort_key) == sorted([(1+2*S.sqrt(2)*S.I)/9,(1-2*S.sqrt(2)*S.I)/9],key=S.default_sort_key)
assert sorted((Ropt.T*Ropt).eigenvals().keys(),key=S.default_sort_key)==[S.Rational(1,81),S.Integer(1)]
assert S.simplify(R.subs({a:S.Integer(1),x:S.Integer(2)})+I)==S.zeros(2)

n=0
for vv in [0.02,0.1,0.25,0.375,0.5,0.75,0.95,1.,1.1,2.,5.,30.]:
    def phi(z): return z*((vv*z-1)**2+3)-8
    low, high=0.0,8.0
    for _ in range(100):
        mid=(low+high)/2
        if phi(mid)<0:low=mid
        else:high=mid
    root=(low+high)/2
    cap = root if vv<1 else 2/vv
    for factor in (0.001,0.2,0.7,0.999,1.001,1.1,1.5,3.0,10.):
        zz=cap*factor
        arr=np.asarray(R.subs({a:math.sqrt(vv),x:zz}),dtype=float)
        sv=np.linalg.svd(arr,compute_uv=False)[0]
        expected = factor < 1
        if expected:assert sv<1-1e-13,(vv,zz,sv)
        else:assert sv>1+1e-13,(vv,zz,sv)
        n+=1
    arr=np.asarray(R.subs({a:math.sqrt(vv),x:cap}),dtype=float)
    assert abs(np.linalg.svd(arr,compute_uv=False)[0]-1)<2e-12
print(f'VERIFY_OK symbolic identities, 12 boundary points, {n} two-sided spectral-norm samples; sharp optimum and resonance')
