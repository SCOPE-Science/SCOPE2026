#!/usr/bin/env python3
"""Exact-rational finite certificate for the cubic alternating divisor range."""
from fractions import Fraction as Q
from itertools import product

SMALL=(2,3,5,7)
ZETA_N=20000
SCALE=10**15
partial_floor=sum(SCALE//(n**3) for n in range(1,ZETA_N+1))
zeta_lo=Q(partial_floor,SCALE)
zeta_hi=Q(partial_floor+ZETA_N,SCALE)+Q(1,2*ZETA_N**2)
prefix=Q(1)
for p in SMALL:
    prefix*=1-Q(1,p**3)
C_low=Q(99819,100000)
C_high=Q(998193,1000000)
assert C_low<1/(prefix*zeta_hi)<=1/(prefix*zeta_lo)<C_high
assert zeta_lo<Q(12020570,10000000) and zeta_hi>Q(12020569,10000000)

# Exact finite conditions for the beginning of the infinite prime tail.
primes=(2,3,5,7,11,13,17,19,23,29)
primorial_factor=Q(1)
for p in primes:
    a=1-Q(1,p**3)
    primorial_factor*=a
    if p>=11:
        assert a*primorial_factor>1/zeta_lo,(p,'tail-condition')
# For all later primes, Nagura's theorem gives q<6p/5 for p>=29;
# then v=q^{-3}>(125/216)u, u=p^{-3}<17/108, so 2v-v*v>u.
assert Q(1,29**3)<Q(17,108)

local2={
    'absent':(Q(1),Q(1)),
    'one':(Q(7,8),Q(7,8)),
    'two':(Q(57,64),Q(57,64)),
    'higher':(Q(455,512),Q(3641,4096)),
}
for p in (3,5,7):
    a=1-Q(1,p**3)
    b=a+Q(1,p**6)
    assert a<b

rows=[]
for tag,(small_lo,small_hi) in local2.items():
    for bits in product((0,1),repeat=3):
        lo,hi=small_lo,small_hi
        for p,bit in zip((3,5,7),bits):
            if bit:
                lo*=1-Q(1,p**3)
                hi*=1-Q(1,p**3)+Q(1,p**6)
        assert C_high*hi<lo,(tag,bits,'shared-point')
        rows.append(dict(tag=tag,bits=''.join(str(p) for p,b in zip((3,5,7),bits) if b) or '-',lo=lo,hi=hi))
assert len(rows)==32
rows.sort(key=lambda r:r['lo'])
components=[]
comparisons=[]
for r in rows:
    if not components:
        components.append(dict(lo=r['lo'],hi=r['hi'],members=[r]))
        continue
    last=components[-1]
    if C_high*r['lo']<=last['hi']:
        comparisons.append('overlap')
        last['hi']=max(last['hi'],r['hi'])
        last['members'].append(r)
    else:
        assert C_low*r['lo']>last['hi'],(r,last,'ambiguous-comparison')
        comparisons.append('gap')
        components.append(dict(lo=r['lo'],hi=r['hi'],members=[r]))
assert len(components)==19
assert comparisons.count('gap')==18
assert comparisons.count('overlap')==13
assert components[0]['lo']==prefix
assert components[-1]['hi']==Q(1)
for i,c in enumerate(components):
    print(f'{i+1:02d} lower=C*({c["lo"]}) upper=({c["hi"]}) members={len(c["members"])}')
print('CERTIFICATE_OK', 'tail_primes',len(primes)-4,'head_classes',len(rows), 'components',len(components), 'gaps',comparisons.count('gap'),'overlaps',comparisons.count('overlap'),'zeta_N',ZETA_N)
