#!/usr/bin/env python3

def primes_up_to(limit):
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    p = 2
    while p * p <= limit:
        if sieve[p]:
            start = p * p
            sieve[start:limit+1:p] = b"\x00" * (((limit - start)//p) + 1)
        p += 1
    return [i for i, bit in enumerate(sieve) if bit]

PRIMES = primes_up_to(50000)
assert len(PRIMES) > 4400

def a2_exact(n):
    # n is one-based: P_n = PRIMES[n-1].
    num = 1
    den = 1
    b = 0
    i = n - 1
    while True:
        p = PRIMES[i + b]
        num *= p
        den *= p - 1
        b += 1
        if num > 2 * den:
            # Strict monotonicity of every factor p/(p-1)>1 means this first
            # crossing is exactly the least admissible b.
            if b > 1:
                prev_num = num // p
                prev_den = den // (p - 1)
                assert prev_num <= 2 * prev_den
            return b, p

def main():
    a = {}
    terminal = {}
    for n in range(1, 45):
        a[n], terminal[n] = a2_exact(n)

    assert a[42] == 3900
    assert a[43] == 4112
    assert a[44] == 4324
    assert PRIMES[41] == 181
    assert PRIMES[42] == 191
    assert PRIMES[43] == 193
    assert terminal[42] == 37199
    assert terminal[43] == 39461
    assert terminal[44] == 41761

    def f(n):
        return a[n+1] + a[n-1] - 2*a[n]

    assert f(31) == -5
    assert f(43) == 0
    assert all(f(n) != 0 for n in range(2, 43))

    print("VERIFY_OK")
    print("a(42)=3900")
    print("a(43)=4112")
    print("a(44)=4324")
    print("f(31)=-5")
    print("f(43)=0")
    print("first_zero=43")

if __name__ == "__main__":
    main()
