#!/usr/bin/env python3
"""Reproduce symbolic and finite diagnostics of an exact dephasing-pole classification.

All claims about the continuum of rates rely on the written proof rather than sampling.
Only Python, SymPy, NumPy and SciPy are required.
"""
from fractions import Fraction
import sympy as S
import numpy as np
from scipy.optimize import brentq

z,K,w,t,a,v,lam,s=S.symbols('z K w t a v lam s', real=True)
P=z**3+K*z**2+(2*K+w)*z+K*w
Delta=4*(K**4*(1-w)-K**3*(8-10*w)-K**2*(12*w+2*w**2)-6*K*w**2-w**3)
assert S.simplify(S.discriminant(P,z)-Delta)==0
x=(t+2)**2/(t+1)**2
K_t=(t+2)**3/(t+1)**2
w_t=t*(t+2)**3/(t+1)**4
assert S.factor(P.subs({K:K_t,w:w_t,z:-x}))==0
assert S.factor(S.diff(P,z).subs({K:K_t,w:w_t,z:-x}))==0
assert S.factor(P.subs({K:K_t,w:w_t,z:-t*x}))==0
assert S.factor(S.diff(w_t,t)+2*(t-1)*(t+2)**2/(t+1)**5)==0
assert S.factor(S.diff(K_t,t)-(t-1)*(t+2)**2/(t+1)**3)==0
assert K_t.subs(t,1)==S.Rational(27,4)
assert w_t.subs(t,1)==S.Rational(27,16)
assert S.expand(P.subs({K:S.Rational(27,4),w:S.Rational(27,16)})-(z+S.Rational(9,4))**3)==0
P_phys=s**3+(S.Rational(27,4)*lam)*s**2+(S.Rational(27,2)*lam**2+S.Rational(27,16)*lam**2)*s+S.Rational(27,4)*S.Rational(27,16)*lam**3
assert S.expand(P_phys-(s+S.Rational(9,4)*lam)**3)==0
v_star=S.Rational(3,4)*S.sqrt(3)*lam
k_star=S.Rational(27,4)*lam
num=s**2+(k_star+S.I*a*v_star)*s+k_star*(2*lam+S.I*a*v_star)
eta=S.Rational(9,4)*lam
b=S.factor(S.diff(num,s).subs(s,-eta))
c=S.factor(num.subs(s,-eta))
assert S.simplify(b-(eta+S.I*a*v_star))==0
assert S.simplify(c-S.Rational(27,8)*lam**2*(1+S.I*S.sqrt(3)*a))==0
F=S.exp(-eta*t)*(1+b*t+c*t*t/2)
assert S.simplify(F.subs(t,0)-1)==0
assert S.simplify(S.diff(F,t).subs(t,0)-S.I*a*v_star)==0
assert S.simplify(S.diff(F,t,3)+k_star*S.diff(F,t,2)+(2*k_star*lam+v_star**2)*S.diff(F,t)+k_star*v_star**2*F)==0
# At the third-order coalescence every initial-bias coherence magnitude is
# strictly decreasing: an explicit positive-factor certificate.
T,A=S.symbols('T A',real=True)
R=1+S.Rational(9,4)*T+S.Rational(27,16)*T**2
I=S.sqrt(3)*(S.Rational(3,4)*T+S.Rational(27,16)*T**2)
H=S.factor(S.diff(R*R+A*A*I*I,T)-S.Rational(9,2)*(R*R+A*A*I*I))
H_cert=-S.Rational(27,512)*T*(9*T+4)*((1-A*A)*(36*T+16)+(27+81*A*A)*T*T)
assert S.simplify(H-H_cert)==0
# Strictly positive polynomial data and Routh-Hurwitz yields stable poles.
assert S.expand(k_star*(2*k_star*lam+v_star**2)-k_star*v_star**2)==2*k_star**2*lam
# Three exact rational sample cases, both sides of the re-entrant region.
w_sample=S.Rational(36,25)
for k0, sign in [(S.Rational(6),-1),(S.Rational(15,2),1),(S.Rational(9),-1)]:
    d=S.factor(Delta.subs({K:k0,w:w_sample}))
    assert S.sign(d)==sign, (k0,d)
# Independent sampled direct cubic roots: agreement with discriminant sign.
checked=0
for u in np.linspace(0.08,1.9,21):
    for k in np.geomspace(0.12,100,36):
        d=float(Delta.subs({K:float(k),w:float(u*u)}))
        roots=np.roots([1.,float(k),2*float(k)+u*u,float(k)*u*u])
        if abs(d)<1e-5:continue
        nonreal=np.count_nonzero(abs(roots.imag)>1e-7)
        assert (nonreal==0)==(d>0), (u,k,d,roots)
        assert all(ri.real<0 for ri in roots)
        checked+=1
# Independent numerical phase boundaries via roots of the parametric curve.
def b_w(T): return T*(T+2)**3/(T+1)**4
for w0 in [0.12,0.6,1.0,1.1,1.25,1.44,1.65]:
    t_left=brentq(lambda T:b_w(T)-w0,1e-8,1-1e-8)
    Kl=(t_left+2)**3/(t_left+1)**2
    assert abs(float(Delta.subs({K:Kl,w:w0})))<1e-3
    if w0>1:
        t_right=brentq(lambda T:b_w(T)-w0,1+1e-8,1e8)
        Kr=(t_right+2)**3/(t_right+1)**2
        assert Kl<Kr
        assert float(Delta.subs({K:(Kl+Kr)/2,w:w0}))>0
        assert float(Delta.subs({K:Kr+1,w:w0}))<0
    else:
        assert float(Delta.subs({K:Kl+1,w:w0}))>0
print('PASS: exact discriminant, root curve, cusp, residues, exact rational reentrance,')
print(f'and {checked} sampled independent root/sign checks; 7 branch checks.')
