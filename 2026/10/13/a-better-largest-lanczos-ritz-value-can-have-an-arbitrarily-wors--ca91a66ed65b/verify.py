from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

# Exact epsilon = 1/10 data.
e=F(1,10)
u=[F(1),F(1),e]
A=[[F(1),F(0),F(0)],[F(0),F(1)+e,F(0)],[F(0),F(0),F(2)]]
uu=dot(u,u)
Au=matvec(A,u)
rho=dot(u,Au)/uu
r=[Au[i]-rho*u[i] for i in range(3)]
r1sq=dot(r,r)/uu
assert rho == F(212,201)
assert r1sq == F(281,40401)

w=[F(-1),F(0),F(1)-e]
V=[u,w]

# Exact Gram G and projected form H in basis columns u,w.
G=[[dot(V[i],V[j]) for j in range(2)] for i in range(2)]
AV=[matvec(A,V[j]) for j in range(2)]
H=[[dot(V[i],AV[j]) for j in range(2)] for i in range(2)]

assert G == [[F(201,100),F(-91,100)],[F(-91,100),F(181,100)]]
assert H == [[F(53,25),F(-41,50)],[F(-41,50),F(131,50)]]

# det(H-theta G) multiplied by 1000:
# 2810 theta^2 - 7611 theta + 4882.
disc=7611**2-4*2810*4882
assert disc == 3053641
theta=(D(7611)+D(disc).sqrt())/D(5620)

# Generalized eigenvector: set alpha=1, solve first row for beta.
def dec(q):
    return D(q.numerator)/D(q.denominator)

beta=-(dec(H[0][0])-theta*dec(G[0][0]))/(dec(H[0][1])-theta*dec(G[0][1]))
yd=[
    D(1)+beta*D(-1),
    D(1),
    D(1)/D(10)+beta*D(9)/D(10)
]
ynorm=sum(z*z for z in yd).sqrt()
yd=[z/ynorm for z in yd]
Ad=[yd[0],D(11)/D(10)*yd[1],D(2)*yd[2]]
res=[Ad[i]-theta*yd[i] for i in range(3)]
r2=(sum(z*z for z in res)).sqrt()
r1=(D(281)/D(40401)).sqrt()
ratio=r2/r1

assert abs(theta-D("1.665207655517674")) < D("1e-15")
assert abs(r2-D("0.449903178976340")) < D("1e-15")
assert ratio > D("5.39")
assert theta > dec(rho)
assert theta < D(2)

# Exact limiting pencil.
G0=[[F(2),F(-1)],[F(-1),F(2)]]
H0=[[F(2),F(-1)],[F(-1),F(3)]]
# theta=5/3, c=(1,2).
th=F(5,3)
c=[F(1),F(2)]
lhs=matvec(H0,c)
rhs=[th*z for z in matvec(G0,c)]
assert lhs==rhs
y0=[F(-1),F(1),F(2)]
A0=[[F(1),F(0),F(0)],[F(0),F(1),F(0)],[F(0),F(0),F(2)]]
Ay0=matvec(A0,y0)
res0=[Ay0[i]-th*y0[i] for i in range(3)]
# normalized by ||y0||^2=6
assert dot(res0,res0)/dot(y0,y0) == F(2,9)

print("VERIFY_OK")
print("epsilon", e)
print("rho", rho)
print("first_residual_sq", r1sq)
print("theta", theta)
print("second_residual", r2)
print("residual_ratio", ratio)
