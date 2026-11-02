from fractions import Fraction as F
from itertools import product

def rhs_formula(mu,sigmas,rates):
 m=mu*mu
 weights=[x*x for x in sigmas]
 def a(q):return F(3)*(3*q**3+21*q*q+60*q+64)/(2*q*(q+1)**2*(q+4))
 def b(q,r):
  p=(q**3*r+q*r**3+2*q*q*r*r+3*(q**3+r**3)+13*(q*q*r+q*r*r)+21*(q*q+r*r)+42*q*r+60*(q+r)+64)
  return F(3)*p/(4*(q+1)**2*(q+r)*(r+1)**2*(q+r+4))
 return (m+sum(w/(1+q) for w,q in zip(weights,rates)),
        -F(21,4)*m*m+m*sum(w*a(q) for w,q in zip(weights,rates))+sum(weights[i]*weights[j]*b(rates[i],rates[j]) for i in range(len(weights)) for j in range(len(weights))))

def by_generator(mu,sigmas,rates,maxorder=4):
 states=[(k,ns) for k in range(-maxorder,maxorder+1) for ns in product(range(maxorder+1),repeat=len(sigmas)) if sum(ns)<=maxorder]
 stset=set(states);start=(0,(0,)*len(sigmas));phi=[{start:F(1)}];lam=[F(0)]
 def V(v):
  out={}
  for (k,ns),c in v.items():
   for h in [k-1,k+1]:
    if abs(h)>maxorder:continue
    def add(key,val):
     if key in stset:out[key]=out.get(key,F(0))+val
    add((h,ns),c*mu/2)
    for j,sg in enumerate(sigmas):
     np=list(ns);np[j]+=1
     add((h,tuple(np)),c*sg/2)
     if ns[j]>0:
      nm=list(ns);nm[j]-=1
      add((h,tuple(nm)),c*sg*ns[j]/2)
  return out
 for p in range(1,maxorder+1):
  y=V(phi[-1]);la=y.get(start,F(0));lam.append(la)
  for j in range(1,p+1):
   for st,c in phi[p-j].items():y[st]=y.get(st,F(0))-lam[j]*c
  y.pop(start,None)
  nphi={}
  for (k,ns),c in y.items():
   d=k*k+sum(rate*n for rate,n in zip(rates,ns))
   if c and d:nphi[(k,ns)]=c/d
  phi.append(nphi)
 return 2*lam[2],24*lam[4]

if __name__=='__main__':
 cases=[(F(1),[F(2),F(3)],[F(1,3),F(5,2)]),(F(2),[F(1),F(1,3)],[F(2),F(4)]),(F(3,2),[F(1,2)],[F(3,7)]),(F(0),[F(1),F(3,2),F(2)],[F(1),F(2),F(3)])]
 for mu,sigs,rts in cases:
  expected=rhs_formula(mu,sigs,rts)
  actual=by_generator(mu,sigs,rts)
  print('rates',rts,'sigs',sigs,'K2 K4 exact comparisons',expected==actual,'numerical',tuple(float(x) for x in expected))
  assert expected==actual,(expected,actual)
