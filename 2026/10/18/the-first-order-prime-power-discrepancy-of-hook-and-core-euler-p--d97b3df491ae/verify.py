"""Reproduce exact finite coefficient checks for a first-order partition congruence."""


def divisor_sums(N):
    sig = [0] * (N + 1)
    for d in range(1, N + 1):
        for k in range(d, N + 1, d):
            sig[k] += d
    return sig


def euler_power(exponent, N, sig):
    # E(x)^exponent, E(x)=product_{j>=1}(1-x^j).
    c = [0] * (N + 1)
    c[0] = 1
    for n in range(1, N + 1):
        numerator = -exponent * sum(sig[j] * c[n-j] for j in range(1, n + 1))
        assert numerator % n == 0
        c[n] = numerator // n
    return c


def product(a, b, N):
    return [sum(a[k] * b[n-k] for k in range(n+1)) for n in range(N+1)]


def check(p, a, N, sig):
    t = p**a
    f = euler_power(t*t-1, N, sig)
    partitions = euler_power(-1, N, sig)
    small = euler_power(t, N//t, sig)
    b = [small[n//t] if n % t == 0 else 0 for n in range(N+1)]
    cores = product(b, partitions, N)
    kernel = [0] * (N+1)
    for unit in range(1, N+1):
        if unit % p == 0:
            continue
        residue = -sig[unit] * pow(unit, -1, p) % p
        j = a-1
        while unit * p**j <= N:
            kernel[unit * p**j] = residue
            j += 1
    predicted = product(cores, kernel, N)
    for n in range(N+1):
        discrepancy = f[n]-cores[n]
        assert discrepancy % p**(a+1) == 0, (p,a,n,'integrality')
        got = (discrepancy // p**(a+1)) % p
        assert got == predicted[n] % p, (p,a,n,got,predicted[n] % p)
    assert next(n for n in range(N+1)
                if (f[n]-cores[n]) % p**(a+2) != 0) == p**(a-1)
    return N+1


def main():
    cases = [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1),(5,2),(7,1),(11,1)]
    N = 96
    sig = divisor_sums(N)
    total = sum(check(p,a,N,sig) for p,a in cases)
    print(f'VERIFY_OK cases={len(cases)} coefficients={total} max_index={N}')


if __name__ == '__main__':
    main()
