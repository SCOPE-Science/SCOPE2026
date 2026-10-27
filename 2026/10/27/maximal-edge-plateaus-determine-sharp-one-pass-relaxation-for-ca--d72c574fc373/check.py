"""Finite diagnostic checks for weighted one-lag relaxation; not a proof."""
import math
import numpy as np
from scipy.optimize import minimize_scalar

def Wmat(w):
 n=len(w)+1; W=np.zeros((n,n))
 for i,a in enumerate(w): W[i+1,i]=a
 return W

def predict(w):
 W=Wmat(w); M=max(w)
 L=run=0
 for a in w:
  run=run+1 if a==M else 0; L=max(L,run)
 c=math.cos(math.pi/(L+1))
 wn=np.linalg.eigvalsh((W+W.T)/2)[-1]
 if M<=c+1e-12: return 1., 'nilpotent',c,wn
 if wn>=1-1e-12:return 0.,'identity',c,wn
 return None,'interior',c,wn

def check(w):
 W=Wmat(w);n=len(w)+1
 def g(t):return np.linalg.norm((1-t)*np.eye(n)+t*W,2)
 opt=minimize_scalar(g,bounds=(0,1),method='bounded',options={'xatol':1e-13})
 t,case,c,wn=predict(w)
 if t is not None: assert abs(opt.x-t)<1e-4,(w,opt.x,t,case)
 else: assert 1e-4<opt.x<1-1e-4,(w,opt.x,case)
 print('weights',w,'M',max(w),'plateau c',round(c,5),'numerical radius',round(wn,5),'regime',case,'topt',round(opt.x,8),'normopt',round(opt.fun,8))
for w in [[.2,.2,.2,.2],[.2,.2,.19,.19],[.2,.19,.2,.19],[.8,.8,.8],[.8,.8,.79],[1.2,.2,.3],[2.8,.2,.3],[.01,.02,.03],[.7,.7,.1,.7,.7],[.7,.699999,.1,.7,.7]]:
 check(w)
print('WEIGHTED_RELAXATION_DIAGNOSTIC_OK')
