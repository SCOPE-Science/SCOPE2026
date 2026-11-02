from fractions import Fraction as Q
from itertools import product

def e2(probs):
    v=Q(0); w=Q(0)
    for p in probs:
        odds=p/(1-p)
        v+=w*odds; w+=odds
    return v

def threshold(cap):
    t=cap/(1-cap); m=1
    while Q(m*(m+1),2)*t*t<1:
        m+=1
    a=1-Q(m*(m-1),2)*t*t
    z=a/(m*t)
    return m, z/(1+z), m*cap+z/(1+z)

count=0
for cap in (Q(1,2), Q(2,5), Q(1,3), Q(1,4), Q(1,6), Q(1,8)):
    m,q,T=threshold(cap)
    assert 0<q<=cap
    assert e2([cap]*m+[q])==1;count+=2
    for n in range(1,7):
        for ps in product((Q(0),cap/2,cap),repeat=n):
            value=e2(ps); mu=sum(ps)
            assert not (value>1 and mu<=T)
            if mu==T and value==1:
                assert sorted(x for x in ps if x) == sorted([cap]*m+[q])
            count+=2
    # Direct strict reversal is attainable arbitrarily above T.
    if q<cap:
        assert e2([cap]*m+[q+min((cap-q)/2,Q(1,100))])>1
    else:
        assert e2([cap]*m+[q,Q(1,100)])>1
    count+=1
print('Exact rational checks passed:',count)
for cap in (Q(1,2),Q(2,5),Q(1,3),Q(1,4),Q(1,10)):
    m,q,T=threshold(cap)
    print('cap',str(cap),'saturated',m,'residual',str(q),'sharp_mean',str(T))
