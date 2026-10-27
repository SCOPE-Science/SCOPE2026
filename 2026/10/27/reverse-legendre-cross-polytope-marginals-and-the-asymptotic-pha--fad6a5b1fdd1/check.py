"""Independent exact moment and Fourier checks for the cross-polytope diagonal marginal."""
import sympy as sp
import mpmath as mp
from math import factorial, comb, pi
x=sp.symbols('x',real=True)
for d in range(1,17):
    p=sp.cancel(sp.Rational(d,2**d)*x**(d-1)*sp.legendre(d-1,1/x)).expand()
    for j in range(13):
        lhs=sp.integrate(p*x**(2*j),(x,-1,1))
        rhs=sp.Rational(factorial(d)*factorial(2*j)*comb(j+d-1,d-1),factorial(d+2*j))
        assert sp.simplify(lhs-rhs)==0,(d,j)
    assert p.subs(x,1)==sp.Rational(d,2**d)
    assert sp.simplify(p.diff(x).subs(x,1)/p.subs(x,1)+sp.Rational((d-1)*(d-2),2))==0
print('exact_moment_checks: 208 passed, d=1..16, j=0..12')
mp.mp.dps=45
for d in (3,5,8):
    poly=sp.Poly(sp.cancel(sp.Rational(d,2**d)*x**(d-1)*sp.legendre(d-1,1/x)),x)
    coefs=[mp.mpf(str(v.p))/mp.mpf(str(v.q)) for v in reversed(poly.all_coeffs())]
    def f_quad(t):return mp.quad(lambda s: mp.polyval(list(reversed(coefs)),s)*mp.cos(t*s),[-1,0,1])
    def f_mom(t):return mp.hyper([d],[(d+1)/2,(d+2)/2],-t*t/4)
    for t in (mp.mpf('.6'),mp.mpf('2.2'),mp.mpf('7.3'),mp.mpf('12.1')):
        err=abs(f_quad(t)-f_mom(t))
        assert err<mp.mpf('1e-36'),(d,t,err)
print('independent_integral_vs_hypergeometric: 12 passed')
for d in (3,4,5,8,11):
    F=lambda z:mp.hyper([d],[(d+1)/2,(d+2)/2],-z*z/4)
    c=(d-1)*(d-2)/2
    for n in (60,120,240):
        N=n*mp.pi
        root=mp.findroot(F,(N+mp.mpf(c)/N-mp.mpf('.02'),N+mp.mpf(c)/N+mp.mpf('.02')),solver='secant',verify=True,maxsteps=100)
        assert root>N and root<(n+1)*mp.pi
        assert abs(root-N-mp.mpf(c)/N)<mp.mpf('2.5e-3'),(d,n,root-N)
print('large_frequency_root_checks: 15 passed; each near n*pi with computed shift')
print('all_checks: passed')
