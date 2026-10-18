"""Exact rational checks for the two-row correlated-quantization SOR reversal.

Execute: python verify.py. This is finite verification; the proof in RESULT.md
establishes the theorem for all time indices and all deterministic starts.
"""
from fractions import Fraction as F

r,h=F(3,5),F(1,5)
w=F(187,100)
a=1-w


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def M(b,c):
    return [[a,-w*b],[-w*a*c,a+w*w*b*c]]

def apply(Q,choice):
    U=[[F(0),F(0)],[F(0),F(0)]]
    for b,c in choice:
        B=M(b,c)
        R=matmul(matmul(B,Q),transpose(B))
        U=[[U[i][j]+R[i][j]/2 for j in range(2)] for i in range(2)]
    return U

def dual(H,choice):
    U=[[F(0),F(0)],[F(0),F(0)]]
    for b,c in choice:
        B=M(b,c)
        R=matmul(matmul(transpose(B),H),B)
        U=[[U[i][j]+R[i][j]/2 for j in range(2)] for i in range(2)]
    return U

aligned=[(r+h,r+h),(r-h,r-h)]
antithetic=[(r+h,r-h),(r-h,r+h)]

# At unrelaxed Gauss-Seidel, exact rational scalar second-moment factors.
qanti=(r*r-h*h)**2
qalign=((r+h)**4+(r-h)**4)/2
assert qanti==F(64,625) and qalign==F(136,625)
assert qanti<qalign<1

# Every realized overrelaxed matrix has complex-conjugate eigenvalues
# of modulus |1-omega|, although their random products behave differently.
for b,c in aligned+antithetic:
    B=M(b,c)
    trace=B[0][0]+B[1][1]
    determinant=B[0][0]*B[1][1]-B[0][1]*B[1][0]
    assert determinant==a*a
    assert trace*trace-4*determinant<0

# A strict exact Lyapunov inequality for correlated (shared) choices.
H=[[F(5),F(4)],[F(4),F(7)]]
K=dual(H,aligned)
D=[[H[i][j]-K[i][j] for j in range(2)] for i in range(2)]
detD=D[0][0]*D[1][1]-D[0][1]**2
assert H[0][0]>0 and H[0][0]*H[1][1]-H[0][1]**2>0
assert D[0][0]==F(149596073,250000000)
assert D[0][1]==F(59086577,195312500)
assert D[1][1]==F(2936244641,7812500000)
assert detD==F(1302500101420780141,9765625000000000000)>0

# A positive-definite covariance eigenmatrix exhibiting exponential
# second-moment growth under antithetic coupled choices.
Q=[[F(1500),F(-748)],[F(-748),F(1305)]]
lam=F(12503553,12500000)
assert Q[0][0]>0 and Q[0][0]*Q[1][1]-Q[0][1]**2==1397996>0
assert apply(Q,antithetic)==[[lam*Q[i][j] for j in range(2)] for i in range(2)]
assert lam>1

# The same univariate two-point marginals are used for both couplings.
for seq in [aligned,antithetic]:
    assert sum((b for b,c in seq),F())/2==r
    assert sum((c for b,c in seq),F())/2==r
    assert sorted(b for b,c in seq)==[r-h,r+h]
    assert sorted(c for b,c in seq)==[r-h,r+h]

# The instability and Lyapunov inequalities are strict, hence persist on an
# open neighborhood by continuity. The script checks only the exact anchor.
print('VERIFY_OK unrelaxed_exact_second_moments=2 sample_spectral_discriminants=4'
      ' aligned_strict_lyapunov=true antithetic_covariance_growth=true'
      ' identical_univariate_marginals=true')
