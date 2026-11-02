import numpy as np
from scipy.special import roots_jacobi

def coeffs(m,a):
 b1=np.sqrt((a+1)*(m+1)/((m+a+2)**2*(m+a+3)))
 b2sq=2*(a+2)*(m+2)*(m+a+2)/((m+a+4)**2*(m+a+3)*(m+a+5))
 return b1,b2sq

def mats(m,a):
 xs,ws=roots_jacobi(3,a,m)
 ts=(xs+1)/2
 ws=ws/ws.sum()
 mu=(m+1)/(m+a+2)
 b1,_=coeffs(m,a)
 P=np.vstack([np.ones(3),(ts-mu)/b1])
 M1=(P*(ws*ts))@P.T
 M2=(P*(ws*ts**2))@P.T
 return M1,M2
count=0
for a in [-0.75,0,0.8,2.5,6.0]:
 for m in [0,1,2,3,5,10,30]:
  A,B=mats(m,a)
  b1,b2sq=coeffs(m,a)
  C=A@B-B@A
  assert abs(C[0,1]-b1*b2sq) < 1e-7, (a,m,C[0,1],b1*b2sq)
  assert abs(C[1,0]+b1*b2sq)<1e-7
  assert abs(C[0,0])<1e-8
  count+=3
for a in [-0.75,0,0.8,2.5,6.0]:
 target=2*(a+2)*np.sqrt(a+1)
 for m in [10000,100000]:
  b1,b2sq=coeffs(m,a)
  assert abs(m**3*b1*b2sq/target-1)<0.01, (a,m,m**3*b1*b2sq/target)
  count+=1
print('PASS',count,'Gaussian quadrature, commutator and asymptotic assertions')

# A genuinely different polynomial-symbol pair: compare its compressed commutator
# against the independently derived universal boundary-jet constant.
def block_poly(m, a, func):
 x, w = roots_jacobi(5, a, m)
 t = (x+1)/2
 w = w / np.sum(w)
 mu = (m+1)/(m+a+2)
 b1, _ = coeffs(m,a)
 P = np.vstack([np.ones(len(t)),(t-mu)/b1])
 return (P*(w*func(t)))@P.T
f=lambda t:t+0.4*t*t+0.3*t*t*t
g=lambda t:t*t+0.2*t*t*t
fp, fpp = 2.7, 2.6
gp, gpp = 2.6, 3.2
delta = fp*gpp - fpp*gp
for a in [-0.5,0.0,2.5]:
 for m in [100,1000]:
  A,B=block_poly(m,a,f),block_poly(m,a,g)
  measured=(A@B-B@A)[0,1]
  expected=delta*(a+2)*np.sqrt(a+1)/m**3
  assert abs(measured/expected-1) < (0.25 if m == 100 else 0.035)
  count+=1
print('PASS',count,'including nonmonomial boundary-jet checks')
