from fractions import Fraction
from itertools import product
from math import comb

def popcount(x): return x.bit_count()

def coord_masks(n):
    return [m for m in range(1<<n) if popcount(m)>=2]

def baseline(n):
    eps=Fraction(1,4*n)
    return {m:(Fraction(0) if popcount(m)<=1 else Fraction(1)+eps*popcount(m)) for m in range(1<<n)}

def add_coeff(c,m,a,free):
    if m in free and a:
        c[m]=c.get(m,0)+a
        if c[m]==0: del c[m]

def eval_coeff(c,d): return sum(Fraction(a)*d[m] for m,a in c.items())

def inequalities(n):
    free=set(coord_masks(n))
    # positivity of all free coords
    for A in free:
        yield {A:1}, 'positive'
    # monotonicity
    for A in range(1<<n):
        for B in range(1<<n):
            if A!=B and (A & ~B)==0:
                c={}; add_coeff(c,B,1,free); add_coeff(c,A,-1,free)
                if c: yield c,'mono'
    # overlapping subadditivity
    for A in range(1<<n):
        for B in range(1<<n):
            if A&B:
                c={}; add_coeff(c,A,1,free); add_coeff(c,B,1,free); add_coeff(c,A|B,-1,free)
                if c: yield c,'subadd'

def is_diversity(n,d):
    for A in range(1<<n):
        v=d[A]
        if v<0: return False
        if (v==0)!=(popcount(A)<=1): return False
    # D2: if B nonempty, delta(A U B)+delta(B U C)>=delta(A U C)
    for A in range(1<<n):
      for B in range(1,1<<n):
       for C in range(1<<n):
        if d[A|B]+d[B|C] < d[A|C]: return False
    return True

checks=0
for n in range(2,9):
    m=(1<<n)-n-1
    q=comb(n,2)
    h=m-q
    assert len(coord_masks(n))==m; checks+=1
    assert h==(1<<n)-n-1-comb(n,2); checks+=1
    d=baseline(n)
    assert is_diversity(n,d) if n<=5 else True
    if n<=5: checks+=1
    min_ratio=None
    inequality_count=0
    for c,kind in inequalities(n):
        slack=eval_coeff(c,d)
        assert slack>0,(n,kind,c,slack)
        l1=sum(abs(a) for a in c.values())
        ratio=slack/l1
        min_ratio=ratio if min_ratio is None or ratio<min_ratio else min_ratio
        inequality_count+=1; checks+=1
    assert min_ratio>0; checks+=1
    eta=min_ratio/2
    # This certifies the entire l_inf box |x-d0|<eta is contained in the diversity region:
    # every listed inequality loses at most l1*eta < slack.
    for c,kind in inequalities(n):
        assert eval_coeff(c,d)-sum(abs(a) for a in c.values())*eta>0
        checks+=1
    # Fixing q pair coordinates leaves exactly h independent higher-set coordinates in that box.
    high=[A for A in coord_masks(n) if popcount(A)>=3]
    assert len(high)==h; checks+=1

# Exact 3-point fiber: t runs over [max pair, min(two-edge sums)].
n=3
for d12,d13,d23 in product(range(1,7), repeat=3):
    if not (d12<=d13+d23 and d13<=d12+d23 and d23<=d12+d13):
        continue
    lo=max(d12,d13,d23)
    hi=min(d12+d13,d12+d23,d13+d23)
    for twot in range(0, 2*13+1):
        t=Fraction(twot,2)
        d={m:Fraction(0) for m in range(1<<3)}
        d[0b011]=Fraction(d12); d[0b101]=Fraction(d13); d[0b110]=Fraction(d23); d[0b111]=t
        got=is_diversity(3,d)
        expected=(Fraction(lo)<=t<=Fraction(hi))
        assert got==expected,(d12,d13,d23,t,got,lo,hi)
        checks+=1

# Compare full-diversity and L1 hidden dimensions.
for n in range(2,13):
    full=(1<<n)-n-1-comb(n,2)
    l1=(1<<(n-1))-1-comb(n,2)
    assert full-l1==(1<<(n-1))-n
    if n==2: assert full==0 and l1==0
    if n==3: assert full==1 and l1==0
    if n==4: assert full==5 and l1==1
    checks+=2 if n in (2,3,4) else 1

print('full_hidden_n2_to_n10',[(n,(1<<n)-n-1-comb(n,2)) for n in range(2,11)])
print('VERIFY_OK',checks,'exact assertions')
