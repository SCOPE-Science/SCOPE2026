#!/usr/bin/env python3
"""Rigorous finite proof certificate for the first Musin power-abscissa contact jump.
All interval endpoints are Decimal numbers rounded outward. Primitive ln/exp
are correctly rounded by Python decimal to 110 significant figures, with
additional 10^-60 absolute outward padding, much exceeding any final ulp.
"""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, localcontext
from math import isqrt

PREC=110
DOWN=Context(prec=PREC,rounding=ROUND_FLOOR)
UP=Context(prec=PREC,rounding=ROUND_CEILING)
PAD=D('1e-60')

def iv_rat(a,b=1):
    a,b=int(a),int(b)
    assert b>0 and a>=0
    return DOWN.divide(D(a),D(b)), UP.divide(D(a),D(b))
def add(a,b):return DOWN.add(a[0],b[0]),UP.add(a[1],b[1])
def sub(a,b):return DOWN.subtract(a[0],b[1]),UP.subtract(a[1],b[0])
def mul(a,b):
    assert a[0]>=0 and b[0]>=0
    return DOWN.multiply(a[0],b[0]),UP.multiply(a[1],b[1])
def div(a,b):
    assert b[0]>0
    return DOWN.divide(a[0],b[1]),UP.divide(a[1],b[0])
def ilog(a):
    assert a[0]>0
    with localcontext(Context(prec=PREC)):
        lo=a[0].ln()
        hi=a[1].ln()
    return DOWN.subtract(lo,PAD),UP.add(hi,PAD)
def iexp(a):
    with localcontext(Context(prec=PREC)):
        lo=a[0].exp()
        hi=a[1].exp()
    return DOWN.subtract(lo,PAD),UP.add(hi,PAD)
def power(a,k):
    assert a[0]>=0 and k>=0
    return DOWN.power(a[0],k),UP.power(a[1],k)
def intersects(a,b):return not (a[1]<b[0] or b[1]<a[0])

def primes_upto(N):
    mark=[True]*(N+1)
    mark[:2]=[False,False]
    for p in range(2,isqrt(N)+1):
        if mark[p]:
            for j in range(p*p,N+1,p):mark[j]=False
    return [p for p in range(2,N+1) if mark[p]]

primes=primes_upto(167)
assert primes[-1]==167
threshold=None

def critical(p,j):
    S=sum(p**a for a in range(1,j+1))
    return div(ilog(iv_rat(S+1,S)),ilog(iv_rat(p)))
threshold=critical(167,1)
events=[]
for p in primes[:-1]:
    for j in range(1,30):
        C=critical(p,j)
        if C[1]<threshold[0]:break
        assert C[0]>threshold[1],('critical value too close to threshold',p,j)
        events.append((C,p,j))
    else:raise AssertionError('j limit')
# Sort by midpoints; then certify pairwise separation of adjacent intervals.
events.sort(key=lambda t:(t[0][0]+t[0][1])/2,reverse=True)
assert len(events)==56
for a,b in zip(events,events[1:]):
    assert a[0][0]>b[0][1],('overlapping thresholds',a,b)
assert min(a[0][0]-b[0][1] for a,b in zip(events,events[1:])) > D('0.000001')

# Classical CA enumeration: each event increases one prime exponent by exactly one.
# At a single critical value both the preceding and following products are retained.
N=1
factors={}
record=[]
for index,(_,p,j) in enumerate(events,1):
    assert factors.get(p,0)+1==j
    factors[p]=j
    N*=p
    if index>=9:
        sigma=1
        for q,e in factors.items():
            sigma*= (q**(e+1)-1)//(q-1)
        rho=iv_rat(sigma,N)
        L=ilog(iv_rat(N))
        U=ilog(L)
        X=iexp(power(U,2))
        record.append({'index':index,'n':N,'sigma':sigma,'rho':rho,'u':U,'x':X})
    if index==9:assert N==55440
    if index==10:assert N==720720
    if index==15:assert N==6983776800
    if index==16:assert N==160626866400
    if index==51:assert N<10**65
    if index==52:assert N>10**65
assert record[0]['index']==9
assert sum(1 for z in record if z['index'] >= 10 and z['n'] < 10**65)==42
assert all(z['n'] >= 10**65 for z in record if z['index'] >= 52)

# A CA number with largest prime >=167 contains 167#, > 10^65.
primorial=1
for p in primes: primorial*=p
assert primorial>10**65

# Exclude all n >=10^65: log n >= 65 log 10 > 149 > exp 5,
# so u=log log n > 5. Since e^gamma <1.8 and Robin's bound
# rho <= e^gamma u + 0.6483/u, the reference secant J_17 is
# bounded by B(u)=(1.8u+0.6483/u)^17/(exp(u^2)-exp(u_*^2)).
# B is strictly decreasing on u>=5: log numerator derivative <17/u;
# log denominator derivative >2u; 17/u <2u there.
ref=record[0]
u5=iv_rat(5)
rho5=add(mul(iv_rat(18,10),u5),div(iv_rat(6483,10000),u5))
den5=sub(iexp(iv_rat(25)),ref['x'])
B5=div(power(rho5,17),den5)
assert B5[1] < D(300000),B5

# Exact rational numerator, certified transcendental denominator.
k=17
RHO0=power(ref['rho'],k)
X0=ref['x']
secs=[]
for v in record[1:]:
    numerator=sub(power(v['rho'],k),RHO0)
    denominator=sub(v['x'],X0)
    assert numerator[0]>0 and denominator[0]>0
    J=div(numerator,denominator)
    secs.append((v['index'],v['n'],J))
choice=next(q for q in secs if q[0]==15)
assert choice[2][0]>D('173600000')
for i,n,J in secs:
    if i!=15:
        assert choice[2][0]>J[1],(i,J,choice)

# Source's k=16 is 720720, independently recover it from the same exact intervals.
sec16=[]
for v in record[1:]:
    num=sub(power(v['rho'],16),power(ref['rho'],16))
    den=sub(v['x'],X0)
    sec16.append((v['index'],div(num,den)))
ref16=next(q[1] for q in sec16 if q[0]==10)
assert all(ref16[0]>q[1][1] for q in sec16 if q[0]!=10)
# An identical u>=5 bound at k=16 is lower than J_16(720720).
B16=div(power(rho5,16),den5)
assert B16[1]<ref16[0]

# Additional finite-horizon normalization against Musin's published k=32 index 27.
sec32=[]
for v in record[1:]:
    num=sub(power(v['rho'],32),power(ref['rho'],32))
    sec32.append((v['index'],div(num,sub(v['x'],X0))))
best32=max(sec32,key=lambda t:t[1][0])
assert best32[0]==27
assert all(best32[1][0]>q[1][1] for q in sec32 if q[0]!=27)

# Quantitative certificate margins, including exclusion against all later CA numbers.
second=max(J[1] for i,n,J in secs if i!=15)
assert choice[2][0] > second*D('1.016')
print('VERIFY_OK',
      'events_above_F167=56',
      'CA_candidates=42',
      'last_below_1e65=51',
      'first_above_1e65=52',
      'first_jump_level=17',
      'm16=720720',
      'm17=6983776800',
      'CA_index17=15',
      'gap_lower_pct=',DOWN.multiply(D(100),DOWN.subtract(D(1),UP.divide(second,choice[2][0]))),
      'tail_B17_upper=',B5[1],
      'finite_k32_index=27',
      'critically_ordered=yes')
