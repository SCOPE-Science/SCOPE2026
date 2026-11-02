"""Exact-rational checks for the private-crosslink Braess network theorem.
Run: python3 verify.py
No third-party packages are required.
"""
from fractions import Fraction as F
from itertools import product

N=0

def check(condition):
    global N
    assert condition
    N += 1

def clip(x, lower, upper):
    return max(lower,min(upper,x))

def flows(Q,k,t):
    B=1-k
    z=clip(2*(B-t)-Q,F(0),Q)
    x=(Q-z)/2
    return x,z

def costs(Q,k,t):
    x,z=flows(Q,k,t)
    direct=1+x+z
    cross=2*(x+z)+k+t
    if z>0 and x>0: check(direct==cross)
    elif z==0: check(cross>=direct)
    else: check(cross<=direct)
    return x,z

def rev(Q,k,t):
    return t*flows(Q,k,t)[1]

def physically(Q,k,z):
    x=(Q-z)/2
    cD=1+x+z
    cX=2*(x+z)+k
    return (2*x*cD+z*cX)/Q

def price_star(Q,k):
    B=1-k
    if B<=0 or Q>=2*B: return F(0)
    if Q<=2*B/3: return B-Q
    return (2*B-Q)/4

def z_social(Q,k):
    return clip(1-k-Q,F(0),Q)

def harm(Q,k,z):
    B=1-k
    return z*(2*(Q-B)+z)/(2*Q)

# Independently enumerate Wardrop inequalities and compare physical aggregates.
for Q in [F(i,12) for i in range(1,38)]:
 for k in [F(i,8) for i in range(0,13)]:
  B=1-k
  tolls={F(i,24) for i in range(0,37)}
  if B>0:
   tolls.update([max(F(0),B-Q), max(F(0),B-Q/2), max(F(0),price_star(Q,k))])
  for t in sorted(tolls):
   x,z=costs(Q,k,t)
   check(x>=0 and z>=0 and 2*x+z==Q)
   check(physically(Q,k,z)==1+Q/2+harm(Q,k,z))
  tstar=price_star(Q,k)
  best=rev(Q,k,tstar)
  check(all(best>=rev(Q,k,t) for t in tolls))
  zstar=flows(Q,k,tstar)[1]
  zso=z_social(Q,k)
  check(zstar>=zso)
  check(all(harm(Q,k,zso)<=harm(Q,k,F(j,32)*Q) for j in range(33)))
  if B>0 and F(2)*B/3<Q<F(2)*B:
   check(harm(Q,k,zstar)>0)
   check(harm(Q,k,zstar)==(2*B-Q)*(3*Q-2*B)/(8*Q))
  elif Q<=2*B/3 and B>0:
   check(harm(Q,k,zstar)<=0)
  else:
   check(harm(Q,k,zstar)==0)
# Tie cases and exact limits.
for B in [F(1,10),F(1,2),F(1),F(5,3)]:
 k=1-B
 for Q in [B/2,2*B/3,B,2*B]:
  t=price_star(Q,k)
  check(rev(Q,k,t)==max(rev(Q,k,F(i,240)) for i in range(0,481)) or
        rev(Q,k,t)>max(rev(Q,k,F(i,240)) for i in range(0,481)))
 check(harm(2*B/3,k,flows(2*B/3,k,price_star(2*B/3,k))[1])==0)
print('VERIFY_OK assertions=',N)
