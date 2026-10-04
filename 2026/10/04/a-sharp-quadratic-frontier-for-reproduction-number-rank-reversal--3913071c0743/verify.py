from fractions import Fraction
from math import sqrt

def F(s,i,lam,memo=None):
    if memo is None: memo={}
    if s==0 or i==0: return Fraction(0)
    k=(s,i,lam)
    if k in memo: return memo[k]
    p=lam*s/(lam*s+1)
    memo[k]=p*(1+F(s-1,i+1,lam,memo))+(1-p)*F(s,i-1,lam,memo)
    return memo[k]

lam=Fraction(2)
m=1+F(3,1,lam)
assert m==Fraction(779,225)
beta=Fraction(675,779)
r=beta*m
assert r==3
p2=Fraction(4)-2*beta-(r-beta)
assert p2==Fraction(104,779) and p2>0
ri=(float(beta)+sqrt(float(beta*beta+4*(r-beta))))/2
assert ri<2
assert r>2
print("VERIFY_OK")
