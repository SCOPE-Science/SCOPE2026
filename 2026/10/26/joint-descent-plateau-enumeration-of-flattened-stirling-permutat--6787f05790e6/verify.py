from math import comb
from collections import Counter

def total_poly(n):
 m=n-1
 # Signed block-pair recurrence on m ordinary absolute labels
 B=[{(0,0):1}]
 for r in range(1,m+1):
  v=Counter()
  for s in range(1,r+1):
   w = {(0,1):1} if s==1 else {(1,s-1):1,(1,s):1,(2,s-1):2**(s-1)-2}
   for (a,b),c in B[r-s].items():
    for (d,e),f in w.items():
     v[a+d,b+e] += comb(r-1,s-1)*c*f
  B.append(dict(v))
 Q=Counter()
 for z in range(m+1):
  d,p = (0,1) if z==0 else (1,z)
  for (a,b),c in B[m-z].items():
   Q[a+d,b+p]+=comb(m,z)*c
 return {k:v for k,v in Q.items() if v}

def direct(n):
 c=Counter()
 def walk(w,k):
  if k>n:
   starts=[w[0]];d=0;p=0
   for a,b in zip(w,w[1:]):
    if a>b: d+=1;starts.append(b)
    if a==b:p+=1
   if all(a<=b for a,b in zip(starts,starts[1:])):c[d,p]+=1
  else:
   for pos in range(len(w)+1):
    walk(w[:pos]+(k,k)+w[pos:],k+1)
 walk((1,1),2)
 return dict(c)

def main():
 for n in range(1,9):
  p=total_poly(n)
  d=direct(n)
  if p != d:
   raise AssertionError((n,p,d))
  print('n=',n,'total=',sum(p.values()),'cells=',len(p))
 print('VERIFICATION_OK')

if __name__=='__main__':
 main()
