from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def mv(A,v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]

def addv(a,b):
    return [x+y for x,y in zip(a,b)]

def scale(c,v):
    return [c*x for x in v]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def subm(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A))] for i in range(len(A))]

def scalem(c,A):
    return [[c*x for x in row] for row in A]

A=[[F(10),F(-1),F(0)],[F(-1),F(10),F(0)],[F(0),F(0),F(1)]]
b=[F(0),F(1),F(0)]
alpha=F(1,6)
I=eye(3)
T=subm(I,scalem(alpha,A))
assert T==[[F(-2,3),F(1,6),F(0)],[F(1,6),F(-2,3),F(0)],[F(0),F(0),F(5,6)]]

# Characteristic polynomial det(A-lambda I)=(1-lambda)((10-lambda)^2-1).
def char(lam):
    return (F(1)-lam)*((F(10)-lam)**2-F(1))
assert char(F(1))==0 and char(F(9))==0 and char(F(11))==0
assert F(2,1)/(F(1)+F(11))==alpha

x=[F(0),F(0),F(0)]
xs=[]
for _ in range(3):
    r=[b[i]-mv(A,x)[i] for i in range(3)]
    x=addv(x,scale(alpha,r))
    xs.append(x)
assert xs[0]==[F(0),F(1,6),F(0)]
assert xs[1]==[F(1,36),F(1,18),F(0)]
assert xs[2]==[F(-1,108),F(29,216),F(0)]
assert xs[2][0] < 0
xstar=[F(1,99),F(10,99),F(0)]
assert mv(A,xstar)==b
assert all(v>=0 for v in xstar)
assert max(abs(F(1)-alpha*lam) for lam in [F(1),F(9),F(11)])==F(5,6)

# Coefficient-level identity for the general 2x2 form:
# [[u,v],[v,-u]]^2 = (u^2+v^2) I.
u,v=F(7,13),F(5,17)  # arbitrary exact placeholders; multiplication pattern is universal
G=[[u,v],[v,-u]]
G2=mm(G,G)
assert G2==[[u*u+v*v,F(0)],[F(0),u*u+v*v]]
print('VERIFY_OK')
