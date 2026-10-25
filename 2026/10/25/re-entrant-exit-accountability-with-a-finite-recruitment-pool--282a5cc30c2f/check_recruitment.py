"""Exact-rational checks for discounted one-vacancy recruitment model."""
from fractions import Fraction as F
from itertools import product

def closed(n,m,kappa,alpha,d,t,p):
    assert 2<=m<=n and 0<t<1 and 0<=p<=1
    rho=1-(1-p)**(n-m)
    D=kappa/F(m*(m-1))
    return alpha*t*D/(1-t*(1-rho))-d

def vacancy_value(n,m,kappa,t,p):
    rho=1-(1-p)**(n-m)
    D=kappa/F(m*(m-1))
    # Unit per-epoch block; per-round multiplier cancels in the accountability sign.
    v=D/(1-t*(1-rho))
    assert v == D+t*(1-rho)*v
    return v

def cut(n,m,kappa,alpha,t,p):
    rho=1-(1-p)**(n-m)
    return alpha*t*kappa/(m*(m-1)*(1-t+t*rho))

# Exact witness: smaller constituency fails, grand constituency passes.
n,m,alpha,kappa,t,p,d=3,2,F(1),F(1),F(3,4),F(1),F(2,5)
assert closed(n,2,kappa,alpha,d,t,p) == F(-1,40)
assert closed(n,3,kappa,alpha,d,t,p) == F(1,10)
assert cut(3,2,kappa,alpha,t,p)==F(3,8)
assert cut(3,3,kappa,alpha,t,p)==F(1,2)
assert kappa*(1-F(1,2))>=F(1,4)
assert kappa*(1-F(1,3))>=F(1,4)

checks=0
for n in range(2,12):
 for m in range(2,n+1):
  for p in [F(0),F(1,7),F(1,4),F(1,2),F(3,4),F(1)]:
   for t in [F(1,5),F(1,3),F(1,2),F(2,3),F(3,4),F(4,5),F(9,10),F(99,100)]:
    for alpha in [F(1,3),F(1)]:
     for kappa in [F(1,2),F(1),F(7,3)]:
      q=cut(n,m,kappa,alpha,t,p)
      assert closed(n,m,kappa,alpha,q,t,p)==0
      assert closed(n,m,kappa,alpha,q+F(1,1000),t,p)<0
      assert vacancy_value(n,m,kappa,t,p)>0
      # Independent partial sum plus exact tail equals Bellman value.
      rho=1-(1-p)**(n-m)
      r=t*(1-rho)
      D=kappa/F(m*(m-1))
      for H in [0,1,2,5]:
       partial=sum([D*r**j for j in range(H)],F(0))
       tail=(D*r**H)/(1-r)
       assert partial+tail==vacancy_value(n,m,kappa,t,p)
      checks+=1

# General sharp adjacent-size reversal: exact rational equivalence for each grid point.
transitions=0
for n in range(3,13):
 for p in [F(0),F(1,7),F(1,4),F(1,2),F(3,4),F(1)]:
  for t in [F(1,5),F(1,3),F(1,2),F(2,3),F(3,4),F(4,5),F(9,10),F(99,100)]:
   low=cut(n,n-1,F(1),F(1),t,p)
   high=cut(n,n,F(1),F(1),t,p)
   assert (high>low)==(t*(2+(n-2)*p)>2)
   if high>low:
    mid=(low+high)/2
    assert closed(n,n-1,F(1),F(1),mid,t,p)<0
    assert closed(n,n,F(1),F(1),mid,t,p)>0
    transitions+=1
print('PASS: exact Bellman identities and thresholds',checks,'parameter combinations; sharp transition',transitions,'witness combinations')
print('Witness: m=2 advantage',closed(3,2,F(1),F(1),F(2,5),F(3,4),F(1)))
print('Witness: m=3 advantage',closed(3,3,F(1),F(1),F(2,5),F(3,4),F(1)))
