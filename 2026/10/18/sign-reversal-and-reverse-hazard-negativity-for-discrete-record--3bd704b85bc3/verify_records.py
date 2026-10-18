"""Exact-rational finite checks of strict-record covariance formulas."""
from fractions import Fraction
from itertools import product

def formulas(p,s,t):
    assert 2<=s<t
    f=[sum(p[:j]) for j in range(len(p))]
    qs=sum(p[j]*f[j]**(s-1) for j in range(len(p)))
    qt=sum(p[j]*f[j]**(t-1) for j in range(len(p)))
    joint=sum(p[a]*f[a]**(s-1)*p[b]*f[b]**(t-s-1)
              for a in range(len(p)) for b in range(a+1,len(p)))
    return qs,qt,joint,joint-qs*qt

def brute(p,s,t):
    qa=qb=qj=Fraction(0)
    for seq in product(range(len(p)),repeat=t):
        prob=Fraction(1)
        for i in seq:prob*=p[i]
        a=seq[s-1]>max(seq[:s-1]);b=seq[t-1]>max(seq[:t-1])
        qa+=prob*a;qb+=prob*b;qj+=prob*(a and b)
    return qa,qb,qj,qj-qa*qb

cases=0
for m in (2,3,4):
    for nums in product((1,2),repeat=m):
        p=tuple(Fraction(v,sum(nums)) for v in nums)
        for s,t in ((2,3),(2,4),(3,4)):
            actual=brute(p,s,t)
            formula=formulas(p,s,t)
            assert actual==formula,(m,nums,s,t,actual,formula)
            cases+=1
print('exact enumeration checks',cases)
neg=pos=0
for m in (2,3,4,5):
    for weights in product((1,2,3),repeat=m):
        p=tuple(Fraction(v,sum(weights)) for v in weights)
        F=[];c=Fraction(0)
        for v in p:c+=v;F.append(c)
        hazard=[p[j]/F[j] for j in range(m)]
        condition=all(hazard[j]>=hazard[j+1] for j in range(m-1))
        for s in range(2,6):
            for t in range(s+1,8):
                cov=formulas(p,s,t)[3]
                if condition:
                    assert cov<0, (m,weights,s,t,cov)
                    neg+=1
                else:
                    pos+=cov>0
print('reverse-hazard sign exact checks',neg)
print('positive nonmonotone examples',pos)
for s in range(2,7):
    for t in range(s+1,11):
        p=(Fraction(1,100),Fraction(1,100),Fraction(98,100))
        assert formulas(p,s,t)[3]>0,(s,t)
print('three-symbol positive witness for 30 pairs passed')
