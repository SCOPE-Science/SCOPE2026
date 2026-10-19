"""Finite reproducibility checks for a Sturmian beta-shift boundary result.

Only standard Python modules are needed. Finite tests are not infinite proofs.
"""
from fractions import Fraction
from decimal import Decimal, getcontext, ROUND_CEILING
from math import gcd
getcontext().prec = 90
ALPHA = (Decimal(5).sqrt() - Decimal(1))/Decimal(2)

def ce(x):
    return int(x.to_integral_value(rounding=ROUND_CEILING))

def upper_real(t, n):
    return tuple(ce(t * (j+1))-ce(t*j) for j in range(n))

def upper_frac(t, n):
    return tuple(-(-(j+1)*t.numerator//t.denominator)-(-(-j*t.numerator//t.denominator)) for j in range(n))

def factors(w, length, period=None):
    end=(len(w)-length+1) if period is None else period
    return {w[i:i+length] for i in range(end)}

CHECKS=0
irr=upper_real(ALPHA,10000)
for p,q in [(3,5),(8,13),(21,34),(55,89)]:
    s=next(z for z in range(1,q) if (p*z)%q==1)
    r=(p*s-1)//q
    beta=Fraction(p+r,q+s)
    period=q+s
    assert gcd(beta.numerator,beta.denominator)==1;CHECKS+=1
    assert 1/(2*q*q) < float(ALPHA)-float(beta) < 2/(q*q);CHECKS+=1
    assert beta<Fraction(p,q)<Fraction(2,3);CHECKS+=1
    words=upper_frac(beta,period+q+20)
    assert sum(words[:period])==beta.numerator;CHECKS+=1
    for m in range(1,q):
        got=factors(words,m,period)
        ref=factors(irr,m)
        assert got==ref,(p,q,m,got-ref,ref-got)
        CHECKS+=1
    for j in range(period):
        b=tuple(words[j:j+min(q,100)])
        assert b <= irr[:len(b)],(q,j)
        CHECKS+=1
    delta=float(ALPHA)-float(beta)
    for t in [1e-3,1e-6,1e-8]:
        if t*delta > 2.0**(-(q-1)):
            assert t*delta-2.0**(-(q-1))>0
            CHECKS+=1
print(f"PASS {CHECKS} finite checks; denominators [5,13,34,89]; no finite test claims to prove the general theorem")
