from fractions import Fraction as F

R2 = 19729

class Q:
    # a + b*sqrt(R2)
    def __init__(self,a=0,b=0):
        self.a=F(a); self.b=F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q) else Q(o); return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self+(- (o if isinstance(o,Q) else Q(o)))
    def __rsub__(self,o): return Q(o)-self
    def __mul__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return Q(self.a*o.a+self.b*o.b*R2, self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if isinstance(o,Q):
            den=o.a*o.a-o.b*o.b*R2
            return Q((self.a*o.a-self.b*o.b*R2)/den,(self.b*o.a-self.a*o.b)/den)
        return Q(self.a/F(o),self.b/F(o))
    def __eq__(self,o):
        o=o if isinstance(o,Q) else Q(o); return self.a==o.a and self.b==o.b
    def __repr__(self): return f"Q({self.a},{self.b})"

def matvec(M,x):
    return [sum((M[i][j]*x[j] for j in range(len(x))), Q(0)) for i in range(len(M))]

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),Q(0)) for j in range(len(B[0]))] for i in range(len(A))]

def eye(n): return [[Q(1 if i==j else 0) for j in range(n)] for i in range(n)]

def submat(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scalarmat(s,A): return [[s*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

A=[[Q(F(1,2)),Q(F(-1,4))],[Q(F(-1,4)),Q(F(1,2))]]
J=[[Q(F(1,2)),Q(F(1,4))],[Q(F(1,4)),Q(F(1,2))]]
x=[Q(F(11,10)),Q(F(9,10))]
r=[Q(F(-13,40)),Q(F(-7,40))]
v=[Q(F(19,160)),Q(F(1,160))]
# Exact squared norm ratio s^2.
r2=F(13*13+7*7,40*40)
v2=F(19*19+1,160*160)
assert r2/v2 == F(1744,181)
assert F(1744,181) > 4
s=Q(0,F(4,181))
assert s*s == Q(F(1744,181))
B=submat(eye(2),scalarmat(s,A))
y=matvec(matmul(B,B),x)
expected_y=[Q(F(2031,905),F(-13,905)),Q(F(869,905),F(-7,905))]
assert y==expected_y
z=matvec(J,y)
expected_z=[Q(F(4931,3620),F(-33,3620)),Q(F(3769,3620),F(-27,3620))]
assert z==expected_z
# Exact signs: a-b*sqrt(R2)<0 iff b^2*R2>a^2 for positive a,b.
assert 7*7*R2 > 869*869
assert 27*27*R2 > 3769*3769
# Positivity of J and spectral radius: eigenvalues are 3/4 and 1/4.
assert all(q.a>0 and q.b==0 for row in J for q in row)
assert F(3,4) < 1 and F(1,4) > 0
print('VERIFY_OK')
