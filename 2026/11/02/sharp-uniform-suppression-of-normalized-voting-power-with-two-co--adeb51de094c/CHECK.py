from fractions import Fraction
from itertools import product
from math import comb
import math

def binom(n,k): return comb(n,k) if 0<=k<=n else 0

def exact_formula(m,p):
  assert m%2==1 and m>=1 and 0<=p<=1
  s=(m+1)//2
  q=(1-p)/2
  hub=Fraction(1,2)-sum(Fraction(binom(m,j))*q**j*(1-q)**(m-j) for j in range(s+1,m+1))
  a=(1+p)/2;b=(1-p)/2
  leaf=Fraction(1,2)*Fraction(binom(m-1,s-1),2**(m-1))
  if s>=2:
    leaf+=Fraction(1,2)*binom(m-1,s-2)*a**(s-2)*b**s
  return hub,leaf

def exhaustive(m,p):
  hub=Fraction(0);leaf=Fraction(0)
  for a,b in product((-1,1),repeat=2):
    for acts in product((-1,1,2,3),repeat=m):
      prob=Fraction(1,4)
      for c in acts:
        prob*= (1-p)/2 if c in (-1,1) else p/2
      effective=lambda c,aa,bb: aa if c==2 else (bb if c==3 else c)
      # hub A flip both ways. Action codes 2=>A, 3=>B
      forA=lambda aa: aa+ b+sum(effective(c,aa,b) for c in acts)
      central=(forA(1)>0 and forA(-1)<0)
      hub+=prob*int(central)
      # leaf 0 flip by selecting direct ballot
      rest=a+b+sum(effective(c,a,b) for c in acts[1:])
      lv=(rest+1>0 and rest-1<0)
      leaf+=prob*int(lv)
  return hub,leaf

def check():
  count=0
  for m in (1,3,5,7):
    for p in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
      a=exhaustive(m,p);b=exact_formula(m,p)
      assert a==b,(m,p,a,b)
      count+=2
      print('m',m,'p',str(p),'hub',str(a[0]),'leaf',str(a[1]))
  print('PASS',count,'independent exact rational formula comparisons')
  # The sharp upper bound is a second, exact finite family of checks.
  checks=0
  for m in range(1,60,2):
    prev=None
    for p in (Fraction(0),Fraction(1,8),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(7,8),Fraction(1)):
      h,d=exact_formula(m,p)
      share=h/(2*h+m*d)
      h1,d1=exact_formula(m,Fraction(1))
      upper=h1/(2*h1+m*d1)
      assert 0<share<=upper
      if prev is not None:
        assert share>=prev
        if m>=3: assert share>prev
      if p==0: assert share==Fraction(1,m+2)
      if p==1: assert share==upper
      prev=share
      checks+=1
  print('PASS',checks,'exact monotonicity and optimal envelope instances')
  asym=math.sqrt(math.pi/2)
  errs=[]
  for m in (101,501,1001,5001,10001):
    h,d=exact_formula(m,Fraction(1))
    r=float(h/(2*h+m*d))
    errs.append(abs(math.sqrt(m)*r-asym)/asym)
  assert all(errs[i]>errs[i+1] for i in range(len(errs)-1))
  assert errs[-1]<0.025
  print('PASS 5 scaled envelope asymptotic checks')

if __name__=='__main__': check()
