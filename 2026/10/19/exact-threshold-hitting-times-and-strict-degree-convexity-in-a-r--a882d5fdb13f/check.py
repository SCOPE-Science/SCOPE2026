"""Exact finite-state checks for an immigration-death process with full resetting.
All computations are rational and independent of asymptotic arguments.
Run: python check.py
"""
from fractions import Fraction as F
from math import factorial

def solve(a, b):
    n=len(b)
    a=[row[:] + [bb] for row,bb in zip(a,b)]
    for i in range(n):
        piv=next(j for j in range(i,n) if a[j][i] != 0)
        a[i],a[piv]=a[piv],a[i]
        d=a[i][i]
        a[i]=[x/d for x in a[i]]
        for j in range(n):
            if j == i: continue
            f=a[j][i]
            if f: a[j]=[x-f*y for x,y in zip(a[j],a[i])]
    return [row[-1] for row in a]

def generator(n, alpha, rate):
    # Q on transient degree states 0,...,n-1. Catastrophe events at 0
    # are ignored (self-resets), while hits at n leave transient set.
    q=[[F(0) for _ in range(n)] for _ in range(n)]
    for k in range(n):
        if k+1<n: q[k][k+1]+=alpha
        q[k][k]-=alpha
        if k>0:
            q[k][k-1]+=k*rate
            q[k][0]+=rate
            q[k][k]-=(k+1)*rate
    return q

def poly(n, alpha, rate, s=F(0)):
    # Discounted no-reset first passage f(0)=1/P_n(s).
    if n==0:return F(1)
    a,b=F(1),F(1)+(s+rate)/alpha
    for k in range(1,n):
        a,b=b, ((alpha+(k+1)*rate+s)*b-k*rate*a)/alpha
    return b

def formula_mean(n, alpha, rate):
    return (poly(n,alpha,rate)-1)/rate

def formula_laplace(n, alpha, rate, s):
    return (s+rate)/(s*poly(n,alpha,rate,s)+rate)

count=0
for alpha in (F(1),F(2),F(3,2),F(7,3)):
 for rate in (F(1,5),F(1,2),F(3,2)):
  old=F(0)
  for n in range(1,12):
   q=generator(n,alpha,rate)
   A=[[-q[i][j] for j in range(n)] for i in range(n)]
   empirical=solve(A,[F(1)]*n)[0]
   exact=formula_mean(n,alpha,rate)
   assert empirical==exact,(n,alpha,rate,empirical,exact)
   assert exact==F(n,1)/alpha*(1+rate*old)
   old=exact
   count+=2
  for s in (F(1,3),F(1),F(5,2)):
   for n in range(1,9):
    q=generator(n,alpha,rate)
    A=[[(s if i==j else 0)-q[i][j] for j in range(n)] for i in range(n)]
    # f_n(s)=E[e^{-s tau_n}]; absorption via transition n-1->n at alpha
    b=[F(0)]*(n-1)+[alpha]
    empirical=solve(A,b)[0]
    exact=formula_laplace(n,alpha,rate,s)
    assert empirical==exact,(n,alpha,rate,s,empirical,exact)
    count+=1
  means=[F(0)]+[formula_mean(n,alpha,rate) for n in range(1,61)]
  for n in range(1,60):
   assert means[n+1]-2*means[n]+means[n-1]>0
   count+=1
  for n in (20,40,60):
   p=poly(n,alpha,rate)
   expected=sum((F(factorial(n),factorial(n-j))*(rate/alpha)**j for j in range(n+1)),F(0))
   assert p==expected
   count+=1
print('PASS',count,'exact generator, resolvent, strict-curvature and polynomial checks')
