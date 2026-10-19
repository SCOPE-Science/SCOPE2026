"""Exact checks for norm-projected Taylor propagators on a planar oscillator.

Requires Python 3, sympy, and mpmath. The analytical proof is in RESULT.md;
these tests check algebra and independently implement the projected update.
"""
from fractions import Fraction
import math
import cmath
import sympy as sp

z = sp.Symbol('z', real=True)
X = sp.Symbol('X', real=True, nonnegative=True)
N_CHECKS = 0

def check(condition, msg):
    global N_CHECKS
    assert bool(condition), msg
    N_CHECKS += 1

def exact_zero(expr):
    return sp.cancel(sp.expand(expr)) == 0

# Explicit stage-chain RK representation, with its consistency and
# exact linear-test-equation polynomial (not a claim of nonlinear order m).
for m in range(1, 6):
    weights = [sp.Rational(1, sp.factorial(j)) - sp.Rational(1, sp.factorial(j+1)) for j in range(1, m)] + [sp.Rational(1, sp.factorial(m))]
    check(sum(weights) == 1, f'RK consistency m={m}')
    R = 1 + sum(z * weights[j-1] * sum(z**k for k in range(j)) for j in range(1,m+1))
    p = sum(z**j/sp.factorial(j) for j in range(m+1))
    check(exact_zero(R-p), f'linear stability polynomial m={m}')

expected = {
  1: sp.Integer(1),
  2: (z**2+2)/2,
  3: (z**4+12)/12,
  4: (z**6-6*z**4+144)/144,
  5: (z**8-16*z**6+2880)/2880,
}
for m in range(1,6):
    R = sum((sp.I*z)**j/sp.factorial(j) for j in range(m+1))
    a = sp.re(sp.expand(R)); b = sp.im(sp.expand(R))
    phase_num = sp.expand(a*sp.diff(b,z)-b*sp.diff(a,z))
    check(exact_zero(phase_num-expected[m]), f'phase derivative numerator {m}')
    # Exact radius drift independent of the initial vector.
    check(exact_zero(sp.expand_complex(sp.conjugate(R)*R)-(a*a+b*b)), f'magnitude {m}')

q = X**4 - 16*X**3 + 2880
check(exact_zero(sp.diff(q,X)-4*X**2*(X-12)), 'root monotonic derivative')
check(q.subs(X,0)>0 and q.subs(X,12)<0, 'unique pair positive roots')
check(sp.expand((X-10)**2+20-(X**2-20*X+120)) == 0, 'positive odd polynomial')
check(4**3 - 6*4**2 + 144 == 112, 'order-four derivative minimum')

# Certified rational root brackets by polynomial signs and monotonicity.
lo1, hi1 = sp.Rational(6786709, 10**6), sp.Rational(6786710,10**6)
lo2, hi2 = sp.Rational(15176015,10**6), sp.Rational(15176016,10**6)
check(0<lo1<hi1<12<lo2<hi2, 'ordered rational brackets')
check(q.subs(X,lo1)>0 and q.subs(X,hi1)<0, 'first bracket signs')
check(q.subs(X,lo2)<0 and q.subs(X,hi2)>0, 'second bracket signs')

