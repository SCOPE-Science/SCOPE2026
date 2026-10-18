"""Exact arithmetic checks for the crown-graph Euclidean distortion threshold.
Run with Python 3 standard library. The proof, not this finite checker,
provides the assertions for all graph orders.
"""
from fractions import Fraction as F
from math import floor

def data(n):
    s=F(2*floor(n*n/4),n)
    u=F((n-1)**2,1)/(F(2*n-1)*s)
    v=F(n*(n-1),4*(n-2)*(2*n-1))
    w=1-u-v
    b=F(n,2*(n-1)); c=F(n-2,2*(n-1))
    r=F(2,n)+1/b+F(n-2,n)/c
    basic=F(n,2)
    balanced=basic+s*(b+c-1)
    spike=F((n-4)**2,2*n)+F(8*(n-1),n)*c
    assert basic==balanced==spike
    assert r*basic==2*n-1
    assert u+v+w==1 and u>0 and v>0
    # KKT derivative identities for the three contact types.
    assert r*u*s == basic/b**2
    assert r*(u*s+v*F(8*(n-1),n)) == basic*F(n-2,n)/c**2
    return w

for n in range(3,501):
    w=data(n)
    assert (w>=0)==(n<=9), (n,w)
print('PASS: exact rational contact and KKT identities for n=3,...,500')

# Prove strict improvement for n=10 by a rational witness, with no optimizer.
# A fine fixed rational grid around the contact parameters suffices.
n=10; s=F(2*floor(n*n/4),n); root=F(2*n-1)
witness=None
for i in range(0,100):
    for j in range(0,100):
        b=F(n,2*(n-1))+F(i,100000)
        c=F(n-2,2*(n-1))+F(j,100000)
        rr=F(2,n)+1/b+F(n-2,n)/c
        upper=max(F(n,2),F(n,2)+(b+c-1)*s,F((n-4)**2,2*n)+F(8*(n-1),n)*c)
        if rr*upper<root:
            witness=(b,c,rr*upper)
            break
    if witness:break
assert witness is not None
print('PASS: strict improvement at n=10:',witness)
