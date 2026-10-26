"""Finite arithmetic checks supporting the stated uniform-conjugacy-class expansion.
Pure standard-library Python; these checks do not certify infinite asymptotics.
"""
from functools import lru_cache
from math import pi, sqrt

_part = [1]
def p(n):
    if n < 0: return 0
    while len(_part) <= n:
        i = len(_part)
        ans = 0
        j = 1
        while j*(3*j-1)//2 <= i:
            sgn = 1 if j%2 else -1
            ans += sgn*_part[i-j*(3*j-1)//2]
            if j*(3*j+1)//2 <= i:
                ans += sgn*_part[i-j*(3*j+1)//2]
            j += 1
        _part.append(ans)
    return _part[n]

def partitions(n, minpart=1):
    if n == 0:
        yield ()
    for a in range(minpart,n+1):
        for tail in partitions(n-a,a):
            yield (a,)+tail

def count_exact(n,k,m):
    return sum(t.count(k)==m for t in partitions(n))

checks = 0
for n in range(1,18):
    assert len(list(partitions(n))) == p(n)
    checks += 1
    for k in range(1,min(6,n)+1):
        for m in range(n//k+1):
            assert count_exact(n,k,m) == p(n-m*k)-p(n-(m+1)*k)
            checks += 1

for n in (100,400,1600,3500):
    pn = p(n)
    assert pn > 0
    for k in (1,2,4,7):
        q = (p(n)-p(n-k))/pn
        approx = (pi/sqrt(6*n))*k
        assert abs(q-approx) < 10*k/n
        checks += 1
    for k in (1,2,3):
        for m in (0,1,2):
            q = (p(n-m*k)-p(n-(m+1)*k))/pn
            approx = pi*k/sqrt(6*n)
            assert abs(q-approx) < 15*k*(m+1)/n
            checks += 1

for n in (60,300,1500):
    pn=p(n)
    for k,l in ((1,2),(1,3),(2,3)):
        for a,b in ((0,0),(1,0),(1,1)):
            prob=(p(n-k*a-l*b)-p(n-k*(a+1)-l*b)-p(n-k*a-l*(b+1))+p(n-k*(a+1)-l*(b+1)))/pn
            assert 0 <= prob < 10000/n
            checks += 1
print('UNLABELLED_FO_FIRST_CORRECTION_FINITE_OK', checks, 'partition_n', p(17), 'p3500_digits',len(str(p(3500))))
