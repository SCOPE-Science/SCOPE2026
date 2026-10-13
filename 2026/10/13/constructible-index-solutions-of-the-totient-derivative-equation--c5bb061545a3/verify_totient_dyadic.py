"""Finite test for D(phi(n))=n on power-of-two totient inputs.

Exact integer sieve. This finite test corroborates but does not replace the
unbounded Fermat-prime argument in RESULT.md.
"""

def derivative(m, spf):
    if m < 2:
        return 0
    x, result = m, 0
    while x > 1:
        p = spf[x]
        exponent = 0
        while x % p == 0:
            x //= p
            exponent += 1
        result += exponent * (m // p)
    return result


def check(limit=1000000):
    phi = list(range(limit+1))
    spf = list(range(limit+1))
    for p in range(2, limit+1):
        if spf[p] == p:
            for j in range(p, limit+1, p):
                phi[j] -= phi[j] // p
                if spf[j] == j:
                    spf[j] = p
    candidates = 0
    found = []
    for n in range(1, limit+1):
        m = phi[n]
        if m & (m - 1) == 0:
            candidates += 1
            if derivative(m, spf) == n:
                found.append(n)
    assert found == [32, 80, 192], (limit, found)
    for n in [31, 81, 112, 176, 244]:
        if n <= limit:
            assert derivative(phi[n], spf) == n
            assert phi[n] & (phi[n]-1) != 0
    assert [(n,phi[n],derivative(phi[n],spf)) for n in found] == [(32,16,32),(80,32,80),(192,64,192)]
    print(f'VERIFY_OK limit={limit} prime_power_totient_candidates={candidates} solutions={found} near_exceptions=[31,81,112,176,244]')

if __name__ == '__main__':
    check()
