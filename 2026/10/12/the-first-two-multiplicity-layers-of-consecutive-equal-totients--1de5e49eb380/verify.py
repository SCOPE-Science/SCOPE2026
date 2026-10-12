#!/usr/bin/env python3
from array import array

LIMIT = 2_000_000
N = LIMIT + 1

phi = array("I", range(N + 1))
for p in range(2, N + 1):
    if phi[p] == p:
        for m in range(p, N + 1, p):
            phi[m] -= phi[m] // p

omega = bytearray(N + 1)
spf = array("I", [0]) * (N + 1)
for i in range(2, N + 1):
    if spf[i] == 0:
        for m in range(i, N + 1, i):
            if spf[m] == 0:
                spf[m] = i
for n in range(2, N + 1):
    p = spf[n]
    omega[n] = omega[n // p] + 1

all_hits = []
low_hits = []
for n in range(2, LIMIT + 1):
    if phi[n] == phi[n + 1]:
        all_hits.append(n)
        if omega[n] <= 2 and omega[n + 1] <= 2:
            low_hits.append(n)

assert low_hits == [3]
assert 3 in all_hits and 15 in all_hits and 164 in all_hits and 194 in all_hits

print(
    "VERIFY_OK",
    f"limit={LIMIT}",
    f"equal_totient_count={len(all_hits)}",
    f"low_layer={low_hits}",
    f"first_hits={all_hits[:8]}",
)
