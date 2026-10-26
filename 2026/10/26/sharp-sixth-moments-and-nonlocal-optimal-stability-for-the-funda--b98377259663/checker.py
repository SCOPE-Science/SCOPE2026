from collections import defaultdict
from fractions import Fraction
from math import comb

def plus(a,b):
 c=a.copy()
 for k,v in b.items():c[k]=c.get(k,0)+v
 return {k:v for k,v in c.items() if v}
def neg(a):return {k:-v for k,v in a.items()}
def mul(a,b):
 c=defaultdict(int)
 for (i,j),x in a.items():
  for (k,l),y in b.items():c[i+k,j+l]+=x*y
 return {k:v for k,v in c.items() if v}
def power(a,n):
 z={(0,0):1}
 for _ in range(n):z=mul(z,a)
 return z
def mon(i,j):return {(i,j):1}
X=plus(plus(mon(1,0),mon(0,1)),mon(-1,-1))
Y=plus(plus(mon(-1,0),mon(0,-1)),mon(1,1))
H=plus(mul(X,Y),{(0,0):-1})
Z=[(1,0),(0,1),(-1,-1)]
W={(0,0):1}
for i in range(3):
 for j in range(i+1,3):
  d=(Z[i][0]-Z[j][0], Z[i][1]-Z[j][1])
  F={(0,0):2, d:-1,(-d[0],-d[1]):-1}
  W=mul(W,F)
assert W[(0,0)]==6

def integrate(q):return Fraction(mul(q,W).get((0,0),0),6)
assert integrate({(0,0):1})==1
assert integrate(mul(X,Y))==1
assert integrate(power(H,2))==1
nums=[]
for i in range(4):nums.append(integrate(mul(power(mul(X,Y),i),power(H,6-2*i))))
phase=integrate(mul(power(X,3),power(H,3)))
print('mixed fundamentals',nums,'phase',phase)
print('weighted', [int(comb(3,i)**2*nums[i]) for i in range(4)])
assert nums==[145,40,13,6]
assert phase==22
print('OK')

# Independent rational-algebra identities for the optimization.
def polyadd(a,b):
 return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)) for i in range(max(len(a),len(b)))]
def polymul(a,b):
 z=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):z[i+j]+=x*y
 return z
def derivative(a):return [j*a[j] for j in range(1,len(a))]
def pad(a,n):return a+[0]*(n-len(a))
num=[75,-44,318,0,139]
den=[1,0,1]
g=[11,-84,-33,20]
lhs=polyadd(polymul(derivative(num),den),[-4*x for x in polymul(num,[0,1])])
rhs=[-4*v for v in g]
assert pad(lhs, max(len(lhs),len(rhs)))==pad(rhs,max(len(lhs),len(rhs)))
Q=[145,0,360,44,117,0,6]
D=polyadd([145*v for v in polymul(polymul(den,den),den)],[-v for v in Q])
assert D==[0,0,75,-44,318,0,139]

def c(u):return 20*u**3-33*u*u-84*u+11
assert c(0)>0 and c(.25)<0 and c(1)<0 and c(3)>0
lo,hi=0.0,.25
for _ in range(120):
 mid=(lo+hi)/2
 if c(mid)>0:lo=mid
 else:hi=mid
root=(lo+hi)/2

def stab(u):return (75-44*u+318*u*u+139*u**4)/(1+u*u)**2
kappa=stab(root)
assert .12525<root<.12527 and 72.22<kappa<72.24
assert kappa<stab(0) and kappa<139
from random import Random
from cmath import exp
rng=Random(6183)
for _ in range(600):
 a=complex(rng.uniform(-2,2),rng.uniform(-2,2))
 b=complex(rng.uniform(-2,2),rng.uniform(-2,2))
 S=abs(a)**2+abs(b)**2
 moment=6*abs(a)**6+117*abs(a)**4*abs(b)**2+360*abs(a)**2*abs(b)**4+145*abs(b)**6+44*(a**3*b.conjugate()**3).real
 assert moment<=145*S**3+1e-8
 assert 145*S**3-moment>=kappa*abs(a)**2*S**2-1e-8
assert abs((145*(1+root**2)**3-(6*root**6+117*root**4+44*root**3+360*root**2+145))/(root**2*(1+root**2)**2)-kappa)<1e-10
print('Exact torus integrals, polynomial identities, cubic intervals, and 600 complex-coefficient tests: PASS')
print('sharp ratio = %.15f; sharp stability coefficient = %.15f'%(root,kappa))
