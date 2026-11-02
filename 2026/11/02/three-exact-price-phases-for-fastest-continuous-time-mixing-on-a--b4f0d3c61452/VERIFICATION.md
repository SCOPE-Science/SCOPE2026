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

# Reproducibility and verification limits

The included `verify.py` was executed with Python 3, SymPy, NumPy and SciPy and passed symbolic spectra at five sizes \(k=2,\ldots,6\), three exact-rational phase representatives, 54 explicit phase-boundary identities, and 40 numerical comparisons against freely varying individual edge rates. The numerical checks are finite and supplementary. The all-parameter correctness argument is in `RESULT.md`: characteristic polynomial factorization, an exact unit-gap feasible set, strict convexity and an unrestricted uniqueness argument. No independent audit has been performed. The examples do not establish priority, which is assessed separately from the source statements and their objectives.
