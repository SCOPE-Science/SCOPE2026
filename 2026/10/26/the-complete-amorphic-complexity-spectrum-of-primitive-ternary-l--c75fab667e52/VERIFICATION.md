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

# Reproducibility and limits

Execute `python3 verify.py` with Python 3 and no third-party packages. Its full finite input domain is all \(729\) ordered triples of two-symbol images, not sampled rules. It tests all primitive incidence matrices, all pair-discrepancy matrices, each exact characteristic polynomial by two determinant formulas, the six explicit three-cycle exceptions, the nilpotent conditions, and the class-size identities. Expected successful terminal output begins `EXHAUSTIVE EXACT CENSUS PASSED`.

The general relation between the spectral radius and the infinite-time amorphic complexity, and between values \(0,1\) and tame/null status, is taken from the referenced Gröger--Krawczyk theorems. Finite exhaustive enumeration verifies the finite arithmetic classification only; it is not a substitute for those results. The primitive exponent bound and height decomposition are mathematically stated in RESULT.md. No independent external audit has been performed.
