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

# Reproducibility

The accompanying `verify_hasse_witt.py` requires Python 3 standard library only. Run `python3 verify_hasse_witt.py` and require `VERIFY_OK`. It checks all Cartier coefficients generated directly from the binomial expansion; predicted block entries and counts; factorial Hankel leading determinants; and specialized rank for small odd primes. Tested primes are 3, 5, 7, 11, 13, 17, 19, and 23.

The mathematical proof is universal and does not infer an all-prime statement from these finite tests. Specifically, the proof verifies the residue congruence, the exhaustive block partition, the minor-order lower bound, and an invertible Vandermonde determinant for every admissible block size.

Scope limitations: the relative Smith factors are for the specific coefficient affine line and linearized Hasse–Witt map. No independent audit or external certification was performed.
