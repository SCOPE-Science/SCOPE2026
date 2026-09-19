import math

N = 1_000_000
checkpoints = {100, 1_000, 10_000, 100_000, 1_000_000}

# Smallest-prime-factor sieve.
spf = [0] * (N + 1)
primes = []
for n in range(2, N + 1):
    if spf[n] == 0:
        spf[n] = n
        primes.append(n)
    for p in primes:
        v = p * n
        if v > N or p > spf[n]:
            break
        spf[v] = p

# For squarefree n, c1(n) is the number of prime factors p == 1 (mod 5)
# modulo 3, and c2(n) is the number of prime factors p == 2 (mod 5)
# modulo 2.  The other two reduced residue classes have modulus 1.
squarefree = bytearray(N + 1)
squarefree[1] = 1
c1 = bytearray(N + 1)
c2 = bytearray(N + 1)

A0000 = 0
A0100 = 0
print("X A_(0,0,0,0) A_(0,1,0,0) difference scaled_difference")
for n in range(1, N + 1):
    if n > 1:
        p = spf[n]
        q = n // p
        if q % p != 0:
            squarefree[n] = squarefree[q]
            if squarefree[n]:
                c1[n] = (c1[q] + (p % 5 == 1)) % 3
                c2[n] = (c2[q] + (p % 5 == 2)) % 2

    if squarefree[n] and n % 5 != 0 and c1[n] == 0:
        if c2[n] == 0:
            A0000 += 1
        else:
            A0100 += 1

    if n in checkpoints:
        d = A0000 - A0100
        scaled = d * math.sqrt(math.log(n)) / n
        print(f"{n} {A0000} {A0100} {d} {scaled:.12f}")

print("dominant pole order: 1/2")
print("next pole orders: 1/8 +/- i*sqrt(3)/8")
