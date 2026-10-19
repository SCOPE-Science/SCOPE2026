"""Exact checks for a Markov slice of the endpoint-tunable tent family.

Run: python verify.py
Requires: Python 3 and sympy.
This verifies transfer-operator identities and checks finite direct
orbit integrals independently of the transfer-matrix derivation.
"""
from fractions import Fraction as F
import sympy as s

b,z,x=s.symbols('b z x')
mu=(b*b+b+1)/(2*(b+1))
P=s.Matrix([
 [0,0,1-b,1-b],
 [0,0,0,-(1-b)**2],
 [b/(1-b),-b**3/(1-b)**2,1-b,1-b],
 [0,b**2/(1-b)**2,0,-(1-b)**2],
])
rho=s.Matrix([1/(1+b),0,1/(1-b*b),0])
v=s.Matrix([-mu*rho[0],rho[0],-mu*rho[2],rho[2]])
w=s.Matrix([[s.integrate(x-mu,(x,0,b)),s.integrate(x*(x-mu),(x,0,b)),
             s.integrate(x-mu,(x,b,1)),s.integrate(x*(x-mu),(x,b,1))]])
assert all(s.cancel(y)==0 for y in P*rho-rho)
assert s.factor(P.charpoly().as_expr())==(b+s.Symbol('lambda'))*(s.Symbol('lambda')-1)*(b*b*s.Symbol('lambda') + b*b-2*b*s.Symbol('lambda')+s.Symbol('lambda')**2+s.Symbol('lambda'))
assert s.cancel(rho[0]*b+rho[2]*(1-b)-1)==0
assert s.cancel(rho[0]*b*b/2+rho[2]*(1-b*b)/2-mu)==0

C0=(b*b-b+1)*(b*b+3*b+1)/(12*(b+1)**2)
C1=-(b*b-b+1)*(b*b+b+1)/(12*(b+1)**2)
C2=(b*b-b+1)*(2*b**3-b*b-b+1)/(12*(b+1)**2)
for n,expected in enumerate([C0,C1,C2]):
 assert s.cancel((w*P**n*v)[0]-expected)==0
N=(b*b-b+1)*(b*b+3*b+1+(b**4+2*b**3-2*b*b+b)*z+b**3*(b*b+b+1)*z*z)
D=12*(b+1)**2*(1+b*z)*(1+(1-b)**2*z+b*b*z*z)
G=N/D
assert s.cancel((w*(s.eye(4)-z*P).inv()*v)[0]-G)==0
var=b*(1-b)*(b*b-b+1)/(12*(1+b)**3)
assert s.cancel(2*G.subs(z,1)-C0-var)==0
Q=b**4+4*b**3-8*b*b+6*b-1
assert s.cancel(s.diff(var,b)+Q/(12*(b+1)**4))==0
# At b=2-sqrt(3), both roots of the quadratic match -b,
# and the covariance generator has a genuine cubic pole.
bstar=2-s.sqrt(3)
assert s.simplify((1-bstar)**2-2*bstar)==0
assert s.simplify(N.subs({b:bstar,z:-1/bstar}))!=0
# The unique variance peak lies in (0,1/2).
assert Q.subs(b,0)<0 and Q.subs(b,s.Rational(1,2))>0
assert s.diff(Q,b).subs(b,s.Rational(1,2))>0
assert s.diff(Q,b,2).subs(b,s.Rational(1,2))<0

# Independent exact orbit integration: start with a partition on which T^n
# is affine, split at preimages of the break at each iteration, integrate
# (x-mu)*(T^n(x)-mu) against the appropriate stationary density.
def direct_cov(beta,n):
    assert 0<beta<F(1,2)
    m=(beta*beta+beta+1)/(2*(beta+1))
    # intervals: (lo,hi,slope,intercept) for T^j(x)
    cells=[(F(0),F(1),F(1),F(0))]
    for _ in range(n):
        nxt=[]
        for lo,hi,A,B in cells:
            bounds=[lo,hi]
            if A:
                cross=(beta-B)/A
                if lo<cross<hi:bounds=[lo,cross,hi]
            for left,right in zip(bounds,bounds[1:]):
                mid=(left+right)/2
                val=A*mid+B
                if val<beta:
                    S=(1-beta)/beta; I=beta
                else:
                    S=-1/(1-beta); I=1/(1-beta)
                nxt.append((left,right,S*A,S*B+I))
        cells=nxt
    answer=F(0)
    for lo,hi,A,B in cells:
        bounds=[lo,hi]
        if lo<beta<hi: bounds=[lo,beta,hi]
        for l,r in zip(bounds,bounds[1:]):
            density=1/(1+beta) if (l+r)/2<beta else 1/(1-beta*beta)
            # (x-m)*(A*x+B-m) = A*x^2 +(B-m-A*m)*x - m*(B-m)
            poly2=A
            poly1=B-m-A*m
            poly0=-m*(B-m)
            answer += density*(poly2*(r**3-l**3)/3+poly1*(r*r-l*l)/2+poly0*(r-l))
    return answer,len(cells)

checks=0
for beta in [F(1,5),F(1,4),F(1,3),F(2,5)]:
    mat=P.subs(b,s.Rational(beta.numerator,beta.denominator))
    vv=v.subs(b,s.Rational(beta.numerator,beta.denominator))
    ww=w.subs(b,s.Rational(beta.numerator,beta.denominator))
    for n in range(9):
        direct,cells=direct_cov(beta,n)
        expected=(ww*(mat**n)*vv)[0]
        assert s.Rational(direct.numerator,direct.denominator)==expected,(beta,n,cells,direct,expected)
        checks+=1
print('PASS: symbolic transfer, density, covariance generator, asymptotic variance, and',checks,'independent exact orbit integrals')
