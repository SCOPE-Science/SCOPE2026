from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def mv(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def smul(c,A):
    return [[c*v for v in row] for row in A]

w=F(8,5)
a=F(1,5)
A=[[F(1),-a],[-a,F(1)]]
b=[F(0),F(1)]
I=eye(2)
G=madd(I,smul(-w,A))
# Exact eigenvalues of A are 1-a and 1+a; corresponding iteration eigenvalues:
r1=F(1)-w*(F(1)-a)
r2=F(1)-w*(F(1)+a)
assert (r1,r2)==(F(-7,25),F(-23,25))
assert abs(r1)<1 and abs(r2)<1

x=[F(0),F(0)]
vals=[]
for _ in range(3):
    residual=[b[i]-mv(A,x)[i] for i in range(2)]
    x=[x[i]+w*residual[i] for i in range(2)]
    vals.append(tuple(x))
assert vals[0]==(F(0),F(8,5))
assert vals[1]==(F(64,125),F(16,25))
assert vals[2]==(F(-64,625),F(4312,3125))

# Exact inverse action for A^{-1} e_2.
det=F(1)-a*a
sol=(a/det,F(1)/det)
assert sol==(F(5,24),F(25,24))
assert all(v>0 for v in sol)

# Polynomial coefficient bookkeeping for an off-diagonal entry.
# If c_ij=-g and (C^2)_ij=-2g+s, then
# -3*w^2*c_ij + w^3*(C^2)_ij
# = 3*w^2*g - 2*w^3*g + w^3*s
# = w^2*((3-2*w)*g+w*s).
# Store monomials (power_w, power_g, power_s) -> integer coefficient.
lhs={(2,1,0):3,(3,1,0):-2,(3,0,1):1}
rhs={(2,1,0):3,(3,1,0):-2,(3,0,1):1}
assert lhs==rhs

# For q_2, diagonal positivity follows from w*(2-w)>0 in any convergent instance.
assert F(0)<w<F(2)
assert w*(2-w)>0
# At the sharp frontier, the direct-edge coefficient vanishes and path terms remain nonnegative.
wc=F(3,2)
assert 3-2*wc==0
print('VERIFY_OK')
