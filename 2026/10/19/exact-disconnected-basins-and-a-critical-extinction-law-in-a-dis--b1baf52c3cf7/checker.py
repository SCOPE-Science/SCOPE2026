import math,random
from fractions import Fraction
# F(x) as exact rational for hand-picked rational parameters; boundaries computed symbolically elsewhere.
for mu in [1.01,1.2,1.5,1.9,1.999]:
 for eps in [1e-6,0.001,0.05,0.15,0.3,0.6,0.95]:
  rp=mu*(1+eps); rm=mu*(1-eps)
  if rp>3:continue
  a=1-1/mu
  b=(1+math.sqrt(1-4*a/rp))/2
  pm=1-1/rm if rm>1 else 0.
  pp=1-1/rp
  assert 0<a<.5<b<1,(mu,eps,a,b)
  assert a<pp<b
  assert pm<a
  assert rp/4<b
  assert abs(rp*b*(1-b)-a)<2e-14
  assert abs(mu*a*(1-a)-a)<2e-14
  def H(x):
   if x==0 or x==1:return 0
   if x==a:return a
   return (rm if x<a else rp)*x*(1-x)
  for tag, x0, target in [('left',a/2,pm),('upper',(a+b)/2,pp),('right',(b+1)/2,pm)]:
   x=x0
   n=60000 if rm>0.99999 and rm<=1 else 30000
   for _ in range(n):x=H(x)
   assert abs(x-target)<(3e-5 if rm<=1.0001 else 1e-7),(mu,eps,tag,x,target)
print('sampled basin checks PASS')
# exact identity for logistic second iterate
import sympy as S
r,x=S.symbols('r x')
f=lambda z:r*z*(1-z)
assert S.simplify(f(f(x))-x+x*(r*x-r+1)*(r*r*x*x-r*(r+1)*x+r+1))==0
p=(r-1)/r
assert S.simplify(f(x)-p-(x-p)*(1-r*x))==0
print('symbolic identities PASS')
