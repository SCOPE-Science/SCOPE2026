"""Exact algebraic checks for the polygonal twist law of a piecewise-affine square map.
Python 3 standard library only. This checks algebraic identities, not literature novelty.
"""
from fractions import Fraction as F
from dataclasses import dataclass

@dataclass(frozen=True)
class Q:
    a: F = F(0)
    b: F = F(0)
    def __add__(self, other):
        other = q(other); return Q(self.a+other.a,self.b+other.b)
    __radd__ = __add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,other): return self + -q(other)
    def __rsub__(self,other): return q(other) + -self
    def __mul__(self,other):
        other=q(other)
        return Q(self.a*other.a+2*self.b*other.b,self.a*other.b+self.b*other.a)
    __rmul__ = __mul__
    def __truediv__(self,other):
        other=q(other); den=other.a*other.a-2*other.b*other.b
        assert den
        return self * Q(other.a/den,-other.b/den)
    def __rtruediv__(self,other): return q(other)/self
    def __repr__(self): return f'({self.a})+({self.b})sqrt(2)'

def q(x):
    if isinstance(x,Q): return x
    return Q(F(x),F(0))

def vecadd(u,v): return tuple(a+b for a,b in zip(u,v))
def vecmul(t,v): return tuple(t*x for x in v)
def matvec(M,v): return tuple(sum(M[i][j]*v[j] for j in range(2)) for i in range(2))
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def half(qx):return qx/2

R2=Q(F(0),F(1)); ONE=q(1); ZERO=q(0)
s=R2/4; t=(2-R2)/4; delta=1-2*s
P4=(t,1-s); P1=(s,t)
B=((q(F(1,2))+R2,q(F(1,2))-R2/2),(-q(F(1,2))+R2/2,q(F(1,2))))
assert B[0][0]*B[1][1]-B[0][1]*B[1][0]==ONE
V=[P4]
for j in range(3):V.append(matvec(B,V[-1]))
assert V[1]==(t,s)
assert V[2]==((R2-1)/2,(R2-1)/2)
assert V[3]==P1
assert s+delta==1-s

def rotate(p): return (1-p[1],p[0])
def rotate_k(p,k):
    for _ in range(k):p=rotate(p)
    return p

def vertices(r):
    vv=[vecmul(q(r),v) for v in V]
    return [rotate_k(v,k) for k in range(4) for v in vv]

def polygon_area(r):
    vv=vertices(r)
    return half(sum(cross(vv[i],vv[(i+1)%len(vv)]) for i in range(len(vv))))

M0=2-R2; M1=7-5*R2
# The signed-area formula is quadratic: each vertex is affine in r.
for r in [F(0),F(1,2),F(1)]:
    area_formula=1-M0*q(r)-half(M1)*q(r)*q(r)
    assert polygon_area(r)==area_formula,(r,polygon_area(r),area_formula)

mB=t*delta  # coefficient of r in the conditional mass of each corner segment
# The other three successive corner segments have equal mass by area invariance.
for r in [F(1,5),F(1,2),F(4,5)]:
    R=q(r)
    mA=t*(1-R)
    mtotal=4*(3*R*mB+mA)
    assert mtotal==M0+M1*R
    rho_left=(R*mB)/mtotal
    rho_right=R/(4*((2+R2)+(1-R2)*R))
    assert rho_left==rho_right

# Change-of-variables formula for the unnormalized rotation-number density:
# M(r) dr/domega = 8/[1+4(sqrt(2)-1)omega]^3.
c=2+R2; d=1-R2
assert 4*c*M0==q(8)
assert c*M1==d*M0
outer_area=M0+M1/2
assert outer_area==(11-7*R2)/2
assert polygon_area(1)==(-9+7*R2)/2

# Direct affine edge-mapping identities (with r arbitrary by linearity).
# Corner edges map successively under B, and the horizontal edge under A.
for r in [F(0),F(1)]:
    rr=q(r)
    x3=vecmul(rr,V[3]); x0=vecmul(rr,V[0]); x1=vecmul(rr,V[1])
    A=lambda p:(p[0]+2*p[1],p[1])
    assert A(x3)==vecadd(x3,(rr*delta,ZERO))
    assert A(rotate(x0))==rotate(x1)

print('VERIFY_OK: exact Q(sqrt(2)) edge maps, polygon area, twist and cubic density identities')
print('Outer-annulus area =',outer_area)
