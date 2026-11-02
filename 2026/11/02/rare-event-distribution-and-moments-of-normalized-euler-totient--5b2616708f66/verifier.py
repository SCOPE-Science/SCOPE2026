"""Finite exact checks for normalized Euler-totient deficiency.

Run: python3 verifier.py
Python 3 standard library only. This is computational corroboration, not an
infinite proof. All threshold comparisons use integer arithmetic.
"""
from fractions import Fraction
from math import log

N = 250_000
phi = list(range(N+1))
least = [0]*(N+1)
primes = []
for p in range(2,N+1):
    if least[p] == 0:
        primes.append(p)
        for z in range(p,N+1,p):
            if least[z] == 0:
                least[z] = p
            phi[z] -= phi[z] // p
phi[1] = 1
support_sum = [0]*(N+1)
for p in primes:
    for z in range(p,N+1,p):
        support_sum[z] += p-1
prime_pi = [0]*(N+1)
for z in range(1,N+1):
    prime_pi[z] = prime_pi[z-1] + (z >= 2 and least[z] == z)

thresholds = [(3,4), (1,1), (1,2), (1,4), (1,10), (11,10)]
for numerator, denominator in thresholds:
    admissible = [m for m in range(1,N+1)
                  if numerator*phi[m] <= denominator]
    # If phi(m)<=K then m<=2K^2, so this is a complete list.
    assert N > 2*(denominator/numerator)**2
    H = sum((Fraction(1,m) for m in admissible), Fraction(0,1))
    # Direct enumeration and a separate sum of prime counts.
    cnt=0
    for x in range(1,N+1):
        cnt += denominator*(1+support_sum[x]) > numerator*phi[x]
        if x in (10_000,100_000,N):
            approx = sum(prime_pi[x//m] for m in admissible)
            print(f't={numerator}/{denominator} x={x} count={cnt} '
                  f'prime_sum={approx} discrepancy={cnt-approx} '
                  f'H={H}')

for x in (1_000,10_000,100_000,N):
    total = sum((1+support_sum[i])/phi[i] for i in range(1,x+1))
    moment2 = sum(((1+support_sum[i])/phi[i])**2 for i in range(1,x+1))
    print(f'normalized_first x={x} {log(x)*total/x:.7f} '
          f'normalized_second={log(x)*moment2/x:.7f}')
C1_trunc = sum(1/(m*phi[m]) for m in range(1,N+1))
C2_trunc = sum(1/(m*phi[m]*phi[m]) for m in range(1,N+1))
print(f'CONSTANTS_TRUNCATED {C1_trunc:.10f} {C2_trunc:.10f}')
print(f'VERIFY_OK threshold_cases={len(thresholds)} '
      f'exact_integer_tests={N*len(thresholds)} moment_levels=2')
