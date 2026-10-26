#!/usr/bin/env python3
"""Exact arithmetic certificates for the two row-equivalent Kaczmarz systems."""
from sympy import Matrix, Rational, sqrt, eye, simplify

Q = Rational
p = Q(1, 4)
q = Q(1, 3)
E = eye(2)
U = Matrix([[1, 1], [1, -1]]) / sqrt(2)
A = Matrix([[Q(1, 2), 0], [0, sqrt(3) / 2]])
B = U * A
assert simplify(A.T * A - B.T * B) == Matrix.zeros(2)
assert simplify(U.T * U - E) == Matrix.zeros(2)

def H(P):
    return (E - P).row_join(E).col_join((-q * P).row_join(E))

# Axis-aligned frame: the first error coordinate is selected with probability 1/4.
H0 = Matrix([[1, 1], [0, 1]])
H1 = Matrix([[0, 1], [-q, 1]])
W = Matrix([[Q(1,10), 0], [0, 1]])
Delta = (1-p) * H0.T*W*H0 + p*H1.T*W*H1-W
assert Delta == Matrix([[Q(1,360), -Q(1,120)], [-Q(1,120), Q(1,10)]])
Strict = Delta-W/100
assert Strict == Matrix([[Q(2,1125), -Q(1,120)], [-Q(1,120), Q(9,100)]])
assert Strict[0,0] > 0 and Strict.det() == Q(163,1800000) > 0

# Mixed-row frame: both row projectors occur with probability 1/2.
u_plus = Matrix([Q(1, 2), sqrt(3)/2])
u_minus = Matrix([Q(1, 2), -sqrt(3)/2])
Pplus = u_plus * u_plus.T
Pminus = u_minus * u_minus.T
assert simplify((Pplus + Pminus)/2 - A.T*A) == Matrix.zeros(2)
order = [0,2,1,3]  # from (x1,x2,y1,y2) to (x1,y1,x2,y2)
Hp = H(Pplus).extract(order, order)
Hm = H(Pminus).extract(order, order)
C = Matrix([[Q(34,5),-Q(39,10),0,0],
            [-Q(39,10),Q(384,5),0,0],
            [0,0,Q(26,5),-Q(31,10)],
            [0,0,-Q(31,10),Q(88,5)]])
assert simplify((Hp.T*C*Hp + Hm.T*C*Hm)/2 - C + eye(4)) == Matrix.zeros(4)
assert C[0,0] > 0 and C[:2,:2].det() == Q(50703,100) > 0
assert C[2,2] > 0 and C[2:4,2:4].det() == Q(8191,100) > 0
assert sum(C[i,i] for i in range(4)) == Q(532,5)

# The common first moment has only stable complex eigenpairs.
for g, radius_squared in [(p,Q(5,6)),(1-p,Q(1,2))]:
    F = Matrix([[1-g,1],[-g/3,1]])
    t = F.trace()
    assert simplify(F.det()-radius_squared) == 0
    assert t*t-4*F.det() < 0 and 0 < F.det() < 1
print('VERIFY_OK: exact equal-Gram row rotation, expanding and contracting second-moment certificates, common stable signed mean')