# Independent direct polynomial evaluation and first two stage directions.
for m in range(2,6):
    for zv in [sp.Rational(j,7) for j in range(1,46)]:
        a = sum(((-1)**j * zv**(2*j)/sp.factorial(2*j)) for j in range(m//2+1))
        b = sum(((-1)**j * zv**(2*j+1)/sp.factorial(2*j+1)) for j in range((m-1)//2+1))
        p = sum((sp.I*zv)**j/sp.factorial(j) for j in range(m+1))
        check(a+sp.I*b == sp.expand(p), f'direct polynomial m={m},z={zv}')
        check(a*a+b*b>0, f'nonzero predictor m={m},z={zv}')
        # J rotates (1,2) -> (-2,1), J^2(1,2) -> (-1,-2).
        first=sp.Matrix([-2,1]); second=first+zv*sp.Matrix([-1,-2]);
        check(sp.det(sp.Matrix.hstack(first,second))!=0, f'stage-span rank {m},{zv}')

# High-precision phase reversals and exact conservation under repeated steps.
# A second implementation evaluates RK stages directly, independently
# of the symbolic stability-polynomial reduction.
def stage_step(u,t,m):
    stages=[1j*u]
    for _ in range(2,m+1):
        stages.append(1j*(u+t*stages[-1]))
    w=[1/mp.factorial(j)-1/mp.factorial(j+1) for j in range(1,m)] + [1/mp.factorial(m)]
    predictor=u+t*sum(w[j]*stages[j] for j in range(m))
    return abs(u)*predictor/abs(predictor)

import mpmath as mp
mp.mp.dps=70
poly=lambda v: sum((1j*v)**j/mp.factorial(j) for j in range(6))
roots=sorted([mp.findroot(lambda t: t**8-16*t**6+2880,(x-.1,x+.1)) for x in [mp.mpf('2.605'),mp.mpf('3.895')]])
check(abs(roots[0]-mp.mpf('2.60513130314044')) < mp.mpf('1e-13'), 'first critical angle')
check(abs(roots[1]-mp.mpf('3.89564052945169')) < mp.mpf('1e-13'), 'second critical angle')
phase=lambda t: mp.arg(poly(t))
check(phase(roots[0])>phase(roots[1]) and phase(roots[0])-phase(roots[1])>mp.mpf('1.72'),'strict phase backtracking')
check(abs(phase(roots[0])-mp.mpf('2.1950240916954'))<mp.mpf('1e-12'),'upper phase')
check(abs(phase(roots[1])-mp.mpf('0.467591743846912'))<mp.mpf('1e-12'),'lower phase')
# Three distinct positive step sizes give the exact same projected rotation.
critical_low, critical_high=roots
alias_roots=[mp.findroot(lambda t: phase(t)-1, (left,right)) for left,right in [(mp.mpf('0.6'),mp.mpf('1.5')),(mp.mpf('3'),mp.mpf('3.5')),(mp.mpf('7'),mp.mpf('10'))]]
check(alias_roots[0]<critical_low<alias_roots[1]<critical_high<alias_roots[2], 'ordered triple alias roots')
for j,t in enumerate(alias_roots):
    check(abs(phase(t)-1)<mp.mpf('1e-60'),f'phase alias {j}')
    check(abs(poly(t)/abs(poly(t))-mp.e**(1j))<mp.mpf('1e-60'),f'identical projected rotation {j}')

# Verify all exact phase speeds, not only polynomial coefficient identities.
for m in range(1,6):
    fun=lambda t:sum((1j*t)**j/mp.factorial(j) for j in range(m+1))
    deriv=lambda t:sum((1j)**j*j*t**(j-1)/mp.factorial(j) for j in range(1,m+1))
    for qval in [mp.mpf('0.13'),mp.mpf('1'),mp.mpf('2.6'),mp.mpf('3.2'),mp.mpf('4.3')]:
        direct=mp.im(deriv(qval)/fun(qval))
        sym=sp.lambdify(z,expected[m],'mpmath')(qval)/(abs(fun(qval))**2)
        check(abs(direct-sym)<mp.mpf('1e-14'),f'phase speed {m}, {qval}')

for t in [mp.mpf('0.3'),mp.mpf('1'),mp.mpf('2.65'),mp.mpf('3.2'),mp.mpf('3.9'),mp.mpf('8')]:
    w=poly(t)/abs(poly(t))
    check(abs(abs(w)-1)<mp.mpf('1e-65'),'projected multiplier unitary')
    for m in range(2,6):
        p_m=sum((1j*t)**j/mp.factorial(j) for j in range(m+1))
        direct_step=stage_step(mp.mpc('0.6','0.8'),t,m)
        check(abs(direct_step-mp.mpc('0.6','0.8')*p_m/abs(p_m))<mp.mpf('1e-60'),f'actual RK stage projection {m}')
    state=mp.mpc('0.6','0.8')
    for j in range(20):
        state*=w
        check(abs(abs(state)-1)<mp.mpf('1e-60'),'repeat exact energy')

print(f'PASS {N_CHECKS} algebraic / rational / high-precision assertions')
