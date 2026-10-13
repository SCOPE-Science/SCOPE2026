#!/usr/bin/env python3
import math

r = 0.02
q = 0.40
p = 0.05
eps = 0.10
sigma = 0.20
gamma = 0.10
mu = 0.01
beta = 0.35
d0 = 0.005
K = 1000.0
c = (r - d0) / K

def state_from_N(N):
    f = d0 + c*N
    Y = (r-f)*N/mu
    H = (gamma+mu+f)*Y/sigma
    X = N*(sigma+f)*(gamma+mu+f)/(beta*sigma)
    Z = N-X-H-Y
    return X,H,Y,Z

def scalar_residual(N):
    X,H,Y,Z = state_from_N(N)
    f = d0 + c*N
    return r*q*N + gamma*Y - (f+eps)*Z + p*X

lo, hi = 902.0, 903.0
assert scalar_residual(lo) > 0.0
assert scalar_residual(hi) < 0.0
for _ in range(120):
    mid = 0.5*(lo+hi)
    if scalar_residual(mid) > 0.0:
        lo = mid
    else:
        hi = mid
N = 0.5*(lo+hi)
X,H,Y,Z = state_from_N(N)

def vector_field(v):
    X,H,Y,Z = v
    N = X+H+Y+Z
    f = d0+c*N
    inc = beta*X*Y/N
    return [
        r*(1-q)*N-inc-(f+p)*X+eps*Z,
        inc-(sigma+f)*H,
        sigma*H-(gamma+mu+f)*Y,
        r*q*N+gamma*Y-(f+eps)*Z+p*X,
    ]

res = vector_field((X,H,Y,Z))
assert max(abs(x) for x in res) < 1e-10

def jacobian(v):
    X,H,Y,Z = v
    N = X+H+Y+Z
    f = d0+c*N
    inc_x = beta*Y/N - beta*X*Y/(N*N)
    inc_h = -beta*X*Y/(N*N)
    inc_y = beta*X/N - beta*X*Y/(N*N)
    inc_z = -beta*X*Y/(N*N)
    di = [inc_x,inc_h,inc_y,inc_z]
    J = [[0.0]*4 for _ in range(4)]
    for j in range(4):
        J[0][j] = r*(1-q) - di[j] - c*X
    J[0][0] -= f+p
    J[0][3] += eps
    for j in range(4):
        J[1][j] = di[j] - c*H
    J[1][1] -= sigma+f
    for j in range(4):
        J[2][j] = -c*Y
    J[2][1] += sigma
    J[2][2] -= gamma+mu+f
    for j in range(4):
        J[3][j] = r*q - c*Z
    J[3][0] += p
    J[3][2] += gamma
    J[3][3] -= f+eps
    return J

J = jacobian((X,H,Y,Z))

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def det4(A):
    def det3(M):
        return (
            M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
        )
    total=0.0
    for j in range(4):
        M=[[A[i][k] for k in range(4) if k!=j] for i in range(1,4)]
        total += ((-1.0)**j)*A[0][j]*det3(M)
    return total

J2 = matmul(J,J)
J3 = matmul(J2,J)
t1 = trace(J)
t2 = trace(J2)
t3 = trace(J3)
a1 = -t1
a2 = 0.5*(t1*t1-t2)
a3 = -(t1*t1*t1-3.0*t1*t2+2.0*t3)/6.0
a4 = det4(J)

assert min(a1,a2,a3,a4) > 0.0
m1 = a1*a2-a3
m2 = a1*a2*a3-a3*a3-a1*a1*a4
assert m1 > 0.04
assert m2 > 1.0e-4

expected = [0.5786699091,0.08810770448,0.004035626673,0.00003990077566]
actual = [a1,a2,a3,a4]
for x,y in zip(actual,expected):
    assert abs(x-y) < 5e-10

assert abs(N-902.955757473) < 1e-9
assert abs(X-362.377257655) < 1e-9
assert abs(H-84.479329039) < 1e-9
assert abs(Y-131.439986279) < 1e-9
assert abs(Z-324.659184500) < 1e-9

print("VERIFY_OK")
