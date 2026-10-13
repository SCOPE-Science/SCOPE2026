#!/usr/bin/env python3
from math import isqrt
import csv
from pathlib import Path

LIMIT = 2_000_000
MAXSIGMA = 3_000_010

def sieve_primes(n):
    isprime = bytearray(b"\x01") * (n + 1)
    isprime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(n) + 1):
        if isprime[p]:
            isprime[p*p:n+1:p] = b"\x00" * (((n - p*p)//p) + 1)
    return isprime

# Small exceptional cases reconstructed independently.
small_prime = sieve_primes(200)
pi_small = [0] * 201
count = 0
for i in range(201):
    count += small_prime[i]
    pi_small[i] = count

generated = []
for q in [p for p in range(3, 62) if small_prime[p]]:
    s = 3 * (q + 1)
    generated.append(("p=2",2,q,s,pi_small[s],q-1,int(pi_small[s] == q-1)))
for q in (5,7,11):
    s = 4 * (q + 1)
    generated.append(("p=3",3,q,s,pi_small[s],2*(q-1),int(pi_small[s] == 2*(q-1))))
s = 48
generated.append(("boundary",5,7,s,pi_small[s],24,int(pi_small[s] == 24)))

with open(Path(__file__).with_name("small_cases.csv"), newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    cert = [(r[0],) + tuple(map(int, r[1:])) for r in reader]
assert header == ["branch","p","q","sigma_pq","pi_sigma","phi_pq","match"]
assert cert == generated
assert [r for r in generated if r[-1] == 1] == [("p=2",2,17,54,16,16,1)]

# Large corroborative sweep for every n with Omega(n)<=2.
spf = list(range(LIMIT + 1))
spf[0] = 0
spf[1] = 1
for p in range(2, isqrt(LIMIT) + 1):
    if spf[p] == p:
        for m in range(p*p, LIMIT + 1, p):
            if spf[m] == m:
                spf[m] = p

isprime = sieve_primes(MAXSIGMA)
primepi = [0] * (MAXSIGMA + 1)
count = 0
for i in range(MAXSIGMA + 1):
    count += isprime[i]
    primepi[i] = count

def factor(n):
    out = []
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out.append((p,e))
    return out

hits = []
checked = 0
for n in range(2, LIMIT + 1):
    fac = factor(n)
    if sum(e for _, e in fac) > 2:
        continue
    checked += 1
    sigma = 1
    phi = 1
    for p,e in fac:
        sigma *= (p ** (e + 1) - 1) // (p - 1)
        phi *= p ** (e - 1) * (p - 1)
    assert sigma <= MAXSIGMA
    if primepi[sigma] == phi:
        hits.append(n)

assert hits == [3,9,34], hits
print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"low_omega_checked={checked}",
    f"exceptional_cases={len(generated)}",
    f"hits={hits}",
)
