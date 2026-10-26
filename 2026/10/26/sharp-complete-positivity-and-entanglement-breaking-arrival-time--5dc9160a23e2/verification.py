"""Independent numerical checks of affine-qubit Choi and critical horizons."""
import math
import numpy as np
from scipy.optimize import brentq
import mpmath as mp

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)

def apply(a,b,t,M):
    p=np.exp(-a*t); q=np.exp(-t); c=b*(-np.expm1(-t))
    return (np.trace(M)*I+c*np.trace(M)*Z+p*np.trace(M@X)*X+q*np.trace(M@Y)*Y+q*np.trace(M@Z)*Z)/2

def choi_direct(a,b,t):
    J=np.zeros((4,4),complex)
    for i in range(2):
       for j in range(2):
          E=np.zeros((2,2),complex); E[i,j]=1
          J+=np.kron(E,apply(a,b,t,E))/2
    return J

def choi_formula(a,b,t):
    p=math.exp(-a*t); q=math.exp(-t); c=b*(1-q)
    return np.array([[1+c+q,0,0,p+q],
                  [0,1-c-q,p-q,0],
                  [0,p-q,1+c-q,0],
                  [p+q,0,0,1-c+q]],dtype=float)/4

def pt(j):
    return j.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)

def conditions(a,b,t):
    p=math.exp(-a*t);q=math.exp(-t);s=math.sqrt(max(0,1-b*b))
    return (abs(p-q)<=s*(1-q),p+q<=s*(1-q))

def root(a,b,kind):
    s=math.sqrt(1-b*b)
    fn=lambda t: ((abs(math.exp(-a*t)-math.exp(-t)) if kind=='cp' else math.exp(-a*t)+math.exp(-t)) /(-math.expm1(-t))) - s
    if kind=='cp' and abs(a-1)<=s:return 0.
    return brentq(fn,1e-10,250,xtol=1e-13)

checks=0
for a in [0.,.1,.3,.7,1.,1.5,2.,3.,8.]:
 for b in [0.,.2,-.5,.9,.999]:
  for t in [.0003,.02,.1,.5,1.,2.,5.,10.,30.]:
   C=choi_direct(a,b,t);D=choi_formula(a,b,t)
   assert np.max(np.abs(C-D)) < 1e-13,(a,b,t,C,D)
   checks+=1
   pcp,peb=conditions(a,b,t)
   if abs(min(np.linalg.eigvalsh(C)))>1e-11:
    assert pcp == (np.linalg.eigvalsh(C).min()>0),(a,b,t,pcp)
    checks+=1
   CP=np.linalg.eigvalsh(C).min()>-1e-11
   PPT=np.linalg.eigvalsh(pt(C)).min()>-1e-11
   if abs(min(np.linalg.eigvalsh(pt(C))))>1e-11:
    assert peb == PPT,(a,b,t,peb)
    checks+=1
   assert not peb or pcp
   checks+=1
for a in [.1,.4,.8,1.,1.2,2.,3.,6.]:
 for b in [0., .3, .9, .99]:
  cp=root(a,b,'cp');eb=root(a,b,'eb')
  assert eb>cp-1e-10
  for t in [1e-4,.01,.1,.5,1,2,5,15,40]:
   v,w=conditions(a,b,t)
   assert v==(t>=cp-1e-9) or abs(t-cp)<1e-8
   assert w==(t>=eb-1e-9) or abs(t-eb)<1e-8
   checks+=2

def mproot(a,s,eb=False):
    a=mp.mpf(a);s=mp.mpf(s)
    L=-mp.log(s)
    lo=mp.mpf('1e-30')
    hi=mp.mpf(2)*L/min(a,mp.mpf(1))+mp.mpf(20)
    def f(t):
      p=mp.exp(-a*t);q=mp.exp(-t)
      return (p+q if eb else abs(p-q))-s*(1-q)
    if not eb and abs(a-1)<=s:return mp.mpf(0)
    for _ in range(250):
      mid=(lo+hi)/2
      if f(mid)>0:lo=mid
      else:hi=mid
    return (lo+hi)/2
mp.mp.dps=95
for astr in ['0.4','0.65','1.5','2.0','3.5']:
 a=mp.mpf(astr)
 exponent=abs(a-1)/min(a,mp.mpf(1))
 coef=2/min(a,mp.mpf(1))
 for sstr in ['1e-3','1e-5','1e-7','1e-9']:
  s=mp.mpf(sstr)
  cp=mproot(a,s);eb=mproot(a,s,True)
  ratio=(eb-cp)/(coef*s**exponent)
  assert mp.mpf('.90') < ratio < mp.mpf('1.15'),(astr,sstr,ratio)
  checks+=1
for ustr in ['-3','-1','-.4','.4','1','3']:
 u=mp.mpf(ustr)
 for Lstr in ['1000','5000']:
  L=mp.mpf(Lstr);s=mp.exp(-L);a=1+u/L
  cp=mproot(a,s);eb=mproot(a,s,True)
  cp_approx=L+mp.log(abs(mp.exp(-u)-1))
  eb_approx=L+mp.log(1+mp.exp(-u))
  assert abs(cp-cp_approx)<mp.mpf('.01'),(ustr,Lstr,'cp',str(cp-cp_approx))
  assert abs(eb-eb_approx)<mp.mpf('.01'),(ustr,Lstr,'eb',str(eb-eb_approx))
  checks+=2
print('checks_passed',checks)
print('example alpha=3 beta=0.6 cp=',root(3.,.6,'cp'),'eb=',root(3.,.6,'eb'))
