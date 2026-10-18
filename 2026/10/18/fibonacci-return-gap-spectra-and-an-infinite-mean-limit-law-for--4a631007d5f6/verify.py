from collections import Counter
from math import isclose

def fib(n):
 a,b=0,1
 for _ in range(n):a,b=b,a+b
 return a

def bs(n):
 if n==0:return True
 word=bin(n)[2:]
 return all(len(block)%2==0 for block in word.split('1'))

def ht(j):return (1<<(j-2))+(2 if j%2==0 else 1)

def prediction(N):
 p=Counter({1:1+(N-1)//2,2:N//2})
 for j in range(2,N):p[ht(j)]+=fib(N-j+2)-1
 return +p

def run():
 for N in range(1,19):
  ss=[x for x in range(1<<N) if bs(x)]
  obs=Counter(b-a for a,b in zip(ss,ss[1:]))
  calc=prediction(N)
  assert ss[0]==0 and ss[-1]==(1<<N)-1,(N,ss[-1])
  assert len(ss)==fib(N+2),(N,len(ss),fib(N+2))
  assert obs==calc,(N,obs,calc)
  assert sum(g*c for g,c in calc.items())==(1<<N)-1,(N,calc)
  if N in [3,5,8,12,18]:
   print('N=',N,'ones=',len(ss),'gap_types=',len(obs),'freq=',dict(sorted(obs.items())))
 print('VERIFY_OK: exact independent binary-digit enumeration agrees with Fibonacci formula for every N=1..18')
if __name__=='__main__':run()
