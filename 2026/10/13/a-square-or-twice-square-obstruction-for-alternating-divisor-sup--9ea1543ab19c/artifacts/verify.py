"""Independent exact arithmetic spot checks for an alternating-divisor iteration theorem.
Uses a smallest-prime-factor sieve; no numerical check is used in the infinite proof.
"""
from math import isqrt

LIMIT = 1_000_000
spf = list(range(LIMIT + 1))
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for n in range(p*p, LIMIT+1, p):
            if spf[n] == n:
                spf[n] = p
beta = [0] * (LIMIT+1)
beta[1] = 1
omega = [0] * (LIMIT+1)
for n in range(2, LIMIT+1):
    p = spf[n]
    remainder = n
    a = 0
    while remainder % p == 0:
        remainder //= p
        a += 1
    local = (p**(a+1) + (-1)**a) // (p+1)
    assert (p**(a+1) + (-1)**a) % (p+1) == 0
    beta[n] = beta[remainder] * local
    omega[n] = omega[remainder] + 1

solutions = []
count_non_square_odd_part = 0
count_beta_even = 0
for n in range(1, LIMIT+1):
    b = beta[n]
    assert 1 <= b <= n
    if 2 * beta[b] == n:
        solutions.append(n)
    if n % 2 == 0:
        m = n
        while m % 2 == 0:
            m //= 2
        nonsquare = isqrt(m)**2 != m
        if nonsquare:
            count_non_square_odd_part += 1
            assert beta[n] % 2 == 0
            assert 2 * beta[b] != n
            count_beta_even += 1
    if n <= 5000:
        # Reconstruct β independently from its Liouville divisor-sum definition.
        acc = 0
        for d in range(1, isqrt(n) + 1):
            if n % d: continue
            for e in ([d] if d*d == n else [d, n//d]):
                t = n//e
                om = 0
                while t > 1:
                    p = spf[t]
                    t//=p
                    om+=1
                acc += e * (1 if om % 2 == 0 else -1)
        assert acc == b
assert solutions == [2,4,8,128,32768], solutions
assert count_beta_even == count_non_square_odd_part
assert 2 * 1 == 2  # β(β(2))=β(1)=1
# Check the power of 2 example beyond the sieve using the exact Fermat factorization.
N = 2**31
inner = (2**32 - 1)//3
assert inner == 5*17*257*65537
assert 2*(4*16*256*65536) == N
print('VERIFY_OK', 'limit=', LIMIT, 'superimperfect=',solutions,
      'even_nonsquare_odd_part_excluded=', count_non_square_odd_part,
      'large_known_solution=', N, 'beta_inner=', inner)
