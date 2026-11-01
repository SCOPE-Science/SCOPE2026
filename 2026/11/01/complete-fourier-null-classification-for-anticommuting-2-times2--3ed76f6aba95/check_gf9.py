"""Exact extension-field spot checks of the anticommutator Fourier-null rule.
GF(9) is F_3[u]/(u*u+1), encoded as a+3*b; no floating point.
Run: python3 check_gf9.py
"""
from random import Random
q=9
v=[(a,b) for b in range(3) for a in range(3)]
def add(x,y):
 a,b=v[x];c,d=v[y];return (a+c)%3+3*((b+d)%3)
def neg(x):
 a,b=v[x];return (-a)%3+3*((-b)%3)
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a,b=v[x];c,d=v[y];return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
def sq(x):return mul(x,x)
def chi(x):
 if x==0:return 0
 z=1
 for _ in range(4):z=mul(z,x)
 return 1 if z==1 else -1
INV2=2
V=[(x,y,z) for x in range(q) for y in range(q) for z in range(q)]
def Q(x):return add(sq(x[0]),mul(x[1],x[2]))
def bil(x,y):return add(mul(x[0],y[0]),mul(INV2,add(mul(x[1],y[2]),mul(x[2],y[1]))))
S=[x for x in V if Q(x)==1]
assert len(S)==q*q+q
zero=(0,0,0)
def predicted(a,b,P,R):
 c=bil(P,R);u=Q(P);vv=Q(R)
 if c==0:return False
 if P!=zero and u==0 and chi(vv)==-1 and a!=0:
  disc=add(add(sq(c),mul(2,mul(mul(a,b),c))),mul(vv,sq(a)))
  if chi(disc)==1:return True
 if R!=zero and vv==0 and chi(u)==-1 and b!=0:
  disc=add(add(sq(c),mul(2,mul(mul(a,b),c))),mul(u,sq(b)))
  if chi(disc)==1:return True
 return False
def direct_formula(a,b,P,R):
 c=bil(P,R)
 n1=sum(bil(P,Z)==neg(a) for Z in S)
 n2=sum(bil(R,Z)==b for Z in S)
 n12=sum(bil(P,Z)==neg(a) and bil(R,Z)==b for Z in S)
 return (q**5*(P==zero and R==zero)+q**3*(c==0)-q*q +
 q**3*(P==zero)*(q*(a==0)-1)+q**3*(R==zero)*(q*(b==0)-1)
 +q*q*n12-q*(n1+n2)+len(S))
rng=Random(272727)
for i in range(2500):
 P=V[rng.randrange(len(V))];R=V[rng.randrange(len(V))];a=rng.randrange(q);b=rng.randrange(q)
 assert (direct_formula(a,b,P,R)==0)==predicted(a,b,P,R),(a,b,P,R)
# Target the rare zero family, rather than only uniform samples.
zeros=0
iso=[P for P in V if P!=zero and Q(P)==0]
nonsq=[R for R in V if chi(Q(R))==-1]
for k in range(350):
 P=iso[rng.randrange(len(iso))];R=nonsq[rng.randrange(len(nonsq))]
 a=rng.randrange(1,q); b=rng.randrange(q)
 if predicted(a,b,P,R):
  assert direct_formula(a,b,P,R)==0
  zeros+=1
assert zeros>=30,zeros
print('EXACT_EXTENSION_FIELD_GF9_OK trials=2850 zero_family_hits='+str(zeros))
