"""Reproducibility checks for the stationary two-lane throughput theorem.
All rates and formulas pertain to the exact product-stationary current."""
from fractions import Fraction as F
from math import sqrt
import random

CHECKS = 0

def check(cond, label):
    global CHECKS
    assert cond, label
    CHECKS += 1

def bisect(f, lo, hi, steps=120):
    fl=f(lo)
    check(fl*f(hi)<0, 'root is bracketed')
    for _ in range(steps):
        mid=(lo+hi)/2
        if f(mid)*fl<=0: hi=mid
        else: lo=mid; fl=f(mid)
    return (lo+hi)/2

# Algebraic reduction, checked identically on rational values of the parameters.
for s_num in range(21):
 for k in range(21):
  u=F(s_num,20); v=F(k,20)
  s=u+v; p=u*v
  for B,gamma in ((F(1),F(-2)),(F(3,2),F(5,3)),(F(7,3),F(-4,3))):
   J=u*(1-u)*(B+gamma*v)+v*(1-v)*(B+gamma*u)
   RHS=B*(s-s*s)+p*(2*B+gamma*(2-s))
   check(J==RHS,'s,p exact identity')

# Unique root of strictly increasing cubic on the real axis (analytic positivity of derivative is in proof).
cubic=lambda q: 8*q**3-16*q**2+11*q-2
qstar=bisect(cubic,0.25,1/3)
cstar=(1-2*qstar)/(qstar*(2-3*qstar))
qspin=(5-sqrt(5))/10
cspin=(5-sqrt(5))/2
check(4/3<cstar<cspin,'ordering of all three thresholds')
check(abs(cstar-1.35700320530498)<1e-12,'numerical root')

def qopt(c):
 if c==0: return .5
 # stable small root, avoid cancellation for very small c
 return 1/(1+c+sqrt(c*c-c+1)) # algebraically: (1+c-sqrt(...))/(3c)

def Js(q,c): return 2*q*(1-q)*(1-c*q)
def J(u,v,c): return u*(1-u)*(1-c*v)+v*(1-v)*(1-c*u)
for c in [0, .05,.2, .7, 1, 4/3, cstar-.00001,cstar,cstar+.00001,cspin,1.5,2,3,10,50]:
    qo=qopt(c)
    check(0<qo<=.5,'diagonal root range')
    check(abs(1-2*(1+c)*qo+3*c*qo*qo)<1e-11,'stationary root')
    Jd=Js(qo,c)
    M=max(.25,Jd)
    random.seed(8032)
    for k in range(12000):
        u=random.random(); v=random.random()
        check(J(u,v,c)<=M+2e-13,'global envelope at random densities')
    check(abs(J(.5,0,c)-.25)<1e-14,'one-lane branch')
    check(abs(J(qo,qo,c)-Jd)<1e-14,'symmetric branch')

# Endpoint metastability threshold at 4/3, and transverse Hessian threshold at cspin.
for c in (1.28,4/3,1.34,cstar,cspin,1.4,2):
 qo=qopt(c)
 boundary_normal_derivative=1-3*c/4
 anti_symmetric_eigenvalue=-2*(1-c*(1-qo))
 check((boundary_normal_derivative<0)==(c>4/3), 'boundary spinodal derivative') if c!=4/3 else check(abs(boundary_normal_derivative)<1e-14, 'boundary threshold')
 if c != cspin: check((anti_symmetric_eigenvalue<0)==(c<cspin),'symmetric stability threshold')
 else: check(abs(anti_symmetric_eigenvalue)<1e-12,'symmetric spinodal equality')

# Exact witness that symmetric branch strictly wins at c=4/3.
check(J(F(2,7),F(2,7),F(4,3))>F(1,4),'lower spinodal witness')
# Exact stationary symmetric current at upper spinodal is below one-lane current.
check(abs(Js(qspin,cspin)-(sqrt(5)-1)/5)<1e-13,'upper spinodal current')
check((sqrt(5)-1)/5<1/4, 'upper spinodal loses globally')

print('assertions:', CHECKS)
print('qstar:',format(qstar,'.14f'))
print('critical repulsion:',format(cstar,'.14f'))
print('spinodals:',format(4/3,'.14f'),format(cspin,'.14f'))
print('coexistence current:',Js(qstar,cstar), J(.5,0,cstar))
