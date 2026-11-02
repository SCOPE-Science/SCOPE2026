"""Independent exact symbolic and finite-graph checks for two-site decay on triangular graphs.
Dependencies: Python 3, sympy, numpy, scipy.  Run: python check_triangular.py
"""
from itertools import combinations
import sympy as s
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

n=s.symbols('n',integer=True, positive=True)
x=s.symbols('x',nonnegative=True)
lam=[2*n-4,n-4,-2]

def spectral_weights(kind):
    d=2*n-4
    common=(n-2 if kind=='adjacent' else 4)
    Auv=(1 if kind=='adjacent' else 0)
    w=[]
    for i in range(3):
        v,z=[lam[j] for j in range(3) if j!=i]
        den=(lam[i]-v)*(lam[i]-z)
        diagonal=(d+v*z)/den
        off=(common-(v+z)*Auv)/den
        w.append((s.factor(diagonal+off),s.factor(diagonal-off)))
    return w

def coefficients(kind):
    w=spectral_weights(kind)
    a=s.S(0); b=s.S(0)
    for sign in range(2):
        ids=range(3) if sign==0 else range(1,3)
        for j in ids:
            v=w[j][sign]
            a+=1/v
            z=sum((v+w[k][sign])/(lam[j]-lam[k]) for k in ids if k!=j)
            b+=z*z/(4*v)
    return s.factor(a),s.factor(b)

expected_adj=[
    (4/(n*(n-1)),s.S(0)),
    ((3*n-8)/(n*(n-2)),1/(n-2)),
    ((n-3)**2/((n-2)*(n-1)),(n-3)/(n-2))]
expected_dis=[
    (4/(n*(n-1)),s.S(0)),
    (2*(n-4)/(n*(n-2)),2/(n-2)),
    ((n*n-5*n+8)/((n-2)*(n-1)),(n-4)/(n-2))]
assert all(s.simplify(a-b)==0 for row,exp in zip(spectral_weights('adjacent'),expected_adj) for a,b in zip(row,exp))
assert all(s.simplify(a-b)==0 for row,exp in zip(spectral_weights('disjoint'),expected_dis) for a,b in zip(row,exp))
AA,BA=coefficients('adjacent'); AD,BD=coefficients('disjoint')
assert s.simplify(AA-(3*n**5-13*n**4-35*n**3+285*n**2-536*n+320)/(4*(n-3)**2*(3*n-8)))==0
assert s.simplify(BA-(3*n**3+59*n**2-383*n+545)/(64*(n-3)**2*(3*n-8)))==0
assert s.simplify(AD-(n-1)*(n**4-5*n**3+4*n**2+16*n-32)/(4*(n-4)*(n*n-5*n+8)))==0
assert s.simplify(BD-(n**3+12*n**2-68*n+64)/(64*(n-4)*(n*n-5*n+8)))==0

# Strict placement comparison at separately optimal absorption rates.
diff=s.factor(AA*BA-AD*BD)
num,den=s.fraction(diff)
P=s.Poly(s.expand(num.subs(n,x+7)),x)
assert all(c>0 for c in P.all_coeffs())
assert s.factor(diff.subs(n,5))<0 and s.factor(diff.subs(n,6))<0
assert s.factor(diff.subs(n,7))>0
print('exact optimum-placement switch: adjacent n=5,6; disjoint n>=7')
print('shifted polynomial coefficients, ascending:',list(reversed(P.all_coeffs())))

# Fixed-rate placement signs: adjacent always preferred at n=5, disjoint at n>=8.
da=s.factor(AA-AD);db=s.factor(BA-BD)
for v in [da,db]:
    numv,denv=s.fraction(v)
    assert all(c>0 for c in s.Poly(s.expand(numv.subs(n,x+8)),x).all_coeffs())
assert da.subs(n,5)<0 and db.subs(n,5)<0
assert da.subs(n,6)<0 and db.subs(n,6)>0
assert da.subs(n,7)<0 and db.subs(n,7)>0
print('fixed-rate placement ordering: n=5 adjacent always; n>=8 disjoint always; n=6,7 rate-dependent')

# Construct original physical graph (not a premade 5-site reduced model).
def original_matrix(nn):
    V=list(combinations(range(nn),2));N=len(V)
    A=np.zeros((N,N),dtype=float)
    for i,u in enumerate(V):
        for j in range(i):
            if len(set(u)&set(V[j]))==1:A[i,j]=A[j,i]=1
    return V,A

for nn in (5,6,7,8,9):
    V,A=original_matrix(nn);N=len(V)
    u=V.index((0,1))
    for kind,vlabel in [('adjacent',(0,2)),('disjoint',(2,3))]:
        v=V.index(vlabel)
        e=np.eye(N)[:,[u,v]]
        B=np.column_stack([e,A@e,A@A@e])
        Q,R=np.linalg.qr(B)
        rank=np.linalg.matrix_rank(B,tol=1e-8)
        assert rank==5,(nn,kind,rank)
        # use SVD of full-graph Krylov basis to avoid rank-deficient QR basis issues
        uu,ss,vt=np.linalg.svd(B,full_matrices=False);Q=uu[:,:5]
        H=Q.T@A@Q
        D=Q.T@e@e.T@Q
        a,b=[float(z.subs(n,nn)) for z in ((AA,BA) if kind=='adjacent' else (AD,BD))]
        for gamma in (.37,1.4,5.8):
            G=-1j*H-gamma*D/2
            X=solve_continuous_lyapunov(G,-np.eye(5))
            numerical=np.trace(X).real
            predicted=a/gamma+b*gamma
            assert abs(numerical-predicted) < 1e-6*(1+predicted),(nn,kind,gamma,numerical,predicted)
        print(f'physical graph T({nn}) {kind}: 5 bright modes; 3 Lyapunov lifetimes match')
print('PASS: 30 full-graph Lyapunov checks, symbolic formula, and all-n positivity certificate')
