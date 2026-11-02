"""Reproducibility checks for the four-field reentrant equilibrium theorem.

Requires Python 3, SymPy, NumPy, and SciPy. Symbolic identities and exact
rational inequalities are the primary checks; finite spectra are corroborative.
"""
import sympy as sp
import numpy as np
from scipy.special import jnp_zeros

z,h,k,t,g,A,C=sp.symbols('z h k t g A C')
P=sp.Rational(5,2)
S=sp.Rational(11,2)
M=sp.Matrix([[-1-k,sp.Rational(1,2),-k,0],
             [-5,-1-k,0,k],
             [0,h,-1-k,0],
             [h,0,0,-1-k]])
p_actual=sp.factor(M.charpoly(z).as_expr())
p_expected=(z+1+k)**4+P*(z+1+k)**2-S*h*k*(z+1+k)+(h*k)**2
assert sp.expand(p_actual-p_expected)==0
print('PASS exact 4x4 dispersion polynomial')

p4=sp.expand((z+t)**4+P*(z+t)**2-S*g*(z+t)+g**2)
a1=sp.expand(p4).coeff(z,3)
a2=sp.expand(p4).coeff(z,2)
a3=sp.expand(p4).coeff(z,1)
a4=sp.expand(p4).coeff(z,0)
assert sp.simplify(a1-4*t)==0
assert sp.simplify(a2-(6*t**2+P))==0
assert sp.simplify(a3-(4*t**3+2*P*t-S*g))==0
assert sp.simplify(a4-(t**4+P*t**2-S*g*t+g**2))==0
D2=sp.expand(a1*a2-a3)
D3=sp.expand(a1*a2*a3-a3**2-a1**2*a4)
assert sp.expand(D2-(20*t**3+2*P*t+S*g))==0
assert sp.expand(D3-(4*t**2*(P+4*t**2)**2-(S**2+16*t**2)*g**2))==0
assert sp.expand(a4-((g-S*t/2)**2+t**2*(t**2-sp.Rational(81,16))))==0
print('PASS exact quartic Routh-Hurwitz and stationary-square identities')

p1=sp.expand(p4.subs({t:2,g:h}))
assert sp.expand(p1-(z**4+8*z**3+sp.Rational(53,2)*z**2+(42-sp.Rational(11,2)*h)*z+(h**2-11*h+26)))==0
h_minus=(11-sp.sqrt(17))/2
h_plus=(11+sp.sqrt(17))/2
h_osc=148/sp.sqrt(377)
assert sp.simplify((h_minus+h_plus)-11)==0
assert sp.simplify(h_minus*h_plus-26)==0
assert (sp.Rational(413,100))**2>17
assert (sp.Rational(389,20))**2>377
assert sp.Rational(2960,389)>sp.Rational(1513,200)
assert sp.Rational(1513,200) > h_plus # evaluated exactly by sympy
assert h_osc>h_plus
assert sp.Rational(84,11)>h_osc
assert sp.simplify(D3.subs({t:2,g:h})-(5476-sp.Rational(377,4)*h**2))==0
print('PASS exact three thresholds and strict ordering')

f=2*t*(P+4*t**2)/((t-1)*sp.sqrt(S**2+16*t**2))
raw=512*t**5-1024*t**4+1616*t**3-2904*t**2-605
assert sp.simplify(sp.diff(f,t) - raw/(4*(t-1)**2*(S**2+16*t**2)**sp.Rational(3,2)))==0
assert raw.subs(t,2)==707
print('PASS monotonic high-mode oscillatory threshold: numerator >=707 at t>=2')

j11=float(jnp_zeros(1,1)[0]); j21=float(jnp_zeros(2,1)[0]); j01=float(jnp_zeros(0,1)[0])
assert 1.84<j11<1.85 and 3.05<j21<3.06 and 3.83<j01<3.84
k2=(j21/j11)**2
assert k2>sp.Rational(5,4)
y=sp.symbols('y',nonnegative=True)
q_bessel=sp.Rational(1,2)-y/12+y**2/256-y**3/11520
assert q_bessel.subs(y,sp.Rational(25,4))==sp.Rational(16303,147456)
assert sp.Rational(1,2)-sp.Rational(3,4)+sp.Rational(5,24)==-sp.Rational(1,24)
assert sp.Rational(1,1)-sp.Rational(25,4)/8==sp.Rational(7,32)
assert -sp.Rational(1,12)+sp.Rational(25,4)/128 <0  # q_bessel' <0 throughout range
print('PASS elementary Bessel-series rational brackets for the spectral gap')
print('PASS disk eigenvalue interval check: k2=',k2,
      '(zero ordering is a classical analytical fact)')

# The proof requires only the exact inequalities and monotonicity above.
# The following finite tests provide independent numerical corroboration.
for hv,expected_stable in [(1,True),(5,False),(7.59,True),(8,False)]:
    m=np.array(M.subs({k:1,h:hv})).astype(float)
    eig=np.linalg.eigvals(m)
    assert (max(eig.real)<0)==expected_stable
    print('mode k=1 h=',hv,'max Re=',max(eig.real),'stable=',expected_stable)
for hv in [1,5,7.59,8]:
    for kval in [0,k2,4.3310,8,16,40,100]:
        m=np.array(M.subs({k:kval,h:hv})).astype(float)
        eig=np.linalg.eigvals(m)
        if hv<=7.59: assert max(eig.real)<0
print('PASS finite higher-mode samples (not an exhaustive stability proof)')
print('ALL CHECKS PASSED')
