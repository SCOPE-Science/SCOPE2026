from fractions import Fraction
from math import isqrt, sqrt

def sqrt_interval(n, scale=10**14):
    """Exact rational enclosure lo <= sqrt(n) < hi."""
    a = isqrt(n*scale*scale)
    lo = Fraction(a, scale)
    hi = Fraction(a+1, scale)
    assert lo*lo <= n
    assert hi*hi > n
    return lo, hi

def recip_sqrt_interval(n):
    lo, hi = sqrt_interval(n)
    return Fraction(1,1)/hi, Fraction(1,1)/lo

def R_interval(n):
    slo, shi = sqrt_interval(n)
    lower = n*slo - 1
    upper = n*shi - 1
    for i in range(1,n):
        rlo, rhi = recip_sqrt_interval(i)
        lower -= rhi
        upper -= rlo
    return lower/(2*n), upper/(2*n)

def P_interval(n):
    lower = Fraction(0,1)
    upper = Fraction(0,1)
    for i in range(1,n):
        rlo, rhi = recip_sqrt_interval(i+1)
        lower += i*rlo
        upper += i*rhi
    return lower/n, upper/n

# Exact certificates for the cutoff signs.
for n in range(1,8):
    lo, hi = R_interval(n)
    assert hi < 1
lo8, hi8 = R_interval(8)
assert lo8 > 1

for n in range(1,5):
    lo, hi = P_interval(n)
    assert hi < 1
lo5, hi5 = P_interval(5)
assert lo5 > 1

# Direct source-form recurrences under a constant subgradient.
def dadapt(nsteps, d0=0.7, G=2.3):
    d = [d0]
    s = 0.0
    gamma = [1.0/G]
    x = [0.0]
    hats = []
    for k in range(nsteps):
        g = -G
        s = s + d[k]*g
        gamma_next = 1.0/(G*sqrt(k+1))
        num = gamma_next*s*s
        for i in range(k+1):
            num -= gamma[i]*d[i]*d[i]*G*G
        hat = num/(2.0*abs(s))
        hats.append(hat)
        d.append(max(d[k],hat))
        gamma.append(gamma_next)
        x.append(-gamma_next*s)
    return d,x,hats

d,x,h = dadapt(8)
for n in range(1,8):
    assert abs(d[n]-d[0]) < 1e-13
    assert abs(x[n]-d[0]*sqrt(n)) < 1e-13
assert d[8] > d[0]
assert abs(d[8]/d[0] - 1.1005958492887689) < 2e-14

def prodigy(nsteps, d0=0.7, G=2.3):
    d = [d0]
    x = [0.0]
    s = 0.0
    hats = []
    for k in range(nsteps):
        g = -G
        lam = d[k]*d[k]
        s += lam*g
        num = 0.0
        for i in range(k+1):
            num += d[i]*d[i]*(-G)*(0.0-x[i])
        hat = num/abs(s)
        hats.append(hat)
        dnext = max(d[k],hat)
        d.append(dnext)
        lam_next = dnext*dnext
        accum = lam_next*G*G
        for i in range(k+1):
            accum += d[i]*d[i]*G*G
        gamma_next = 1.0/sqrt(accum)
        x.append(-gamma_next*s)
    return d,x,hats

d2,x2,h2 = prodigy(5)
for n in range(1,5):
    assert abs(d2[n]-d2[0]) < 1e-13
    assert abs(x2[n] - n*d2[0]/sqrt(n+1)) < 1e-13
assert d2[5] > d2[0]
assert abs(d2[5]/d2[0] - 1.0301323403131262) < 2e-14

# Common objective check: all gradients entering the cutoff proposals are -G.
d0 = 0.7
D = d0*sqrt(8.0) + 0.3
G = 2.3
dd,xd,_ = dadapt(8,d0,G)
pp,xp,_ = prodigy(5,d0,G)
for k in range(8):
    assert xd[k] < D
for k in range(5):
    assert xp[k] < D

print("verification passed")
