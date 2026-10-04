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
Run `python3 verify.py`.

The checker implements the exact largest-prime peeling procedure with rational arithmetic.

It performs three finite regression checks:

1. It generates every nonempty exponent vector with entries in
\[
\{0,1,2\}
\]
on the eight primes
\[
2,3,5,7,11,13,17,19,
\]
for a total of
\[
3^8-1=6560
\]
products, and verifies exact recovery of the original exponent vector.

2. It checks every positive integer
\[
n\le20000
\]
and verifies that the decoder accepts exactly the integers whose prime factors are all in
\[
\{2,3\}.
\]

3. It scans every reduced positive rational with numerator and denominator at most \(250\). Whenever the decoder accepts, it reconstructs the rational exactly from the recovered exponent vector and verifies that every exponent is nonnegative.

These computations are regression evidence only. The all-rational decision theorem is proved in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
