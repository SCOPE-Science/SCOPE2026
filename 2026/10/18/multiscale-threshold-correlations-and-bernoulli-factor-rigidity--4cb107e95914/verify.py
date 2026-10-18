"""Exact rational checks for threshold observations of full Chebyshev maps."""
from fractions import Fraction as F
from itertools import product

def zigzag(q, u):
    v = q * u
    j = v.numerator // v.denominator
    d = v - j
    return d if j % 2 == 0 else 1 - d

def covariance_formula(Q, p):
    j = (Q*p).numerator // (Q*p).denominator
    t = Q*p-j
    if t == 0:
        return F(0)
    if j%2==0:
        return min((1-p)*t, p*(1-t))/Q
    return -min(p*t,(1-p)*(1-t))/Q

def joint_by_preimages(Q, p):
    # Count length([0,p] intersect g_Q^-1([0,p])) exactly.
    total = F(0)
    for j in range(Q):
        a,b=F(j,Q),F(j+1,Q)
        u = min(b,p)-a
        if u <= 0: continue
        if j%2==0:
            total += min(u,p/Q)
        else:
            total += max(F(0),u-(1-p)/Q)
    return total

def words(q,p,n):
    pts={F(0),F(1)}
    for i in range(n):
        m=q**i
        for j in range(m):
            pts.add(F(j,m)); pts.add(F(j+1,m))
            pts.add(F(j+p if j%2==0 else j+1-p,m))
    pts=sorted(pts)
    ans={bits:F(0) for bits in product((0,1),repeat=n)}
    for a,b in zip(pts,pts[1:]):
        if a==b:continue
        y=(a+b)/2
        bits=[]
        for _ in range(n):
            bits.append(int(y<p))
            y=zigzag(q,y)
        ans[tuple(bits)]+=b-a
    return ans

for q in range(2,9):
    for n in (1,2,3):
        Q=q**n
        for p in (F(1,7),F(2,5),F(1,2),F(4,7),F(9,11),F(1,q),F(q-1,q)):
            got=joint_by_preimages(Q,p)-p*p
            expect=covariance_formula(Q,p)
            assert got==expect,(q,n,p,got,expect)
            assert abs(got)<=p*(1-p)/Q
            if n==1 and p.denominator==q and 0<p<1: assert got==0
    for j in range(1,q):
        p=F(j,q)
        for n in range(2,5):
            joint=words(q,p,n)
            for bits,prob in joint.items():
                expect=p**sum(bits)*(1-p)**(n-sum(bits))
                assert prob==expect,(q,j,n,bits,prob,expect)
assert covariance_formula(2,F(1,4))!=0
assert covariance_formula(4,F(1,4))==0
print('VERIFY_OK: exact lag covariances q=2..8 and lags 1..3; all symbolic words length 2..4 at q-grid thresholds; strict bounds and higher-lag cancellations.')
