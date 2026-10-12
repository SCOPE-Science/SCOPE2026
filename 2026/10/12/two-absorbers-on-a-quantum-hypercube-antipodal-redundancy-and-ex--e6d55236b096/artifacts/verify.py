"""Exact Walsh/Krawtchouk checks for two absorbing sites of a quantum hypercube."""
from fractions import Fraction
from itertools import combinations
from math import comb


def kraw(d, k, r):
    return sum((-1)**j * comb(r, j) * comb(d-r, k-j)
               for j in range(max(0, k-(d-r)), min(k, r)+1))


def formula(d, r, x):
    u = (1 << r) - 1
    h, ell = x.bit_count(), (x ^ u).bit_count()
    if r == d:
        return Fraction(1, 1) - Fraction(1, comb(d, h))
    amount = Fraction(2)
    for k in range(1, d):
        c = comb(d, k)
        rr, a, b = kraw(d,k,r),kraw(d,k,h),kraw(d,k,ell)
        assert abs(rr) < c
        amount += Fraction(c*(a*a+b*b)-2*rr*a*b, c*c-rr*rr)
    return Fraction(1) - amount / (1 << d)


def independent(d,r,x):
    u=(1<<r)-1
    total=Fraction(0)
    for k in range(d+1):
        inds=[sum(1<<j for j in sel) for sel in combinations(range(d),k)]
        a=[1 for t in inds]
        b=[(-1)**((t&u).bit_count()) for t in inds]
        v=[(-1)**((t&x).bit_count()) for t in inds]
        c=len(inds); R=sum(b)
        A=sum(v); B=sum(vi*bi for vi,bi in zip(v,b))
        if abs(R)==c:
            numerator=Fraction(A*A,c)
        else:
            numerator=Fraction(c*(A*A+B*B)-2*R*A*B,c*c-R*R)
        total += numerator/(1<<d)
    return Fraction(1) - total

n=0
for d in range(2,7):
  for r in range(1,d+1):
    vals=[]
    for x in range(1<<d):
      a,b=formula(d,r,x),independent(d,r,x)
      assert a==b and 0<=a<=1,(d,r,x,a,b)
      vals.append(a)
      n+=1
    bright = d+1 if r==d else 2*d
    assert sum(vals)==(1<<d)-bright,(d,r,sum(vals),bright)
    if r==d:
      assert {x for x,s in enumerate(vals) if s==0}=={0,(1<<d)-1}
    else:
      u=(1<<r)-1
      assert {x for x,s in enumerate(vals) if s==0}=={0,u,((1<<d)-1),((1<<d)-1)^u},(d,r)
print('VERIFY_OK exact_walsh_states=',n,'rank_formula=passed zero_survival_sites=passed')

try:
    import numpy as np
    from scipy.linalg import expm
except ImportError:
    print('OPTIONAL_NUMERICAL_CHECK_SKIPPED scipy_or_numpy_missing')
else:
    cases=[(2,1,1.1,0.7,120),(3,1,1.4,0.9,250),(3,3,.9,1.3,200),
           (4,2,1.1,0.7,600),(4,4,1.5,0.5,400)]
    maxdiff=0.0
    for d,r,g0,g1,t in cases:
        N=1<<d; u=(1<<r)-1
        H=np.zeros((N,N),dtype=complex)
        for x in range(N):
            for j in range(d): H[x,x^(1<<j)]=1
        H[0,0]-=1j*g0
        H[u,u]-=1j*g1
        U=expm(-1j*t*H)
        for x in range(N):
            got=float(np.vdot(U[:,x],U[:,x]).real)
            predicted=float(formula(d,r,x))
            maxdiff=max(maxdiff,abs(got-predicted))
    print('NUMERIC_TIME_CHECK cases=',len(cases),'maximum_absolute_difference=',maxdiff)
    assert maxdiff < 0.003
