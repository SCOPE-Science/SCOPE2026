from decimal import Decimal, getcontext, ROUND_CEILING
from math import isqrt

getcontext().prec = 70
GAMMA = Decimal('0.5772156649015328606065120900824024310421593359399235988057672349')

def is_prime_power(n):
    # only used to label samples
    for p in range(2, n+1):
        prime = all(p%d for d in range(2,isqrt(p)+1))
        if not prime: continue
        x=p
        while x<n: x*=p
        if x==n: return True
    return False

def prime_pi(n):
    sieve=bytearray(b'\x01')*(n+1)
    if n>=0: sieve[0]=0
    if n>=1: sieve[1]=0
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return sum(sieve)

def check(m):
    x=(Decimal(m)-GAMMA).exp()
    R=int(x.to_integral_value(rounding=ROUND_CEILING))
    pi=prime_pi(R)
    R0=R+pi
    K=1+(m-1)*R0
    D=1+(m-1)*(K+R0)
    assert D==m*K
    M0=sum(K//ell + 1 for ell in range(1,R+1))
    old=2*m*(m-1)*int(Decimal(m).exp().to_integral_value(rounding=ROUND_CEILING))
    assert M0>D
    assert D<old
    return (m,R,pi,K,D,M0,old)

samples=[m for m in range(2,14) if is_prime_power(m)]
rows=[check(m) for m in samples]
print('VERIFY_OK samples=%d max_m=%d' % (len(rows), max(samples)))
for row in rows:
    print('m=%d R=%d piR=%d K=%d D=%d M0=%d old=%d' % row)
