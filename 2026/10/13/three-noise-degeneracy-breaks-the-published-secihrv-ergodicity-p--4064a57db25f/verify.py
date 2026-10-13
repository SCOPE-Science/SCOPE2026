from fractions import Fraction as F

def transpose(M):
    return list(map(list, zip(*M)))

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]

def qform(A,z):
    return sum((z[i]*A[i][j]*z[j] for i in range(len(z)) for j in range(len(z))), F(0))

# Generic nonzero rational amplitudes for the three printed diffusion columns.
a,b,c,eps = F(2),F(3),F(5),F(2,5)
G = [
    [-a,-b,F(0)],
    [ a,F(0),-c],
    [F(0),F(0),eps*c],
    [F(0),F(0),(F(1)-eps)*c],
    [F(0),F(0),F(0)],
    [F(0),F(0),F(0)],
    [F(0), b,F(0)],
]
A = matmul(G, transpose(G))
e5=[F(0)]*7; e5[4]=F(1)
e6=[F(0)]*7; e6[5]=F(1)
assert qform(A,e5)==0 and qform(A,e6)==0
assert all(A[4][j]==0 and A[j][4]==0 for j in range(7))
assert all(A[5][j]==0 and A[j][5]==0 for j in range(7))

# Published V depends on 1,2,3,4,6,7 in V1, and on 4,6,7 in V2-V4, never x5.
xstar=[F(1)]*7

def V(x):
    s=sum((x[i]-xstar[i] for i in [0,1,2,3,5,6]),F(0))
    V1=s*s
    V2=(x[3]-xstar[3])**2
    V3=(x[5]-xstar[5])**2
    V4=(x[6]-xstar[6])**2
    return V1+F(2,3)*V2+F(1,2)*V3+F(1,4)*V4
for t in [F(1),F(10),F(1000)]:
    x=xstar[:]; x[4]+=t
    assert V(x)==0

# Eq. (50) omits x3 and x5, so a nonempty level set contains unbounded rays.
m1=m2=m3=F(1); theta1=theta2=theta3=F(1); FF=F(1)
def level(x):
    return (m1*(x[0]-theta1*xstar[0])**2 +
            m2*(x[1]-theta2*xstar[1])**2 +
            m3*(x[3]-theta3*xstar[3])**2 +
            m3*(x[5]-theta3*xstar[5])**2 +
            m2*(x[6]-theta2*xstar[6])**2)
for t in [F(1),F(10),F(1000)]:
    x=[F(2),F(1),t,F(1),t,F(1),F(1)]
    assert level(x)==FF
print('VERIFY_OK')
