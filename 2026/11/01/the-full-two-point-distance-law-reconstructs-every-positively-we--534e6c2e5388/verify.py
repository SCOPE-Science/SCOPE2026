"""Independent checks of the star-network pair-distance spline and inverse."""
from fractions import Fraction as F
from collections import Counter
from itertools import combinations
import random,math

def predicted(lengths,t):
    lengths=list(lengths); k=len(lengths); L=sum(lengths); t=F(t)
    return 2/L+(k*(k-3)*t-2*(k-2)*sum(max(F(0),t-a) for a in lengths)+2*sum(max(F(0),t-a-b) for a,b in combinations(lengths,2)))/L**2

def independent(lengths,t):
    lengths=list(lengths);L=sum(lengths);t=F(t)
    same=sum(max(F(0),a-t) for a in lengths)
    cross=sum(max(F(0),t)-max(F(0),t-a)-max(F(0),t-b)+max(F(0),t-a-b) for a,b in combinations(lengths,2))
    return 2*(same+cross)/L**2

def impulse(lengths):
    k=len(lengths);c=Counter()
    for a in lengths:c[a]-=2*(k-2)
    for a,b in combinations(lengths,2):c[a+b]+=2
    return c

def reconstruct(k,imp):
    residual=Counter(imp);out=[]
    while len(out)<k:
        nonzero=[x for x in residual if residual[x]!=0]
        assert nonzero, (out,residual)
        a=min(nonzero);mass=residual[a]
        assert mass<0 and -mass%(2*(k-2))==0,(out,a,mass)
        m=-mass//(2*(k-2)); assert m<=k-len(out)
        old=list(out)
        out += [a]*m
        # remove negative singles for newly recovered lengths
        residual[a]+=2*(k-2)*m
        # remove known-new pair positives and new-new positives
        for x in old:
            residual[x+a]-=2*m
        residual[2*a]-=m*(m-1)
    assert all(v==0 for v in residual.values()),residual
    return sorted(out)

N=0
rng=random.Random(20261031)
for k in range(3,11):
  for j in range(80):
    lengths=[F(rng.randint(1,22),rng.randint(1,7)) for z in range(k)]
    for t in [F(i,7) for i in range(0,120)]:
      assert predicted(lengths,t)==independent(lengths,t),(k,j,t)
      N+=1
    assert reconstruct(k,impulse(lengths))==sorted(lengths)
    N+=1
# deliberate cancellation at t=3: 1+2 cancels single arm 3
assert impulse([F(1),F(2),F(3)])[F(3)]==0
assert reconstruct(3,impulse([F(1),F(2),F(3)]))==[F(1),F(2),F(3)]
# Degree-two paths have identical distribution under arbitrary splits
for t in [F(j,7) for j in range(0,40)]:
    assert predicted([F(5)],t)==predicted([F(2),F(3)],t)
    N+=1
# Normalized density test via exact symbolic polygonal integration
for ls in [[F(1),F(2),F(3)],[F(1),F(1),F(1),F(1)], [F(2,3),F(4,3),F(7,3)]]:
    knots=sorted(set([F(0),*ls,*[a+b for a,b in combinations(ls,2)]]))
    integ=sum((predicted(ls,a)+predicted(ls,b))*(b-a)/2 for a,b in zip(knots,knots[1:]))
    assert integ==1,(ls,integ)
    N+=1
print('VERIFY_OK',N,'exact independent density identities, inverse reconstructions and normalization checks')
