#!/usr/bin/env python3
"""Exact rational test of extremal orbit inequalities and gradient certificates.
This finite check corroborates, but does not replace, the all-dimensional proof.
"""
from fractions import Fraction as F

SHAPES={
 2:(F(3,2),F(1,2),F(1)),
 3:(F(1),F(1,2),F(5,8)),
 4:(F(3,4),F(1,2),F(7,12)),
 5:(F(13,21),F(1,2),F(1,2)),
}
DUAL={
 2:[('I',1,0,F(4,3)),('II',1,None,F(1)),('II',0,None,F(2,3))],
 3:[('I',1,2,F(3)),('II',1,None,F(1))],
 4:[('I',1,2,F(16,7)),('I',2,1,F(16,7)),('II',1,None,F(3,7))],
 5:[('I',2,1,F(20,13)),('I',3,0,F(50,13)),('II',1,None,F(8,13))],
}

def moments(p,typ,i,j=None):
 if typ=='I':
  return (F(i*(p-i),p),F(j*(2-j),2),F((2*i-p*j)**2,2*p*(p+2)))
 assert typ=='II'
 return (F(0),F(2*i*(2-i)),F(2*p*(i-1)**2,p+2))

checks=0
for p,(u,v,w) in SHAPES.items():
 all_orbits=[]
 for i in range(1,p):
  for j in range(3): all_orbits.append(('I',i,j,moments(p,'I',i,j)))
 for j in range(3): all_orbits.append(('II',j,None,moments(p,'II',j)))
 for t,i,j,E in all_orbits:
  val=sum(s*e for s,e in zip((u,v,w),E))
  assert val<=1,(p,t,i,j,val)
  checks+=1
 gradient=[F(p-1)/u,F(1)/v,F(1)/w]
 cert=[F(0)]*3
 for typ,i,j,weight in DUAL[p]:
  E=moments(p,typ,i,j)
  assert sum(s*e for s,e in zip((u,v,w),E))==1,(p,typ,i,j)
  assert weight>0
  cert=[x+weight*e for x,e in zip(cert,E)]
  checks+=2
 assert cert==gradient,(p,cert,gradient)
 checks+=3
 print(f'p={p}: {len(all_orbits)} orbit feasibility inequalities, positive KKT identity verified')

for p in range(6,500):
 n=p+2
 r2=F((n*n)//4,n)
 assert r2>=2
 for j in range(3):
  E=moments(p,'II',j)
  assert sum(E)<=r2
  checks+=1
 assert sum(moments(p,'II',1))==2
 assert ((sum(moments(p,'II',1))==r2)==(p==6))
print(f'PASS: {checks} exact rational comparisons and identities; no floating tolerances.')
