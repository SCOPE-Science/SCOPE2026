import itertools,math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

def test(ns,t):
 N=sum(ns); labels=[i for i,k in enumerate(ns) for _ in range(k)]
 A=np.array([[1.0 if labels[i]!=labels[j] else 0.0 for j in range(N)] for i in range(N)])
 L=np.diag(A.sum(axis=1))-A
 P=expm(-t*L)
 d=np.array([[0 if i==j else (1 if labels[i]!=labels[j] else 2) for j in range(N)] for i in range(N)])
 maxpair=(-1,None)
 for i in range(N):
  for j in range(i+1,N):
   diff=P[i]-P[j]
   pos=np.flatnonzero(diff>1e-11); neg=np.flatnonzero(diff<-1e-11)
   if not len(pos) or not len(neg): continue
   c=d[np.ix_(pos,neg)].reshape(-1)
   ae=[]
   for k in range(len(pos)):
    ae.append([float(kk//len(neg)==k) for kk in range(len(c))])
   for h in range(len(neg)):
    ae.append([float(kk%len(neg)==h) for kk in range(len(c))])
   b=np.concatenate((diff[pos],-diff[neg]))
   opt=linprog(c,A_eq=ae,b_eq=b,bounds=(0,None),method='highs')
   if not opt.success:raise ValueError(opt.message)
   score=opt.fun/d[i,j]
   if score>maxpair[0]:maxpair=(score,(i,j))
 m=max(ns)
 form=2*(m-1)/m*math.exp(-(N-m)*t)-(m-2)/m*math.exp(-N*t)
 assert abs(maxpair[0]-form)<2e-8,(ns,t,maxpair,form)
 return maxpair

cases=0
for ns in ((1,1,1),(2,1,1),(3,2,1),(3,3,1),(4,2,2),(5,1,1),(5,2,1),(4,4,3),(2,2,2,2),(1,1,1,1)):
 for t in (0.001,0.04,0.17,0.5,1.0):
  test(ns,t);cases+=1
print('PASS',cases,'independent spectral-exponential/linear-program transport comparisons')
for ns in [(5,1,1),(6,1,1),(9,2,1),(4,2,2),(3,3,3)]:
 m=max(ns); N=sum(ns)
 if 2*m>N+2:
  tstar=math.log(N*(m-2)/(2*(m-1)*(N-m)))/m
  r=2*(m-1)*(N-m)/(N*(m-2))
  peak=2*(m-1)/N*r**((N-m)/m)
  f=lambda t: 2*(m-1)/m*math.exp(-(N-m)*t)-(m-2)/m*math.exp(-N*t)
  assert abs(f(tstar)-peak)<1e-12
  assert peak>1 and f(tstar)>f(tstar*0.9) and f(tstar)>f(tstar*1.1)
  print('amplification',ns,'peak time',round(tstar,8),'peak',round(peak,8))
