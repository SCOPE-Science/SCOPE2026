import math
from scipy.integrate import quad
from scipy.special import ndtr,gamma
D=rho=1.
def F(u):
 h=math.sqrt(2*u)
 return (3-2*u)*ndtr(-h)+h*math.exp(-u)/math.sqrt(2*math.pi)

def K(a,c=1):
 return rho*c*math.sqrt(D)*gamma(a+1)*(4*a+5)/(2*math.sqrt(math.pi)*(2*a+1)*(2*a+3))

def C(t,a):
 c=a+1
 return rho*math.sqrt(D)*c/4 /t**(a+.5)*quad(lambda u:u**(a-.5)*F(u),0,t,epsabs=1e-11)[0]

def Inum(a):return quad(lambda u:u**(a-.5)*F(u),0,250,epsabs=1e-12,limit=200)[0]
for a in [-.4,-.25,0,.25,.5,1.,1.5]:
 I=Inum(a)
 theo=2*gamma(a+1)*(4*a+5)/(math.sqrt(math.pi)*(2*a+1)*(2*a+3))
 assert abs(I/theo-1)<1e-8,(a,I,theo)
 print(f'a={a}: Mellin={I:.12g}, closed={theo:.12g}')
 for t in [10,100,1000]:
  rat=C(t,a)*t**(a+.5)/K(a,a+1)
  print(' t',t,'ratio',rat)
  if t==1000: assert abs(rat-1)<1e-6
print('PASS Mellin and finite-time asymptotic comparisons')
