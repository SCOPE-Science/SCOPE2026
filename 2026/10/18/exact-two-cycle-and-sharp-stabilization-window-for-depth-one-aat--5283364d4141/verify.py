"""Reproduce exact depth-one/depth-two AATGS comparisons on shifted rotations.
Standalone; uses Python standard library plus optional NumPy only for its numerical replay.
"""
import math, random
from fractions import Fraction as F


def pair(z,w): return (z[0]+w[0],z[1]+w[1])
def scale(c,z): return(c*z[0],c*z[1])
def dot(z,w): return z[0]*w[0]+z[1]*w[1]
def norm(z): return math.sqrt(dot(z,z))
def mat(mu,om,z): return (mu*z[0]-om*z[1],om*z[0]+mu*z[1])
def sub(z,w):return pair(z,scale(-1,w))

def aatgs(mu,om,depth,x0,steps):
    x=x0;f=scale(-1,mat(mu,om,x)); xs=[x];fs=[f];Qs=[];Us=[];thetas=[]
    for j in range(steps):
        if norm(f)<1e-13:break
        beta=mu/(mu*mu+om*om)
        if j:
            u=sub(xs[-1],xs[-2]); q=sub(fs[-1],fs[-2]);
            for ui,qi in zip(Us[-(depth-1):] if depth>1 else [],Qs[-(depth-1):] if depth>1 else []):
                s=dot(q,qi);u=sub(u,scale(s,ui));q=sub(q,scale(s,qi))
            s=norm(q)
            assert s>1e-13, (j,mu,om,s)
            Qs.append(scale(1/s,q));Us.append(scale(1/s,u))
            Qs=Qs[-depth:];Us=Us[-depth:]
            theta=[dot(qi,f) for qi in Qs]
            thetas.append(theta)
            xbar=x;fbar=f
            for ui,qi,c in zip(Us,Qs,theta):
                xbar=sub(xbar,scale(c,ui));fbar=sub(fbar,scale(c,qi))
            xnew=pair(xbar,scale(beta,fbar))
        else:xnew=pair(x,scale(beta,f))
        x=xnew;f=scale(-1,mat(mu,om,x));xs.append(x);fs.append(f)
    return xs,fs,thetas

checks=0
for m,o in [(1,1),(1,10),(3,4),(1,100),(2,3),(100,1)]:
 for z in [(1.,0.),(.5,-2.),(-1.,.3)]:
  one,fr,th=aatgs(m,o,1,z,8)
  b=m/(m*m+o*o);ratio=o/math.sqrt(m*m+o*o)
  for k,(x,f) in enumerate(zip(one,fr)):
   assert abs(norm(x)/norm(z)-ratio**k)<4e-11
   assert abs(norm(f)/norm(fr[0])-ratio**k)<4e-11
   checks+=2
  assert all(abs(t[0])<1e-10 for t in th),th;checks+=1
  two,fr2,th2=aatgs(m,o,2,z,3)
  assert norm(two[-1])<2e-9, (m,o,z,two)
  assert norm(two[2])>1e-11
  checks+=2
  # Direct orthogonality at each MR step, and nonsingularity of secant Gram matrix.
  for j in range(1,min(len(fr),7)):
   assert abs(dot(fr[j],sub(fr[j],fr[j-1])))<1e-8*norm(fr[j-1])**2
   checks+=1
print('NUMERICAL AATGS CHECKS PASSED:',checks)

# Symbolic certificate in the rational case A=I+2J, x0=(1,1).
mu,om=F(1),F(2);S=mu*mu+om*om;beta=mu/S
z=(F(1),F(1));r0=scale(-1,mat(mu,om,z));
def B(v):return sub(v,scale(beta,mat(mu,om,v)))
r1=B(r0);r2=B(r1)
d1=sub(r1,r0);d2=sub(r2,r1)
assert dot(r1,d1)==0 and dot(r2,d2)==0
assert d1[0]*d2[1]-d1[1]*d2[0]!=0
assert dot(r0,r0)==10 and dot(r1,r1)==F(8)
print('EXACT RATIONAL: beta=',beta,'residual norm ratio squared=',F(4,5),'secant det=',d1[0]*d2[1]-d1[1]*d2[0])

# New: source algorithm with a *fixed* input beta, not adaptively chosen.
def fixed_aatgs1(mu,om,beta,x0,steps):
    x=x0;f=scale(-1,mat(mu,om,x));xs=[x];fs=[f];coefs=[]
    for j in range(steps):
        if j:
            u=sub(xs[-1],xs[-2]);q=sub(fs[-1],fs[-2]); assert dot(q,q)>0
            theta=dot(f,q)/dot(q,q);coefs.append(theta)
            xnew=pair(sub(x,scale(theta,u)),scale(beta,sub(f,scale(theta,q))))
        else:xnew=pair(x,scale(beta,f))
        x=xnew;f=scale(-1,mat(mu,om,x));xs.append(x);fs.append(f)
    return xs,coefs

checks2=0
for mu,omega in [(1.,1.),(1.,3.),(1.,50.),(3.,2.),(5.,1.)]:
 S=mu*mu+omega*omega;bm=mu/S
 beta_max=bm*(1+math.sqrt(2+mu*mu/(omega*omega)))
 for multiple in [.01,.5,1.,1.2,1.8,2.,2.05,2.2,2.8,3.7]:
  beta=multiple*bm
  x0=(.4,-1.7)
  xs,coefs=fixed_aatgs1(mu,omega,beta,x0,6)
  z=math.sqrt((1-beta*mu)**2+(beta*omega)**2)
  r=omega/math.sqrt(S)
  for j,x in enumerate(xs):
   predicted=z**((j+1)//2)*r**(j//2)
   assert abs(norm(x)/norm(x0)-predicted)<5e-8,(mu,omega,multiple,j,x,predicted)
   checks2+=1
  for j,c in enumerate(coefs,1):
   predict=1-bm/beta if j%2 else 0.
   assert abs(c-predict)<1e-7*(1+abs(predict)),(mu,omega,multiple,j,c,predict)
   checks2+=1
 assert beta_max>2*bm
 checks2+=1
print('FIXED-BETA TWO-CYCLE CHECKS PASSED:',checks2)
