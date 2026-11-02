"""Independent exact checks for frequency-class covariance in uniform weak compositions.
Requires Python 3 standard library only. All arithmetic is rational/integer.
"""
from fractions import Fraction
from math import comb, prod
from itertools import combinations

def fall(z, m):
    return prod(z-j for j in range(m))

def all_weak(n,k):
    if k==1:
        yield (n,)
    else:
        for a in range(n+1):
            for rem in all_weak(n-a,k-1):
                yield (a,)+rem

def moments_from_counts(n,k,r,s):
    pool=list(all_weak(n,k))
    Q=len(pool)
    Er=Es=Ers=0
    for x in pool:
        u=x.count(r); v=x.count(s)
        Er+=u;Es+=v;Ers+=u*v
    return (Fraction(Er,Q),Fraction(Es,Q),Fraction(Ers,Q))

def moments_from_stars(n,k,r,s):
    Q=comb(n+k-1,k-1)
    Er=Fraction(k*comb(n-r+k-2,k-2),Q)
    Es=Fraction(k*comb(n-s+k-2,k-2),Q)
    if k>=3:
        Ers=Fraction(k*(k-1)*comb(n-r-s+k-3,k-3),Q)
    elif n==r+s:
        Ers=Fraction(2,Q)
    else:
        Ers=Fraction(0)
    return Er,Es,Ers

def ratio_closed(n,k,r,s):
    if k==2:
        return Fraction(n+1,2) if n==r+s else Fraction(0)
    t=n+k-1
    return (Fraction(k-2,k)*Fraction(fall(n,r+s),fall(n,r)*fall(n,s))
            *Fraction(fall(t,r+1)*fall(t,s+1),fall(t,r+s+2)))

def rational_curve_signs(n,r,s,kmax):
    vals=[ratio_closed(n,k,r,s) for k in range(2,kmax+1)]
    positive=[k for k,R in enumerate(vals,2) if R>1]
    assert not positive or positive==list(range(min(positive),max(positive)+1))
    # Prove finite sequence has at most a single rising-to-falling change (not strictly)
    signs=[(vals[i+1]>vals[i])-(vals[i+1]<vals[i]) for i in range(len(vals)-1)]
    assert all(not(signs[i]<0 and signs[j]>0) for i in range(len(signs)) for j in range(i+1,len(signs)))

assertion_count=0
# Independent exhaustive generation of all weak compositions.
for n in range(3,11):
    for k in range(2,8):
        for r in range(1,n):
            for s in range(r+1,n+1):
                if r+s>n: continue
                M=moments_from_counts(n,k,r,s)
                assert M==moments_from_stars(n,k,r,s),(n,k,r,s,M)
                Er,Es,Ers=M
                assert Er>0 and Es>0
                assert Ers/(Er*Es)==ratio_closed(n,k,r,s),(n,k,r,s)
                assertion_count+=2
# Scan broad integer parameter windows for interval property and unimodality.
for n in range(3,51):
    for r in range(1,n):
        for s in range(r+1,n+1):
            if r+s>n:continue
            rational_curve_signs(n,r,s,40)
            assertion_count+=2
n,r,s=10,1,6
v=[ratio_closed(n,k,r,s) for k in range(2,8)]
assert v==[Fraction(0),Fraction(22,25),Fraction(26,25),Fraction(26,25),Fraction(1),Fraction(20,21)],v
assertion_count+=1
print('PASS',assertion_count,'exact assertions; example ratios',v)
