"""Exact rational verification of the stated two-patch competition witness.

The universal parameter theorem is proved analytically in RESULT.md; this
standalone standard-library checker validates only its rational example.
"""
from fractions import Fraction as F

P1, P2, d, e = F(1), F(1), F(1,4), F(15,26)
Q1, Q2 = F(2), F(1)
m1, m2 = F(17,8), F(3,4)
V1, V2 = F(27,13), F(45,52)


def det(M):
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]


def trace(M):
    return M[0][0]+M[1][1]


def resident_flow(z1,z2):
    return (d*(z2/P2-z1/P1)+z1*(m1-z1),
            d*(z1/P1-z2/P2)+z2*(m2-z2))


def invader_flow(z1,z2):
    return (e*(z2/Q2-z1/Q1)+z1*(m1-z1),
            e*(z1/Q1-z2/Q2)+z2*(m2-z2))

assert resident_flow(Q1,Q2) == (0,0)
assert invader_flow(V1,V2) == (0,0)
a = d*(Q1/P1-Q2/P2)
assert a==F(1,4)
assert (m1-Q1,m2-Q2)==(a/Q1,-a/Q2)
Lv = [[m1-Q1-e/Q1,e/Q2],[e/Q1,m2-Q2-e/Q2]]
assert Lv == [[F(-17,104),F(15,26)],[F(15,52),F(-43,52)]]
assert det(Lv)== -a*a/(Q1*Q2) == F(-1,32)
Lu = [[m1-V1-d/P1,d/P2],[d/P1,m2-V2-d/P2]]
assert Lu == [[F(-21,104),F(1,4)],[F(1,4),F(-19,52)]]
assert det(Lu)==F(61,5408)>0
assert trace(Lu)==F(-59,104)<0
assert Q1/P1!=Q2/P2 and Q1>0 and Q2>0
# Verify the exact positive determinant decomposition.
t1,t2 = V1/Q1,V2/Q2
D=t1-t2
assert t1>1 and D>0
bracket=d*(Q1*t1/P1-Q2*t2/P2)-e*D
assert bracket==Q1*Q1*t1*(t1-1)+d*Q2*D/P2>0
assert det(Lu)==e*D*bracket/(Q1*Q2*t1*t2)
alpha=-(d/(P1*P2))*(Q2/Q1+Q1/Q2)
assert alpha==F(-5,8)<0
# Exact spectral signs: negative determinant implies one positive real root;
# positive determinant/negative trace imply both real parts negative.
print('PASS: exact rational resident-profile mimicry certificate')
