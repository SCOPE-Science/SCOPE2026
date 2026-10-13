from fractions import Fraction as F

# Exact arithmetic in Q(sqrt(3)): values are pairs a + b*r with r^2 = 3.
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x): return (-x[0], -x[1])
def sub(x, y): return add(x, neg(y))
def mul(x, y): return (x[0]*y[0] + 3*x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def scale(q, x): return (q*x[0], q*x[1])
def eq(x, y): return x == y

Z = (F(0), F(0)); O = (F(1), F(0)); R = (F(0), F(1))
def rat(a, b=1): return (F(a,b), F(0))

def vadd(x,y): return [add(a,b) for a,b in zip(x,y)]
def vscale(q,x): return [scale(q,a) for a in x]
def dot(x,y):
    s=Z
    for a,b in zip(x,y): s=add(s,mul(a,b))
    return s

def mm(A,B):
    return [[sumq([mul(A[i][k],B[k][j]) for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,x): return [sumq([mul(A[i][j],x[j]) for j in range(len(x))]) for i in range(len(A))]
def sumq(xs):
    s=Z
    for x in xs: s=add(s,x)
    return s

def tr(A): return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
def madd(A,B): return [[add(A[i][j],B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]
def mscale(q,A): return [[scale(q,x) for x in row] for row in A]
def outer(x,y): return [[mul(a,b) for b in y] for a in x]

A = [[rat(1,80), scale(F(1,80),R)], [scale(F(1,80),R), rat(1,20)]]
b = [rat(-5,8), Z]
x0 = [Z,Z]
g0 = b
d0 = vscale(F(-1),g0)
alpha = F(64)
s = vscale(alpha,d0)
y = mv(A,s)
g1 = vadd(g0,y)

# Hessian is SPD: A11 > 0 and det(A)=1/6400.
detA = sub(mul(A[0][0],A[1][1]),mul(A[0][1],A[1][0]))
assert detA == rat(1,6400)
assert A[0][0][0] > 0
assert d0 == [rat(5,8),Z]
assert s == [rat(40),Z]
assert y == [rat(1,2), scale(F(1,2),R)]
assert g1 == [rat(-1,8), scale(F(1,2),R)]

# Strong Wolfe for c1=1e-4, c2=9/10.
g0d0 = dot(g0,d0)
g1d0 = dot(g1,d0)
g0s = dot(g0,s)
sAs = dot(s,mv(A,s))
fchange = add(g0s, scale(F(1,2),sAs))
assert g0d0 == rat(-25,64)
assert g1d0 == rat(-5,64)
assert fchange == rat(-15)
armijo_rhs = scale(F(1,10000),g0s)
assert fchange[1] == armijo_rhs[1] == 0 and fchange[0] <= armijo_rhs[0]
assert abs(g1d0[0]) <= F(9,10)*abs(g0d0[0])

# Geometry and secant parameters: ||y||^2=1, s^T y=20, m=1/2, z=20.
y2 = dot(y,y); sy = dot(s,y); s2 = dot(s,s)
assert y2 == rat(1) and sy == rat(20) and s2 == rat(1600)
# rho=1 gives t=m=1/2; eta=1 gives t=1-m=1/2. secant then gives nu=1/2.
t = F(1,2); nu = F(1,2)

I = [[O,Z],[Z,O]]
yyt = outer(y,y)
T = madd(mscale(t,I), mscale(nu,yyt))
T_expected = [[rat(5,8),scale(F(1,8),R)],[scale(F(1,8),R),rat(7,8)]]
assert T == T_expected

# P = I - s y^T/(s^T y) + T s s^T/(s^T y).
P = madd(madd(I, mscale(F(-1,20), outer(s,y))), mscale(F(1,20), mm(T,outer(s,s))))
P_expected = [[rat(50),neg(R)],[scale(F(10),R),rat(1)]]
assert P == P_expected
S = mscale(F(1,2),madd(P,tr(P)))
detS = sub(mul(S[0][0],S[1][1]),mul(S[0][1],S[1][0]))
assert detS == rat(-43,4)
Pg1 = mv(P,g1)
gPg = dot(g1,Pg1)
d1 = vscale(F(-1),Pg1)
gd1 = dot(g1,d1)
assert gPg == rat(-5,32)
assert gd1 == rat(5,32)
assert gd1[0] > 0 and gd1[1] == 0
print('VERIFY_OK')
