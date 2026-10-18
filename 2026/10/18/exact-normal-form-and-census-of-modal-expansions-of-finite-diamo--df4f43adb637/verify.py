from itertools import product,permutations
from math import comb,factorial
from collections import Counter

def profile(n):
 p=sum(comb(n,r)**2*factorial(r) for r in range(n+1))
 a=(n+2)**n+2*n**(n+1)+sum(comb(n,r)**2*factorial(r)*(n-r+1)**(n-r) for r in range(2,n+1))+n
 b=n*((n+1)*2**n+n*n*(n-1)+n)
 c=p+n
 d=n*(2*n+1+2**n)
 return a+b+c+d+1

def structure(n,need_orbits=False):
 m=n+2; top=m-1
 def le(a,b):return a==0 or b==top or a==b
 def meet(a,b):return a if le(a,b) else b if le(b,a) else 0
 def join(a,b):return b if le(a,b) else a if le(b,a) else top
 ops=[(i,j,meet(i,j),join(i,j)) for i in range(m) for j in range(m)]
 box=[]
 dia=[]
 for v in product(range(m),repeat=m-1):
  f=v+(top,)
  if all(f[k]==meet(f[i],f[j]) for i,j,k,_ in ops):box.append(f)
  if all(le(f[i],f[j]) for i in range(m) for j in range(m) if le(i,j)):dia.append(f)
 valid=[]
 for B in box:
  for D in dia:
   if all(le(meet(B[i],D[j]),D[k]) for i,j,k,_ in ops):valid.append((B,D))
 assert len(valid)==profile(n),(n,len(valid),profile(n))
 print('n',n,'B',len(box),'D',len(dia),'valid',len(valid))
 if not need_orbits:return
 res=[]; orig=set(valid)
 for perm in permutations(range(1,n+1)):
  t=(0,)+perm+(top,)
  inv=[0]*m
  for i,j in enumerate(t):inv[j]=i
  def trans(f):return tuple(t[f[inv[i]]] for i in range(m))
  fixed=sum(trans(B)==B and trans(D)==D for B,D in valid)
  res.append(fixed)
 assert sum(res)%factorial(n)==0
 print('Burnside',Counter(res),'isomorphism',sum(res)//factorial(n))
 return valid

if __name__=='__main__':
 for n in (3,4):structure(n,True)
 print('n5 and n6 closed census',profile(5),profile(6))
