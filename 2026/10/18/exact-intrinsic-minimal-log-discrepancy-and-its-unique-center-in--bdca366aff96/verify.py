"""Exact finite checks for intrinsic minimal discrepancy in a toric Fano family.

This checks selected dimensions/parameters, not the infinite theorem.
Run: python verify.py
"""
from fractions import Fraction
from math import gcd,prod

def datum(n,h):
    u=h;q=[]
    for j in range(n):
        q.append(1+u)
        u *= 1+u
    L=prod(q)
    w=[1]+[L//z for z in q]
    return q,L,w

def minimal_age(weights):
    vals=[(Fraction(1), 'ray')]
    for j,b in enumerate(weights):
        for k in range(1,b):
            age=sum(Fraction((k*a)%b,b) for i,a in enumerate(weights) if i!=j)
            if age:vals.append((age, f'chart={j},k={k}'))
    return min(vals)

for n, hs in [(2,range(3,18)),(3,range(3,8))]:
    for h in hs:
        q,L,w=datum(n,h)
        assert all(gcd(q[i],q[j])==1 for i in range(n) for j in range(i))
        assert all(w[i]>w[i+1] for i in range(1,n))
        assert h*sum(w)==L+h-1
        target=Fraction(1,h)+Fraction(h-1,h*w[1])
        direct=Fraction(sum(w)-w[1],w[1])
        assert target==direct
        actual,witness=minimal_age(w)
        assert actual == target,(n,h,w,target,actual,witness)
        print('PASS',n,h,'largest_weight',w[1],'mld',str(actual),'witness',witness)
print('VERIFY_OK')
