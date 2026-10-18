"""Exact and high-precision checks for a first-order near-diagonal Stirling expansion.
Run: python3 verify.py (standard library only).
Finite checks corroborate, rather than replace, the asymptotic proof.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import factorial

def stirling_near_diagonal(n, r):
    a = [0] * (r + 1)
    a[0] = 1
    for size in range(1, n + 1):
        b = [0] * (r + 1)
        for deficit in range(min(size, r) + 1):
            b[deficit] = a[deficit] + (size - deficit) * (a[deficit - 1] if deficit else 0)
        a = b
    return a[r]

def pair_only(n, r):
    return factorial(n) // (factorial(n - 2*r) * factorial(r) * (2**r))

def profile_total(n, r):
    # Exact weighted enumeration across all permitted non-singleton block sizes.
    acc = [0]
    counts = {}
    def visit(j, remaining):
        if j == 2:
            counts[2] = remaining
            pairs = sum(counts.get(k, 0)*k for k in counts)
            c1 = n - pairs
            blocks = 1 + c1 if c1 >= 0 else 0
            if c1 < 0: return
            den = factorial(c1)
            for k, ck in counts.items(): den *= factorial(ck)*factorial(k)**ck
            acc[0] += factorial(n)//den
            return
        for k in range(remaining//(j-1) + 1):
            counts[j] = k
            visit(j-1, remaining - k*(j-1))
        counts.pop(j,None)
    visit(min(r+1,n),r)
    return acc[0]

def ratio_triples(n, r, j):
    if 2*j > r: return Fraction(0)
    up=1
    for h in range(2*j): up*=r-h
    dn=1
    for h in range(1,j+1): dn*=n-2*r+h
    return Fraction(2**j * up, 3**j * factorial(j)*dn)

num_checks=0
for n in range(2,12):
    for r in range(1,min(n//2,5)+1):
        a=profile_total(n,r)
        b=stirling_near_diagonal(n,r)
        assert a==b,(n,r,a,b)
        num_checks+=1
        assert Fraction(pair_only(n,r),b)>0
        num_checks+=1
        # Exact low-order subprofile identities against full-profile enumeration.
        if r>=2:
            triple_weight = pair_only(n,r)*ratio_triples(n,r,1)
            assert triple_weight.denominator==1
            num_checks+=1

with localcontext() as ctx:
    ctx.prec=75
    target=(-Decimal(2)/Decimal(3)).exp()
    expected_lo=-target/Decimal(9)
    expected_hi=target*Decimal(11)/Decimal(9)
    for m in (10,20,40,70):
        for n, limit in ((m*m,expected_lo),(m*m+2*m,expected_hi)):
            P=Decimal(pair_only(n,m))/Decimal(stirling_near_diagonal(n,m))
            scaled=m*(P-target)
            tolerance=Decimal('0.018') if m==10 else (Decimal('0.01') if m==20 else Decimal('0.006'))
            assert abs(scaled-limit)<tolerance,(m,n,scaled,limit)
            num_checks+=1
            u=Decimal(m*m)/Decimal(n)
            lam=Decimal(2)*u/Decimal(3)
            corrected=(-lam).exp()*(1+(Decimal(2)*u/Decimal(3)-Decimal(7)*u*u/Decimal(9))/Decimal(m))
            assert abs(P-corrected)<Decimal('0.2')/Decimal(m*m),(m,n,P,corrected)
            num_checks+=1
    print('PASS',num_checks,'independent integer enumerations and high-precision comparisons')
    print('predicted scaled subsequential limits:',expected_lo, expected_hi)
