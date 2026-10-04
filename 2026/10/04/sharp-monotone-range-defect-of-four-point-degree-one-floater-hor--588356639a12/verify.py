from fractions import Fraction as F

# Published uniform-grid d=1 formula gives weights proportional to (-1,2,-2,1).
w = [F(-1), F(2), F(-2), F(1)]

# Evaluate the barycentric cardinal coefficients exactly away from nodes.
def basis(x):
    den = sum(wj / (x - F(j)) for j, wj in enumerate(w))
    return [(wj / (x - F(j))) / den for j, wj in enumerate(w)]

# Midpoint of the left cell.
L = basis(F(1,2))
assert L == [F(15,38), F(15,19), F(-5,19), F(3,38)]
assert sum(L, F(0)) == 1

# Strictly positive strictly increasing witness.
y = [F(1,100), F(2,100), F(98,100), F(99,100)]
val = sum(a*b for a,b in zip(L,y))
assert val == F(-4,25)

# Step extremizer at x=1/2 already has defect 7/38.
ystep = [F(0), F(0), F(1), F(1)]
step_half = sum(a*b for a,b in zip(L,ystep))
assert step_half == F(-7,38)

# Coefficients for monotone increments at rational x.
def coeffs(x):
    D = x*x - 3*x + 6
    c1 = x*(x*x - 5*x + 8)/D
    c2 = -x*(x-4)*(x-1)/D
    c3 = x*(x-2)*(x-1)/D
    return F(1), c1, c2, c3, F(0)

for x in [F(1,4),F(1,2),F(3,4),F(5,4),F(3,2),F(7,4),F(9,4),F(5,2),F(11,4)]:
    B = basis(x)
    C = coeffs(x)
    assert C[1] == B[1]+B[2]+B[3]
    assert C[2] == B[2]+B[3]
    assert C[3] == B[3]

# Exact middle-cell domination bound: 7/38 > 8/(45 sqrt(3)).
# Square both positive sides.
assert F(49,38*38) > F(64,45*45*3)

# Critical quartic and algebraic defect polynomial.
def q(x):
    return x**4 - 6*x**3 + 29*x**2 - 60*x + 24

def p(z):
    return 15*z**4 + 30*z**3 + 671*z**2 + 656*z - 144

# Rational brackets around the unique roots quoted in the text.
ta = F(51623280849514,10**14)
tb = F(51623280849515,10**14)
assert q(ta) > 0 and q(tb) < 0

da = F(18441311642852,10**14)
db = F(18441311642854,10**14)
assert p(da) < 0 and p(db) > 0

# Directly map the tau bracket through g and enclose the delta bracket.
def g(x):
    return x*(4-x)*(1-x)/(x*x-3*x+6)
ga, gb = g(ta), g(tb)
lo, hi = min(ga,gb), max(ga,gb)
# tau is at a maximum, so endpoint images lie just below delta; both are close.
assert lo > F(1844131164284,10**13)
assert hi < F(1844131164286,10**13)

# Reflection identity for the defect-driving coefficient.
for x in [F(1,10),F(1,2),F(9,10)]:
    c2x = coeffs(x)[2]
    c2r = coeffs(3-x)[2]
    assert c2r == 1-c2x

print('VERIFY_OK')
