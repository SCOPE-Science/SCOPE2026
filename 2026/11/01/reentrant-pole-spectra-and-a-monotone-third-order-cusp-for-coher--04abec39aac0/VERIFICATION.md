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

# Verification of the exact spectral classification

The standalone script `checker.py` requires Python 3, SymPy, NumPy and SciPy. Run `python checker.py` from the extracted package directory; the script was executed successfully with the package's own source. It certifies symbolic identities for the discriminant, double-root parametrization and cusp, inverse Laplace formula and monotonicity factorization; exact rational example checks and 756 independently computed root comparisons support the analytic statements.

The written proof, not the sampled tests, justifies the all-positive-parameter root classification. The physical decoherence model is taken from the cited primary research. The calculation concerns the transfer-function poles and, at the cusp only, the coherent ergotropy of an equatorial pure qubit. It does not prove an all-parameter information-backflow transition, microscopic complete positivity, or publication uniqueness. Independent validation has not been performed.
