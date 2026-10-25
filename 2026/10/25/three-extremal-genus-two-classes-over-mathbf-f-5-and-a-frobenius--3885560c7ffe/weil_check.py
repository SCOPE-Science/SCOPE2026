#!/usr/bin/env python3
"""Independent genus-two point counts over F5 and F25, using v^2+v+2=0."""
REPS=[(1,0,0,0,4,0,1),(1,0,1,0,3,0,4),(1,0,1,2,2,2,1)]
K=[(a,b) for a in range(5) for b in range(5)]

def mul(a,b):
 x,y=a;u,v=b
 # alpha^2 = 4 alpha + 3
 return ((x*u+3*y*v)%5,(x*v+y*u+4*y*v)%5)

def f_eval(coeff,x):
 acc=(0,0)
 for c in reversed(coeff):
  t=mul(acc,x)
  acc=((t[0]+c)%5,t[1])
 return acc

S={mul(a,a) for a in K};assert len(S)==13
for c in REPS:
 n1=2+sum(2 if sum(c[i]*pow(x,i,5) for i in range(7))%5 in (1,4) else 0 for x in range(5))
 n2=2+sum(1 if f_eval(c,x)==(0,0) else (2 if f_eval(c,x) in S else 0) for x in K)
 A1=6-n1;A2=(n2-26+A1*A1)//2
 assert (n1,n2) in ((12,26),(12,28),(12,24))
 assert A2 in (17,18,19)
 print('coefficients',c,'points_F5',n1,'points_F25',n2,'Weil_polynomial',[1,-A1,A2,-5*A1,25])
