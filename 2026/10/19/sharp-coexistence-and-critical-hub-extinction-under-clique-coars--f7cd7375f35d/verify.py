"""Exact checks for a competitive population system on a clique-joined hub.

Requires Python >=3.10, sympy, numpy, scipy.
A numerical integration is corroboration only; global claims are proved analytically.
"""
from fractions import Fraction
from math import isclose
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

z=sp.symbols('z',positive=True)

def H(part):
    return z*sum(sp.Rational(q,1)/(1+z*(q-1)) for q in part)

def threshold(part):
    if len(part)==1:return sp.S.One
    f=sp.factor(sp.together(H(part)-1))
    roots=sp.solve(sp.together(f).as_numer_denom()[0],z)
    good=[v for v in roots if v.is_real and 0<float(v)<1]
    assert len(good)==1,(part,roots)
    return sp.simplify(good[0])

def adjacency(part):
    m=sum(part); A=sp.zeros(m+1)
    for k in range(1,m+1):A[0,k]=A[k,0]=1
    k=1
    for q in part:
      for i in range(k,k+q):
       for j in range(i+1,k+q):A[i,j]=A[j,i]=1
      k+=q
    return A

for part in [[1]*6,[2,1,1,1,1],[2,2,1,1],[2,2,2],[4,2],[6],[1,1]]:
    t=threshold(part)
    A=adjacency(part); M=sp.eye(A.rows)+z*A
    Hf=H(part)
    h=sp.factor((1-Hf)/(1-z*Hf))
    if len(part)>=2:
        assert sp.simplify(Hf.subs(z,t)-1)==0
        assert sp.simplify(h.subs(z,t))==0
        hcoef=sp.simplify(1-z**2*sum(q/(1+z*(q-1)) for q in part))
        assert sp.simplify(hcoef.subs(z,t)-(1-t))==0
    xs=[h]
    for q in part:xs.extend([(1-z*h)/(1+z*(q-1))]*q)
    assert all(sp.simplify(v)==0 for v in M*sp.Matrix(xs)-sp.ones(len(xs),1))
    at=sp.Rational(1,10) if len(part)==1 or t>sp.Rational(1,10) else t/2
    eq=sp.Matrix([x.subs(z,at) for x in xs]);
    assert all(e>0 for e in eq)
    ev=np.linalg.eigvalsh(np.array(M.subs(z,at)).astype(float))
    assert ev.min()>1e-9
    if len(part)>=2:
      vec=sp.Matrix([sp.S.One]+[-t/(1+t*(q-1)) for q in part for _ in range(q)])
      B=sp.diag(*[sp.S.Zero]+[1/(1+t*(q-1)) for q in part for _ in range(q)])
      J=-B*(sp.eye(A.rows)+t*A)
      assert all(sp.simplify(v)==0 for v in J*vec)
    print('partition',part,'tau_critical',t,'numeric',round(float(t),9))

assert threshold([1]*6)==sp.Rational(1,6)
assert threshold([2,2,2])==sp.Rational(1,5)
assert threshold([4,2])==(-1+2*sp.sqrt(2))/7
assert threshold([6])==sp.S.One
assert sp.Rational(1,6)<sp.Rational(1,5)<(-1+2*sp.sqrt(2))/7<1

# Subadditivity of f(q): exact numerator is positive for integer p,q>=1 and 0<z<1.
p,q=sp.symbols('p q',positive=True)
f=lambda w:w/(1+z*(w-1))
diff=sp.factor(sp.together(f(p)+f(q)-f(p+q)))
print('merge difference:',diff)
assert sp.simplify(diff.subs({p:2,q:4,z:sp.Rational(1,3)}))>0

# Numerical trajectory comparisons (not proof of any asymptotic claim).
def run(part,tau,t_end=7000.0):
 A=np.array(adjacency(part)).astype(float)
 n=A.shape[0]; y0=np.array([.35]+[.12+.05*((i*7)%5) for i in range(n-1)])
 def rhs(t,y):return y*(1-y-tau*A@ y)
 ts=[t_end/2,t_end]
 sol=solve_ivp(rhs,[0,t_end],y0,method='DOP853',rtol=2e-11,atol=1e-13,t_eval=ts,max_step=10.0)
 assert sol.success
 return sol.y[:,-1]
part=[2,2,2];t=float(threshold(part))
y=run(part,t)
print('critical t hub',7000*y[0],'target',1/(1-t))
assert abs(7000*y[0]-1/(1-t))<0.012
leaf_target=1/(1+t)
for val in y[1:]:
 assert abs(7000*(val-leaf_target) - (-t/(1+t))/(1-t))<.02

for tau,expected in [(0.12,'interior'),(0.28,'boundary')]:
 y=run([2,2,2],tau,3000)
 h= float(((1-H([2,2,2]))/(1-z*H([2,2,2]))).subs(z,tau)) if expected=='interior' else 0
 target_leaf=(1-tau*h)/(1+tau)
 assert abs(y[0]-h)<1e-8 and np.max(np.abs(y[1:]-target_leaf))<1e-8
 print('tau',tau,'hub',y[0],'leaves',y[1:])
print('ALL SYMBOLIC AND NUMERICAL CHECKS PASSED')
