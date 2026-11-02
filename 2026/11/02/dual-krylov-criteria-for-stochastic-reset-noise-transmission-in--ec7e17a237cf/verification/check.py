"""Finite checks for strong-rate fluctuations under common-clock partial reset.
Execute: python verify_reset40.py (NumPy and SciPy required).
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

checks = 0

def assert_close(a, b, atol=1e-10, rtol=1e-9):
    global checks
    np.testing.assert_allclose(a, b, atol=atol, rtol=rtol)
    checks += 1

def assert_true(cond):
    global checks
    assert bool(cond)
    checks += 1

def laplacian(n, edges):
    L = np.zeros((n,n))
    for i,j,w in edges:
        L[i,i] += w
        L[j,j] += w
        L[i,j] -= w
        L[j,i] -= w
    return L

def stationary(L, omega, r, rate, coupling):
    n = len(omega)
    P = np.diag([1.0]*r + [0.0]*(n-r))
    J = np.eye(n)-P
    m = np.linalg.solve(coupling*L+rate*P, omega)
    K = coupling*(np.kron(L,np.eye(n))+np.kron(np.eye(n),L))
    K += rate*(np.eye(n*n)-np.kron(J,J))
    source = rate*np.outer(P@m,P@m)
    C = np.linalg.solve(K,source.reshape(n*n)).reshape(n,n)
    assert_close(C,C.T, atol=2e-10)
    assert_close(coupling*(L@C+C@L)+rate*(C-J@C@J),source,atol=1e-10)
    assert_true(np.linalg.eigvalsh(C).min()>-1e-9)
    return m,C

def theory(L, omega, r, coupling):
    H=L[:r,:r]; E=L[r:,:r]; G=L[r:,r:]
    m0=np.linalg.solve(G,omega[r:])/coupling
    h=omega[:r]-coupling*E.T@m0
    g=E@h
    T=solve_continuous_lyapunov(G,2*coupling*np.outer(g,g))
    assert_close(G@T+T@G,2*coupling*np.outer(g,g),atol=1e-10)
    return m0,h,g,T

# Two-node exact rational benchmark: graph edge 1--2; only node 1 reset.
L=laplacian(2, [(0,1,1.0)])
for coupling in [0.3,1,2.5]:
  for rate in [0.1,1,3,10,100]:
    m,C=stationary(L,np.array([1.,0.]),1,rate,coupling)
    assert_close(m,np.array([1/rate,1/rate]))
    assert_close(C[0,0],(rate+coupling)/(rate**2*(rate+3*coupling)))
    assert_close(C[0,1],coupling/(rate**2*(rate+3*coupling)))
    assert_close(C[1,1],coupling/(rate**2*(rate+3*coupling)))

# Three-node chain: one clock feeds a full-rank two-dimensional covariance.
L=laplacian(3,[(0,1,1.),(1,2,1.)]);omega=np.array([1.,0.,0.])
m0,h,g,T=theory(L,omega,1,1.)
assert_close(T,np.array([[2/3,1/3],[1/3,1/3]]))
assert_true(np.linalg.det(T)>0)
for rate in [100,300,1000]:
  m,C=stationary(L,omega,1,rate,1.)
  assert_close(rate*m[:1],h,atol=2e-9)
  assert_close(rate*(m[1:]-m0),-np.linalg.solve(L[1:,1:],L[1:,:1]@h),atol=1e-9)
  assert_true(np.max(abs(rate**2*C[:1,:1]-np.outer(h,h)))<15/rate)
  assert_true(np.max(abs(rate**3*C[:1,1:]+np.outer(h,h)@L[:1,1:]))<30/rate)
  assert_true(np.max(abs(rate**3*C[1:,1:]-T))<100/rate)

# A symmetric star: common reset clock and antisymmetric reset drifts stay invisible at the unreset center.
L=laplacian(3,[(0,2,1.),(1,2,1.)]);omega=np.array([1.,-1.,0.]);
m0,h,g,T=theory(L,omega,2,1.)
assert_close(g,np.zeros(1)); assert_close(T,np.zeros((1,1)))
for rate in [0.2,1,5,100]:
  m,C=stationary(L,omega,2,rate,1.)
  assert_close(m[2:],np.array([0.]),atol=1e-12)
  assert_close(C[2:,2:],np.zeros((1,1)),atol=1e-11)
  assert_true(C[0,0]>0)

# Random weighted graphs: directly compare finite moment equations against the singular perturbation limits.
rng=np.random.default_rng(4040)
for n in [3,4,5,6]:
  for case in range(8):
    # Spanning path plus extra edges ensures connectedness.
    edges=[(i,i+1,float(rng.uniform(.5,1.8))) for i in range(n-1)]
    for i in range(n):
      for j in range(i+2,n):
        if rng.random()<.45:
          edges.append((i,j,float(rng.uniform(.4,1.6))))
    L=laplacian(n,edges)
    r=int(rng.integers(1,n));omega=rng.normal(size=n);coupling=float(rng.uniform(.6,1.6))
    m0,h,g,T=theory(L,omega,r,coupling)
    rate=2000.
    m,C=stationary(L,omega,r,rate,coupling)
    assert_true(np.linalg.eigvalsh(T).min()>-1e-9)
    assert_true(np.linalg.norm(rate**2*C[:r,:r]-np.outer(h,h)) < .2*(1+np.linalg.norm(h)**2))
    assert_true(np.linalg.norm(rate**3*C[:r,r:]+coupling*np.outer(h,h)@L[:r,r:]) < .4*(1+np.linalg.norm(h)**2))
    assert_true(np.linalg.norm(rate**3*C[r:,r:]-T) < .9*(1+np.linalg.norm(T)))
    # Krylov nullspace/rank identity, certified for numerical singular values at modest n.
    Krylov=np.column_stack([np.linalg.matrix_power(L[r:,r:],k)@g for k in range(n-r)])
    rk=np.linalg.matrix_rank(Krylov,tol=1e-7)
    rk2=np.linalg.matrix_rank(T,tol=1e-7)
    assert_true(rk==rk2)



# Jointly reset two-node boundary with full-rank fluctuations at two unreset nodes.
L=laplacian(4,[(0,1,1.),(1,2,1.),(2,3,1.)])
omega=np.array([0.,1.,0.,0.]); r=2
m0,h,g,T=theory(L,omega,r,1.)
assert_close(T,np.array([[2/3,1/3],[1/3,1/3]]))
assert_true(np.linalg.matrix_rank(T)==2)
for rate in [100.,400.,1000.]:
    m,C=stationary(L,omega,r,rate,1.)
    assert_true(np.linalg.norm(rate**3*C[r:,r:]-T)<20/rate)

# The cubic coefficient can vanish without exact cancellation at any positive rate.
L=laplacian(4,[(0,3,1.),(1,3,1.),(0,2,1.)])
omega=np.array([1.,-1.,0.,0.]);r=3
m0,h,g,T=theory(L,omega,r,1.)
assert_close(g,np.array([0.]))
assert_true(abs((L[r:,:r]@L[:r,:r]@h).item())>.5)
for rate in [1.,10.,100.,300.]:
    m,C=stationary(L,omega,r,rate,1.)
    assert_true(C[3,3]>0)
    assert_true(rate**3*C[3,3]<.3)

print(f"PASS: {checks} assertions including jointly reset networks")
