"""Exact and high-precision checks of a Hermite disk-localization identity.

This is a finite consistency check. The proof of the all-index theorem is analytic.
"""
from math import factorial
from sympy import symbols, factor, simplify, exp, integrate, Rational, expand, sqrt, ceiling
from mpmath import mp

x = symbols('x', nonnegative=True)
checks = 0

def c(assertion, reason):
    global checks
    if not assertion:
        raise AssertionError(reason)
    checks += 1

def F(n,t):
    return t*t-2*n*t+n*(n-1)

def density(n):
    # Exponential factor stripped. For n=0 or 1, the removable t powers cancel.
    return factor(x**(n-2)*F(n,x)**2 / (2*factorial(n)))

for n in range(0,51):
    dn = density(n)
    dp = density(n+1)
    # Derivative identity, using product rule for e^-x.
    H = factor(x**(n-1)*F(n,x)*F(n+1,x) / (2*factorial(n+1)))
    c(simplify((H.diff(x)-H) - (dn-dp)) == 0, f'difference derivative n={n}')
    c(simplify(dn.subs(x, Rational(1,3))) > 0, f'positive density n={n}')

# Direct exact primitive for first 12 n: CDF(lambda_n) computed as 1 - e^-x times polynomial.
def exact_tail_poly(n):
    # density = e^-x * sum c_k*x^k, integrate from x to infinity.
    q=expand(density(n))
    p = 0
    for k in range(n+3):
        ck = q.coeff(x,k)
        if ck:
            p += ck * factorial(k) * sum(x**j/factorial(j) for j in range(k+1))
    return factor(p)

for n in range(0,15):
    tail = exact_tail_poly(n)
    c(simplify(tail.subs(x,0)-1)==0, f'cdf normalization n={n}')
    c(simplify(tail.diff(x)-tail + density(n)) == 0, f'cdf derivative n={n}')
    if n < 14:
        c(simplify(tail-exact_tail_poly(n+1) + x**(n-1)*F(n,x)*F(n+1,x)/(2*factorial(n+1)))==0,
          f'CDF adjacent difference n={n}')

# Exact simultaneous double triple plateau at x=2: centers n=1 and n=4.
c(F(1,2)==0 and F(4,2)==0, 'triangular radius zeroes')
P=[exact_tail_poly(n).subs(x,2) for n in range(6)]
c(P[0]==P[1]==P[2], 'first triple plateau')
c(P[3]==P[4]==P[5], 'second triple plateau')
c(simplify(P[3]-P[0]-Rational(2,3))==0, 'difference between CDF tails')

mp.dps=50
for radius in [mp.mpf('0.1'),mp.mpf('0.7'),mp.mpf('1'),mp.mpf('1.9'),mp.mpf('2'),mp.mpf('2.5'),mp.mpf('3'),mp.mpf('4.1'),mp.mpf('6'),mp.mpf('12.2'),mp.mpf('20')]:
    rminus = radius+mp.mpf('0.5')-mp.sqrt(radius+mp.mpf('0.25'))
    rplus=radius+mp.mpf('0.5')+mp.sqrt(radius+mp.mpf('0.25'))
    candidates={0,int(mp.ceil(rminus)),int(mp.ceil(rplus))}
    for n in range(0,100):
        # Avoid n0 and n1 singular gammas: define q_n(t) polynomial explicitly.
        if n<=1:
            lval=mp.quad(lambda t: mp.exp(-t)* t**(n-2)*(t*t-2*n*t+n*(n-1))**2 /(2*mp.factorial(n)),[0,radius]);
        else:
            # expanded quartic in t, with powers shifted by n-2
            p=[n*n*(n-1)**2,-4*n*n*(n-1), 6*n*n-2*n,-4*n,1]
            lval=sum(p[j]*mp.gammainc(n-1+j,0,radius) for j in range(5))/(2*mp.factorial(n))
        if n == 0: vals=[]
        vals.append(lval)
    mx=max(vals)
    cm=max(vals[j] for j in candidates)
    c(abs(mx-cm)<mp.mpf('1e-39'),f'three-candidate spectral norm radius {radius}')

print(f'PASS: {checks} exact symbolic and numerical check groups')
print('Triangular x=2 exact separation: 2/(3e^2); centers n=1 and n=4')
print('Three candidate indices: 0, ceil(x+1/2-sqrt(x+1/4)), ceil(x+1/2+sqrt(x+1/4))')
