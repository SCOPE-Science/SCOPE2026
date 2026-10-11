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
Run `python verify.py` from a directory with Python 3, NumPy, SciPy and mpmath installed. The code uses a fixed seed, independent union-normal polygon area geometry, adaptive quadrature, direct tangential area identities, sampled gap inequalities, and high-precision asymptotic comparisons. The run returned `VERIFY_OK 6012 checks; asymptotic_ratios= [1.1404796236093042, 1.069193749678258, 1.0343244178686752]`.

The verifier is not a formal certificate for all \(n,m\), or all polygons. The all-quantifier proof is analytic and is supplied in `RESULT.md`. No separate outside audit or validation has been performed. Additional bibliographic checking would be needed before any external novelty or priority assertion.
