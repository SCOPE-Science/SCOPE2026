"""Finite checks of the explicit weighted harmonic Bergman Toeplitz formulas.
Analytic infinite-dimensional statements require the written proof; tests do not prove them.
"""
from fractions import Fraction
from math import factorial, isclose
import mpmath as mp

checks=0

def demand(p,context):
    global checks
    checks+=1
    if not p: raise AssertionError(context)

def moment(n,alpha):
    out=Fraction(1)
    for r in range(1,n+1):
        out*=Fraction(r,1)/(alpha+1+r)
    return out

def weight_square(k,m,alpha):
    if k>=0:
        return moment(k+m,alpha)/moment(k,alpha)
    j=-k
    if j<m:
        return moment(m,alpha)**2/(moment(j,alpha)*moment(m-j,alpha))
    return moment(j,alpha)/moment(j-m,alpha)

def pos_eigen(k,m,alpha):
    if k<m:
        return (moment(k+m,alpha)-moment(m,alpha)**2/moment(m-k,alpha))/moment(k,alpha)
    return moment(k+m,alpha)/moment(k,alpha)-moment(k,alpha)/moment(k-m,alpha)

alphas=[Fraction(-3,4),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(1),Fraction(2),Fraction(4)]
for a in alphas:
 for m in range(1,13):
    for k in range(-48,49):
      demand(weight_square(k,m,a)==weight_square(-m-k,m,a),('reflection',a,m,k))
      c=weight_square(k,m,a)-weight_square(k-m,m,a)
      demand(c==- (weight_square(-k,m,a)-weight_square(-k-m,m,a)),('odd',a,m,k))
      if k>0:
        demand(c==pos_eigen(k,m,a),('formula',a,m,k))
        demand(c>0,('positive',a,m,k))
      elif k==0:
        demand(c==0,('zero',a,m,k))
    S=sum((moment(m,a)**2/(moment(j,a)*moment(m-j,a)) for j in range(m)),Fraction(0))
    for N in [m,2*m+9,100]:
      lhs=sum((pos_eigen(k,m,a) for k in range(1,N+1)),Fraction(0))
      rhs=sum((weight_square(k,m,a) for k in range(N-m+1,N+1)),Fraction(0))-S
      demand(lhs==rhs,('telescoping',a,m,N))
    demand(S<m,('nonzero trace',a,m))

for m in range(1,31):
 a=Fraction(0)
 tr=Fraction(2)*(m-sum((moment(m,a)**2/(moment(j,a)*moment(m-j,a)) for j in range(m)),Fraction(0)))
 demand(tr==Fraction(m*(5*m+1),3*(m+1)),('trace0',m))
 for k in range(1,5*m+1):
  f=Fraction(k*k*(k+1),(m+1)**2*(k+m+1)) if k<m else Fraction(m*m,(k+1)*(k+m+1))
  demand(pos_eigen(k,m,a)==f,('spectrum0',m,k))
  demand(f<=Fraction(m*m,(m+1)*(2*m+1)),('op-norm0',m,k))
 demand(pos_eigen(m,m,a)==Fraction(m*m,(m+1)*(2*m+1)),('peak0',m))

mp.mp.dps=65
for alpha in [-.75,-.5,0,1,2,4]:
  for m in [1,2,3,5,9]:
    def h(k): return mp.gamma(k+1)*mp.gamma(alpha+2)/mp.gamma(k+alpha+2)
    for n in [10000,20000,50000]:
      c=h(n+m)/h(n)-h(n)/h(n-m)
      val=n*n*c
      target=m*m*(alpha+1)
      demand(abs(val/target-1)<(20*m+50)/(n-m),('asymptotic',alpha,m,n,val,target))
print('PASS checks:',checks)
