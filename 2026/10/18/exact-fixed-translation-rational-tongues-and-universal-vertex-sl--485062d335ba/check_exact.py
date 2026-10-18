"""Exact finite checks supporting the analytic rational-tongue theorem.
This script is a reproducibility test, not a proof for all denominators.
"""
from fractions import Fraction
from math import gcd

def polynomials(p,q):
    assert 1 <= p < q and gcd(p,q)==1
    digit=[((j+1)*p)//q-(j*p)//q for j in range(q)]
    c=[1]+digit[1:-1]+[0]
    ceil=lambda n:-((-n)//q)
    assert c==[ceil((j+1)*p)-ceil(j*p) for j in range(q)]  # upper mechanical via ceiling
    return digit,c

def poly(c,t):
    return sum(v*t**j for j,v in enumerate(c))

def check_pair(p,q,t):
    d,c=polynomials(p,q)
    Q=sum(t**j for j in range(q))
    S=poly(c,t)
    lo=S/Q
    hi=(S+t**(q-1)-t**q)/Q
    assert Fraction(p,q)<lo<hi<1
    # q-periodic boundary orbits from exact formal linear recurrence
    a=Fraction(0)
    lower=[a]
    for j in range(q):
        a=t*a+lo-d[j]
        lower.append(a)
    assert lower[-1]==0 and all(0<x<1 for x in lower[1:-1])
    e=d.copy();e[0]=1;e[-1]=0
    a=Fraction(1)
    upper=[a]
    for j in range(q):
        a=t*a+hi-e[j]
        upper.append(a)
    assert upper[-1]==1 and all(0<x<1 for x in upper[1:-1])
    # implicit differentiation along both exact boundary cycles
    lo_prime=-sum(t**(q-1-j)*lower[j] for j in range(q))/Q
    hi_prime=-sum(t**(q-1-j)*upper[j] for j in range(q))/Q
    assert lo_prime<0 and hi_prime<0
    return lo,hi,lo_prime,hi_prime

def run():
    total=0
    for q in range(2,71):
      for p in range(1,q):
        if gcd(p,q)>1:continue
        d,c=polynomials(p,q)
        assert sum(c)==p
        assert sum(j*c[j] for j in range(q))==Fraction((p-1)*(q-1),2)
        for t in [Fraction(1,7),Fraction(1,2),Fraction(5,6),Fraction(99,100)]:
          check_pair(p,q,t)
          total+=1
    print(f'Exact rational checks: {total} parameter triples, all boundary points, symbolic q-word identities, derivative signs pass.')
    for p,q in [(1,2),(1,3),(2,5),(3,8),(4,9),(7,19)]:
      d,c=polynomials(p,q)
      t=Fraction(999,1000)
      lo,hi,_,_=check_pair(p,q,t)
      # first-order endpoint slopes in b as functions of t near 1
      sl_lo=(lo-Fraction(p,q))/(1-t)
      sl_hi=(hi-Fraction(p,q))/(1-t)
      assert abs(sl_lo-Fraction(q-1,2*q))<Fraction(1,100)
      assert abs(sl_hi-Fraction(q+1,2*q))<Fraction(1,100)
    print('Near-rigid derivative coefficients pass for six reduced fractions at lambda=999/1000.')
    for p,q,t in [(1,2,Fraction(3,5)),(2,5,Fraction(3,5)),(3,8,Fraction(9,10))]:
      print('example',p,q,'lambda',t,'bounds and derivatives', check_pair(p,q,t))

if __name__=='__main__':run()
