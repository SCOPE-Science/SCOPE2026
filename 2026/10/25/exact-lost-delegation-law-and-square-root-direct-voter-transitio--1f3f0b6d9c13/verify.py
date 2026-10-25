from fractions import Fraction
from itertools import product
from math import prod

def analytic(m,n,q):
    r=1-q
    def success(a,b):
        t=0; fac=Fraction(1); total=Fraction(0)
        while True:
            total+=q*(r**t)*fac
            if t%2==0:
                k=t//2; ph=Fraction(b-k,b)
            else:
                k=(t+1)//2; ph=Fraction(a-k,a)
            fac*=ph; t+=1
            if not fac: break
        return total
    return success(m,n),success(n,m)

def brute(m,n,q):
    deg=[n]*m+[m]*n
    choices=[[-1]+list(range(m,m+n)) if i<m else [-1]+list(range(m)) for i in range(m+n)]
    sums=[Fraction(0),Fraction(0)]
    total=Fraction(0)
    for actions in product(*choices):
        prob=Fraction(1)
        for i,d in enumerate(actions):
            prob*=q if d==-1 else (1-q)/deg[i]
        if prob==0: continue
        total+=prob
        for v in range(m+n):
            seen=set(); w=v
            while w!=-1 and w not in seen:
                seen.add(w);w=actions[w]
            if w==-1: sums[int(v>=m)]+=prob
    return sums[0]/m,sums[1]/n,total

for m,n in [(1,1),(1,2),(2,2),(2,3),(3,2),(2,4),(3,3),(3,4)]:
 for q in [Fraction(1,2),Fraction(1,3)]:
  x=analytic(m,n,q); y=brute(m,n,q)
  assert x==y[:2],(m,n,q,x,y)
  assert y[2]==1
  print(m,n,str(q),'P_A=',x[0],'P_B=',x[1],'lost=',m*(1-x[0])+n*(1-x[1]))
print('ALL EXACT BRUTE PASS')
