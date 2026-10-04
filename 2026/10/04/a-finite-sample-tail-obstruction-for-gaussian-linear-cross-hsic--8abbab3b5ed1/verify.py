from fractions import Fraction as F
from math import cos, sin, sqrt


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

# Exact reduction check on deterministic rational first-half data.
x=[F(1),F(3),F(-2),F(4),F(0)]
y=[F(2),F(-1),F(5),F(0),F(3)]
n=len(x)
xb=sum(x,F(0))/n; yb=sum(y,F(0))/n
a=[q-xb for q in x]; b=[q-yb for q in y]
z=[a[i]*b[i] for i in range(n)]
C=sum(z,F(0)); Q=sum((q-C/n)**2 for q in z)
# h_ij and the first-half factor.
def h(i,j): return (x[i]-x[j])*(y[i]-y[j])/2
f1=sum((h(i,j) for i in range(n) for j in range(n) if i!=j),F(0))/(n*(n-1))
assert f1==C/(n-1)
# Set a nonzero symbolic second-half factor f2=7/5; studentizer is homogeneous in it.
f2=F(7,5)
cross=f1*f2
g=[]
for i in range(n):
    g.append(sum((h(i,j)*f2 for j in range(n) if j!=i),F(0))/(n-1))
s2=F(4*(n-1),(n-2)**2)*sum((q-cross)**2 for q in g)
expected_s2=f2*f2*n*n*Q/F((n-1)*(n-2)**2)
assert s2==expected_s2
# Squared studentized statistic agrees with the reduced expression.
T2=F(n)*cross*cross/s2
reduced2=F((n-2)**2)*C*C/F(n*(n-1))/Q
assert T2==reduced2

# Exact n=4 regularity certificate. Columns are derivatives before harmless
# global normalization factors, projected to H; first three rows suffice.
M=[
 [F(-9,8),F(1,8),F(-9,8),F(1,8)],
 [F(-1,8),F(9,8),F(-1,8),F(9,8)],
 [F(7,8),F(-3,8),F(13,8),F(3,8)],
 [F(3,8),F(-7,8),F(-3,8),F(-13,8)],
]
minor=[[M[r][c] for c in (0,1,2)] for r in (0,1,2)]
assert det3(minor)==F(-15,16)

# Odd-n core: the last two coordinates are roots of 11 t^2+66 t+36.
# Their sum is -6 and product 36/11, so total sum and reciprocal sum vanish.
root_sum=F(-6); root_prod=F(36,11)
assert F(1)+F(2)+F(3)+root_sum==0
assert F(1)+F(1,2)+F(1,3)+root_sum/root_prod==0
# Positive discriminant and no root collision with 0,1,2,3.
disc=66*66-4*11*36
assert disc>0
for q in (0,1,2,3):
    assert 11*q*q+66*q+36 != 0

# Numerical stress checks for the n=3 circle identity.
e1=(1/sqrt(2),-1/sqrt(2),0.0)
e2=(1/sqrt(6),1/sqrt(6),-2/sqrt(6))
for A,B in ((0.1,0.8),(0.2,2.3),(1.5,4.0),(5.1,0.4)):
    u=[cos(A)*e1[i]+sin(A)*e2[i] for i in range(3)]
    v=[cos(B)*e1[i]+sin(B)*e2[i] for i in range(3)]
    zz=[u[i]*v[i] for i in range(3)]
    cc=sum(zz); qq=sum((q-cc/3)**2 for q in zz)
    assert abs(cc-cos(A-B))<1e-12
    assert abs(qq-F(1,6))<1e-12

print('VERIFY_OK')
