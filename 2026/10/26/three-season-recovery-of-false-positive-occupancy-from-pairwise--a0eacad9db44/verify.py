#!/usr/bin/env python3
"""Exact rational check of three-season occupancy moment inversion."""
from fractions import Fraction as F
from itertools import product
import json

def derive(pi,gamma,epsilon,f,d):
 assert gamma>0 and epsilon>0 and gamma<1 and epsilon<1 and pi==gamma/(gamma+epsilon)
 assert len(d)==3 and all(f < x < 1 for x in d)
 latent=[1-pi,pi]
 tr=[[1-gamma,gamma],[epsilon,1-epsilon]]
 joint={obs:F(0) for obs in product((0,1),repeat=3)}
 for x in product((0,1),repeat=3):
  a=latent[x[0]]*tr[x[0]][x[1]]*tr[x[1]][x[2]]
  for y in product((0,1),repeat=3):
   b=a
   for t in range(3):
    rate=d[t] if x[t] else f
    b*=rate if y[t] else 1-rate
   joint[y]+=b
 assert sum(joint.values())==1
 m=tuple(sum(prob*obs[t] for obs,prob in joint.items()) for t in range(3))
 c={(i,j):sum(prob*(obs[i]-m[i])*(obs[j]-m[j]) for obs,prob in joint.items()) for i,j in ((0,1),(1,2),(0,2))}
 return m,c,joint

def recover(m,c):
 a,b=c[(0,1)],c[(1,2)]
 assert a!=0 and b!=0 and a!=b
 f=(a*m[2]-b*m[0])/(a-b)
 r01=a/((m[0]-f)*(m[1]-f))
 r12=b/((m[1]-f)*(m[2]-f))
 r02=c[(0,2)]/((m[0]-f)*(m[2]-f))
 assert r01==r12 and r02>0
 pi=r02/(r01*r01+r02)
 lam=r02/r01
 d=tuple(f+(x-f)/pi for x in m)
 return pi,pi*(1-lam),(1-pi)*(1-lam),f,d

def digest(m,c):
 return { 'means':[str(x) for x in m], 'covariances': {str(k):str(v) for k,v in c.items()} }

def main():
 pi,gamma,epsilon,f,d=F(2,5),F(1,5),F(3,10),F(1,10),(F(3,5),F(4,5),F(7,10))
 m,c,joint=derive(pi,gamma,epsilon,f,d)
 recovered=recover(m,c)
 assert recovered==(pi,gamma,epsilon,f,d)
 out={'example': {'initial':[str(pi),str(gamma),str(epsilon),str(f)]+[str(x) for x in d], 'moments':digest(m,c), 'recovered':[str(x) if not isinstance(x,tuple) else [str(y) for y in x] for x in recovered], 'joint':{''.join(map(str,k)):str(v) for k,v in joint.items()}}}
 cases=0
 for den in (10,12):
  for gamma_n,epsilon_n in ((1,2),(2,1),(3,2),(2,3),(4,1)):
   gamma=F(gamma_n,den);epsilon=F(epsilon_n,den)
   pi=gamma/(gamma+epsilon)
   f=F(1,10)
   d=(F(5,10),F(7,10),F(8,10))
   m,c,_=derive(pi,gamma,epsilon,f,d)
   assert recover(m,c)==(pi,gamma,epsilon,f,d)
   cases+=1
 # Negative memory parameter check.
 gamma=F(4,5);epsilon=F(3,5);pi=gamma/(gamma+epsilon)
 m,c,_=derive(pi,gamma,epsilon,F(1,10),(F(5,10),F(7,10),F(8,10)))
 assert recover(m,c)==(pi,gamma,epsilon,F(1,10),(F(5,10),F(7,10),F(8,10)))
 cases+=1
 # Construct distinct interior models with exactly identical pair moments when first/third detection match.
 pi,gamma,epsilon,f,d=F(2,5),F(1,5),F(3,10),F(1,10),(F(3,5),F(4,5),F(3,5))
 m,c,_=derive(pi,gamma,epsilon,f,d)
 assert m[0]==m[2] and c[(0,1)]==c[(1,2)]
 f2=F(1,8)
 r01=c[(0,1)]/((m[0]-f2)*(m[1]-f2))
 r02=c[(0,2)]/((m[0]-f2)*(m[2]-f2))
 pi2=r02/(r01*r01+r02);lam2=r02/r01
 gamma2=pi2*(1-lam2);epsilon2=(1-pi2)*(1-lam2)
 d2=tuple(f2+(t-f2)/pi2 for t in m)
 assert all(F(0)<x<F(1) for x in (pi2,gamma2,epsilon2,f2,*d2)) and all(x>f2 for x in d2)
 m2,c2,_=derive(pi2,gamma2,epsilon2,f2,d2)
 assert m==m2 and c==c2 and f!=f2
 out['degenerate_moments']={'same_means':[str(x) for x in m], 'same_covariances':{str(k):str(v) for k,v in c.items()}, 'model_A':[str(x) for x in (pi,gamma,epsilon,f,*d)], 'model_B':[str(x) for x in (pi2,gamma2,epsilon2,f2,*d2)]}
 out['tested_nondegenerate_parameter_sets']=cases+1
 print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__': main()
