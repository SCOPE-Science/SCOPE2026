"""Reproducibility checks for geometric Gaussian widths of symmetric-edge tree polytopes."""
import numpy as np
from scipy.stats import norm
from math import sqrt, log
from fractions import Fraction
from itertools import product

rng = np.random.default_rng(20261019)

def exact_integer_determinant(matrix):
    """Fraction-free Bareiss determinant; no floating-point rounding."""
    a = [[int(v) for v in row] for row in matrix.tolist()]
    n = len(a)
    if n == 1:
        return a[0][0]
    den, sign = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        piv = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * piv - a[i][k] * a[k][j]
                assert num % den == 0
                a[i][j] = num // den
            a[i][k] = 0
        den = piv
    return sign * a[n - 1][n - 1]
# Exact Gram matrix identities for multiple tree shapes (path, star, broom).
for N in range(3, 15):
    edge_sets = [ [(i, i+1) for i in range(N-1)], [(0, i) for i in range(1,N)] ]
    if N >= 5: edge_sets.append([(0,i) for i in range(1,N-2)] + [(0,N-2),(N-2,N-1)])
    for edges in edge_sets:
        A=np.zeros((N,N-1), dtype=int)
        for j,(u,v) in enumerate(edges): A[u,j]=1;A[v,j]=-1
        determinant=exact_integer_determinant(A.T@A)
        assert determinant == N, (N, edges, determinant)

# Gaussian shared-edge correlations are +-1/2 (disjoint covariance zero).
for N in range(4, 15):
    edges=[(i,i+1) for i in range(N-1)]
    B=np.zeros((N,N-1))
    for i,(u,v) in enumerate(edges):B[u,i]=1/sqrt(2);B[v,i]=-1/sqrt(2)
    C=B.T@B
    assert np.max(abs(np.diag(C)-1))<1e-12
    for i in range(N-1):
        for j in range(N-1):
            assert abs(C[i,j]-(1 if i==j else (-.5 if abs(i-j)==1 else 0)))<1e-12

# Quantitative checks for the critical realization and its phase transition.
for n in (512,1024,4096,16384):
    b=norm.isf(1/n)
    for s in (-.5,0,1):
        q=(b+s)/sqrt(2)
        ell=max(2, int(1/(2*norm.sf(q))))
        phase=sqrt(2)*norm.isf(1/(2*ell))-b
        assert abs(phase-s)<.07, (n,s,ell,phase)

# Direct finite-dimensional Gaussian support formula from the vertex set,
# independently of the graph incidence maximum expression.
for N in (4,6,8):
    edges=[(0,i) for i in range(1,N-2)]+[(0,N-2),(N-2,N-1)]
    for j in range(30):
        g=rng.normal(size=N)
        u=(g-g.mean())/np.linalg.norm(g-g.mean())
        h=max(abs(u[a]-u[b]) for a,b in edges)
        verts=[]
        for a,b in edges:
            e=np.zeros(N);e[a]=1;e[b]=-1
            verts.extend([e,-e])
        assert abs(h-max(float(np.dot(v,u)) for v in verts))<1e-12

# Numerical illustration, not a proof or independent certification.
def sample_normalized_broom(n,ell,R=1000):
    # Standard Gaussian coordinates; include Euclidean intrinsic normalization.
    g0=rng.normal(size=R)
    leaf=rng.normal(size=(R,n))
    chain=rng.normal(size=(R,ell))
    star=np.max(np.abs(leaf-g0[:,None]),axis=1)
    prev=np.concatenate((g0[:,None],chain[:,:-1]),axis=1)
    path=np.max(np.abs(chain-prev),axis=1)
    rest=np.concatenate((g0[:,None],leaf,chain),axis=1)
    radius=np.linalg.norm(rest-rest.mean(axis=1,keepdims=True),axis=1)
    return np.maximum(star,path)*sqrt(n+ell+1)/radius

for n,s in ((1024,0),(1024,1),(4096,1)):
    b=norm.isf(1/n)
    ell=int(1/(2*norm.sf((b+s)/sqrt(2))))
    x=sample_normalized_broom(n,ell,R=800)-b
    for t in (max(s,.5)+.7,max(s,1)+1.):
        empir=float(np.mean(x<=t)); theo=float(2*norm.cdf(t)-1)
        # Finite-size deviations are expected at this slowly converging extreme-value scale.
        print("FINITE_SIZE_CDF", n,ell,s,t,round(empir,4),round(theo,4))
    print('ILLUSTRATION',n,ell,s,float(np.mean(x)),float(np.mean(x< s)),float(np.mean(x<=s+.3)))
print('VERIFY_OK exact_gram=34 independent_support_checks=90 phase_boundary_cases=12 simulation_only=3')
