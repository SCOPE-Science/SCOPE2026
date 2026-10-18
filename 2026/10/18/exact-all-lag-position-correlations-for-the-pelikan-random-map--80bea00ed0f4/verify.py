from fractions import Fraction as Q
from itertools import product
from math import comb

def pi(j,p):
 q=1-p
 if p==Q(2,3): return Q(j+1,2**(j+2))
 return (2*p-1)/(3*p-2)*(Q(1,2**(j+1))-(q/p)**(j+1))

def tail(k,p):
 # sum_j>=k pi(j)*4^-j-1
 r=(1-p)/p
 if p==Q(2,3):
  # sum (j+1)*2^-j-2 *4^-j-1 = 1/16 * sum (j+1) (1/8)^j
  x=Q(1,8)
  return Q(1,16)*x**k*(Q(k+1,1)/(1-x)+x/(1-x)**2)
 B=(2*p-1)/(3*p-2)
 return B*(Q(1,8)**(k+1)/(1-Q(1,8))-(r/Q(4))**(k+1)/(1-r/Q(4)))

def I(k,p):
 return Q(3,4)*sum((pi(j,p)/2**(j+1) for j in range(k)),Q(0))+Q(1,12*2**k)*sum((pi(j,p) for j in range(k)),Q(0))+Q(7*2**k,3)*tail(k,p)

def moment_formula(n,p):
 q=1-p
 acc=Q(0)
 for h in range(n+1):
  for k in range(n-h+1):
   if (n-h+k)%2:continue
   down=(n-h+k)//2;up=n-down
   def C(n,k):return comb(n,k) if 0<=k<=n else 0
   count=C(n,(n+h+k)//2)-C(n,(n+h+k)//2+1)
   acc+=count*p**down*q**up*Q(1,2**h)*I(k,p)
 return acc

def run_word(x,word):
 for d in word:
  if d=='D':x=x*2
  else:x=x/2
  if x>=1:x-=1
 return x

def moment_integral(n,p):
 q=1-p; m=n+3;den=2**m;total=Q(0)
 for word in product('DU',repeat=n):
  w=p**word.count('D')*q**word.count('U')
  S=word.count('U')-word.count('D')
  a=Q(2)**(-S)
  v=Q(7,3)*a*tail(m,p)
  for t in range(1,den):
   l=Q(t,den);r=Q(t+1,den); mid=(l+r)/2
   j=0
   while mid<Q(1,2**(j+1)):j+=1
   density=pi(j,p)*2**(j+1)
   b=run_word(mid,word)-a*mid
   # exact polynomial integrals
   v+=density*(a*(r**3-l**3)/3+b*(r*r-l*l)/2)
  total+=w*v
 return total

if __name__=='__main__':
 for p in [Q(3,5),Q(2,3),Q(3,4),Q(9,10)]:
  print('p',p)
  for n in range(6):
   a=moment_formula(n,p);b=moment_integral(n,p)
   print(n,float(a),float(b),a==b)
   assert a==b,(n,p,a-b)
  known={
   1:(2*p-1)*(3*p+25)/(24*(5*p-1)),
   2:(2*p-1)*((3*p+1)**2/(3*(5*p-1))-(11*p+6)/16),
   3:(2*p-1)*((3*p+1)**3/(6*(5*p-1))-(28*p*p+40*p+9)/32),
  }
  for lag,exact in known.items():
   assert moment_formula(lag,p)==exact,('published_small_lag',p,lag)
 print('EXACT_FINITE_NOISE_AND_INTEGRAL_CHECKS_OK')
