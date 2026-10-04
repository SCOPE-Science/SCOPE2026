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

The checker replays the three exact factorization branches for distinct odd primes, verifies the prime-square inequalities, and confirms directly that
\[
15=3\cdot5
\]
satisfies
\[
\frac{2n}{\sigma(n)}-1=\frac14.
\]

It additionally enumerates all odd semiprimes up to \(200000\) and finds only \(15\). That finite enumeration is a regression check only; the proof of exhaustiveness is the unbounded factorization argument.

A successful replay prints `VERIFY_OK`.
