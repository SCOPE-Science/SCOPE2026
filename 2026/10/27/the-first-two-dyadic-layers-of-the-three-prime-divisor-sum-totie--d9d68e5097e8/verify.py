"""Exact-rational checks for the small-dyadic-layer sigma/phi classification."""
from fractions import Fraction

def primes(n):
    return [x for x in range(2,n+1) if x>1 and all(x%d for d in range(2,int(x**.5)+1))]

def H(p,t):
    assert t>=1
    return Fraction(p*p,(p-1)**2)*(1-Fraction(1,p**(t+1)))

def Hinf(p): return Fraction(p*p,(p-1)**2)

W1, W2 = Fraction(4,3), Fraction(8,7)
# Prime-size sieve is complete: p in [11,13] for first shell, and p in [17,31] for second.
assert H(7,1)==W1 and Hinf(13)*Hinf(17)<W1
assert H(13,1)>W2 and Hinf(31)*Hinf(37)<W2
assert Hinf(11)*Hinf(23)<W1
# For a=2, any q>=167 fails the upper sieve.
assert Hinf(17)*Hinf(167)<W2
assert Hinf(19)*Hinf(83)<W2
assert Hinf(23)*Hinf(47)<W2
assert Hinf(29)*Hinf(37)<W2

allowed1=[]
for p in primes(166):
    for q in primes(166):
        if p>=q:continue
        if H(p,1)*H(q,1)<=W1<Hinf(p)*Hinf(q):
            allowed1.append((p,q))
assert allowed1==[(11,19)],allowed1
assert H(11,1)*H(13,1)>W1
assert H(11,1)*H(17,1)>W1
assert H(11,1)*H(19,1)==W1

allowed2=[]
for p in primes(166):
    for q in primes(166):
        if p>=q:continue
        if H(p,1)*H(q,1)<=W2<Hinf(p)*Hinf(q):
            allowed2.append((p,q))
expected2=[(17,q) for q in [127,131,137,139,149,151,157,163]]+[(19,q) for q in [71,73,79]]+[(23,43),(29,31)]
assert allowed2==expected2,(allowed2,expected2)
seed2=[(17,127),(19,71),(23,43),(29,31)]
for p,q in seed2:
    assert H(p,1)*H(q,1)==W2,(p,q)
for p,q in set(allowed2)-set(seed2)-{(17,163),(19,79)}:
    assert H(p,1)*Hinf(q)<W2<H(p,2)*H(q,1),(p,q)
for p,q,d in [(17,163,16),(19,79,18)]:
    assert H(p,2)*Hinf(q)<W2,('small b',p,q)
    assert pow(q,d,p)==1 and all(pow(q,r,p)!=1 for r in range(1,d))
    assert H(p,3)*H(q,d-1)>W2,('large b',p,q)

# Exact divisor-sum ratio confirmations for all five solutions.
solutions=[(1,11,19),(2,17,127),(2,19,71),(2,23,43),(2,29,31)]
ns=[]
for a,p,q in solutions:
    n=2**a*p*q
    sig=(2**(a+1)-1)*(1+p)*(1+q)
    phi=2**(a-1)*(p-1)*(q-1)
    assert sig==4*phi,(a,p,q)
    ns.append(n)
assert sorted(ns)==[418,3596,3956,5396,8636]

# Independent direct search for a,b,c<=8 and odd primes <170,
# using the original integer factors rather than fractional H comparisons.
checked=0
observed=[]
for a in (1,2):
    for p in primes(166):
        if p==2:continue
        for q in primes(166):
            if q<=p:continue
            for b in range(1,9):
                sp=(p**(b+1)-1)//(p-1)
                for c in range(1,9):
                    sq=(q**(c+1)-1)//(q-1)
                    sigma=(2**(a+1)-1)*sp*sq
                    phi=2**(a-1)*p**(b-1)*(p-1)*q**(c-1)*(q-1)
                    if sigma==4*phi:
                        observed.append((a,p,q,b,c))
                    checked+=1
assert observed==[(1,11,19,1,1),(2,17,127,1,1),(2,19,71,1,1),(2,23,43,1,1),(2,29,31,1,1)],observed
print('VERIFY_OK: exact 2-shell sieve, 13 second-shell candidate pairs, two multiplicative-order exclusions, %d direct prime-power cases; solutions %s'%(checked,sorted(ns)))
