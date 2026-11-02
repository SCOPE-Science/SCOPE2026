"""Finite algebraic and numerical tests for the discrete-IFR mean-tail bound.
The infinite-support theorem is proved in RESULT.md; the tests are diagnostic only.
"""
from fractions import Fraction as Q
from decimal import Decimal, getcontext
from math import log, exp, isfinite
import random

getcontext().prec=70
count=0

def check(cond, desc):
    global count
    assert cond, desc
    count +=1

def poly(x):return x*x*x-x-1
lo=Q(331,250);hi=Q(4,3)
check(poly(lo)<0,'lower isolating bracket')
check(poly(hi)>0,'upper isolating bracket')
for _ in range(180):
    mid=(lo+hi)/2
    if poly(mid)<0:lo=mid
    else:hi=mid
    check(poly(lo)<0 and poly(hi)>0,'root enclosure')
a=(Decimal(lo.numerator)/Decimal(lo.denominator)+Decimal(hi.numerator)/Decimal(hi.denominator))/2
s=a**(-4)
check(abs(a*a*a-a-1)<Decimal('1e-52'),'plastic constant root')
check(abs(s-(a-1))<Decimal('1e-50'),'constant identity')
check(Q(55,9)<2*(Q(331,250)**2+Q(331,250)),'H2(3) bound')
for x in [Q(3),Q(6)]:
    y=1+1/x
    h=x+sum((y**j for j in range(1,5)),Q(0))
    check(h<4*(Q(331,250)**2+Q(331,250)),'H4 endpoint bound')
check(Q(402,581)>Q(175,256),'integral-bound rational inequality')
check(6*(4*a.ln()-1)>1-s,'true integral comparison')

r=a/(1+a);b=1-1/a;t=r*r
check(abs(t-s)<Decimal('1e-51'),'tail equals sharp bound')
check(abs(r-r*r-t/a)<Decimal('1e-51'),'adjacent masses equal')
check(abs(t*a-(1-r))<Decimal('1e-51'),'zero mean')
check(Decimal(0)<b<r<1,'IFR ratio chain')
check(abs((1-r)+(r-t)+t-1)<Decimal('1e-51'),'total mass')

# Check explicit probability mass through a truncation plus exact geometric remainder.
for j in range(1,51):
    pj=(r-r*r)*b**(j-1)
    sj=t*b**(j-1)
    check(pj>=0 and abs(pj-(sj-sj*b))<Decimal('1e-50'),'geometric atom')

# For any x, F_s(x) >= sx; logarithmic tail sum calculated through geometric series.
ss=float(s)
def F(x):
    y=1+1/x
    # count j with 1-s*y**j >0; small correction avoids roundoff at transition
    n=max(0,int(log(1/ss)/log(y)))
    out=sum(max(0.,1-ss*y**j) for j in range(1,n+3))
    return out
for k in range(1,20001):
    x=exp(log(1)+(log(3000))*k/20000)
    check(F(x)>=(ss*x)-2e-8*max(1,ss*x),f'envelope test x={x}')
for x in [1,1.05,1.1,1.2,1.324717957,1.33,1.6,2,3,6,9,50,500,3000]:
    check(F(x)+1e-7>=ss*x,'selected envelope test')

# Empirical finite-support IFR laws. Build decreasing survival ratios and compute
# actual integrable laws; only cases satisfying the two hypotheses are assessed.
rng=random.Random(731129)
tests=0
for trial in range(9000):
    vals=sorted([rng.random() for _ in range(9)],reverse=True)
    # survivals indexed from -4 to +5; force upper endpoint survival 0.
    survival=[1.]
    for z in vals:survival.append(survival[-1]*z)
    survival.append(0.)
    # S(-4),...,S(5),S(6)=0; atoms at -4..5 from drops.
    mass=[survival[i]-survival[i+1] for i in range(len(survival)-1)]
    positions=list(range(-4,-4+len(mass)))
    mean=sum(j*p for j,p in zip(positions,mass))
    pm0=mass[positions.index(0)]
    pm1=mass[positions.index(1)]
    if mean>=-1e-13 and pm0>0 and pm1>=pm0-1e-13:
        tail=sum(p for j,p in zip(positions,mass) if j>=1)
        check(tail>=ss-1e-11,'finite IFR distribution')
        tests+=1
print('PASS:',count,'assertions; tested qualifying IFR laws:',tests)
print('plastic constant:',a)
print('sharp tail:',s)
print('sharp extremizer ratio:',b)
