from fractions import Fraction
from itertools import product

def harmonic_count(n, k, ell):
    exps = (k, -k, ell, -ell)
    count = 0
    for idx in product(range(n), repeat=4):
        balances = [0] * n
        for j, e in zip(idx, exps):
            balances[j] += e
        if all(v == 0 for v in balances):
            count += 1
    return count

def fracpart(x):
    q = x.numerator // x.denominator
    return x - q

def B2_periodic(x):
    y = fracpart(x)
    return y*y - y + Fraction(1,6)

def watson_order(sample):
    x = sorted(sample)
    n = len(x)
    mean = sum(x, Fraction(0))/n
    s = Fraction(0)
    for i,u in enumerate(x, 1):
        target = Fraction(2*i-1, 2*n)
        s += (u-target)**2
    return s - n*(mean-Fraction(1,2))**2 + Fraction(1,12*n)

def watson_kernel(sample):
    n = len(sample)
    total = Fraction(0)
    for u in sample:
        for v in sample:
            total += B2_periodic(u-v)
    return total/(2*n)

def run():
    mixed_checks = 0
    equal_checks = 0
    for n in range(2,9):
        for k in range(1,6):
            got = harmonic_count(n,k,k)
            assert got == 2*n*n-n
            equal_checks += 1
            for ell in range(1,7):
                if ell == k:
                    continue
                got = harmonic_count(n,k,ell)
                assert got == n*n
                mixed_checks += 1

    samples = [
        [Fraction(1,10),Fraction(2,5)],
        [Fraction(1,10),Fraction(2,5),Fraction(9,10)],
        [Fraction(1,12),Fraction(1,3),Fraction(7,12),Fraction(11,12)],
        [Fraction(2,17),Fraction(5,17),Fraction(8,17),Fraction(9,17),Fraction(15,17)],
        [Fraction(1,20),Fraction(3,20),Fraction(7,20),Fraction(13,20),Fraction(17,20),Fraction(19,20)],
    ]
    kernel_checks = 0
    for s in samples:
        assert watson_order(s) == watson_kernel(s)
        kernel_checks += 1

    print("VERIFY_OK")
    print(f"mixed_harmonic_count_checks={mixed_checks}")
    print(f"equal_harmonic_count_checks={equal_checks}")
    print(f"watson_kernel_checks={kernel_checks}")
    print("max_index_count_n=8")

if __name__ == "__main__":
    run()
