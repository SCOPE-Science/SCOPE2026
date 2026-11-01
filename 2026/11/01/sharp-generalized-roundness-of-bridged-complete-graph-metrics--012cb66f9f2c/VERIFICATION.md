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

# Verification of the bridge-barbell negative-type classification

The standalone verifier is `verify_bridge_barbells.py`. Run with Python 3 and installed NumPy and SciPy:

`python verify_bridge_barbells.py`

The script constructs the unit graph shortest-path matrix directly for each pair of clique sizes; it does not use a saved distance table. It compares the full zero-sum quadratic form to the proof's reduction using exact rational arithmetic for 525 tests. It then compares the two-by-two threshold root with the eigenvalues of the separately centered powered-distance Gram matrix for 100 pairs and checks critical rank and near-endpoint signs. It evaluates 81 strict-monotonicity comparisons and five two-parameter asymptotic cases.

Observed successful output:

```
EXACT_QUADRATIC_FORM_OK 525
CRITICAL_INERTIA_OK 100
STRICT_MONOTONICITY_CHECK_OK 81
ASYMPTOTIC_CHECK_OK limit= 1.709511291351 coefficient= 0.188526473848
ALL_BRIDGE_BARBELL_CHECKS_OK
```

The exact form checks use integer exponents \(1,2,3\), not arbitrary real exponents. Floating-point spectral comparisons test finite instances, not universal signs or rigorous root error bounds. The analytic argument in `RESULT.md` proves the universal real-exponent classification, monotonicity, and asymptotic law; the verifier is corroboration only.
