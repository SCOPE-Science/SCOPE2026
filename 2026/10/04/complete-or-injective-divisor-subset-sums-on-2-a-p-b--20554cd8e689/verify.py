from itertools import product

PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)

def subset_sums(values):
    sums = {0}
    for value in values:
        sums |= {s + value for s in tuple(sums)}
    return sums

def check(a, b, p):
    divisors = [2**i * p**j for j in range(b + 1) for i in range(a + 1)]
    sums = subset_sums(divisors)
    M = 2**(a + 1) - 1
    sigma = M * (p**(b + 1) - 1) // (p - 1)
    if p <= 2**(a + 1):
        assert sums == set(range(sigma + 1))
    else:
        assert len(sums) == 2**len(divisors)
        assert len(sums) == 2**((a + 1) * (b + 1))
        omitted = sigma + 1 - len(sums)
        expected = M * (p**(b + 1) - 1) // (p - 1) + 1 - (M + 1)**(b + 1)
        assert omitted == expected
        assert omitted >= M

count = 0
for a, b, p in product(range(1, 5), range(1, 3), PRIMES):
    check(a, b, p)
    count += 1
print("VERIFY_OK", count)
