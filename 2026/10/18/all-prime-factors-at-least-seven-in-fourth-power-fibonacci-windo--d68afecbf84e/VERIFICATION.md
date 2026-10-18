---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 artifacts/verify.py` using a Python standard-library interpreter. The independent script checks the formula for every length \(1\le k\le400\), constructs the integer quartic Fibonacci windows directly, calculates their gcd from the first five translates, tests that the next four translates yield the same gcd, factors all relevant lengths and gcds, computes multiplicative orders in \(\mathbb F_p[t]/(t^2+3t+1)\), and verifies each prediction for prime factors at least seven. Successful output is `PASS quartic prime-primary checks, lengths 1..400`. The infinitely quantified theorem follows from the algebraic proof, not these tests.

The exceptional prime factors \(2,3,5\) are not classified. No external or independent mathematical audit has been performed.
