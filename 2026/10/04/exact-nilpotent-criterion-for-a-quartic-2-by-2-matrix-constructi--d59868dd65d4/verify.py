from itertools import product

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def sub(A,B): return [[A[i][j]-B[i][j] for j in range(2)] for i in range(2)]
def smul(c,A): return [[c*A[i][j] for j in range(2)] for i in range(2)]
def powm(A,n):
    R=[[1,0],[0,1]]
    for _ in range(n): R=mm(R,A)
    return R
def tr(A): return A[0][0]+A[1][1]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def zero(A): return A==[[0,0],[0,0]]

# A counterexample satisfying the hypotheses u != 0, u != +/-t, det(V)=0
# of the source's Theorem 2.1, but not its asserted x=w conclusion.
V=[[2,1],[-4,-2]]
U=[[1,0],[-2,0]]
X=add(U,V); Y=sub(U,V); Z=U
assert det(V)==0 and V[0][0] != 0 and V[0][0] not in (V[1][0],-V[1][0])
assert zero(mm(V,V))
assert tr(mm(U,V))==0
A=add(mm(U,V),mm(V,U))
assert zero(mm(A,A))
assert add(powm(X,4),powm(Y,4))==smul(2,powm(Z,4))
assert U[0][0] != U[1][1]

# Exhaustive exact-arithmetic stress test of the corrected iff criterion.
Vs=[
 [[1,1],[-1,-1]],
 [[2,1],[-4,-2]],
 [[3,1],[-9,-3]],
 [[2,2],[-2,-2]],
]
checked=0
for V0 in Vs:
    assert tr(V0)==0 and det(V0)==0 and zero(mm(V0,V0))
    for x,y,z,w in product(range(-4,5), repeat=4):
        U0=[[x,y],[z,w]]
        X0=add(U0,V0); Y0=sub(U0,V0)
        qeq=(add(powm(X0,4),powm(Y0,4))==smul(2,powm(U0,4)))
        crit=(tr(mm(U0,V0))==0)
        assert qeq==crit
        checked += 1
print('VERIFY_OK explicit_counterexample=1 exhaustive_pairs=%d criterion=trace(UV)==0' % checked)
print('V=%r U=%r X=%r Y=%r Z=%r traceUV=%d' % (V,U,X,Y,Z,tr(mm(U,V))))
