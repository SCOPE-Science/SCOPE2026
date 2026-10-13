"""Exact rational Jacobian check for a normalized degree-contact SIR system.

No external Python packages required. Run: python3 verification.py
"""
from fractions import Fraction as Q

D = 6
ZERO = (Q(0),) * D


class Dual:
    def __init__(self, val, deriv=ZERO):
        self.v = Q(val)
        self.d = tuple(deriv)

    @staticmethod
    def var(v, j):
        d = list(ZERO)
        d[j] = Q(1)
        return Dual(v, d)

    def __add__(self, other):
        other = as_dual(other)
        return Dual(self.v + other.v, tuple(a+b for a,b in zip(self.d, other.d)))

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.v, tuple(-a for a in self.d))

    def __sub__(self, other):
        return self + (-as_dual(other))

    def __rsub__(self, other):
        return as_dual(other) + (-self)

    def __mul__(self, other):
        other = as_dual(other)
        return Dual(self.v*other.v,
                    tuple(a*other.v+b*self.v for a,b in zip(self.d,other.d)))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_dual(other)
        return Dual(self.v/other.v,
                    tuple((a*other.v-b*self.v)/other.v**2 for a,b in zip(self.d,other.d)))

    def __rtruediv__(self, other):
        return as_dual(other).__truediv__(self)


def as_dual(x):
    return x if isinstance(x,Dual) else Dual(x)


def field(z):
    s1,s2,i1,i2,r1,r2 = z
    mu=Q(1,2); beta=Q(1,2); gamma=Q(1,4); treatment=Q(1,4)
    theta=(i1+2*i2)/(s1+i1+r1+2*(s2+i2+r2))
    recover=gamma+treatment/(1+theta)
    return (
        1-beta*s1*theta-mu*s1,
        1-2*beta*s2*theta-mu*s2,
        beta*s1*theta-(mu+recover)*i1,
        2*beta*s2*theta-(mu+recover)*i2,
        recover*i1-mu*r1,
        recover*i2-mu*r2,
    )


base=(2,2,0,0,0,0)
z=[Dual.var(value,j) for j,value in enumerate(base)]
out=field(z)
assert all(item.v==0 for item in out), 'Not an equilibrium'
J=tuple(tuple(item.d) for item in out)
expected=(
    (Q(-1,2), 0, Q(-1,6), Q(-1,3), 0, 0),
    (0,Q(-1,2),Q(-1,3),Q(-2,3),0,0),
    (0,0,Q(-5,6),Q(1,3),0,0),
    (0,0,Q(1,3),Q(-1,3),0,0),
    (0,0,Q(1,2),0,Q(-1,2),0),
    (0,0,0,Q(1,2),0,Q(-1,2)),
)
assert J==tuple(tuple(Q(x) for x in row) for row in expected), (J,expected)
assert all(J[i][j]==0 for i in (2,3) for j in (0,1,4,5))
B=((J[2][2],J[2][3]),(J[3][2],J[3][3]))
trace=B[0][0]+B[1][1]
det=B[0][0]*B[1][1]-B[0][1]*B[1][0]
assert trace==Q(-7,6) and det==Q(1,6)
assert (Q(-1)+Q(-1,6))==trace and Q(-1)*Q(-1,6)==det
assert all(J[i][i]==Q(-1,2) for i in (0,1,4,5))
R_printed=Q(1,2)*2*Q(5,3)/1
R_normalized=Q(1,2)*Q(5,3)/1
assert R_printed==Q(5,3)>1 and R_normalized==Q(5,6)<1
print('J =',J)
print('Infectious trace and determinant =',trace,det)
print('Full spectrum: -1, -1/6, and -1/2 (multiplicity 4)')
print('Printed threshold:',R_printed,'normalized-contact threshold:',R_normalized)
print('VERIFY_OK')
