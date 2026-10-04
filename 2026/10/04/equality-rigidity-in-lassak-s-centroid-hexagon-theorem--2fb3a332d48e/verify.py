from fractions import Fraction as F

# Exact algebraic consistency checks for the equality analysis.
def f(w,z):
    return 28*z*z*(w*w-3*w+2)+20*z*w*(2-w)+w*w*(7*w*w+3*w-34)

def fac(w,z):
    return (w-2)*(7*w**3+17*w*w+28*w*z*z-20*w*z-28*z*z)

# Degree bounds are deg_w <= 4, deg_z <= 2. Equality on a 5 x 3
# rational grid therefore certifies the polynomial identity by interpolation.
for w in map(F, range(5)):
    for z in map(F, range(3)):
        assert f(w,z) == fac(w,z)

def q(w,z):
    return 7*w**3+17*w*w+28*w*z*z-20*w*z-28*z*z

def completion_lhs(w,z):
    return 7*(w-1)*q(w,z)

def completion_rhs(w,z):
    return (196*(w-1)*(w-1)*z*z
            -140*w*(w-1)*z
            +25*w*w
            +w*w*(7*w-8)*(7*w+18))

for w in map(F, range(5)):
    for z in map(F, range(3)):
        assert completion_lhs(w,z) == completion_rhs(w,z)

# The threshold polynomial p has its relevant root strictly above 8/7.
def p(w): return w**3+w*w-2*w-4
def dp(w): return 3*w*w+2*w-2
assert p(F(8,7)) == F(-1196,343)
assert dp(F(8,7)) > 0
# dp is increasing for w >= 8/7 because d2p = 6w+2 > 0.

# Low-branch strict deficit identity, checked after clearing denominators.
def cenP_num(w): return w**4+w**3-2*w*w-4*w+8
def cenP_den(w): return 3*w*(w*w+3*w+4)
def r(w): return 7*w**3+17*w*w+8*w-28
for w in map(F, [1,2,3,4,5]):
    lhs = 4*cenP_den(w) - 21*cenP_num(w)
    rhs = -3*(w-2)*r(w)
    assert lhs == rhs
assert r(F(1)) == 4
# r'(w)=21w^2+34w+8 is positive for every w >= 1.

# Exact shoelace area and centroid of the normalized extremal pentagon.
pts=[(F(0),F(2)),(F(-2),F(0)),(F(-1),F(-1)),(F(1),F(-1)),(F(2),F(0))]
a2=F(0); nx=F(0); ny=F(0)
for (x1,y1),(x2,y2) in zip(pts, pts[1:]+pts[:1]):
    cr=x1*y2-x2*y1
    a2 += cr
    nx += (x1+x2)*cr
    ny += (y1+y2)*cr
area=a2/2
cx=nx/(3*a2)
cy=ny/(3*a2)
assert area == 7
assert cx == 0
assert cy == F(4,21)

print('VERIFY_OK centroid-hexagon equality rigidity')
