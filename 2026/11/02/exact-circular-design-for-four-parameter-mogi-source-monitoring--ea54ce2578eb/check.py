"""Symbolic and exact-arithmetic checks for circular Mogi-source information design.

Requires Python 3 and SymPy. Execute: python check.py
The general angular optimality argument is proved in RESULT.md, not by sampling.
"""
from sympy import (Matrix, Rational, symbols, simplify, factor, diff,
                   sqrt, exp, I, pi, N, zeros)

amp, depth, rad = symbols('amp depth rad', positive=True)
cx, cy = symbols('cx cy', real=True)
par = (amp, depth, cx, cy)

def station_jacobian(x, y):
    L = (x-cx)**2+(y-cy)**2+depth**2
    mean = Matrix([amp*(x-cx)/L**Rational(3,2),
                   amp*(y-cy)/L**Rational(3,2),
                   amp*depth/L**Rational(3,2)])
    return mean.jacobian(par).subs({cx: 0, cy: 0})

def info(positions):
    return sum((j.T*j for x,y in positions for j in [station_jacobian(x,y)]),
               zeros(4,4))

# Four equally spaced sites make exact rational-trigonometric symbolic
# calculations possible without approximating angles.
F = info(((rad,0),(0,rad),(-rad,0),(0,-rad)))
R2 = rad**2+depth**2
want = Matrix([
    [4/R2**2, -8*amp*depth/R2**3, 0, 0],
    [-8*amp*depth/R2**3, 4*amp**2*(rad**2+4*depth**2)/R2**4,0,0],
    [0,0,4*amp**2*(depth**2+Rational(5,2)*rad**2)/R2**4,0],
    [0,0,0,4*amp**2*(depth**2+Rational(5,2)*rad**2)/R2**4]
])
assert (F-want).applyfunc(simplify) == zeros(4,4)
formula = 4**4*amp**6*rad**2*(depth**2+Rational(5,2)*rad**2)**2/R2**14
assert simplify(F.det()-formula)==0

# An equilateral three-site network also has both angular moments zero.
tri = ((rad,0), (-rad/2,sqrt(3)*rad/2),
       (-rad/2,-sqrt(3)*rad/2))
F3=info(tri)
want3=want*Rational(3,4)
assert (F3-want3).applyfunc(simplify) == zeros(4,4)

# Verify angular first/second moment necessity and strict angular loss
# for a deliberately unbalanced four-station geometry at exact parameters.
F_bad=info(((rad,0),(rad,0),(-rad,0),(0,-rad)))
subs={amp:2,depth:3,rad:1}
fb=F_bad.subs(subs)
fo=F.subs(subs)
assert fb.det()>=0
assert fo.det()>fb.det()

z=symbols('z',positive=True)
shape=z*(1+Rational(5,2)*z)**2/(1+z)**14
assert simplify(diff(shape,z)+(5*z+2)*(55*z**2+11*z-2)/(4*(1+z)**15)) == 0
zs=(sqrt(561)-11)/110
assert simplify(55*zs**2+11*zs-2)==0
assert 0<N(zs)<Rational(1,5)
print('PASS: four-site and three-site exact information matrices')
print('PASS: determinant formula and angular imbalance inequality')
print('PASS: derivative factorization and unique positive-radius root')
print('Optimal radius/depth =', N(sqrt(zs),18))
