"""Exact-arithmetic regression checks for local-reset mean-field growth moments.

Python >=3.9, standard library only. Analytical proofs are separate.
"""
from fractions import Fraction as F
from math import isclose, sqrt

checks=0

def check(flag, description):
    global checks
    checks+=1
    if not flag:
        raise AssertionError(description)

def determinant(a,b,c,d):
    return a*d-b*c

def moment_values(n,r,m,phi,x0):
    delta=r-m
    den=delta*(r-2*m)+phi*(2*delta-r/n)
    q=r*x0*x0*m*m/(delta*delta)
    variance=q*(delta+phi/n)/den
    cross=q*(phi/n)/den
    return variance,cross,den

for n in range(2,12):
  N=F(n)
  for rn in range(3,9):
    r=F(rn)
    for mi in range(1,2*rn):
      m=F(mi,2)
      if m>=r: continue
      for pi in range(0,14):
        phi=F(pi,4)
        x0=F(7,5)
        delta=r-m
        a=2*m-r-2*phi*(N-1)/N
        b=2*phi*(N-1)/N
        c=2*phi/N
        d=2*m-2*r-2*phi/N
        V,C,den=moment_values(N,r,m,phi,x0) if delta*(r-2*m)+phi*(2*delta-r/N)!=0 else (None,None,0)
        check(determinant(a,b,c,d)==2*den,"matrix determinant reduction")
        if den>0 and (a+d)<0:
          M=r*x0/delta
          q=r*x0*x0*m*m/(delta*delta)
          check(a*V+b*C+q==0,"variance equation")
          check(c*V+d*C==0,"cross-covariance equation")
          check(C*(N*delta+phi)==phi*V,"correlation ratio")
          # Raw-moment moment ODE, independent of the centered representation.
          raw_diag=V+M*M
          raw_cross=C+M*M
          check(a*raw_diag+b*raw_cross+r*x0*x0==0,"raw diagonal equation")
          check(c*raw_diag+d*raw_cross+2*r*x0*M==0,"raw cross equation")
          if phi>0:
            check(V>0 and C>0 and C<V,"strict positivity")
            check(-2*r*x0*x0*m*m*(N-1)/(N*den*den)<0,"strict variance derivative")
          if m==r/2 and phi>0:
            check(C==x0*x0/(N-1),"critical covariance locking")
            check(V==x0*x0/(N-1)*(1+N*r/(2*phi)),"critical variance")
          check((V+(N-1)*C)/N==q*(delta+phi)/(N*den),"mean variance")
        if phi==0 and r>2*m:
          # Exact independent Pareto moment check.
          check(V==r*x0*x0/(r-2*m)-(r*x0/(r-m))**2,"independent reset limit")

# Sharp Perron-root threshold from the explicitly positive off-diagonal 2x2 matrix.
for n in (2,3,4,8,31,100,1000):
  for phi in (0.0,0.1,0.4,0.5,0.9,2,10,100):
    r=1.0
    critical=(3*r+2*phi-sqrt((r-2*phi)**2+8*r*phi/n))/4
    a=2*critical-r-2*phi*(n-1)/n
    b=2*phi*(n-1)/n
    c=2*phi/n
    d=2*critical-2*r-2*phi/n
    check(abs(a*d-b*c)<1e-9,"Perron boundary determinant")
    check(critical>=r/2-1e-12 and critical<r,"critical location")
  check(isclose((3+1-sqrt(4/n))/4,1-1/(2*sqrt(n)),abs_tol=1e-14),"critical N^-1/2 scale")

# Stress-test the rational phase boundary, finite-N confinement, and monotonic switch.
for n in range(2,24):
  r=F(5)
  for k in range(1,2*n-1):
    m=r*F(2*n+k,4*n)  # m above r/2, below r for the chosen range
    if not (r/2<m<r): continue
    denom=2*n*(r-m)-r
    if denom>0:
      pc=F(n)*(r-m)*(2*m-r)/denom
      for phi in (pc/F(2),pc,2*pc):
        D=(r-m)*(r-2*m)+phi*(2*(r-m)-r/n)
        check((D>0)==(phi>pc),"sharp redistribution threshold")

print(f"PASS {checks} exact-rational and floating boundary assertions")
print("Scope: finite equations, algebraic identities, and selected threshold checks only.")
print("Infinite-time stationarity and moment necessity/sufficiency are analytic proof obligations.")
