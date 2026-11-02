"""Finite exact and numerical checks for three-atom Hausdorff multipliers.
No finite test replaces any infinite-dimensional argument.
"""
import math
from math import comb, gcd


def moments(p, q, b, c, u, v, rational=True):
    """Exact constant Fourier coefficient of (bU+cV)^u (b/U+c/V)^v."""
    total = 0
    for j in range(u + 1):
        for k in range(v + 1):
            # j and k count occurrences of the frequency-q term in positive/negative factors
            # net frequency is q*(j-k) + p*((u-j)-(v-k))
            if (q*(j-k) + p*((u-j)-(v-k)) == 0 if rational
                    else j == k and u-j == v-k):
                total += comb(u,j)*comb(v,k)*b**(j+k)*c**(u+v-j-k)
    return total

count = 0
for p in range(1, 9):
    for q in range(1, 9):
        if p == q or gcd(p,q)!=1:
            continue
        for b,c in [(1,2),(2,3)]:
            for d in range(p+q):
                for u in range(d+1):
                    v=d-u
                    assert moments(p,q,b,c,u,v) == moments(p,q,b,c,u,v,False)
                    count+=1
            assert moments(p,q,b,c,p,q)-moments(p,q,b,c,p,q,False)==b**p*c**q
            count+=1
print('EXACT_MOMENT_TESTS_PASSED',count)

# The radial integral identity is checked numerically against a uniform angle law.
for b,c in [(1.,2.),(2.,2.),(0.3,1.1)]:
    d,R=abs(b-c),b+c
    for a in (0.1,0.3,0.6,0.9):
        r=math.sqrt(d*d+4*b*c*a*a)
        F=2*math.asin(a)/math.pi
        samples=100001
        # deterministic angle midpoint quadrature
        actual=sum((math.sqrt(b*b+c*c+2*b*c*math.cos(2*math.pi*(j+0.5)/samples))<=r)
                   for j in range(samples))/samples
        assert abs(actual-F)<2e-5, (b,c,a,actual,F)
        count+=1
print('TOTAL_CHECKS_PASSED',count)
