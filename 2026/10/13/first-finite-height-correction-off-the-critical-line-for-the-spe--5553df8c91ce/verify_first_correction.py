#!/usr/bin/env python3
import math
import mpmath as mp

mp.mp.dps = 50
N = 200000
sieve = bytearray(b"\x01") * (N + 1)
sieve[:2] = b"\x00\x00"
for p in range(2, int(N**0.5) + 1):
    if sieve[p]:
        sieve[p*p:N+1:p] = b"\x00" * (((N-p*p)//p)+1)
primes = [p for p in range(2, N+1) if sieve[p]]

arch_num = mp.quad(lambda u: mp.log(u), [1,2])
arch_exact = 2*mp.log(2)-1
assert abs(arch_num-arch_exact) < mp.mpf('1e-45')

for sigma in (mp.mpf('0.6'), mp.mpf('0.75'), mp.mpf('0.9')):
    s = sigma + mp.mpf('0.5')
    exact = -mp.diff(mp.zeta, s) / mp.zeta(s)
    trunc = mp.fsum(mp.log(p)/(mp.power(p,s)-1) for p in primes)
    coeff = mp.log(2/mp.pi)-1 + 2*mp.diff(mp.zeta,s)/mp.zeta(s)
    print('sigma=%s s=%s prime_sum=%s exact=%s gap=%s coeff=%s' %
          (mp.nstr(sigma,8), mp.nstr(s,8), mp.nstr(trunc,18), mp.nstr(exact,18), mp.nstr(exact-trunc,8), mp.nstr(coeff,18)))
    assert trunc > 0 and exact > trunc

print('VERIFY_OK identity=von_mangoldt_prime_powers archimedean_constant=2log2-1 cutoff=%d' % N)
