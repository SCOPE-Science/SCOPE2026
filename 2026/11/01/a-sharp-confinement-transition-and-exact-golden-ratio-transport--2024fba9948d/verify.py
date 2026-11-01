"""Exact symbolic checks for remainder-added linear map transport identities.

Run: python verify.py  (SymPy required). Analytical orbit and measure proofs are in RESULT.md.
"""
from fractions import Fraction
import sympy as s

z=s.sqrt(5)
phi=(1+z)/2
t=s.simplify(1/phi)
mu=z/5
low=s.simplify((1+t)/(1+t**2))
high=s.simplify(1/(1+t**2))
x=s.symbols('x',real=True)
zero=lambda v:s.simplify(v)==0
assert zero(phi**2-phi-1)
assert zero(t-phi+1)
assert zero(low*t+high*(1-t)-1)
assert zero(low*t**2/2+high*(1-t**2)/2-mu)
# Lebesgue transfer on affine branch densities a_i*x+b_i.
L=s.Matrix([
 [1/phi**2,0,1/phi**2,0],
 [0,1/phi,1/phi**2,1/phi],
 [1/phi**2,0,0,0],
 [0,1/phi,0,0],
]).applyfunc(s.simplify)
h=s.Matrix([0,low,0,high])
assert all(zero(v) for v in L*h-h)
assert all(zero(v) for v in s.Poly(s.expand(L.charpoly().as_expr()-s.prod([s.Symbol('lambda')-e for e in (1,t,-t**2,-t**3)])),s.Symbol('lambda')).all_coeffs())
g0=s.Matrix([low,-mu*low,high,-mu*high])
assert all(zero(q) for q in (L*L-t**3*L-t**3*s.eye(4))*g0)
p=s.Matrix([[
 s.integrate((x-mu)*x,(x,0,t)),
 s.integrate((x-mu),(x,0,t)),
 s.integrate((x-mu)*x,(x,t,1)),
 s.integrate((x-mu),(x,t,1)),
]]).applyfunc(s.simplify)
A=s.Rational(1,2)-z/5
B=(z-2)/10
cov=lambda n:s.simplify(A*t**n+B*(-t**2)**n)
for n in range(16):
    assert zero((p*L**n*g0)[0]-cov(n)),n
assert zero(cov(0)-(3-z)/10)
assert zero(cov(1)-(z-2)/10)
sigma=s.simplify(cov(0)+2*(A*t/(1-t)+B*(-t*t)/(1+t*t)))
assert zero(sigma-(5+3*z)/50)
# The two expressions for all finite n variance agree identically on checked n.
for n in range(1,16):
    direct=s.simplify(n*cov(0)+2*sum((n-j)*cov(j) for j in range(1,n)))
    gh=lambda r:s.simplify((r*((n-1)-n*r)+r**(n+1))/(1-r)**2)
    closed=s.simplify(n*cov(0)+2*A*gh(t)+2*B*gh(-t*t))
    assert zero(direct-closed),n
# Exact digit-displacement for integer slopes, independent of smoothness.
for a in [1,2,3,7]:
    m=a+1
    for denom in [3,7,13,19]:
        for nom in range(denom):
            u=Fraction(nom,denom)
            X=Fraction(nom,a*denom)
            sumdigits=0
            for n in range(1,19):
                digit=(m*u).__floor__()
                un=m*u-digit
                Xnew=X+u
                sumdigits+=digit
                assert a*(Xnew-Fraction(nom,a*denom))==sumdigits+un-Fraction(nom,denom)
                u=un;X=Xnew
print('PASS: invariant density, transfer matrix, 16 autocovariances, exact variance law, digit transport identity')
