import math,cmath

def w(n,x): return sum(math.exp(2*k*x) for k in range(n+1))
def b(n,x):
 vals=[math.exp(2*k*x) for k in range(n+1)];return -.5+sum(k*t for k,t in enumerate(vals))/sum(vals)
def c(n,s,x):return math.exp(-s/2)*math.sqrt(w(n,x)/w(n,x-s))
checks=0
for n in range(1,7):
 for s in [-1.3,-.41,.33,1.9]:
  for x in [-3.1,-1.5,-.2,0,.7,2.2,4.1]:
   e=1e-5
   rate=(math.log(c(n,s,x+e))-math.log(c(n,s,x-e)))/(2*e)
   assert abs(rate-(b(n,x)-b(n,x-s)))<4e-8
   assert c(n,s,x)>0
   if s>0:assert c(n,s,x)<=math.exp((n-.5)*s)*(1+1e-12)
   else:assert c(n,s,x)<=math.exp(-s/2)*(1+1e-12)
   checks+=3
 for r in [i*.13-.48 for i in range(0,8*n)]:
  if r>=n-.5:break
  for x in [-13.,-7.,-1.,3.,9.,13.]:
   # reciprocal fundamental solution of (L-r)u=0 has logarithmic derivative r-b
   e=1e-5
   f=lambda y:(r+.5)*y-.5*math.log(w(n,y))
   assert abs((f(x+e)-f(x-e))/(2*e)-(r-b(n,x)))<1e-8
   checks+=1
print('verified',checks,'finite algebra/derivative/norm samples')
