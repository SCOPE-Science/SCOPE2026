#!/usr/bin/env python3
import json
from fractions import Fraction
from pathlib import Path

ALPHABET = "012"
F = {"0":"0","1":"01","2":"011"}
START = "0121012"

def morph(u):
    return "".join(F[c] for c in u)

def least_period(s):
    for p in range(1, len(s)+1):
        if all(s[j] == s[j-p] for j in range(p, len(s))):
            return p
    raise AssertionError("period search failed")

def is_14_5_free_direct(w):
    n = len(w)
    for i in range(n):
        for j in range(i+1, n+1):
            s = w[i:j]
            p = least_period(s)
            if 5*len(s) >= 14*p:
                return False
    return True

def is_rich_factor_set(w):
    pals = set()
    n = len(w)
    for i in range(n):
        for j in range(i+1, n+1):
            s = w[i:j]
            if s == s[::-1]:
                pals.add(s)
    return len(pals) == n

def occurrences(text, pat):
    m = len(pat)
    return sum(text[i:i+m] == pat for i in range(len(text)-m+1))

def is_rich_lps(w):
    # Equivalent prefix criterion: every nonempty prefix has a
    # unioccurrent longest palindromic suffix.
    for end in range(1, len(w)+1):
        z = w[:end]
        lps = None
        for L in range(len(z), 0, -1):
            s = z[-L:]
            if s == s[::-1]:
                lps = s
                break
        assert lps is not None
        if occurrences(z, lps) != 1:
            return False
    return True

def good_a(u):
    w = morph(u)
    return is_rich_factor_set(w) and is_14_5_free_direct(w)

def good_b(u):
    w = morph(u)
    return is_rich_lps(w) and is_14_5_free_direct(w)

def enumerate_with(pred):
    levels = {len(START): [START]}
    assert pred(START)
    for n in range(len(START)+1, 51):
        nxt = []
        for u in levels[n-1]:
            for c in ALPHABET:
                q = u + c
                if pred(q):
                    nxt.append(q)
        levels[n] = sorted(nxt)
    return levels

def critical_exponent(w):
    best = Fraction(1,1)
    best_data = None
    for i in range(len(w)):
        for j in range(i+1, len(w)+1):
            s = w[i:j]
            p = least_period(s)
            e = Fraction(len(s), p)
            if e > best:
                best = e
                best_data = (i,j,p,s)
    return best, best_data

root = Path(__file__).resolve().parent
cert = json.loads((root/"certificate.json").read_text(encoding="utf-8"))

A = enumerate_with(good_a)
B = enumerate_with(good_b)
expected = {int(k):v for k,v in cert["survivor_counts_by_preimage_length"].items()}
assert {n:len(A[n]) for n in expected} == expected
assert {n:len(B[n]) for n in expected} == expected
assert A == B

assert len(A[49]) == 3
assert A[49] == sorted(cert["length_49_extremizers"])
assert A[50] == []

for row in cert["extremizer_checks"]:
    u = row["preimage"]
    w = morph(u)
    assert len(u) == 49
    assert w == row["binary_image"]
    assert len(w) == row["image_length"]
    assert is_rich_factor_set(w)
    assert is_rich_lps(w)
    assert is_14_5_free_direct(w)
    ce, data = critical_exponent(w)
    assert ce.numerator == row["critical_exponent_numerator"]
    assert ce.denominator == row["critical_exponent_denominator"]
    assert 5*ce.numerator < 14*ce.denominator
    assert data[0] == row["critical_factor_start_0_based"]
    assert data[1] == row["critical_factor_end_exclusive_0_based"]
    assert data[2] == row["critical_period"]

cp = cert["common_prefix"]
assert len(cp) == 47
assert all(u.startswith(cp) for u in A[49])
assert sorted(u[47:] for u in A[49]) == ["00","01","20"]

print(
    "VERIFY_OK start=0121012 max_preimage=49 extremizers=3 "
    "length50=0 richness_methods=2 common_prefix=47 counts="
    + ",".join(f"{n}:{expected[n]}" for n in sorted(expected))
)
