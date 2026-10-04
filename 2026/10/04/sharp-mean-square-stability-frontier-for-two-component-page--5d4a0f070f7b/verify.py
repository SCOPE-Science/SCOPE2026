from fractions import Fraction
import math

def mat(alpha, h):
    return [
        [1.0, -2.0*alpha, alpha*alpha],
        [1.0/3.0, (2.0-4.0*alpha)/3.0, (3.0*alpha*alpha-2.0*alpha)/3.0],
        [1.0/3.0, -2.0*alpha/3.0,
         (2.0-4.0*alpha+3.0*alpha*alpha+2.0*alpha*alpha*h*h)/3.0],
    ]

def coeffs(alpha, h):
    H = h*h
    c1 = -(1.0+2.0*H/3.0)*alpha*alpha + 8.0*alpha/3.0 - 7.0/3.0
    c2 = -(2.0/3.0+8.0*H/9.0)*alpha**3 + (8.0/3.0+10.0*H/9.0)*alpha*alpha - 34.0*alpha/9.0 + 16.0/9.0
    c3 = 4.0*(alpha-1.0)*((alpha-1.0)**2+H*alpha*alpha)/9.0
    return c1,c2,c3

def jury(alpha, h):
    c1,c2,c3 = coeffs(alpha,h)
    return (
        1.0-abs(c3),
        1.0+c1+c2+c3,
        1.0-c1+c2-c3,
        1.0-c2+c1*c3-c3*c3,
    )

def threshold(h):
    H=h*h
    return (3.0+math.sqrt(25.0+32.0*H))/(4.0*(1.0+2.0*H))

# Exact rational branch enumeration.
alpha = Fraction(2,5)
h = Fraction(1,3)
x = Fraction(7,5)
y = Fraction(-3,7)
xp = x-alpha*y

branches = []
# Refresh probability 1/3.
branches.append((Fraction(1,3), xp, xp))
# Recursive branch probability 2/3 split equally across sigma=+/-.
for sig in (-1,1):
    yp = (1-alpha*(1+sig*h))*y
    branches.append((Fraction(1,3), xp, yp))

X1 = sum(w*u*u for w,u,v in branches)
Y1 = sum(w*u*v for w,u,v in branches)
Z1 = sum(w*v*v for w,u,v in branches)

X0,Y0,Z0 = x*x,x*y,y*y
H = h*h
Xm = X0-2*alpha*Y0+alpha*alpha*Z0
Ym = Fraction(1,3)*X0 + (Fraction(2)-4*alpha)/3*Y0 + (3*alpha*alpha-2*alpha)/3*Z0
Zm = Fraction(1,3)*X0 - 2*alpha/3*Y0 + (2-4*alpha+3*alpha*alpha+2*alpha*alpha*H)/3*Z0
assert (X1,Y1,Z1) == (Xm,Ym,Zm)

# P(1) identity and full Jury grid.
for j in range(100):
    h = 0.99*j/99 if j else 0.0
    astar = threshold(h)
    for frac in (0.001,0.1,0.5,0.9,0.999999):
        a = frac*astar
        vals = jury(a,h)
        assert min(vals) > -2e-9, (h,a,vals)
        c1,c2,c3 = coeffs(a,h)
        p1 = 1+c1+c2+c3
        formula = a*(2+3*a-2*(1+2*h*h)*a*a)/9
        assert abs(p1-formula) < 2e-12
    for frac in (1.000001,1.01,1.2):
        a = frac*astar
        vals = jury(a,h)
        assert vals[1] < 2e-8, (h,a,vals)

# Boundary and endpoint values.
for h in (0.0,0.2,0.5,0.9,0.999):
    a = threshold(h)
    c1,c2,c3 = coeffs(a,h)
    assert abs(1+c1+c2+c3) < 2e-10
assert abs(threshold(0.0)-2.0) < 1e-14
assert abs((3+math.sqrt(57))/12 - 0.8791528696058958) < 1e-14

print("verification passed")
