from collections import Counter

def N(t,n,r):
 d=1<<t; H=t+2; q=1<<n; r%=q
 if n==0: return 1
 if n==1: return 2
 if n<H:
  return (q*q//4 if r in (0,2) else q*q//2 if r==1 else 0)
 if r%(1<<H)==1: return (1<<(t+1))*q
 if r%(1<<H)==2: return (1<<t)*q
 if n<d: return q*q//4 if r==0 else 0
 if r%(1<<d)==0: return (1<<(2*(d-1)))*N(t,n-d,r//(1<<d))
 return 0

def verify(t,n):
 q=1<<n; d=1<<t
 h=Counter(pow(x,d,q) for x in range(q))
 obs=[0]*q
 for a,na in h.items():
  for b,nb in h.items():obs[(a+b)%q]+=na*nb
 for r in range(q):
  expect=N(t,n,r)
  if obs[r]!=expect: return (t,n,r,obs[r],expect)
 assert sum(obs)==q*q
 return True
if __name__=='__main__':
 k=0
 for t in (2,3,4,5):
  for n in range(0,12 if t<=3 else 10):
   r=verify(t,n)
   assert r is True, r
   k+=1
 print('VERIFIED',k,'complete residue distributions')
 for t in range(2,6):
  H=t+2; d=1<<t
  print('t',t,'d',d,'density=',(2**(d-t-1),2**d-1))
