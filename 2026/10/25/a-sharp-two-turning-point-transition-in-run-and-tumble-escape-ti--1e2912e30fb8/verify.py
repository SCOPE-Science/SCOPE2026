"""Reproduce the exit-time moment identities and the sharp variance-phase boundary.

Requires Python 3 and SymPy; run `python verify.py`.
"""
import sympy as sp

x, s, a, g = sp.symbols('x s a g', positive=True)
b = a + g

# Independent backward first-moment calculation. Write S_j=u_{+,j}+u_{-,j},
# D_j=u_{+,j}-u_{-,j} for the jth moment from each moving state.
# For j=1: D_1'=-2, S_1'=2*a*D_1; u_{+,1}(1)=0,
# u_{-,1}(0)=u_{+,1}(0)+1/b.
D1 = -1/b - 2*x
S1_at_1 = -D1.subs(x, 1)
S1 = sp.factor(S1_at_1 - sp.integrate(2*a*D1, (x, x, 1)))
mean_backward = sp.factor((S1.subs(x, 0) + D1.subs(x, 0))/2)

# Second moment: D_2'=-2*S_1, S_2'=2*a*D_2-2*D_1,
# and u_{-,2}(0)=u_{+,2}(0)+2*u_{+,1}(0)/b+2/b**2.
D2_at_0 = -2*mean_backward/b-2/b**2
D2 = sp.factor(D2_at_0 - 2*sp.integrate(S1, (x, 0, x)))
S2_at_1 = -D2.subs(x, 1)
S2_at_0 = sp.factor(S2_at_1 - sp.integrate(2*a*D2 - 2*D1, (x, 0, 1)))
second_backward = sp.factor((S2_at_0+D2_at_0)/2)
variance_backward = sp.factor(second_backward-mean_backward**2)

# Independent derivation via the Laplace transform. This expansion is enough
# for moments through order two; it is exact in the coefficients at s=0.
k2 = s*(s+2*a)
cosh_term = sum(k2**j/sp.factorial(2*j) for j in range(3))
sinhc_term = sum(k2**j/sp.factorial(2*j+1) for j in range(3))
den = cosh_term + s*(s+2*a+g)/(s+a+g)*sinhc_term
coef1 = sp.factor(sp.diff(den, s).subs(s, 0))
coef2 = sp.factor(sp.diff(den, s, 2).subs(s, 0)/2)
mean_laplace = coef1
variance_laplace = sp.factor(mean_laplace**2-2*coef2)

mean = 1+a+a/(a+g)
variance = a*(2*a**3+4*a**2*g+8*a**2+2*a*g**2+12*a*g+9*a+4*g**2+6*g+6)/(3*(a+g)**2)
Q = (2*a**4+(6*g+4)*a**3+(6*g**2+12*g)*a**2
     +(2*g**3+10*g**2+6*g-3)*a+2*g**3+3*g**2+3*g)
for expr, target, name in [
    (mean_backward, mean, 'backward mean'),
    (variance_backward, variance, 'backward variance'),
    (mean_laplace, mean, 'Laplace mean'),
    (variance_laplace, variance, 'Laplace variance'),
    (sp.diff(variance, a), 2*Q/(3*(a+g)**3), 'variance derivative'),
    (sp.diff(mean, a), 1+g/(a+g)**2, 'mean derivative'),
]:
    assert sp.cancel(expr-target) == 0, name
assert sp.factor(Q.subs(g,0)) == a*(2*a**3+4*a**2-3)
assert sp.simplify(sp.diff(Q, a, 2) - (24*a**2+(36*g+24)*a+12*g**2+24*g)) == 0
assert sp.simplify(sp.diff(Q, g) - (6*a**3+(12*g+12)*a**2
                              +(6*g**2+20*g+6)*a+6*g**2+6*g+3)) == 0
assert Q.subs({a:sp.Rational(1,4),g:0}) < 0
assert all(c > 0 for c in sp.Poly(Q.subs(g,1),a).all_coeffs())

# Numerical illustration of the unique double root Q=Q_a=0 and an example
# of the two simple extrema; these approximate values are not the proof.
critical = sp.nsolve((Q, sp.diff(Q,a)), (a,g), (.28,.11), prec=38)
ac, gc = [float(v) for v in critical]
assert 0.28765 < ac < 0.28766 and 0.11389 < gc < 0.11390
assert sp.diff(Q,g).subs({a:ac,g:gc}) > 0
assert sp.diff(Q,a,2).subs({a:ac,g:gc}) > 0
roots = sp.nroots(Q.subs(g,sp.Rational(1,20)), maxsteps=100)
positive = sorted(float(sp.re(root)) for root in roots
                  if abs(float(sp.im(root))) < 1e-11 and sp.re(root) > 0)
assert len(positive) == 2 and 0 < positive[0] < positive[1]
print('All exact symbolic checks passed.')
print('Critical (a,g):', ac,gc)
print('Two extrema at g=1/20:', positive)
