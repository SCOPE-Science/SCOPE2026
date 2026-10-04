#!/usr/bin/env python3
import math

SQRT = math.sqrt
PI = math.pi

# Normalized symmetric Dicke coordinates of |phi(t)>^{otimes 3}.
def v(t):
    c = math.cos(t/2.0)
    s = math.sin(t/2.0)
    return [c**3, SQRT(3.0)*c*c*s, SQRT(3.0)*c*s*s, s**3]

def outer(x):
    return [[x[i]*x[j] for j in range(4)] for i in range(4)]

def mat_sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(4)] for i in range(4)]

def mat_add(A,B):
    return [[A[i][j]+B[i][j] for j in range(4)] for i in range(4)]

def mat_scale(a,A):
    return [[a*A[i][j] for j in range(4)] for i in range(4)]

def mat_mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def trace(A):
    return sum(A[i][i] for i in range(4))

def delta(t):
    return mat_sub(outer(v(t)), outer(v(t+PI/2.0)))

def frob(A,B):
    return trace(mat_mul(A,B))

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def norm(x):
    return SQRT(dot(x,x))

def jacobi_eigs(A, sweeps=80):
    A=[row[:] for row in A]
    n=len(A)
    for _ in range(sweeps):
        p=q=0; m=0.0
        for i in range(n):
            for j in range(i+1,n):
                if abs(A[i][j])>m:
                    m=abs(A[i][j]); p=i; q=j
        if m<1e-14:
            break
        app,aqq,apq=A[p][p],A[q][q],A[p][q]
        phi=0.5*math.atan2(2.0*apq,aqq-app)
        c,s=math.cos(phi),math.sin(phi)
        for k in range(n):
            if k!=p and k!=q:
                akp,akq=A[k][p],A[k][q]
                A[k][p]=A[p][k]=c*akp-s*akq
                A[k][q]=A[q][k]=s*akp+c*akq
        A[p][p]=c*c*app-2*c*s*apq+s*s*aqq
        A[q][q]=s*s*app+2*c*s*apq+c*c*aqq
        A[p][q]=A[q][p]=0.0
    return sorted(A[i][i] for i in range(n))

# Three-point least-favorable prior.
T=PI/3.0
M=mat_scale(1.0/13.0, mat_add(mat_add(mat_scale(5.0,delta(-T)), mat_scale(3.0,delta(0.0))), mat_scale(5.0,delta(T))))
lam=SQRT(2114.0)/104.0
expected=[-lam,0.0,0.0,lam]
e=jacobi_eigs(M)
assert max(abs(a-b) for a,b in zip(e,expected)) < 5e-12, (e,expected)

# Explicit orthonormal kernel basis.
u1=[-5*SQRT(3.0),-8.0,3.0,0.0]
u1=[x/(2*SQRT(37.0)) for x in u1]
u2=[60.0,-153*SQRT(3.0),-308*SQRT(3.0),333.0]
u2=[x/(2*SQRT(117327.0)) for x in u2]
assert abs(norm(u1)-1.0)<1e-12
assert abs(norm(u2)-1.0)<1e-12
assert abs(dot(u1,u2))<1e-12
for u in (u1,u2):
    Mu=[sum(M[i][j]*u[j] for j in range(4)) for i in range(4)]
    assert norm(Mu)<1e-12

B0=mat_scale(1.0/lam,M)
K=[[-2*SQRT(2114.0)/1443.0,82*SQRT(2.0)/1443.0],
   [82*SQRT(2.0)/1443.0,2*SQRT(2114.0)/1443.0]]
# Q K Q^T.
Q=[[u1[i],u2[i]] for i in range(4)]
QK=[[sum(Q[i][a]*K[a][b] for a in range(2)) for b in range(2)] for i in range(4)]
QKQt=[[sum(QK[i][a]*Q[j][a] for a in range(2)) for j in range(4)] for i in range(4)]
B=mat_add(B0,QKQt)
be=jacobi_eigs(B)
expected_B=[-1.0,-4.0/39.0,4.0/39.0,1.0]
assert max(abs(a-b) for a,b in zip(be,expected_B))<2e-11, (be,expected_B)

V=0.5+SQRT(2114.0)/208.0
def P_direct(t):
    return 0.5+0.25*frob(delta(t),B)
def P_closed(t):
    c=math.cos(t)
    return V+SQRT(2114.0)/219856.0*(1-c)*(2*c-1)*(246*c+713)
for t in (-T,0.0,T):
    assert abs(P_direct(t)-V)<2e-12, (t,P_direct(t),V)
for k in range(2001):
    t=-T+2*T*k/2000.0
    pd=P_direct(t); pc=P_closed(t)
    assert abs(pd-pc)<3e-12, (t,pd,pc)
    assert pd >= V-3e-12, (t,pd,V)
print('VERIFY_OK')
print('V=%.15f' % V)
print('least_favorable_weights=5/13,3/13,5/13')
print('measurement_eigenvalues=-1,-4/39,4/39,1')
