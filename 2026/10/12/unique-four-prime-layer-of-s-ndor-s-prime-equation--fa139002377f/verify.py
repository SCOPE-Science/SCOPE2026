from fractions import Fraction
from math import isqrt

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d <= n:
        if n%d==0: return False
        d += 2
    return True

# If the least prime were at least 5, the Euler-product side already exceeds 1.
assert Fraction(2*4*6*10*12,5*7*11*13) > 1
# Once p=3, q>=11 would again force the normalized product above 1.
assert Fraction(4*10**3,3*11**3) > 1
# q=7 reduces to 3(r-8)(s-8)=163, impossible modulo 3.
assert 163 % 3 != 0
# q=5 reduces to (r-16)(s-16)=235.
factor_pairs=[]
for a in range(1,236):
    if 235%a==0:
        b=235//a
        if a<=b: factor_pairs.append((a,b))
prime_pairs=[]
for a,b in factor_pairs:
    rr,ss=16+a,16+b
    if 5<rr<ss and isprime(rr) and isprime(ss):
        prime_pairs.append((rr,ss))
assert prime_pairs == [(17,251)]
p,q,r,s=3,5,17,251
assert p*q*r*s - 2*(p-1)*(q-1)*(r-1)*(s-1) == 5
# Regression scan using the exact solved-for-s formula for p,q,r below 500.
hits=[]
pr=[n for n in range(3,500) if isprime(n)]
for i,p in enumerate(pr):
  for j in range(i+1,len(pr)):
    q=pr[j]
    for k in range(j+1,len(pr)):
      r=pr[k]
      A=p*q*r
      B=2*(p-1)*(q-1)*(r-1)
      den=B-A
      num=B-5
      if den<=0 or num%den: continue
      s=num//den
      if s>r and isprime(s) and A*s-B*(s-1)==5:
        hits.append((p,q,r,s))
assert hits == [(3,5,17,251)]
print('VERIFY_OK unique_quadruple=(3,5,17,251) symbolic_reductions=4 scan_prime_bound=500 violations=0')
