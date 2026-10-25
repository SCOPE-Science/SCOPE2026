"""Independent exact-rational checks for two-cap holomorphic concentration.
The checker tests finite instances; the accompanying proof handles all degrees.
"""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product

def beta_num(a,b):
    return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))

def eig(n,d,a,b,t):
    assert 0<=a and 0<=b and a+b<=d and 0<t<1
    N=n+d
    if 2*t>=1:
        return sum(F(comb(N-1,j))*t**j*(1-t)**(N-1-j) for j in range(a+1)) + sum(F(comb(N-1,j))*t**j*(1-t)**(N-1-j) for j in range(b+1))
    c=N-a-b-2
    const=F(factorial(N-1),factorial(a)*factorial(b)*factorial(c-1))
    inside=F(0)
    for j in range(c):
        for r in range(j+1):
            inside+=F((-1)**j*comb(c-1,j)*comb(j,r),(a+r+1)*(b+j-r+1))*t**(a+b+j+2)
    return 1-const*inside

def exact_gap(n,d,t):
    # beta density integrated after conditional Beta symmetrization.
    N=n+d
    coeff=F(factorial(N-1),factorial(d)*factorial(n-3))
    upper=min(t,1-t)
    # u=s-t and 0<=u<=min(t,1-t).
    value=F(0)
    for j in range(n-2):
        w=F((-1)**j*comb(n-3,j))*(1-t)**(n-3-j)
        value+=w*(t**(d-1)*upper**(j+2)/F(j+2) - upper**(d+j+1)/F(d+j+1))
    return coeff*t*value

def run():
    checks=0
    for n in range(3,8):
      for d in range(2,9):
       for t in (F(1,13),F(2,7),F(3,7),F(1,2),F(4,7),F(11,13)):
        vals={(a,b):eig(n,d,a,b,t) for a in range(d+1) for b in range(d-a+1)}
        top=vals[d,0]
        second=vals[d-1,1]
        assert top == vals[0,d],(n,d,t,'symmetry')
        assert top>second, (n,d,t,'top')
        assert second == vals[1,d-1], (n,d,t,'second symmetry')
        assert top-second == exact_gap(n,d,t), (n,d,t,'gap identity',top-second,exact_gap(n,d,t))
        for (a,b),v in vals.items():
         if (a,b) in ((d,0),(0,d)):
          assert v==top
         else:
          assert v<=second,(n,d,t,a,b,v,second)
         checks+=1
        # Strict stochastic order at full counted degree.
        for a in range((d//2)+1,d):
         assert vals[a+1,d-a-1]>vals[a,d-a]
         checks+=1
    # Degree one exactly two top directions.
    for n in range(3,9):
     for t in (F(1,7),F(1,2),F(6,7)):
      assert eig(n,1,1,0,t)==eig(n,1,0,1,t)>eig(n,1,0,0,t)
      checks+=1
    print(f'PASS: {checks} exact-rational eigenvalue, ordering, and gap assertions')
if __name__=='__main__':run()
