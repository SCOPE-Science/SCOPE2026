"""Exact checks for two-radius component covariance in uniform interval samples.

Uses only standard-library rational arithmetic. Finite checks supplement the proof.
"""
from fractions import Fraction as F
from math import comb, exp

checks=0

def verify(statement):
    global checks
    checks += 1
    assert statement

def direct(n,r,s):
    # Sum over n-1 labelled internal spacing indicators; exact simplex survival.
    p_r=(1-r)**n
    p_s=(1-s)**n
    joint=(max(F(0),F(1)-r-s))**n
    m=n-1
    return m*(p_s-p_r*p_s)+m*(m-1)*(joint-p_r*p_s)

def compact(n,r,s):
    return (n-1)*(1-s)**n*(1-(n-1)*(1-r)**n)+(n-1)*(n-2)*max(F(0),F(1)-r-s)**n

for n in range(3,27):
    for a in range(1,13):
        for b in range(a,14):
            r,s=F(a,29),F(b,29)
            v=direct(n,r,s)
            verify(v==compact(n,r,s))
            verify((v>0)==(1-(n-1)*(1-r)**n+(n-2)*(max(F(0),F(1)-r-s)/(1-s))**n>0))
            if r==s:
                verify(v>0)
            if (n-1)*(1-r)**n < 1:
                verify(v>0)
            if (n-1)*(1-r)**n > 1 and s>=1-r:
                verify(v<0)
            if (n-1)*(1-r)**n == 1 and s>=1-r:
                verify(v==0)

n,r,s=3,F(2,25),F(7,10)
verify(direct(n,r,s)==F(-17192,1953125))

# For arbitrary fixed first radius, normalized covariance decreases on the
# meaningful radius range. Rational checks do not prove this in general.
for n in range(3,35):
    for a in range(1,14):
        r=F(a,47)
        vals=[]
        for b in range(a,46):
            s=F(b,47)
            normalized=compact(n,r,s)/((n-1)*(1-s)**n)
            vals.append(normalized)
        for x,y in zip(vals,vals[1:]):
            verify(x>=y)

# In the 1/n scaling, both the exact and asymptotic covariances exhibit
# positive and negative values on either side of d=(exp(c)-1)/c.
for c,d in [(0.5,0.6),(0.5,1.5),(1,1.5),(1,2.5),(2,3),(2,4)]:
    limit=exp(-d)*(1-exp(-c)*(1+c*d))
    for n in [1000,4000]:
        # No sign cancellation requirement at exact transition points.
        got=float(compact(n,F(str(c))/n,F(str(d))/n))/n
        verify(abs(got-limit)<0.012)
        verify((got>0)==(limit>0))

if __name__=='__main__':
    print(f'VERIFY_OK exact_or_asymptotic_assertions={checks}')
