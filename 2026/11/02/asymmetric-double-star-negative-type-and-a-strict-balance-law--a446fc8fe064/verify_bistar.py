"""Reproducible checks for the unweighted two-hub tree negative-type theorem.

Run: python verify_bistar.py
All experiments are finite checks; the universal proof is in RESULT.md.
Python 3.10+, standard library only.
"""
from fractions import Fraction
from itertools import product
from math import log, sqrt


def radial(m, n, p):
    a=2.0**p
    b=3.0**p - 1.0 - a*a/2.0
    return a*(1+1/m)-a*a/2, a*(1+1/n)-a*a/2, b

def critical(m, n):
    lo=1.0
    hi=min(log(2+2/m,2), log(2+2/n,2))
    for _ in range(95):
        p=(lo+hi)/2
        u,v,b=radial(m,n,p)
        if u*v-b*b>0:lo=p
        else:hi=p
    return (lo+hi)/2

def exact_test():
    count=0
    for m in range(2,7):
      for n in range(2,7):
       N=m+n+2
       for p in (1,2):
        A=Fraction(2**p);C=Fraction(3**p)
        for z in range(31):
         xs=[Fraction(((i+1)*(z+3)+(i*i+z*z)%11)%17-8,5) for i in range(N-2)]
         u=Fraction(((z+1)*7)%13-6,3)
         v= -sum(xs)-u
         vec=xs[:m]+xs[m:]+[u,v]
         dist=lambda i,j: (0 if i==j else
              (2 if (i<m and j<m) or (m<=i<m+n and m<=j<m+n) else
               1 if ((i<m and j==m+n) or (j<m and i==m+n) or
                     (m<=i<m+n and j==m+n+1) or (m<=j<m+n and i==m+n+1) or
                     set((i,j))==set((m+n,m+n+1))) else
               2 if ((i<m and j==m+n+1) or (j<m and i==m+n+1) or
                     (m<=i<m+n and j==m+n) or (m<=j<m+n and i==m+n)) else 3))
         Q=sum(vec[i]*vec[j]*dist(i,j)**p for i in range(N) for j in range(N) if i!=j)
         X=sum(xs[:m]);Y=sum(xs[m:]);
         fluctA=sum((q-X/m)**2 for q in xs[:m]);fluctB=sum((q-Y/n)**2 for q in xs[m:])
         U=A*(1+Fraction(1,m))-A*A/2
         V=A*(1+Fraction(1,n))-A*A/2
         B=C-1-A*A/2
         center=u+A*X/2-(A-2)*Y/2
         rhs=-(A*fluctA+A*fluctB)-2*center**2-U*X**2-V*Y**2+2*B*X*Y
         assert Q==rhs,(m,n,p,z,Q,rhs)
         count+=1
    print('EXACT_ZERO_SUM_QUADRATIC_IDENTITY_OK',count)

def root_test():
    count=0
    for m in range(2,26):
      for n in range(2,26):
       p=critical(m,n)
       pm=min(log(2+2/m,2),log(2+2/n,2))
       pb=log(2+2/(m+n),2)
       assert pb<p<pm
       u,v,b=radial(m,n,p)
       assert abs(u*v-b*b)<2e-12
       assert u>0 and v>0 and b>0
       for pp,sign in ((1,(1)),((p+1)/2,(1)),((p+pm)/2,(-1))):
        a,b_,c=radial(m,n,pp)
        if sign>0: assert a*b_-c*c >-1e-12
        else: assert a*b_-c*c <1e-12
       count+=1
    print('CRITICAL_ROOT_INTERVAL_AND_RANK_OK',count)

def balance_test():
    tests=0
    for total in range(4,81):
      vals=[critical(m,total-m) for m in range(2,total//2+1)]
      assert all(vals[i+1]>vals[i] for i in range(len(vals)-1))
      tests+=len(vals)
    print('FIXED_LEAF_BUDGET_BALANCE_DIAGNOSTICS_OK',tests)

def scaling_test():
    L=log(2);J=3*log(3)-4*L
    for rho in (0.5,1.0,2.0,4.0):
      target=(2/rho)/(L*(1+1/rho)+sqrt(L*L*(1-1/rho)**2+J*J/rho))
      for n in (300,1200,4000):
       m=int(rho*n); p=critical(m,n)
       # For finite n the relative correction is O(1/n).
       assert abs(n*(p-1)-target)<0.012,(rho,n,n*(p-1),target)
    for m in (2,3,7):
      for n in (1200,4000,16000):
       val=n*(critical(m,n)-1)
       assert abs(val-1/L)<0.024,(m,n,val)
    print('ASYMMETRIC_LARGE_BRANCHING_LIMIT_DIAGNOSTICS_OK')

if __name__=='__main__':
 exact_test();root_test();balance_test();scaling_test()
 print('ALL_UNBALANCED_DOUBLE_STAR_NEGATIVE_TYPE_CHECKS_OK')
