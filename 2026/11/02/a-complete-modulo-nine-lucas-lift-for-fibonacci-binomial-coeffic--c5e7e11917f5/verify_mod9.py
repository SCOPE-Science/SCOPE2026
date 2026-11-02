#!/usr/bin/env python3
"""Direct integer and 3-adic unit checks of a Fibonacci-binomial congruence modulo nine."""
from math import comb

MOD = 9

def residual(m, r):
    return [1, (-1)**m * (1-6*m), 1-6*m, 2*(-1)**m][r] % MOD

def predicted(n, k):
    m, r = divmod(n, 4)
    a, s = divmod(k, 4)
    b, t = divmod(n-k, 4)
    assert m-a-b in (0, 1)
    u = residual(m, r)
    u = u * pow(residual(a, s), -1, MOD) % MOD
    u = u * pow(residual(b, t), -1, MOD) % MOD
    if s+t == r:
        return u * pow(7, m//3-a//3-b//3, MOD) * comb(m, a) % MOD
    assert s+t == r+4
    return 6 * u * (b+1) * comb(m, a) % MOD

def v3_unit(n):
    exponent = 0
    while n % 3 == 0:
        n //= 3
        exponent += 1
    return exponent, n % MOD

def run():
    bound = 160
    fib = [0, 1]
    for _ in range(bound+1):
        fib.append(fib[-1] + fib[-2])
    fac = [1]
    unit = [1]
    valuation = [0]
    int_count = 0
    for j in range(1, bound+1):
        fac.append(fac[-1] * fib[j])
        v, u = v3_unit(fib[j])
        unit.append(unit[-1] * u % MOD)
        valuation.append(valuation[-1] + v)
    for n in range(bound+1):
        m, r = divmod(n, 4)
        fact_unit = 1
        for j in range(1, m+1):
            _, u = v3_unit(j)
            fact_unit = fact_unit * u % MOD
        wanted = pow(2, m, MOD) * pow(7, m//3, MOD) * fact_unit * residual(m, r) % MOD
        assert unit[n] == wanted, ('unit', n, unit[n], wanted)
        for k in range(n+1):
            exact = fac[n] // (fac[k] * fac[n-k])
            assert exact * fac[k] * fac[n-k] == fac[n]
            got = exact % MOD
            want = predicted(n, k)
            assert got == want, (n, k, got, want)
            int_count += 1
            v = valuation[n] - valuation[k] - valuation[n-k]
            if v >= 2:
                assert got == 0
            elif v == 1:
                assert got in (3,6)
            else:
                assert got in (1,2,4,5,7,8)
    print('VERIFY_OK integer_pairs=', int_count, 'rows=', bound+1,
          'unit_product_checks=', bound+1, 'modulus=', MOD)

if __name__ == '__main__':
    run()
