from fractions import Fraction
import math

def mat(alpha, h):
    A = 1.0 - alpha
    d2 = (alpha * h) ** 2
    return [
        [A*A, 0.0, d2],
        [-A*alpha, A/2.0, d2],
        [alpha*alpha, -alpha, 0.5+d2],
    ]

def coeffs(alpha, h):
    H = h*h
    c1 = -(1+H)*alpha*alpha + 2.5*alpha - 2.0
    c2 = (-1.5*H*alpha**3 + 1.5*H*alpha**2
          -0.5*alpha**3 + 2.0*alpha**2 - 2.75*alpha + 1.25)
    c3 = (alpha-1.0)*((alpha-1.0)**2 + 2.0*H*alpha*alpha)/4.0
    return c1, c2, c3

def jury(alpha, h):
    c1, c2, c3 = coeffs(alpha, h)
    return (
        1.0 - abs(c3),
        1.0 + c1 + c2 + c3,
        1.0 - c1 + c2 - c3,
        1.0 - c2 + c1*c3 - c3*c3,
    )

def threshold(h):
    H = h*h
    return (1.0 + math.sqrt(9.0 + 32.0*H))/(2.0*(1.0 + 4.0*H))

# Exact branch-enumeration check with rational parameters.
alpha = Fraction(2, 5)
h = Fraction(1, 3)
A = 1 - alpha
d = alpha*h
x = Fraction(7, 5)
e = Fraction(-2, 7)

branches = []
for sig in (-1, 1):
    xp = A*x - sig*d*e
    # refresh branch
    er = -alpha*x - sig*d*e
    branches.append((xp, er))
    # no-refresh branch
    en = -alpha*x + (1 - sig*d)*e
    branches.append((xp, en))

X1 = sum(u*u for u,v in branches)/4
Y1 = sum(u*v for u,v in branches)/4
Z1 = sum(v*v for u,v in branches)/4

X0, Y0, Z0 = x*x, x*e, e*e
d2 = d*d
Xm = A*A*X0 + d2*Z0
Ym = -A*alpha*X0 + A*Y0/Fraction(2,1) + d2*Z0
Zm = alpha*alpha*X0 - alpha*Y0 + (Fraction(1,2)+d2)*Z0
assert (X1, Y1, Z1) == (Xm, Ym, Zm)

# Exact determinant identity at many rational points.
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

for anum in range(1, 10):
    aa = Fraction(anum, 7)
    for hnum in range(0, 6):
        hh = Fraction(hnum, 7)
        H = hh*hh
        A = 1-aa
        d2 = (aa*hh)**2
        N = [
            [A*A, Fraction(0), d2],
            [-A*aa, A/Fraction(2), d2],
            [aa*aa, -aa, Fraction(1,2)+d2],
        ]
        Iminus = [
            [1-N[0][0], -N[0][1], -N[0][2]],
            [-N[1][0], 1-N[1][1], -N[1][2]],
            [-N[2][0], -N[2][1], 1-N[2][2]],
        ]
        lhs = det3(Iminus)
        rhs = aa*(2+aa-(1+4*H)*aa*aa)/4
        assert lhs == rhs

# Dense deterministic test of the full cubic Jury criterion.
for j in range(0, 100):
    h = 0.99*j/99 if j else 0.0
    astar = threshold(h)
    for frac in (0.01, 0.1, 0.5, 0.9, 0.999999):
        alpha = frac*astar
        vals = jury(alpha, h)
        assert min(vals) > -2e-10, (h, alpha, vals)
    for frac in (1.000001, 1.01, 1.2):
        alpha = frac*astar
        vals = jury(alpha, h)
        assert vals[1] < 2e-9, (h, alpha, vals)

# Boundary P(1)=0 and limiting values.
for h in (0.0, 0.2, 0.5, 0.9, 0.999):
    a = threshold(h)
    c1, c2, c3 = coeffs(a, h)
    assert abs(1+c1+c2+c3) < 1e-10
assert abs(threshold(0.0)-2.0) < 1e-15
assert abs((1+math.sqrt(41))/10 - 0.7403124237432849) < 1e-15

print("verification passed")
