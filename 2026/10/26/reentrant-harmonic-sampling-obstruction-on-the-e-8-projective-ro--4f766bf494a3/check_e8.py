from itertools import combinations,product
from collections import Counter
from math import comb
roots=[]
for i,j in combinations(range(8),2):
 for s,t in product((-2,2),repeat=2):
  x=[0]*8;x[i]=s;x[j]=t;roots.append(tuple(x))
for signs in product((-1,1),repeat=8):
 if signs.count(-1)%2==0:roots.append(signs)
assert len(roots)==240 and len(set(roots))==240

def canonical(x):
 for z in x:
  if z:
   return x if z>0 else tuple(-y for y in x)
L=sorted({canonical(x) for x in roots})
assert len(L)==120
N=len(L)
dot=lambda x,y:sum(a*b for a,b in zip(x,y))
counts=Counter(abs(dot(a,b)) for i,a in enumerate(L) for b in L[i+1:]);print('pair inner abs scaled8:', counts)
A=[[int(i!=j and dot(L[i],L[j])==0) for j in range(N)] for i in range(N)]
assert all(sum(row)==63 for row in A)
common=Counter()
for i in range(N):
 for j in range(i+1,N):
  s=sum(A[i][k]*A[j][k] for k in range(N))
  common[(A[i][j],s)]+=1
assert set(common)=={(1,30),(0,36)}
print('graph common neighbors:',common)
# Gegenbauer coefficient by recurrence (l+1) C_{l+1} =2(l+3)t C_l-(l+5)C_{l-1}; at t=1/2, 0,1 use rational with sympy or integer divisions
from fractions import Fraction

def Cseq(t,limit):
 t=Fraction(t)
 C=[Fraction(1),6*t]
 for l in range(1,limit):
  C.append((2*(l+3)*t*C[-1]-(l+5)*C[-2])/(l+1))
 return C
c0=Cseq(0,30); ch=Cseq(Fraction(1,2),30); c1=Cseq(1,30)
for l in range(0,30,2):
 b,d,h=map(int,(c0[l],ch[l],c1[l]))
 E=(h+63*b+56*d,h+3*b-4*d,h-9*b+8*d)
 assert all(x>=0 for x in E)
 print(l,E,'rank',int(E[0]>0)+84*int(E[1]>0)+35*int(E[2]>0))
