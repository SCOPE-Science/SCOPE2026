"""Exact-arithmetic coefficient and log-concavity checks for antiholes."""
from math import comb

def coefficients(n):
    a = [n*comb(n-k,k)//(n-k) for k in range(n//2+1)]
    while len(a)<=3:
        a.append(0)
    a[2]+=n
    a[3]+=n
    return a

for n in range(5,501):
    a=coefficients(n)
    assert all(a[k]**2>a[k-1]*a[k+1] for k in range(1,len(a)-1)),n
    assert a[2] == n*(n-1)//2
print('COEFFICIENT_CHECK_OK n=5..500 exact_integer_profiles=496')
