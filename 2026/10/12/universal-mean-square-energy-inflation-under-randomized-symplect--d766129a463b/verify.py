"""Independent exact-arithmetic diagnostics for random-step symplectic Euler."""
from fractions import Fraction as F
from itertools import product


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return sum(A[i][i] for i in range(len(A)))


def transpose(A):
    return [list(row) for row in zip(*A)]


def step(h):
    return [[1-h*h,h],[-h,F(1)]]


def cov(h, C):
    A=step(h)
    return mm(mm(A,C),transpose(A))


def averaged(C,steps):
    return [[sum(cov(h,C)[i][j] for h in steps)/len(steps)
             for j in range(2)] for i in range(2)]


def basis(k):
    return [[[F(1),F(0)],[F(0),F(0)]],
            [[F(0),F(1)],[F(1),F(0)]],
            [[F(0),F(0)],[F(0),F(1)]]][k]


def operator(h):
    cols=[cov(h,basis(j)) for j in range(3)]
    return [[cols[j][i][k] for j in range(3)] for (i,k) in [(0,0),(0,1),(1,1)]]


def det3(A):
    a,b,c=A[0];d,e,f=A[1];g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def quadratic_energy(h):
    return [[F(1),h/2],[h/2,F(1)]]


def vec_update(h,x):
    M=step(h)
    return [sum(M[i][j]*x[j] for j in range(2)) for i in range(2)]


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

# Every fixed step below the deterministic stability ceiling preserves its
# own non-Euclidean positive-definite quadratic form exactly.
for h in (F(1,10),F(1,4),F(1,2),F(1),F(3,2),F(19,10)):
    S=step(h);P=quadratic_energy(h)
    assert S[0][0]*S[1][1]-S[0][1]*S[1][0] == 1
    assert cov(h,P)==P
    assert P[0][0]*P[1][1]-P[0][1]**2>0
    for k in range(3):
        C=basis(k);D=cov(h,C);v=[C[0][0],C[0][1],C[1][1]]
        assert [D[0][0],D[0][1],D[1][1]]==[
            dot(row,v) for row in operator(h)]

u,v=F(1,2),F(1)
O1,O2=operator(u),operator(v)
M=[[(O1[i][j]+O2[i][j])/2 for j in range(3)] for i in range(3)]
expected=[[F(9,32),F(3,8),F(5,8)],
          [-F(3,16),-F(1,4),F(3,4)],
          [F(5,8),-F(3,2),F(1)]]
assert M==expected
traceM=tr(M);M2=mm(M,M)
sigma2=(traceM**2-tr(M2))/2
determinant=det3(M)
assert (traceM,sigma2,determinant)==(F(33,32),F(49,64),F(49,64))
# Characteristic polynomial: 64*z**3-66*z**2+49*z-49.
p=lambda z:64*z**3-66*z**2+49*z-49
assert p(F(1))<0<p(F(51,50))
assert (-132)**2-4*192*49 < 0 # derivative positive on all reals

# The expected state matrix is strictly Schur stable in the witness.
B=[[(step(u)[i][j]+step(v)[i][j])/2 for j in range(2)] for i in range(2)]
detB=B[0][0]*B[1][1]-B[0][1]*B[1][0]
assert (tr(B),detB)==(F(11,8),F(15,16))
assert tr(B)**2-4*detB < 0

# Direct enumeration of independent random steps against iterated covariance
# for each finite horizon and multiple nonzero starting states.
for x0 in ([F(1),F(0)],[F(0),F(1)],[F(2,3),-F(5,7)]):
    C=[[x0[i]*x0[j] for j in range(2)] for i in range(2)]
    for k in range(1,8):
        C=averaged(C,(u,v))
        total=F(0)
        for seq in product((u,v),repeat=k):
            y=x0[:]
            for h in seq:
                y=vec_update(h,y)
            total+=dot(y,y)
        assert tr(C)==total/(2**k)

# The exact Rayleigh-quotient second-variation identity gives the analytic
# leading quadratic coefficient of the simple positive moment eigenvalue.
for h in (F(1,4),F(1,2),F(4,5),F(3,2),F(19,10)):
    P=quadratic_energy(h)
    detP=1-h*h/4
    Q=[[P[1][1]/detP,-P[0][1]/detP],
       [-P[1][0]/detP,P[0][0]/detP]]
    for d in (F(1,128),F(1,256)):
        if not(0<h-d<h+d<2):continue
        A=averaged(P,(h-d,h+d))
        difference=[[A[i][j]-P[i][j] for j in range(2)] for i in range(2)]
        ratio=tr(mm(Q,difference))/tr(mm(Q,P))
        assert ratio==F(2)*d*d*(h*h+d*d)/(4-h*h)

print('verification passed: fixed-step invariants, exact characteristic and mean spectra, 762 enumerated paths across 21 expectations, jitter perturbation identities')
