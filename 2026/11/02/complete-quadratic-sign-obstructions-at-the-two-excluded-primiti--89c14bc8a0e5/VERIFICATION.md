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

# Exact finite verification

Run `python3 verify.py` from the directory containing this file. The script first enumerates the complete projective coefficient space at each of two primes, checks the full exceptional lists, and then enumerates every raw coefficient triple independently, checking that its normalized obstruction classes agree with the projective table. It uses Python integer modular arithmetic only; no external packages, randomization, published tables, or unprovided dependencies.

For prime 19, all 360 admissible projective classes are checked, resulting in exactly 9 exceptions, with 162 exceptional admissible raw triples. For prime 31, all 960 admissible projective classes are checked, resulting in exactly 3 exceptions, with 90 exceptional admissible raw triples. The proof is exhaustive at these two primes and makes no inference about other primes.

The archive's dated version 2014-05-29 supplied the earlier primitive-root polynomial context. The explicit excluded-prime conjecture was inspected in a later source revision (2020-02-28), and that distinction is retained in the science account.
