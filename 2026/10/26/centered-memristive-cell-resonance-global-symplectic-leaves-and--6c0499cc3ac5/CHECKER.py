"""Standalone exact and numerical checks for the centered memristive recurrence."""
from fractions import Fraction
from itertools import product
from math import log, cosh, tanh

# Laurent-polynomial coefficients of the mixed Euler difference operator.
def conv(a,b):
    c={}
    for k,x in a.items():
        for l,y in b.items(): c[k+l]=c.get(k+l,Fraction(0))+x*y
    return {k:v for k,v in c.items() if v}

n=0
for lam in [Fraction(1,7),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(6,7)]:
    coef={1:lam,0:1-2*lam,-1:lam-1}
    double=conv(coef,coef)
    assert double[2]==lam**2 and double[-2]==(1-lam)**2
    assert sum(double.values())==0
    # Scalar four-step companion determinant.
    det=double[-2]/double[2]
    assert det==((1-lam)/lam)**2
    assert (det==1)==(lam==Fraction(1,2))
    n+=1
print('EXACT_LAURENT_AND_JACOBIAN_IDENTITIES_PASS',n)

# Direct five-point-centered recurrence (T=1, L(x)=x**3-2*x/5).
def L(x): return x**3-Fraction(2,5)*x

def z(p,q,r): return (r-p)/2+L(q)
def step(p0,p1,p2,p3):
    # z_(k+1)=z_(k-1): z(p1,p2,p3)=z(p3,p4,p5) after two steps.
    # single step from z_k=z_(k-2) in p0..p3: p4=2*p2-p0-2*(L(p3)-L(p1)).
    p4=2*p2-p0-2*(L(p3)-L(p1))
    return (p1,p2,p3,p4)

checks=0
for q in range(1,8):
  for p in range(-3,4):
    init=tuple(Fraction(i,3*q) for i in (p,p+1,p+2,p+3))
    X=init
    ze=z(X[1],X[2],X[3]); zo=z(X[0],X[1],X[2]);
    for j in range(5):
      X=step(*X)
      Y=step(*X)
      assert z(Y[1],Y[2],Y[3])==ze
      assert z(Y[0],Y[1],Y[2])==zo
      O_new=init[3] if j==0 else None
      X=Y
      checks+=1
print('EXACT_PARITY_INVARIANTS_PASS',checks)

# Test arbitrary alternating amplitude, with a fixed smooth passive example.
def passive_L(x): return 0.5*log(cosh(x))
def passive_Lp(x): return 0.5*tanh(x)
for u,v in [(-2.0,1.0),(-1.0,2.0),(1.0,2.0),(-3.0,3.0)]:
    x=[u,v,u,v,u,v,u]
    for k in range(2,5):
        z_m1=(x[k]-x[k-2])/2+passive_L(x[k-1])
        z_p1=(x[k+2]-x[k])/2+passive_L(x[k+1])
        assert abs(z_m1-z_p1)<1e-12
    a=passive_Lp(u); b=passive_Lp(v)
    M=[[1+4*a*b,-2*b],[-2*a,1]]
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert abs(det-1)<1e-12
    assert abs((M[0][0]+M[1][1])-(2+4*a*b))<1e-12
print('PASSIVE_ALTERNATING_CYCLES_AND_RECIPROCAL_MULTIPLIERS_PASS',4)

# Exact orbit samples for a polynomial L, checking the two-shear normal form.
for a,b in product([Fraction(-2),Fraction(-1),Fraction(0),Fraction(1),Fraction(2)],repeat=2):
    E=a; O=b
    nue=Fraction(3,7); nuo=Fraction(-5,11)
    x0=E-2*(nuo-L(O)); x1=O; x2=E; x3=O+2*(nue-L(E))
    X=(x0,x1,x2,x3)
    assert z(x1,x2,x3)==nue
    assert z(x0,x1,x2)==nuo
    Y=step(*step(*X))
    O_prime=O+2*(nue-L(E))
    E_prime=E+2*(nuo-L(O_prime))
    assert Y[1]==O_prime and Y[2]==E_prime
    assert z(Y[1],Y[2],Y[3])==nue
    assert z(Y[0],Y[1],Y[2])==nuo
print('EXACT_TWO_SHEAR_CONJUGACY_PASS',25)
print('GLOBAL_DYNAMICAL_EXCLUSIONS_REQUIRE_ANALYTICAL_PROOF')
