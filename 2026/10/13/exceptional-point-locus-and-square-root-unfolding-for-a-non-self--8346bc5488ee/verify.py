#!/usr/bin/env python3
import cmath

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def rank2(A, tol=1e-12):
    if max(abs(x) for row in A for x in row) < tol:
        return 0
    if abs(det2(A)) < tol:
        return 1
    return 2

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def z_of_eta(eta,m=1.0):
    return m*(eta*eta+1)/(eta*eta-1)

def boundary_matrix(A,eta):
    Z=[[eta,0j],[0j,1/eta]]
    AZ=mm(A,Z)
    return [[(1.0 if i==j else 0.0)+0.5j*AZ[i][j] for j in range(2)] for i in range(2)]

def delta(A):
    d=det2(A); a=A[0][0]; q=A[1][1]
    return (d-4)**2+16*a*q

# Exact-style floating checks for two matrices at eta=-i.
A_def=[[1+0j,3+0j],[-3+0j,-1+0j]]
A_sem=[[-2+0j,0j],[0j,2+0j]]
eta=-1j
assert abs(delta(A_def)) < 1e-12
assert abs(delta(A_sem)) < 1e-12
assert rank2(boundary_matrix(A_def,eta)) == 1
assert rank2(boundary_matrix(A_sem,eta)) == 0
assert abs(z_of_eta(eta)) < 1e-12

# Transverse family A(s)=[[1,3],[-3,-1+s]].
# The exact discriminant is 24*s+s^2.  Compare the two energy splitting
# with the analytic leading coefficient.
ratios=[]
for s in (1e-4,1e-6,1e-8):
    A=[[1+0j,3+0j],[-3+0j,-1+s+0j]]
    D=delta(A)
    d=det2(A)
    root=cmath.sqrt(-D)
    ep=(-1j*(d-4)+root)/4
    em=(-1j*(d-4)-root)/4
    zp,zm=z_of_eta(ep),z_of_eta(em)
    eta0=-1j
    pred=-2*eta0/((eta0*eta0-1)**2)*root
    ratios.append((zp-zm)/pred)
assert abs(ratios[-1]-1) < 1e-6
print('VERIFY_OK defective_rank=1 semisimple_rank=0 split_ratio={:.12f}'.format(ratios[-1].real))
