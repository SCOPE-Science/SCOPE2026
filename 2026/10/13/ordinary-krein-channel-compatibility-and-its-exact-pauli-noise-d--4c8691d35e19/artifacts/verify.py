"""Finite consistency checks for the analytic Choi-support and Pauli-distance theorem.
Run with Python 3, standard library only. The mathematical proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt

I=((1+0j,0j),(0j,1+0j))
Z=((1+0j,0j),(0j,-1+0j))
X=((0j,1+0j),(1+0j,0j))
Y=((0j,-1j),(1j,0j))

def adj(K):
    return tuple(tuple(K[j][i].conjugate() for j in range(len(K))) for i in range(len(K[0])))

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))

def action(K,R):
    return mul(mul(K,R),adj(K))

def apply(Ks,R):
    return tuple(tuple(sum(action(K,R)[i][j] for K in Ks) for j in range(2)) for i in range(2))

def vec(K):
    return (K[0][0],K[1][0],K[0][1],K[1][1])

def choi(Ks):
    return tuple(tuple(sum(vec(K)[i]*vec(K)[j].conjugate() for K in Ks) for j in range(4)) for i in range(4))

def choinorm_trace(M):
    # Explicit special-case unnormalized Choi difference for two Pauli mixtures
    # is checked through the underlying Kraus action rather than eigenvalue heuristics.
    return sum(abs(M[i][i]) for i in range(4))

def near(A,B,atol=1e-12):
    return all(abs(A[i][j]-B[i][j])<=atol for i in range(len(A)) for j in range(len(A[0])))

rho0=((1+0j,0j),(0j,0j))
rho01=((0j,1+0j),(0j,0j))
for c in (0j,0.5+0j,0.3+0.4j,-0.65+0.2j,0+1j):
    assert abs(c)<=1+1e-14
    K0=((1+0j,0j),(0j,c.conjugate()))
    K1=((0j,0j),(0j,sqrt(max(0,1-abs(c)**2))+0j))
    Ks=(K0,K1)
    norm=tuple(tuple(sum(mul(adj(K),K)[i][j] for K in Ks) for j in range(2)) for i in range(2))
    assert near(norm,I)
    assert near(apply(Ks,rho0),rho0)
    assert near(apply(Ks,rho01),((0j,c),(0j,0j)))
    C=choi(Ks)
    # In the input-first Choi basis, Gamma=Z^T tensor Z.
    gamma=(1,-1,-1,1)
    assert all(abs(C[i][j])<1e-12 for i in (1,2) for j in range(4))
    assert all(abs(C[i][j])<1e-12 for i in range(4) for j in (1,2))
    assert all(abs(gamma[i]*C[i][j]-C[i][j])<1e-12 for i in range(4) for j in range(4))
    assert all(near(mul(Z,K),mul(K,Z)) for K in Ks)

# The X unitary's Choi vector is supported in the negative Gamma eigenspace.
v=vec(X)
assert abs(v[0])<1e-12 and abs(v[3])<1e-12
assert sum(abs(v[i])**2 for i in (1,2))==2

for qi,qx,qy,qz in (
    (F(7,10),F(1,10),F(1,10),F(1,10)),
    (F(1,10),F(3,10),F(1,4),F(7,20)),
    (F(0),F(1),F(0),F(0)),
    (F(1),F(0),F(0),F(0)),
    (F(0),F(0),F(1,2),F(1,2)),
):
    assert qi+qx+qy+qz==1
    t=qx+qy
    # Pauli action on the basis-state witness and the compatible I/Z mixture.
    pauli=tuple(tuple(sum(complex(w)*action(U,rho0)[i][j] for w,U in zip((qi,qx,qy,qz),(I,X,Y,Z))) for j in range(2)) for i in range(2))
    compat=tuple(tuple(sum(complex(w)*action(U,rho0)[i][j] for w,U in ((qi+qx,I),(qz+qy,Z))) for j in range(2)) for i in range(2))
    assert near(compat,rho0)
    assert abs(pauli[0][0]-(1-float(t)))<1e-12
    assert abs(pauli[1][1]-float(t))<1e-12
    assert abs(abs(pauli[0][0]-compat[0][0])+abs(pauli[1][1]-compat[1][1])-2*float(t))<1e-12
    # Matching upper bound: qx*(Ad_X-id) + qy*(Ad_Y-Ad_Z).
    for R in (rho0,rho01):
        pR=tuple(tuple(sum(complex(w)*action(U,R)[i][j] for w,U in zip((qi,qx,qy,qz),(I,X,Y,Z))) for j in range(2)) for i in range(2))
        cR=tuple(tuple(sum(complex(w)*action(U,R)[i][j] for w,U in ((qi+qx,I),(qz+qy,Z))) for j in range(2)) for i in range(2))
        diff=tuple(tuple(pR[i][j]-cR[i][j] for j in range(2)) for i in range(2))
        rhs=tuple(tuple(complex(qx)*(action(X,R)[i][j]-R[i][j])+complex(qy)*(action(Y,R)[i][j]-action(Z,R)[i][j]) for j in range(2)) for i in range(2))
        assert near(diff,rhs)
print('VERIFY_OK')
