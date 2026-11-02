#!/usr/bin/env python3
"""Exact rational interval certificate for the reciprocal-divisor range on [19/10,191/100].
No external dependencies. All inequalities use integers and Fractions, never floating point.
"""
from fractions import Fraction as F
from math import isqrt

SCALE=10**9
N=1024

def pow_bounds(n, a, b):
    """Enclose n^(-a/b) by integer power comparisons (n>=1, a,b>=1)."""
    if n==1: return F(1),F(1)
    t=n**a
    val=SCALE**b
    lo, hi=0,SCALE+1
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**b*t<=val:lo=mid
        else:hi=mid
    return F(lo,SCALE),F(lo+1,SCALE)

def zeta_bounds(a,b):
    if a<=b: raise ValueError('r<=1')
    low=high=F(0)
    for n in range(1,N+1):
        l,h=pow_bounds(n,a,b)
        low+=l;high+=h
    # Integral test for tail; n>N: integral_{N+1}^inf<=sum<=integral_N^inf
    tl,_=pow_bounds(N+1,a-b,b)
    _,th=pow_bounds(N,a-b,b)
    low+=tl*F(b,a-b)
    high+=th*F(b,a-b)
    return low,high

def imul(x,y):return (x[0]*y[0],x[1]*y[1])
def iadd(x,y):return x[0]+y[0],x[1]+y[1]
def isub(x,y):return x[0]-y[1],x[1]-y[0]
def idiv(x,y):
    assert y[0]>0
    return x[0]/y[1],x[1]/y[0]
def one_minus(x):return F(1)-x[1],F(1)-x[0]
def zeta_and_powers(a,b):
    u=pow_bounds(2,a,b)
    v=pow_bounds(3,a,b)
    w5=pow_bounds(5,a,b)
    w7=pow_bounds(7,a,b)
    w11=pow_bounds(11,a,b)
    z=zeta_bounds(a,b)
    W=imul(imul(z,one_minus(u)),one_minus(v))
    tail7=imul(imul(W,one_minus(w5)),one_minus(w7))
    tail11=imul(tail7,one_minus(w11))
    return dict(u=u,v=v,w5=w5,w7=w7,w11=w11,z=z,W=W,tail7=tail7,tail11=tail11)

def chk(label,lhs,rhs):
    gap=rhs[0]-lhs[1]
    assert gap>0,f'FAIL: {label}, gap={float(gap)}'
    print('PASS',label,'gap>', '%.9f'%float(gap))

a=zeta_and_powers(19,10)
b=zeta_and_powers(191,100)
for label,c in [('r=19/10',a),('r=191/100',b)]:
    for name in ['z','u','v','W','tail7','tail11']:
        lo,hi=c[name]
        print('INTERVAL',label,name,'%.10f < X < %.10f'%(float(lo),float(hi)))
print('N',N,'scale',SCALE)

# Monotone Euler tail: W(r) decreases; tail7(r) decreases. u,v decrease.
# Main gap: W(19/10) < 1+v(191/100).
chk('only gap after prime three',a['W'],iadd((F(1),F(1)),b['v']))
# Uniform no-prime >=5 gap: 1+7^-19/10 < tail7(191/100).
chk('prime seven is non-mighty',iadd((F(1),F(1)),a['w7']),b['tail7'])
chk('prime eleven is non-mighty',iadd((F(1),F(1)),a['w11']),b['tail11'])
# Gaps among positive powers of three have smaller multiplicative step than first:
three_increment=idiv(iadd(iadd((F(1),F(1)),a['v']),imul(a['v'],a['v'])),iadd((F(1),F(1)),a['v']))
chk('three higher powers connected',three_increment,b['W'])
# Analogous for two, all higher powers connected in each of the two bands.
two_increment=idiv(iadd(iadd((F(1),F(1)),a['u']),imul(a['u'],a['u'])),iadd((F(1),F(1)),a['u']))
chk('two lower powers connected',two_increment,b['W'])
higher3=idiv(b['W'],one_minus(imul(b['v'],b['v'])))
chk('two upper powers connected',two_increment,higher3)
# The three positive bands overlap and fill one single interval:
chk('upper prime-three meets low positive-two',iadd((F(1),F(1)),a['u']),idiv(b['W'],one_minus(b['v'])))
chk('positive-two bands meet',imul(iadd((F(1),F(1)),a['u']),iadd((F(1),F(1)),a['v'])),idiv(b['W'],one_minus(b['u'])))

# Recheck the finite exceptional range of Defant's consecutive-prime lemma.
# For primes above 396738 the cited published lemma uses Dusart's prime-gap bound.
limit=397000
sieve=bytearray(b'\x01')*(limit+1)
sieve[:2]=b'\x00\x00'
for j in range(2,isqrt(limit)+1):
    if sieve[j]:
        sieve[j*j:limit+1:j]=b'\x00'*(((limit-j*j)//j)+1)
primes=[j for j in range(2,limit+1) if sieve[j]]
count=0
for j in range(len(primes)-1):
    p=primes[j]
    if p>=396738:break
    if j+1 not in (1,2,4):
        assert primes[j+1]**2 < 2*p*p
        count+=1
print('PRIME_RATIO_OK',count,'finite consecutive-prime comparisons')

print('VERIFY_OK exact rational interval certificate for every real 1.9<=r<=1.91')
