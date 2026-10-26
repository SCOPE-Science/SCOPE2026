"""Finite and interval-arithmetic checks for the stalled nearest-neighbor substitution.
Run: python3 verify.py. Uses only Python's standard library.
Finite diagnostics supplement the analytic theorem; they are not an infinite proof.
"""
from fractions import Fraction
from math import log, exp, comb
from decimal import Decimal, localcontext

checks = 0

def verify(test, description):
    global checks
    if not test:
        raise AssertionError(description)
    checks += 1


def P(m, s):
    # Positive at s=0+, negative at s=1-. Unique root proved separately.
    lam = s + 1/s
    return (1-s)*lam**(m-1)-s*s


def bracket(m, bits=150):
    lo, hi = Fraction(1, 2**(bits+2)), Fraction(2**(bits+2)-1, 2**(bits+2))
    verify(P(m,lo)>0 and P(m,hi)<0, 'root end signs')
    for _ in range(bits):
        mid=(lo+hi)/2
        if P(m,mid)>0: lo=mid
        else: hi=mid
    verify(P(m,lo)>0 and P(m,hi)<0,'root bracket signs')
    return lo,hi


def lengths(m, depth):
    # Exact counts from applying substitutions to finite seeds, in parallel.
    a=[1]*(m+depth+4)
    for _ in range(depth):
        a=[a[i+1] if i<m else a[0]+a[i-1]+a[i+1]
           for i in range(len(a)-1)]
    return a[0]

prev_lam=None
with localcontext() as ctx:
    ctx.prec=80
    for m in range(1,21):
        low, high=bracket(m)
        mid=(low+high)/2
        s=Decimal(mid.numerator)/Decimal(mid.denominator)
        lam=s+1/s
        verify(lam>2,'positive spectral gap')
        verify(1-s <= Decimal(2)**(1-m),'asymptotic elementary bound')
        if prev_lam is not None:
            verify(lam<prev_lam, 'strictly decreasing Perron root')
        prev_lam=lam
        c=1/(lam-2)
        def ell(n):
            if n is None: return c
            return lam**n if n<m else c+(lam**m-c)*s**(n-m)
        for n in range(m+35):
            rhs=ell(n+1) if n<m else 1+ell(n-1)+ell(n+1)
            verify(abs(rhs-lam*ell(n))<Decimal('1e-22')*max(1,abs(rhs)),
                   'eigenfunction recurrence m=%d n=%d'%(m,n))
        verify(abs(1+2*c-lam*c)<Decimal('1e-22')*lam*c, 'boundary at infinity')
        verify(min(ell(n) for n in range(m+35))>0,'positive eigenvector')

verify(lengths(2,34)==17598130109,'published 34-step count')
verify(lengths(4,600)<2**600,'600-step finite comparison')
verify(lengths(4,700)>2**700,'700-step finite comparison')
verify(lengths(7,1000)<2**1000,'1000-step finite comparison')
# Basic recursion sanity via direct word expansion (small sizes).
def sub(m,word):
    out=[]
    for j in word:
        if j<m: out.append(j+1)
        else: out.extend((0,j-1,j+1))
    return out
for m in range(1,7):
    word=[0]
    for depth in range(1,8):
        word=sub(m,word)
        verify(len(word)==lengths(m,depth),'direct expansion m=%d n=%d'%(m,depth))

# Exact rational certificate that the formerly misleading 1000-step observation
# must eventually reverse by time 72000 (without generating a huge superword).
s_upper=Fraction(9848553,10000000)
lam_lower=Fraction(200023288,100000000)
verify(P(7,s_upper)<0,'rational root upper bound')
verify(s_upper+1/s_upper > lam_lower, 'rational Perron lower bound')
verify(1/(lam_lower-2) < 4300, 'Perron order-unit upper bound')
x=Fraction(11644,100000000)  # lambda_lower / 2 = 1 + x
verify(sum(comb(72000,j)*x**j for j in range(16)) > 4300,
       'binomial lower certificate for the 72000-step reversal')

s7=float(sum(bracket(7))/2)
print('CHECKS_PASSED', checks)
print('lambda_7',repr(s7+1/s7))
print('radix_7_1000_root',repr(exp(log(lengths(7,1000))/1000)))
