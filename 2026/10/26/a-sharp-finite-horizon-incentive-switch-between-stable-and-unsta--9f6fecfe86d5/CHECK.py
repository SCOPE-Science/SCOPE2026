"""Exact and numerical verification of a two-period scalar incentive theorem.

Only Python standard library. Algebraic proof and completeness arguments
are provided separately in RESULT.md; tests do not replace proofs.
"""
from fractions import Fraction as F
from random import Random
from decimal import Decimal, localcontext

rng = Random(2604277701)
algebra = 0
rational_minima = 0
phase_checks = 0

for _ in range(18000):
    A = F(rng.randint(1, 30), rng.randint(1, 18))
    e = F(rng.randint(1, 50), rng.randint(1, 18))
    a = F(rng.randint(-70, 70), rng.randint(1, 20))
    y = a - A / 2
    g = ((a-A)**2+e) * (1+a*a)
    constant = A**4/16 + A*A*(e+1)/4 + e
    shifted = y**4 + (1+e-A*A/2)*y*y + A*(e-1)*y + constant
    assert g == shifted
    pp = 2*a**3 - 3*A*a*a + (A*A+1+e)*a - A
    derivative = 2*(a-A)*(1+a*a)+2*a*((a-A)**2+e)
    assert derivative == 2*pp
    assert g - (((A-a)-A)**2+e)*(1+(A-a)**2) == A*(e-1)*(2*a-A)
    algebra += 3

for tnum in range(2,20):
    for tden in range(1,tnum):
        t=F(tnum,tden)
        A=t+1/t
        amin=1/t
        amax=t
        assert amin+amax==A and amin*amax==1
        assert ((amin-A)**2+1)*(1+amin**2)==A*A
        assert ((amax-A)**2+1)*(1+amax**2)==A*A
        assert (1+A*A/4)**2-A*A==(A*A-4)**2/16
        assert amin<1<amax
        rational_minima+=5

assert F(2)*((F(1,2)-F(5,2))**2+1)*(1+F(1,2)**2)==F(25,2)
assert F(2)*((F(2)-F(5,2))**2+1)*(1+F(2)**2)==F(25,2)
assert F(1681,128)-F(25,2)==F(81,128)

with localcontext() as ctx:
    ctx.prec=65
    values_A=['0.125','0.5','1','1.25','1.5','1.75','1.95','2','2.05','2.5','3','4','8']
    values_e=['0.0625','0.25','0.5','0.75','0.9375','1','1.0625','1.25','2','4','8']
    for A_s in values_A:
        for e_s in values_e:
            A=Decimal(A_s); e=Decimal(e_s)
            if e==1:
                if A<=2: roots=[A/2]
                else:
                    d=(A*A-4).sqrt()
                    roots=[(A-d)/2,(A+d)/2]
            else:
                lo,hi=(Decimal(0),A/2) if e>1 else (A/2,A)
                def P(a): return 2*a*a*a-3*A*a*a+(A*A+1+e)*a-A
                assert P(lo)<0<P(hi)
                for _ in range(230):
                    mid=(lo+hi)/2
                    if P(mid)>0: hi=mid
                    else: lo=mid
                roots=[(lo+hi)/2]
            for a in roots:
                assert Decimal(0)<a<A
            if A<=1:
                status='stable'
            elif A<2:
                edge=(A-1)*(3-A)
                status='stable' if e>edge else 'unstable' if e<edge else 'neutral'
            elif A==2:
                status='stable' if e>1 else 'unstable' if e<1 else 'neutral'
            else:
                status='stable' if e>1 else 'unstable' if e<1 else 'both'
            if status=='stable': assert len(roots)==1 and roots[0]<1
            elif status=='unstable': assert len(roots)==1 and roots[0]>1
            elif status=='neutral': assert len(roots)==1 and abs(roots[0]-1)<Decimal('1e-55')
            else: assert len(roots)==2 and roots[0]<1<roots[1]
            phase_checks+=1

print('EXACT_POLYNOMIAL_IDENTITIES:',algebra)
print('EXACT_RATIONAL_BRANCH_IDENTITIES:',rational_minima)
print('HIGH_PRECISION_PHASE_CASES:',phase_checks)
print('EXACT_RATIONAL_WITNESS: A=5/2, eta=1, a=1/2 or 2, leader cost=25/2')
print('RESULT: PASS')
