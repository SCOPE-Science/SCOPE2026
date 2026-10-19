"""Exact covariance check for two-sample heavy-ball random reshuffling."""
import sympy as s
r,b=s.symbols('r b',real=True)
A=s.Matrix([[1+b-r,-b],[1,0]])
B=s.expand(A*A)
q=r*s.Matrix([b-r,1])
den=(1-b**2)*(2+2*b-r)*(r*r-2*(1+b)*r+2*(1+b*b))
N11=r*r*(4*b*b*(1+b)+r*(1-4*b-5*b*b)+2*b*r*r)
N12=-r*r*(3*b*b*r-4*b*b-3*b*r*r+6*b*r-4*b+r**3-3*r*r+3*r)
N22=r*r*(b*b*r-4*b*r+4*b+2*r*r-5*r+4)
C=s.Matrix([[N11,N12],[N12,N22]])/den
assert all(s.cancel(z)==0 for z in C-B*C*B.T-q*q.T), 'covariance Lyapunov mismatch'
assert s.factor(C[0,0].subs(b,0)-r**3/((2-r)*(r*r-2*r+2)))==0
assert s.simplify(s.limit(C[0,0]/r**2,r,0)-b**2/(1-b**4))==0
c=s.symbols('c',positive=True)
assert s.limit((C[0,0].subs(b,c*s.sqrt(r)))/r**3,r,0)==c*c+s.Rational(1,4)
assert s.limit((C[0,0].subs(b,r))/r**3,r,0)==s.Rational(1,4)
print('Symbolic covariance, zero momentum identity, fixed momentum asymptotics, crossover: PASS')
# Independent path enumeration at 5 epoch horizons using exact rational arithmetic.
checks=0
for rr,bb in [(s.Rational(1,2),s.Rational(1,3)),(s.Rational(1,4),s.Rational(3,4)),(s.Rational(3,4),s.Rational(1,2)),(s.Rational(1,1),s.Rational(0)),(s.Rational(1,10),s.Rational(1,8))]:
    AA=A.subs({r:rr,b:bb});BB=AA*AA;qq=q.subs({r:rr,b:bb})
    # Sequence-average of state from zero start after each of four epochs.
    covariance=s.zeros(2,2)
    states=[s.zeros(2,1)]
    for epoch in range(1,7):
        states=[BB*v+sign*qq for v in states for sign in (-1,1)]
        direct=sum((v*v.T for v in states),s.zeros(2,2))/len(states)
        covariance=BB*covariance*BB.T+qq*qq.T
        assert direct==covariance,(rr,bb,epoch)
        checks+=1
print(f'{checks} exact-rational full-path covariance comparisons: PASS')
import numpy as np
for rr,bb in [(0.005,0.05),(0.05,0.5),(0.2,0.85),(1.1,0.4),(0.85,0.0)]:
    ma=np.asarray(A.subs({r:rr,b:bb}),dtype=float)
    mb=ma@ma
    v=np.asarray(q.subs({r:rr,b:bb}),dtype=float).ravel()
    cov=np.zeros((2,2))
    for _ in range(8000):cov=mb@cov@mb.T+np.outer(v,v)
    exact=float(C[0,0].subs({r:rr,b:bb}))
    assert np.isclose(cov[0,0],exact,atol=1e-10,rtol=1e-9),(rr,bb,cov[0,0],exact)
print('5 independent matrix-Lyapunov numerical comparisons: PASS')
# The iid-with-replacement comparator uses an independent gradient sign each step.
u,v,w=s.symbols('u v w')
T=s.Matrix([[u,v],[v,w]])
force=s.Matrix([r,0])
iid_cov=s.solve(list(T-A*T*A.T-force*force.T),[u,v,w])
iid_formula=r*(1+b)/((1-b)*(2+2*b-r))
assert s.cancel(iid_cov[u]-iid_formula)==0
assert s.simplify(s.limit((C[0,0]/iid_formula)/r,r,0)-2*b*b/((1+b)*(1+b*b)))==0
assert s.limit(((C[0,0]/iid_formula).subs(b,0))/r**2,r,0)==s.Rational(1,2)
print('Independent-sampling comparator and sharp ratio limits: PASS')
assert s.simplify(s.limit(C[1,1]/r**2,r,0)-1/(1-b**4))==0
assert s.simplify(s.limit(C[0,0]/C[1,1],r,0)-b*b)==0
assert s.limit((C[0,0]/C[1,1]).subs(b,0)/r,r,0)==s.Rational(1,4)
print('Two stationary epoch-phase variances and limiting phase ratios: PASS')
