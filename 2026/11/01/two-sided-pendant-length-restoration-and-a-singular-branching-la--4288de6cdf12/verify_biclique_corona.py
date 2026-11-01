"""Supplemental arithmetic checks for negative type on bipartite coronas.
Finite checks do not replace the analytical proof.
Run with python verify_biclique_corona.py (requires mpmath and numpy).
"""
from fractions import Fraction as F
import itertools
import math
import numpy as np
import mpmath as mp

mp.mp.dps=65

def block(q,t,p):
    P=lambda x:mp.power(mp.mpf(x),p)
    X=q-(q-1)*P(2)
    Y=q*P(1+t)-P(t)-(q-1)*P(2+t)
    Z=q*P(1+2*t)-(q-1)*P(2+2*t)
    return X,Y,Z

def threshold(q,t):
    top=mp.log(mp.mpf(q)/(q-1),2)
    def det(p):
        x,y,z=block(q,t,p)
        return x*z-y*y
    lo=mp.mpf('0');hi=top
    assert det(lo)>0 and det(hi)<0
    for _ in range(200):
        mid=(lo+hi)/2
        if det(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def limiting_c(t):
    A=mp.log(2);B=mp.log((t+2)/(t+1));C=mp.log((2*t+2)/(2*t+1))
    return 2/(A+C+mp.sqrt((A-C)**2+4*B**2))

def Dmatrix(q,t,p,typ=float):
    # indexing 0..q-1: A core, q..2q-1: B core,
    # 2q..3q-1: A leaf, 3q..4q-1: B leaf.
    k=2*q; mat=np.zeros((4*q,4*q))
    for i in range(4*q):
      for j in range(i):
        a,b=i%k,j%k
        d=(0 if a==b else (1 if (a//q)!=(b//q) else 2)) + t*((i>=k)+(j>=k))
        mat[i,j]=mat[j,i]=d**p
    return mat

def exact_test(q,t,alpha,p=1):
    N=2*q
    def dist(i,j):
        a,b=i%N,j%N
        d=F(0) if a==b else (F(1) if a//q!=b//q else F(2))
        return d + t*(int(i>=N)+int(j>=N))
    Q=sum(alpha[i]*alpha[j]*dist(i,j)**p for i in range(4*q) for j in range(4*q) if i!=j)
    P=lambda x:x**p
    C=P(2);H=P(t)-P(t+2);L=P(2*t+2)
    Qfl=F(0)
    means=[]
    for s in (0,q):
        ac=[alpha[i] for i in range(s,s+q)]
        al=[alpha[i+N] for i in range(s,s+q)]
        am=sum(ac)/q;lm=sum(al)/q
        means.append((am,lm))
        for j in range(q):
            for k in range(q):
                if j==k:continue
                Qfl+=C*(ac[j]-am)*(ac[k]-am)+L*(al[j]-lm)*(al[k]-lm)
        Qfl+=2*H*sum((ac[j]-am)*(al[j]-lm) for j in range(q))
    (cA,lA),(cB,lB)=means
    cp=(cA+cB)/2; cm=(cA-cB)/2; lm=(lA-lB)/2
    assert cp==-(lA+lB)/2
    S=(q-1)*(P(2)+P(2*t+2)-2*P(t+2))+q*(1+P(1+2*t)-2*P(1+t))-2*P(t)
    X=q-(q-1)*P(2)
    Y=q*P(1+t)-P(t)-(q-1)*P(t+2)
    Z=q*P(1+2*t)-(q-1)*P(2*t+2)
    Qdec=Qfl+2*q*S*cp**2-2*q*(X*cm**2+2*Y*cm*lm+Z*lm**2)
    assert Q==Qdec,(q,t,Q,Qdec)

n=0
for q in range(2,7):
  for t in (F(1,3),F(1),F(5,2)):
    for k in range(12):
      alpha=[F(((i*i+3*i+7*k+k*i)%11)-5,1) for i in range(4*q)]
      alpha[-1]=-sum(alpha[:-1]); exact_test(q,t,alpha)
      n+=1
print('EXACT_POWER_DISTANCE_QUADRATIC_DECOMPOSITION_OK',n)

m=0
for q in (3,4,5,7):
  for t in (mp.mpf('0.05'),mp.mpf('0.5'),mp.mpf('1'),mp.mpf('4')):
    p=float(threshold(q,t));N=4*q; H=np.eye(N)-np.ones((N,N))/N
    for exponent,expected in ((p-0.025,1),(p+0.025,-1)):
      E=np.linalg.eigvalsh(-H@Dmatrix(q,float(t),exponent)@H)
      # one near-zero eigenvalue for constants; remaining eigenvalues strictly +/-
      vals=E[np.abs(E)>1e-7]
      if expected==1:assert min(vals)>0,(q,t,exponent,min(vals))
      else:assert min(vals)<-1e-6,(q,t,exponent,min(vals))
      m+=1
    E=np.linalg.eigvalsh(-H@Dmatrix(q,float(t),p)@H)
    assert sum(np.abs(E)<1e-7)==2,(q,t,E[:5])
    assert E[2]>1e-6,(q,t,E[:5])
print('FULL_POWERED_DISTANCE_INERTIA_AND_ENDPOINT_RANK_OK',m)

for q in (3,4,5,8,15):
  top=mp.log(mp.mpf(q)/(q-1),2)
  for t in (mp.mpf('1e-12'),mp.mpf('0.05'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('20'),mp.mpf('1e12')):
    p=threshold(q,t)
    assert 0<p<top
    if t==mp.mpf('1e-12') or t==mp.mpf('1e12'):
      assert abs(p-top)<mp.mpf('0.02')
print('TWO_SIDED_PENDANT_LENGTH_RESTORATION_DIAGNOSTICS_OK')

for t in (mp.mpf('0.01'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('3'),mp.mpf('100')):
 c=limiting_c(t)
 vals=[float(q*threshold(q,t)) for q in (200,1000,5000)]
 assert vals[0]>vals[1]>vals[2]>float(c)
 assert abs(vals[-1]-float(c))<0.005,(t,vals,c)
 print('BRANCHING_CONSTANT',str(t),float(c),vals)
assert abs(limiting_c(mp.mpf('1e-9'))-1/(2*mp.log(2)))<mp.mpf('1e-6')
assert abs(limiting_c(mp.mpf('1e9'))-1/mp.log(2))<mp.mpf('1e-6')
print('NONCOMMUTING_SMALL_LENGTH_LARGE_BRANCH_LIMITS_OK')
print('ALL_BIPARTITE_CORONA_NEGATIVE_TYPE_CHECKS_OK')
