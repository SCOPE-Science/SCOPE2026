"""Exact rational audit of the fourth-power random cubic probability formula."""
from fractions import Fraction as Q
from collections import defaultdict
from math import comb

def law(p):
    b0=(p**3-p)//3
    b1=p*p*(p-1)//2
    b2=p*(p-1)
    b3=comb(p,3)
    n1=b1+p
    n2=b2
    n3=b3
    D={0:Q(1)-Q(p-1,2*p*p)-Q(1,p**3),2*p:Q(p-1,2*p*p),p*p:Q(1,p**3)}
    T={0:Q(1)-Q(p-1,p*p)-Q(n1+n2+n3,p**6),p:Q(p-1,p*p),p*p:Q(n1,p**6),2*p*p:Q(n2,p**6),3*p*p:Q(n3,p**6)}
    h=defaultdict(Q)
    for r,count in [(0,b0),(1,b1),(3,b3)]:h[r]+=Q(count,p**3)
    for r,v in D.items():h[r+1]+=Q(b2,p**3)*v
    for r,v in T.items():h[r]+=Q(p,p**3)*v
    h={r:v for r,v in h.items() if v}
    assert sum(h.values())==1
    assert sum(r*v for r,v in h.items())==1
    assert max(h)==3*p*p
    assert h[3*p*p]==Q(comb(p,3),p**8)
    return h

hist={0:201852,1:277749,3:32805,7:13122,9:972,10:4374,18:486,27:81}
h=law(3)
assert {i:int(v*3**12) for i,v in h.items()}==hist
for p in [3,5,7,11,13,17,19]:law(p)
print('FORMULA_OK primes=3,5,7,11,13,17,19 exact_p3_cubics=531441 mean=1')
