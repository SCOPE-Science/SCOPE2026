"""Finite support checks for 3-variable ternary dependence structures.
Only mathematical objects and direct verification; not a proof of the infinite theorem.
"""
from itertools import product
from collections import defaultdict

def add(a,b,q):return a^b if q==4 else (a+b)%q
def mul(a,b,q):
 if q!=4:return a*b%q
 def shift(x):
  z=x<<1
  return (z&3)^((z>>2)*3)
 res=0
 for i in range(2):
  if (b>>i)&1:res^=a
  a=shift(a)
 return res

def check(q,d):
 V=list(product(range(q),repeat=d)); zero=(0,)*d
 S={x: {tuple(mul(a,u,q) for u in x) for a in range(q)} for x in V}
 idx={x:i for i,x in enumerate(V)}
 state={}
 for i,x in enumerate(V):
  for j,y in enumerate(V):
   if x==zero and y==zero:t='ZZ'
   elif x==zero:t='ZX'
   elif y==zero:t='XZ'
   elif x==y:t='XX'
   elif y in S[x]:t='PP'
   else:t='II'
   state[(i,j)]=t
 spans={}
 for i,x in enumerate(V):
  for j,y in enumerate(V):
   if state[(i,j)]=='II':
    spans[(i,j)]={tuple(add(mul(a,u,q),mul(b,v,q),q) for u,v in zip(x,y)) for a in range(q) for b in range(q)}
 profiles=defaultdict(set); perpair=defaultdict(set)
 for i,x in enumerate(V):
  for j,y in enumerate(V):
   st=state[(i,j)]
   prof=set()
   for k,z in enumerate(V):
    dep = st!='II' or z in spans[(i,j)]
    prof.add((state[(i,k)],state[(j,k)],dep))
   perpair[st].add(frozenset(prof))
   profiles[st]|=prof
 assert all(len(ps)==1 for ps in perpair.values()),[(k,len(v)) for k,v in perpair.items()]
 return {k:sorted(v) for k,v in sorted(profiles.items())},len(V)

if __name__=='__main__':
 pbyq={}
 for q,d in [(2,3),(2,4),(3,3),(3,4),(4,3),(5,3),(7,3)]:
  prof,size=check(q,d)
  cl='q2' if q==2 else 'q3' if q==3 else 'q4plus'
  if cl in pbyq:assert pbyq[cl]==prof,(cl,q,d)
  else:pbyq[cl]=prof
  print(f'q={q} dim={d} vertices={size} pair_classes={len(prof)} entries='+str({k:len(v) for k,v in prof.items()}))
 assert len(pbyq)==3
 print('THREE-PROFILE CHECK PASSED')
