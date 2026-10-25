"""Exact and numerical checks for symmetric double-star stochastic mixing."""
import numpy as np
import sympy as s

z=s.sqrt(2)
t=1+z
for k in range(1,13):
    D=s.simplify(1+k*t**2)
    a=s.simplify((2+z)/D)
    b=s.simplify((1+k*(1+z))/D)
    g=s.simplify(2/D)
    assert s.simplify(k*a+b-1)==0
    assert s.simplify(a*(t-1)-g*t)==0
    assert s.simplify(k*a*(1-t)+2*b-g)==0
    assert s.simplify(g*( (k+1)*a+2*b-g)-2*a*b)==0
    assert float(a)>float(g)>0
    assert float(b)>0
    n=2*k+2
    # vertices: hub L=0, leaves 1..k, hub R=k+1, leaves k+2..2k+1
    L=s.zeros(n)
    def edge(u,v,w):
        L[u,u]+=w;L[v,v]+=w;L[u,v]-=w;L[v,u]-=w
    for i in range(1,k+1): edge(0,i,a)
    edge(0,k+1,b)
    for i in range(k+2,2*k+2): edge(k+1,i,a)
    P=s.eye(n)-L
    assert all(s.simplify(sum(P[i,j] for j in range(n))-1)==0 for i in range(n))
    assert all(float(P[i,j])>-1e-12 for i in range(n) for j in range(n))
    x=s.Matrix([1]+[t]*k+[-1]+[-t]*k)
    assert all(s.simplify(v)==0 for v in L*x-g*x)
    spec=np.linalg.eigvalsh(np.array(P,dtype=float))
    mu=max(abs(spec[:-1]))
    assert abs(mu-(1-float(g)))<1e-9, (k,mu,g)
    # compare with maximum-degree/Metropolis chain
    Lmd=s.zeros(n)
    for i in range(1,k+1):
      for u,v in [(0,i),(k+1,k+1+i)]:
        Lmd[u,u]+=s.Rational(1,k+1);Lmd[v,v]+=s.Rational(1,k+1)
        Lmd[u,v]-=s.Rational(1,k+1);Lmd[v,u]-=s.Rational(1,k+1)
    u,v=0,k+1
    Lmd[u,u]+=s.Rational(1,k+1);Lmd[v,v]+=s.Rational(1,k+1)
    Lmd[u,v]-=s.Rational(1,k+1);Lmd[v,u]-=s.Rational(1,k+1)
    evals=np.linalg.eigvalsh(np.array(Lmd,dtype=float))
    gamma=(k+3-np.sqrt((k+3)**2-8))/(2*(k+1))
    assert abs(evals[1]-gamma)<1e-12
    if k>1: assert float(g)>gamma

# Random full-dimensional feasible competitors with nonuniform edge weights.
rng=np.random.default_rng(314159)
trials=0
for k in (1,2,3,4,6):
 n=2*k+2
 D=1+k*(3+2*np.sqrt(2)); theoretical=1-2/D
 for _ in range(400):
  # arbitrary nonnegative spoke weights and bridge; symmetric matrix
  # scale to ensure hub stochastic constraints.
  raw=rng.random(2*k+1)
  b=raw[-1]/(k+1)
  aL=raw[:k]/(k+1)
  aR=raw[k:2*k]/(k+1)
  weights=np.r_[aL,aR]
  P=np.zeros((n,n))
  for i in range(k):
   u,v=0,1+i;P[u,v]=P[v,u]=aL[i]
   u,v=k+1,k+2+i;P[u,v]=P[v,u]=aR[i]
  P[0,k+1]=P[k+1,0]=b
  np.fill_diagonal(P,1-P.sum(axis=1))
  assert P.min()>=-1e-14
  ev=np.linalg.eigvalsh(P)
  mu=np.max(abs(ev[:-1]))
  assert mu>theoretical-1e-10
  trials+=1
print('VERIFY_OK: exact radical identities for 12 graph orders; 2000 fully nonuniform feasible competitors; stochasticity, 2k+2 eigenvalue comparisons and Metropolis asymptotic comparison')
