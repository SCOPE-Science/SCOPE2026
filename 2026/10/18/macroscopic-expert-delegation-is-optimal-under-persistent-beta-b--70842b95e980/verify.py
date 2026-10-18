"""Reproduce exact beta-binomial delegation thresholds using rational arithmetic."""
from fractions import Fraction as Q
from math import comb, factorial


def beta_integer(a, b):
    return Q(factorial(a-1)*factorial(b-1), factorial(a+b-1))


def prob_beta_binomial(m, j, a, b):
    return comb(m,j)*beta_integer(a+j,b+m-j)/beta_integer(a,b)


def score(k, r, a, b, q):
    m=2*k-r
    tail_c=sum((prob_beta_binomial(m,j,a,b) for j in range(max(0,k-r),m+1)),Q(0))
    tail_w=sum((prob_beta_binomial(m,j,a,b) for j in range(k+1,m+1)),Q(0))
    return q*tail_c+(1-q)*tail_w


def delta(k, r, a, b, q):
    pref=comb(2*k-r-1,k)*beta_integer(a+k-r-1,b+k+1)/beta_integer(a,b)
    ratio=Q(1)
    for j in range(k-r-1,k+1): ratio *= Q(a+j,b+j)
    return pref*(q-(1-q)*ratio)


def binomial_score(k,r,p,q):
    m=2*k-r
    def tail(t):
        return sum((comb(m,j)*p**j*(1-p)**(m-j) for j in range(max(0,t),m+1)),Q(0))
    return q*tail(k-r)+(1-q)*tail(k+1)

assertions=0
for a,b in [(3,2),(4,1),(5,3),(2,1)]:
  for k in range(1,13):
    q=Q(7,10)
    vals=[score(k,r,a,b,q) for r in range(k+1)]
    for r in range(k):
      assert vals[r+1]-vals[r] == delta(k,r,a,b,q),(a,b,k,r)
      assertions+=1
    max_idx=[r for r,v in enumerate(vals) if v==max(vals)]
    assert all(x+1==y for x,y in zip(max_idx,max_idx[1:]))
    assertions+=1
for k in range(1,30):
  vals=[score(k,r,3,2,Q(7,10)) for r in range(k+1)]
  alpha=Q(4*k-2,7)
  r0=-(-alpha.numerator//alpha.denominator)
  expected=[r0] + ([r0+1] if alpha.denominator==1 else [])
  assert [r for r,v in enumerate(vals) if v==max(vals)]==expected, (k,expected)
  assertions+=1
for k in range(1,30):
  vals=[binomial_score(k,r,Q(3,5),Q(7,10)) for r in range(k+1)]
  assert [r for r,v in enumerate(vals) if v==max(vals)]==[1], k
  assertions+=1
print(f'Exact rational assertions passed: {assertions}')
for k in (1,2,3,4,10,20,29):
 r0=-(-((4*k-2)//1)//7) # ceiling integer
 r0=(4*k-2+6)//7
 print('k=',k,'r=',r0,'rate=',round(float(score(k,r0,3,2,Q(7,10))),8))
