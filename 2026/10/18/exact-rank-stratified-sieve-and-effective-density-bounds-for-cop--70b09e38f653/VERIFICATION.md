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

Run `python3 verify.py` using a standard Python 3 interpreter. No third-party packages are required. The script computes exact ranks in finite quadratic algebras, verifies the first 167 relevant ranks against direct recurrence iteration, checks 10,000 gcd values by companion-matrix powering, recomputes an eleven-prime finite sieve using exact rational inclusion-exclusion, and verifies the integer-rounded event-density sum through 100,000.

All these checks passed during preparation of this package. The infinite-density conclusion uses a separate symbolic proof and the published Rosser--Schoenfeld prime-counting inequality. The finite tests do not prove universal identities or independent verification.
