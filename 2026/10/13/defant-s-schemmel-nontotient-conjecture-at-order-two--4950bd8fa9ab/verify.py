#!/usr/bin/env python3
import json
from math import gcd, prod
from pathlib import Path

CERT_PATH = Path(__file__).with_name("cover_certificate.json")
cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
rows = cert["rows"]
period = cert["period"]
M = cert["crt_modulus"]
C = cert["crt_residue"]

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def divisors(n):
    out = []
    for d in range(1, int(n ** 0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)

def multiplicative_order(a, q):
    assert gcd(a, q) == 1
    for d in divisors(q - 1):
        if pow(a, d, q) == 1:
            return d
    raise AssertionError("order not found")

for row in rows:
    a, m, q, c = row["a"], row["m"], row["q"], row["c"]
    assert is_prime(q), q
    assert multiplicative_order(3, q) == m, (q, m)
    assert (pow(3, a, q) * c + 2) % q == 0, (a, m, q, c)

coverage = []
for t in range(period):
    hits = [row for row in rows if t % row["m"] == row["a"]]
    assert hits, t
    coverage.append(len(hits))

assert prod(row["q"] for row in rows) == M
assert gcd(C, M) == 1
for row in rows:
    assert C % row["q"] == row["c"], row

powers41 = [pow(3, s, 41) for s in range(8)]
assert len(set(powers41)) == 8
assert 11 not in powers41
assert C % 41 == 13

# Periodic all-t divisibility replay for several complete periods.
for t in range(0, 10 * period):
    ok = False
    for row in rows:
        if t % row["m"] == row["a"]:
            q = row["q"]
            assert (pow(3, t, q) * (C % q) + 2) % q == 0
            ok = True
    assert ok

print(
    "VERIFY_OK",
    f"rows={len(rows)}",
    f"period={period}",
    f"coverage_min={min(coverage)}",
    f"coverage_max={max(coverage)}",
    f"M={M}",
    f"C={C}",
    f"powers_mod_41={powers41}",
)
