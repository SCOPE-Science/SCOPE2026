"""Finite consistency checks for the two-channel Stuart--Landau polygon theorem.

The universal theorem is analytical; these tests do not replace its proof.
Run with: python verify.py
Requires Python 3 standard library only.
"""
import cmath
import math
from fractions import Fraction

checks = 0

def require(test, explanation):
    global checks
    checks += 1
    if not test:
        raise AssertionError(explanation)

def roots(alpha, x, y, h):
    q = alpha * complex(x, y)
    abar = alpha * complex(1, -h)
    b = 2 * alpha - q
    discriminant = b*b + 4 * q * abar
    return ((-b + cmath.sqrt(discriminant))/2,
            (-b - cmath.sqrt(discriminant))/2)

def stable(x, y, h):
    if x >= 1:
        return False
    return (1-x) * (y-2*h)**2 > (2-x)**2 * (x+h*h)

def mul(a,b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])

def add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def neg(a):
    return (-a[0], -a[1])

for x,h,y in [(Fraction(3,4),Fraction(1,2),Fraction(7,2)),
              (Fraction(3,4),Fraction(1,2),Fraction(-3,2)),
              (Fraction(1,2),Fraction(0),Fraction(3,2)),
              (Fraction(1,2),Fraction(0),Fraction(-3,2)),
              (Fraction(0),Fraction(1),Fraction(4))]:
    require((1-x)*(y-2*h)**2 == (2-x)**2*(x+h*h), 'exact stability boundary')
    s = (y-h*x)/(2-x)
    lam=(Fraction(0),s)
    coeff=(2-x,-y)
    q=(x,y)
    abar=(Fraction(1),-h)
    p=add(add(mul(lam,lam),mul(coeff,lam)),neg(mul(q,abar)))
    require(p==(0,0), 'exact imaginary root of quadratic')

for m in (3,4,5,6,7,8,11,17):
    theta=[2*math.pi*j/m for j in range(m)]
    phase2=[cmath.exp(2j*t) for t in theta]
    for alpha in (.23,1.,2.7):
        for x in (0.,.13,.49,.77,.95,1.,1.2,2.3):
            for h in (-2.,-.6,0.,.4,1.7):
                for y in (-15.,-5.,-2.,-.7,0.,.9,3.,6.,15.):
                    rr=roots(alpha,x,y,h)
                    sign=stable(x,y,h)
                    if abs((1-x)*(y-2*h)**2-(2-x)**2*(x+h*h))>1e-8:
                        require((max(z.real for z in rr)<-1e-9)==sign,
                                'exact stability inequality disagrees with roots')
                    # Fourier coefficients of the real-linear Jacobian are verified
                    # independently for several arbitrary complex perturbations.
                    q=alpha*complex(x,y)
                    A=alpha*complex(1,h)
                    for seed in (1,2):
                        zz=[complex(math.sin(seed*(j+1)),math.cos((seed+2)*(j+1))) for j in range(m)]
                        mean=sum(zz)/m
                        outgoing=[-A*(zz[j]+phase2[j]*zz[j].conjugate())+q*mean for j in range(m)]
                        ak=[sum(zz[j]*cmath.exp(-1j*k*theta[j]) for j in range(m))/m for k in range(m)]
                        actual=[sum(outgoing[j]*cmath.exp(-1j*k*theta[j]) for j in range(m))/m for k in range(m)]
                        predicted=[-A*ak[k]-A*ak[(2-k)%m].conjugate()+(q*ak[0] if k==0 else 0) for k in range(m)]
                        require(max(abs(v-w) for v,w in zip(actual,predicted)) < 5e-12, 'Fourier Jacobian identity')
print('PASS:',checks,'finite checks; proof of universal statement is in RESULT.md')
