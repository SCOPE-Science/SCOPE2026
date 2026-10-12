from fractions import Fraction as F

# Exact example: a=0, d=3/5.
a = F(0)
d = F(3,5)
p = 1/(1-a*a)
q = 1/(1-d*d)
r = 1/(1-a*d)

assert p == F(1)
assert q == F(25,16)
assert r == F(1)

x = q/(p+q)
y = p/(p+q)
assert x == F(25,41)
assert y == F(16,41)

# With v=(5,4)/sqrt(41), W has rational entries.
W = [
    [p*x, r*F(20,41)],
    [r*F(20,41), q*y],
]
assert W == [
    [F(25,41), F(20,41)],
    [F(20,41), F(25,41)],
]

# Exact eigenvectors/eigenvalues.
uplus = [F(1),F(1)]
uminus = [F(1),F(-1)]
def mv(M,v):
    return [sum(M[i][j]*v[j] for j in range(2)) for i in range(2)]

assert mv(W,uplus) == [F(45,41),F(45,41)]
assert mv(W,uminus) == [F(5,41),F(-5,41)]
assert F(45,41)/F(5,41) == F(9)

# rho=4/5 and (1+rho)/(1-rho)=9.
rho = r*r  # temporary exact square numerator route below
rho_exact = F(4,5)
assert (1+rho_exact)/(1-rho_exact) == 9

# Determinant structural identity on several rational stable distinct pairs.
tests = [(F(0),F(3,5)), (F(1,3),F(-1,2)), (F(2,5),F(3,4))]
for aa,dd in tests:
    pp=1/(1-aa*aa)
    qq=1/(1-dd*dd)
    rr=1/(1-aa*dd)
    lhs=pp*qq-rr*rr
    rhs=(aa-dd)**2/((1-aa*aa)*(1-dd*dd)*(1-aa*dd)**2)
    assert lhs==rhs and lhs>0

# Determinant objective x(1-x) is maximized at 1/2;
# the condition optimum here is 25/41, hence genuinely different.
assert x != F(1,2)
assert x*(1-x) < F(1,4)

print("VERIFY_OK")
print("optimal_squared_weights", x, y)
print("condition_number", F(9))
