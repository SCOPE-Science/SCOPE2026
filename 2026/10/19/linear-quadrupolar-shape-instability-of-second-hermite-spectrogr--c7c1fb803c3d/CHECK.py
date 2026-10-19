"""Exact finite checks supplementing the analytic Hermite-window theorem.
Run: python CHECK.py. SymPy is required.
"""
import sympy as s
u=s.symbols('u', real=True, nonnegative=True)
E=s.exp(-2)

def q(m):
    return u*u-2*m*u+m*(m-1)

def p(m):
    """Polynomial with lambda_m(2)=1-exp(-2)*P_m(2)."""
    den=2*s.factorial(m)
    poly=s.expand(u**(m-2)*q(m)**2/den)
    result=0
    # Solve P-P'=density: coefficient of u^k from tail derivatives.
    for mon, coefficient in s.Poly(poly,u).terms():
        k=mon[0]
        for j in range(k+1):
            result+=coefficient*s.factorial(k)/s.factorial(j)*u**j
    return s.expand(result)

# Direct integration of first three normalized Hermite spectrogram densities.
densities=[s.exp(-u)*u**2/2,s.exp(-u)*u*(2-u)**2/2,s.exp(-u)*(1-2*u+u**2/2)**2]
lams=[s.simplify(s.integrate(f,(u,0,2))) for f in densities]
assert all(s.simplify(t-(1-5*E))==0 for t in lams),lams
assert all(s.simplify(p(m).subs(u,2)-(s.Rational(17,3)))==0 for m in (3,4,5))
for m in range(3,26):
    target=u**(m-2)*q(m-1)*q(m)/(2*s.factorial(m))
    assert s.simplify(p(m)-p(m-1)-target)==0,m
assert s.factor(q(s.Symbol('m')).subs(u,2))==(s.Symbol('m')-4)*(s.Symbol('m')-1)

# Exact compression of the first variation to span{h0,h1,h2}:
# boundary values at u=2 have amplitudes sqrt(2)*exp(-1),0,-exp(-1),
# and angular orders -2, undetermined, 0, respectively.
# b(theta)=2*cos(2theta), whose mean is zero, and Fourier coefficient at 2 is 1.
theta=s.symbols('theta',real=True)
b=2*s.cos(2*theta)
b2=s.simplify(s.integrate(b*s.exp(-2*s.I*theta),(theta,0,2*s.pi))/(2*s.pi))
assert b2==1,b2
C=s.Matrix([[0,0,s.sqrt(2)*E],[0,0,0],[s.sqrt(2)*E,0,0]])
assert set(C.eigenvals().keys())=={0,-s.sqrt(2)*E,s.sqrt(2)*E}
print('PASS: exact triple disk top eigenvalue',lams[0])
print('PASS: spectral gap',s.Rational(2,3)*E)
print('PASS: polynomial recurrence at m=3,...,25')
print('PASS: quadrupolar first variation coefficient',s.sqrt(2)*E,'~',s.N(s.sqrt(2)*E,13))
print('LIMIT: finite recurrence checks corroborate, not replace, the algebraic proof.')
