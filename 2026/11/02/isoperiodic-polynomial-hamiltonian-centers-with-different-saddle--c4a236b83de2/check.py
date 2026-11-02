"""Standalone finite consistency checks for polynomial harmonic Hamiltonians.

The analytic theorem is independent of these finite tests.
"""
from fractions import Fraction as F
from math import cos, pi, comb, factorial


def hcart(x, y, p, q, k):
    assert p % 2 == 0 and q >= k and (q - k) % 2 == 0
    return F((x*x+y*y)**(p//2), p) + (x*x+y*y)**((q-k)//2) * (complex(x,y)**k).real


def hpolar_identity(x, y, p, q, k):
    # Compute harmonic polynomial by an exact binomial expansion.
    s = 0
    for j in range(0,k+1,2):
        s += (-1)**(j//2)*comb(k,j)*x**(k-j)*y**j
    return F((x*x+y*y)**(p//2),p) + (x*x+y*y)**((q-k)//2)*s


def rising(v,n):
    r=F(1)
    for k in range(n): r *= v+k
    return r


def coeff(j,p,q):
    alpha=F(q-p,p); beta=F(2,p)
    return F(comb(2*j,j),4**j)*beta/F(2*j)*rising(beta+1+2*j*alpha,2*j-1)/factorial(2*j-1)

for k in (1,3,5):
    for x in range(-4,5):
        for y in range(-4,5):
            a=hcart(x,y,4,5,k)
            b=hpolar_identity(x,y,4,5,k)
            assert a==b,(x,y,k)
cs=[coeff(j,4,5) for j in range(1,9)]
assert cs[0]==F(1,4),cs[0]
assert all(c>0 for c in cs)
for j in range(1,8):
    # Averaging cos^(2j)(k theta) over an integer number of periods.
    for k in (1,3,5):
        N=160000
        sample=sum(cos(2*pi*k*t/N)**(2*j) for t in range(N))/N
        exact=F(comb(2*j,j),4**j)
        assert abs(sample-float(exact))<2e-12,(j,k,sample,exact)
print('PASS: 243 polynomial test points, 8 exact positive area coefficients, 21 circle-moment checks')
