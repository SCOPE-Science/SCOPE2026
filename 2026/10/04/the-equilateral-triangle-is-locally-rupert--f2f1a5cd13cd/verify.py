from fractions import Fraction
from math import sqrt, sin, cos, acos, pi

# Exact arithmetic in Q(sqrt(3)): a+b*sqrt(3).
class Q3:
    __slots__=("a","b")
    def __init__(self,a=0,b=0):
        self.a=Fraction(a); self.b=Fraction(b)
    def __add__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return Q3(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q3(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q3) else Q3(o)))
    def __rsub__(self,o): return Q3(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return Q3(self.a*o.a+3*self.b*o.b, self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __eq__(self,o):
        o=o if isinstance(o,Q3) else Q3(o)
        return self.a==o.a and self.b==o.b
    def val(self): return float(self.a)+float(self.b)*sqrt(3)

def dot(u,v):
    s=Q3()
    for x,y in zip(u,v): s=s+x*y
    return s

def matvec(A,v):
    return [dot(row,v) for row in A]

r=Q3(0,1)
half=Q3(Fraction(1,2))
# Vertices and outward side normals of the normalized triangle.
V=[
    [Q3(0),Q3(1)],
    [-r*Fraction(1,2),Q3(Fraction(-1,2))],
    [ r*Fraction(1,2),Q3(Fraction(-1,2))]
]
N=[
    [Q3(0),Q3(-1)],
    [-r*Fraction(1,2),Q3(Fraction(1,2))],
    [ r*Fraction(1,2),Q3(Fraction(1,2))]
]
# B = A'_0 for the explicit rotation path.
B=[
    [Q3(Fraction(-1,2),Fraction(-1,4)),Q3(Fraction(-1,2))],
    [Q3(0),Q3(Fraction(-1,2),Fraction(1,4))]
]
q=[Q3(-4,2),Q3(0)]
b=matvec(B,q)
assert b==[Q3(Fraction(1,2)),Q3(0)]

active=[]
for i,ni in enumerate(N):
    for j,vj in enumerate(V):
        if dot(ni,vj)==half:
            d=dot(ni,[x+y for x,y in zip(matvec(B,vj),b)])
            active.append((i,j,d))
assert len(active)==6
mild=Q3(Fraction(-1,4),Fraction(1,8))
strong=Q3(Fraction(-1,4),Fraction(-5,8))
assert sum(d==mild for _,_,d in active)==5
assert sum(d==strong for _,_,d in active)==1
assert mild.val()<0 and strong.val()<0

# Numerical replay of the actual 3D rotations and strict containment.
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def rz(a):
    return [[cos(a),-sin(a),0.0],[sin(a),cos(a),0.0],[0.0,0.0,1.0]]
def rx(a):
    return [[1.0,0.0,0.0],[0.0,cos(a),-sin(a)],[0.0,sin(a),cos(a)]]
def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
phi=-5*pi/12
Vf=[(0.0,1.0),(-sqrt(3)/2,-0.5),(sqrt(3)/2,-0.5)]
Nf=[(0.0,-1.0),(-sqrt(3)/2,0.5),(sqrt(3)/2,0.5)]
qf=(2*sqrt(3)-4,0.0)
for t in (0.1,0.05,0.01,0.001,0.0001):
    th=acos(1-t)
    Q=mm(mm(rz(t/4+phi),rx(th)),rz(-phi))
    # Orthogonality and determinant-one checks.
    QT=[[Q[j][i] for j in range(3)] for i in range(3)]
    QQ=mm(QT,Q)
    assert max(abs(QQ[i][j]-(1.0 if i==j else 0.0)) for i in range(3) for j in range(3))<2e-14
    det=(Q[0][0]*(Q[1][1]*Q[2][2]-Q[1][2]*Q[2][1])
         -Q[0][1]*(Q[1][0]*Q[2][2]-Q[1][2]*Q[2][0])
         +Q[0][2]*(Q[1][0]*Q[2][1]-Q[1][1]*Q[2][0]))
    assert abs(det-1)<2e-14
    # Project Q(v+q,0), translate back by q, and check all three strict side inequalities.
    for vx,vy in Vf:
        p=mv(Q,[vx+qf[0],vy+qf[1],0.0])
        fx,fy=p[0]-qf[0],p[1]-qf[1]
        for nx,ny in Nf:
            assert nx*fx+ny*fy < 0.5

print("VERIFY_OK equilateral triangle local Rupert passage")
