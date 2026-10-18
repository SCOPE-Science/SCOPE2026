"""Reproduce exact two-operator resolvent-pair identities and limiting covariance constants.

Run: python paired_split_verify.py
Dependencies: numpy>=1.23, scipy>=1.9, sympy>=1.10
All arithmetic identities are checked exactly; quadrature and limiting ratios are numerical cross-checks.
"""
from fractions import Fraction as F
from itertools import product
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad_vec

H1=sp.Matrix([[2,0],[0,1]])
H2=sp.Matrix([[2,1],[1,2]])
x0=sp.Matrix([1,2]); I=sp.eye(2)
h=sp.symbols('h')
R1=(I+h*H1).inv()
R2=(I+h*H2).inv()
Bplus=R2*R1
Bminus=R1*R2
M=(Bplus+Bminus)/2
D=(Bminus-Bplus)/2
Q=H1**2+H2**2
J=H1*H2-H2*H1
A=(H1+H2)/2

def coeff_mat(expr,k):
 return expr.applyfunc(lambda a:sp.diff(a,h,k).subs(h,0)/sp.factorial(k))

assert coeff_mat(M,0)==I
assert coeff_mat(M,1)==-2*A
assert coeff_mat(M,2)==Q+(H1*H2+H2*H1)/2
assert coeff_mat(D,0)==sp.zeros(2)
assert coeff_mat(D,1)==sp.zeros(2)
assert coeff_mat(D,2)==J/2
assert J != sp.zeros(2)
print('EXACT: paired resolvent expansions and commutator sign PASSED')

def second_moment_pair(n,step):
 subs={h:step}
 P=Bplus.subs(subs);N=Bminus.subs(subs)
 mean=sp.zeros(2,1);moment=sp.zeros(2)
 for choices in product((P,N),repeat=n):
  y=x0
  for B in choices:y=B*y
  mean+=y/(2**n)
  moment+=y*y.T/(2**n)
 return mean,moment-mean*mean.T

def recurrence_pair(n,step):
 mm=M.subs(h,step); dd=D.subs(h,step)
 mean=x0;cov=sp.zeros(2)
 for k in range(n):
  cov=mm*cov*mm.T+dd*cov*dd.T+dd*mean*mean.T*dd.T
  mean=mm*mean
 return mean,cov

for n,step in [(1,F(1,5)),(2,F(1,7)),(3,F(1,9)),(4,F(1,11)),(5,F(1,13))]:
 a,b=second_moment_pair(n,sp.Rational(step.numerator,step.denominator))
 c,d=recurrence_pair(n,sp.Rational(step.numerator,step.denominator))
 assert a==c and b==d
 print('EXACT: enumeration and covariance recursion agree for',n,'pairs')

a1=np.asarray(H1,float);a2=np.asarray(H2,float)
a=(a1+a2)/2; j=a1@a2-a2@a1; q=a1@a1+a2@a2
u0=np.array([1.,2.]); T=1.
eT=expm(-a*T)
def kern_m(s): return (expm(-a*(T-s))@q@expm(-a*s)@u0)/4
def kern_pair(s):
 v=expm(-a*(T-s))@j@expm(-a*s)@u0
 return np.outer(v,v)/8
def kern_iid(s):
 delta=a1-a2
 v=expm(-a*(T-s))@delta@expm(-a*s)@u0
 return np.outer(v,v)/4
V=quad_vec(kern_m,0,T,epsabs=1e-12)[0]
K=quad_vec(kern_pair,0,T,epsabs=1e-12)[0]
Ki=quad_vec(kern_iid,0,T,epsabs=1e-12)[0]
print('EXPECTED LIMIT: paired mean bias vector',V)
print('EXPECTED LIMIT: paired covariance matrix',K)
print('EXPECTED LIMIT: iid covariance matrix',Ki)
assert np.trace(K)>0 and np.trace(Ki)>0


def run_cov(n,paired):
 step=T/(2*n) if paired else T/n
 r1=np.linalg.inv(np.eye(2)+step*a1)
 r2=np.linalg.inv(np.eye(2)+step*a2)
 if paired: P=r2@r1;N=r1@r2
 else: P=r1;N=r2
 m=(P+N)/2; d=(P-N)/2
 mean=u0.copy();cov=np.zeros((2,2))
 for k in range(n):
  cov=m@cov@m.T+d@cov@d.T+np.outer(d@mean,d@mean)
  mean=m@mean
 return step,mean,cov

for n in (50,100,200,400,800):
 st,m,cov=run_cov(n,True)
 r=np.trace(cov)/(st**3*np.trace(K))
 rb=np.linalg.norm((m-eT@u0)/st-V)
 assert abs(r-1)<2.1/n and rb < 3/n
 print(f'NUMERIC: paired N={n}, trace ratio={r:.9f}, bias error={rb:.7g}')
for n in (50,100,200,400,800):
 st,m,cov=run_cov(2*n,False)
 r=np.trace(cov)/(st*np.trace(Ki))
 assert abs(r-1)<3/n
 print(f'NUMERIC: iid same-budget steps={2*n}, trace ratio={r:.9f}')

# Commuting operators have identical two-step products, hence exactly zero pairing variance.
rc1=(I+h*H1).inv()
rc2=(I+h*(3*H1+I)).inv()
assert sp.simplify(rc1*rc2-rc2*rc1)==sp.zeros(2)
print('EXACT: commuting pair has identically zero ordering variance')
print('ALL CHECKS PASSED')
