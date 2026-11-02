import numpy as np
from scipy.optimize import minimize
from verify import parameters

def run(d,t):
 r,la,m2,y,s=parameters(d,t)
 aL2=(1-t)**2*la*(1-la); bL2=m2
 aJ2=s*s/d; bJ2=(1-2*s)/(d*(d-1)); yJ=1-s
 def objJ(z):
  yy, loga,logb=z;return -(loga+(d-1)*logb)
 def constraintsJ(z):
  yy,loga,logb=z;a=np.exp(loga);b=np.exp(logb)
  return np.array([(yy-t)/np.sqrt(d)-a,(1-yy)/np.sqrt(d)-a,yy/d-np.sqrt((a*a+(d-1)*b*b)/d)])
 resJ=minimize(objJ,[0.8, np.log(np.sqrt(aJ2)),np.log(np.sqrt(bJ2))],method='SLSQP',constraints=[{'type':'ineq','fun':constraintsJ}],options={'ftol':1e-13,'maxiter':1500})
 def objL(z):
  yy,loga,logb=z;return loga+(d-1)*logb
 def constraintsL(z):
  yy,loga,logb=z;a=np.exp(loga);b=np.exp(logb)
  return np.array([1-((v-yy)**2/(d*a*a)+(d-1)*v*v/(d*b*b)) for v in (t,1)])
 resL=minimize(objL,[y,np.log(np.sqrt(aL2)),np.log(np.sqrt(bL2))],method='SLSQP',constraints=[{'type':'ineq','fun':constraintsL}],options={'ftol':1e-13,'maxiter':1500})
 errJ=max(abs(resJ.x[0]-yJ),abs(np.exp(resJ.x[1])-np.sqrt(aJ2)),abs(np.exp(resJ.x[2])-np.sqrt(bJ2)))
 errL=max(abs(resL.x[0]-y),abs(np.exp(resL.x[1])-np.sqrt(aL2)),abs(np.exp(resL.x[2])-np.sqrt(bL2)))
 return resJ.success,resL.success,errJ,errL
for d in (2,3,5):
 for t in (.05,.25,.6,.9):
  print(d,t,run(d,t))
