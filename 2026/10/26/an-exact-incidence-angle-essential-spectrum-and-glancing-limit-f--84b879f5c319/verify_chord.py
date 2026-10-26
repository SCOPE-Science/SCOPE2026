import math
from scipy.special import loggamma,gammaln
from scipy.optimize import minimize_scalar

def base(alpha,x):
 b=(alpha+2)/2
 return math.exp((alpha+1)*math.log(2)+2*loggamma(b+1j*x).real-gammaln(alpha+2))
def profile(alpha,d):
 phi=math.asin(d)
 # convenient y=-xi >= 0, even base
 obj=lambda y: -((alpha+1)*math.log(math.cos(phi))+2*phi*y+math.log(base(alpha,y)))
 top= max(10, 3*(alpha+1)/(math.pi-2*phi))
 r=minimize_scalar(obj,bounds=(0,top),method='bounded',options={'xatol':1e-10})
 return math.exp(-r.fun),r.x
for alpha in [-.5,0,1,2]:
 C0=math.sqrt(math.pi)*math.exp(gammaln((alpha+2)/2)-gammaln((alpha+3)/2))
 L=2*math.pi/math.gamma(alpha+2)*((alpha+1)/math.e)**(alpha+1)
 rows=[(d,*profile(alpha,d)) for d in [0,.4,.9,.99,.9999]]
 print(alpha,'C0',C0,'L',L,'rows',rows)
 assert abs(rows[0][1]-C0)<1e-8
 assert abs(rows[-1][1]-L)/L<.025
print('CHECK_OK: endpoints, variational max, glancing asymptotic')
