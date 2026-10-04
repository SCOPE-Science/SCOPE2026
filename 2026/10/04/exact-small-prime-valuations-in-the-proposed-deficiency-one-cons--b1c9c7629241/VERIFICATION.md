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

The theorem is proved symbolically in `RESULT.md`. The standalone exact-integer program `verify.py` provides a separate computational check.

Running

`python3 verify.py`

produces exactly:

`VERIFY_OK k_cases=119 valuation_pairs=2037 deficiency_cases=119`

For every tested \(k\) from \(2\) through \(120\), the program constructs \(M\), computes \(\binom{M+k-1}{k}\) exactly, and checks the valuation formula for every prime \(p\le k\). It also divides each of \(M,M+1,\ldots,M+k-1\) by all primes at most \(k\) to verify that only \(M\) is \(k\)-smooth.

Finite verification does not establish the theorem for all \(k\); the universal statement follows from the carry and divisibility arguments in `RESULT.md`. The checker does not assess bibliographic originality.
