#!/usr/bin/env python3
import json
from pathlib import Path

def fib_prefix(N):
    s = "0"
    while len(s) < N:
        s = "".join("01" if c == "0" else "0" for c in s)
    return s[:N]

def min_block_factor(s, k, max_m):
    for m in range(1, max_m + 1):
        if k*m > len(s):
            break
        blocks = [s[j*m:(j+1)*m] for j in range(k)]
        if len(set(blocks)) == k:
            return m
    return None

def block_profile(s, k, M):
    out = []
    for m in range(1, M + 1):
        blocks = [s[j*m:(j+1)*m] for j in range(k)]
        out.append((m, blocks, len(set(blocks))))
    return out

root = Path(__file__).resolve().parent
cert = json.loads((root / "certificate.json").read_text(encoding="utf-8"))
f = fib_prefix(5000)

expected = {(3,6):(18,19), (4,10):(40,41)}
for case in cert["cases"]:
    k = case["k"]
    M = case["claimed_radius"]
    N, expected_count = expected[(k,M)]
    assert case["window_length"] == N
    factors = sorted({f[i:i+N] for i in range(len(f)-N+1)})
    # The Fibonacci word is Sturmian, so it has exactly N+1 length-N factors.
    # Observing N+1 distinct factors in this prefix therefore exhausts all of them.
    assert len(factors) == expected_count == N + 1
    rebuilt = [{"factor":x,"minimum_block_length":min_block_factor(x,k,M)} for x in factors]
    assert rebuilt == case["rows"]
    vals = [r["minimum_block_length"] for r in rebuilt]
    assert all(v is not None for v in vals)
    assert max(vals) == M

w3 = cert["witnesses"]["k3"]
w4 = cert["witnesses"]["k4"]
assert f[w3["index"]:w3["index"]+18] == w3["factor"]
assert f[w4["index"]:w4["index"]+40] == w4["factor"]

p3 = block_profile(w3["factor"], 3, 6)
assert [q[2] for q in p3[:5]] == [2,2,2,2,2]
assert p3[5][2] == 3

p4 = block_profile(w4["factor"], 4, 10)
assert all(q[2] < 4 for q in p4[:9])
assert p4[9][2] == 4

dist3 = {}
dist4 = {}
for case in cert["cases"]:
    d = {}
    for r in case["rows"]:
        d[r["minimum_block_length"]] = d.get(r["minimum_block_length"],0) + 1
    if case["k"] == 3:
        dist3 = d
    else:
        dist4 = d

assert dist3 == {2:8,3:4,4:1,5:2,6:4}
assert dist4 == {3:4,4:2,5:4,6:27,7:2,9:1,10:1}

print(
    "VERIFY_OK "
    "factors18=19 factors40=41 "
    "R3=6 R4=10 "
    "dist3=2:8,3:4,4:1,5:2,6:4 "
    "dist4=3:4,4:2,5:4,6:27,7:2,9:1,10:1"
)
