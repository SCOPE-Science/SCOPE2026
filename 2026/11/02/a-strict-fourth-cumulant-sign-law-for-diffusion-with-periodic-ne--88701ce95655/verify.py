"""Reproduction checks for the periodic local-resetting renewal theorem.
Requires Python 3, sympy and mpmath. Prints PASS only after all assertions.
"""
import sympy as sp
import mpmath as mp

x = sp.symbols('x', positive=True, real=True)
u = sp.sinh(x); h = sp.cosh(x); c = sp.cosh(2*x)
H = 2*u**3 + 6*u - 3*x*(u**2 + 2)
assert sp.simplify(2*H - (sp.sinh(3*x)+9*u-3*x*sp.cosh(2*x)-9*x)) == 0
assert sp.series(H,x,0,8).expand().coeff(x,5) == sp.Rational(1,20)
assert sp.simplify(c-1-2*u**2)==0
for n in range(2,101):
    assert 9**n+3 > (2*n+1)*4**n
for n in range(1,101):
    assert 2**(2*n-1)*(2*n+1)>2

mp.mp.dps=60
count=0
for D, ell, r in [(1,1,.01),(1,1,.05),(1,1,.2),(1,1,1),(1,1,4),(1,1,16),(1,1,100),(2.3,.7,1.7)]:
    D=mp.mpf(str(D));ell=mp.mpf(str(ell));r=mp.mpf(str(r))
    alpha=ell*mp.sqrt(r/D)/2
    U=mp.sinh(alpha); H0=mp.cosh(alpha); C=mp.cosh(2*alpha)
    def phi(t):
        z=ell*mp.sqrt((r+t)/D)/2
        return (t+r*mp.cosh(z))/(t*mp.cosh(2*z)+r*mp.cosh(z))
    m=2*U**2/(r*H0)
    var=(4*U**2*H0**2-2*alpha*U*(U**2+2))/(r**2*H0**2)
    C2=ell**2/m
    C4=ell**4*(3*var-2*m**2)/m**3
    C4_alt=r*ell**4*H0*(2*U**3+6*U-3*alpha*(U**2+2))/(4*U**5)
    mt=-mp.diff(phi,0)
    var_t=mp.diff(phi,0,2)-mt**2
    assert mp.almosteq(m,mt,rel_eps=mp.mpf('1e-40')),(r,'m',m,mt)
    assert mp.almosteq(var,var_t,rel_eps=mp.mpf('1e-40')),(r,'v',var,var_t)
    assert mp.almosteq(C4,C4_alt,rel_eps=mp.mpf('1e-37')),(r,'C4',C4,C4_alt)
    assert mp.mpf(2)/3 < var/m**2 < 1
    assert C4>0
    # Independent implicit-root check by matching analytic Taylor coefficients.
    # log phi(z) + log cosh(ell*k) = 0.
    A=ell**2/(2*m)
    B=ell**4*(var/(8*m**3)-1/(12*m))
    for k in [mp.mpf('0.0002'),mp.mpf('0.0006'),mp.mpf('0.001')]:
        p=A*k**2+B*k**4
        resid=mp.log(phi(p))+mp.log(mp.cosh(ell*k))
        assert abs(resid)<mp.mpf('20')*k**6
        count+=1
    # Published diffusivity formula equivalence.
    Deff=D*alpha**2*H0/U**2
    assert mp.almosteq(C2/2,Deff,rel_eps=mp.mpf('1e-40'))
    count+=6

print('PASS: symbolic coefficient inequalities, moment identities, SCGF Taylor residual, '+str(count)+' numerical assertions')
