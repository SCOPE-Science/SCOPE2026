"""Independent finite symbolic and geometric checks for a random cyclic quadrilateral.

Requires Python 3, SymPy. No external data or services are needed.
"""
import math
import random
import sympy as s

x, y = s.symbols('x y'); pi = s.pi
f = lambda t: s.sin(pi*t)
g = lambda t: s.sin(2*pi*t)

def one(h):
    return s.simplify(3*s.integrate((1-x)**2*h(x), (x,0,1)))

def two(h,k):
    inner=s.integrate((1-x-y)*k(y), (y,0,1-x))
    return s.simplify(6*s.integrate(h(x)*inner, (x,0,1)))

def check(name, actual, claimed):
    residue = s.trigsimp(s.simplify(s.expand_trig(actual-claimed)))
    assert residue==0, (name, residue)
    print(f'{name}: OK')

m_f=one(f); m_g=one(g)
check('E(sin pi D)', m_f, 3/pi-12/pi**3)
check('E(sin 2pi D)',m_g,3/(2*pi))
check('E(sin^2 pi D)',one(lambda t:f(t)**2),s.Rational(1,2)-3/(4*pi**2))
check('E(sin^2 2pi D)',one(lambda t:g(t)**2),s.Rational(1,2)-3/(16*pi**2))
check('E(sin pi D sin 2pi D)',one(lambda t:f(t)*g(t)),8/(3*pi**2))
check('E(sin pi D1 sin pi D2)',two(f,f),3/pi**2)
check('E(sin 2pi D1 sin 2pi D2)',two(g,g),s.Rational(9,4)/pi**2)
check('E(sin pi D1 sin 2pi D2)',two(f,g),3/pi**2)

EP=8*m_f
EA=2*m_g
EP2=16*one(lambda t:f(t)**2)+48*two(f,f)
EA2=one(lambda t:g(t)**2)+3*two(g,g)
EPA=4*one(lambda t:f(t)*g(t))+12*two(f,g)
check('E(P)',EP,24*(pi**2-4)/pi**3)
check('E(A)',EA,3/pi)
check('E(P^2)',EP2,8+132/pi**2)
check('E(A^2)',EA2,s.Rational(1,2)+105/(16*pi**2))
check('E(PA)',EPA,140/(3*pi**2))
check('Var(P)',EP2-EP**2,8-444/pi**2+4608/pi**4-9216/pi**6)
check('Var(A)',EA2-EA**2,(8*pi**2-39)/(16*pi**2))
check('Cov(P,A)',EPA-EP*EA,4*(216-19*pi**2)/(3*pi**4))
assert (216-19*math.pi**2)>0

# Independent direct Cartesian geometry and iid-circle sampling check.
rng=random.Random(20261003)
samples=150000
sum_p=sum_a=sum_pa=0.0
for _ in range(samples):
    angles=sorted(2*math.pi*rng.random() for j in range(4))
    vertices=[(math.cos(t),math.sin(t)) for t in angles]
    perimeter=sum(math.dist(vertices[j],vertices[(j+1)%4]) for j in range(4))
    area=abs(sum(vertices[j][0]*vertices[(j+1)%4][1]-vertices[(j+1)%4][0]*vertices[j][1] for j in range(4)))/2
    gaps=[((angles[(j+1)%4]-angles[j])%(2*math.pi))/(2*math.pi) for j in range(4)]
    p2=2*sum(math.sin(math.pi*d) for d in gaps)
    a2=sum(math.sin(2*math.pi*d) for d in gaps)/2
    assert abs(perimeter-p2)<1e-12 and abs(area-a2)<1e-12
    sum_p+=perimeter;sum_a+=area;sum_pa+=perimeter*area
cov_MC=sum_pa/samples-(sum_p/samples)*(sum_a/samples)
cov_exact=float((EPA-EP*EA).evalf(20))
print(f'Monte Carlo covariance {cov_MC:.9f}, exact {cov_exact:.9f}')
assert abs(cov_MC-cov_exact)<0.03
print('All 16 exact symbolic identities and geometric cross-checks passed.')
