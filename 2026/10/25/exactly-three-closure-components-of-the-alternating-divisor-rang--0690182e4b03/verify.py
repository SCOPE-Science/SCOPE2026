"""Independent exact-rational boundary and finite-prime checks for a squarefull alternating divisor range theorem.
Run: python3 verify.py. The infinite tail argument uses Nagura's prime-gap theorem and is not replaced by finite checks.
"""
from fractions import Fraction as F
from math import isqrt, pi

def primes_up_to(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(n+1) if sieve[i]]

def f(p,a):
    t=F(-1,p*p)
    return sum((t**j for j in range(a+1)),F(0))

P=primes_up_to(100)
for p in [5,7,11,13,17,19,23]:
    prod=F(1)
    for q in P[P.index(p)+1:]:
        prod*=f(q,3)
        if prod<=f(p,3):break
    else:raise AssertionError(('missing finite prime tail',p))

L_coef=F(612360,697)
L_lower=L_coef/F(22,7)**6
L_upper=L_coef/F(157,50)**6
c2={0:F(1),2:f(2,2),3:f(2,3)}
c3={0:F(1),2:f(3,2),3:f(3,3)}
assert c2[2]==F(13,16) and c2[3]==F(51,64)
assert c3[2]==F(73,81) and c3[3]==F(656,729)
assert c2[3]*c3[3]*L_coef==630
assert c3[3]*L_coef==F(13440,17)
for opts in [[(0,0)],[(0,3),(0,2)],[(3,0),(2,0)],[(3,3),(3,2),(2,3),(2,2)]]:
    constants=sorted(c2[a]*c3[b] for a,b in opts)
    assert all(d*L_upper < c for c,d in zip(constants,constants[1:])),opts
assert c2[3]*L_upper < c2[2]*c3[2] # overlap both-present and two-only bands
assert c2[2] < c3[3]*L_lower # first open gap
assert c3[2] < L_lower # second open gap
assert F(630)/F(22,7)**6 < F(13,16)

def squarefull(n):
    m=n
    for p in primes_up_to(isqrt(n)+1):
        if p*p>m:break
        if m%p==0:
            e=0
            while m%p==0:e+=1;m//=p
            if e<2:return False
    return m==1

def value(n):
    m=n;r=1.
    for p in primes_up_to(isqrt(n)+1):
        if p*p>m:break
        if m%p==0:
            e=0
            while m%p==0:e+=1;m//=p
            r*=float(f(p,e))
    if m>1:r*=float(f(m,1))
    return r

L=float(L_coef)/pi**6
bands=[(630/pi**6,13/16),(13440/(17*pi**6),73/81),(L,1)]
for n in range(1,50001):
    if squarefull(n):
        v=value(n)
        assert any(a-1e-12<=v<=b+1e-12 for a,b in bands),(n,v)
print('VERIFY_OK: exact finite-prime inequalities, exact rational band checks, and 50,000-integer squarefull sample')
