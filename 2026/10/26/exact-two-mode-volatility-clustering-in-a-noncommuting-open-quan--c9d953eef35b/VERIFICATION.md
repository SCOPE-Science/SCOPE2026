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

Execute `python verify.py` in an environment with NumPy and SciPy. The program constructs the exact five matrices independently using a Hermitian matrix square root; verifies channel eigenmodes and the stationary state; then enumerates all 5, 25, 125, 625, 3125 and 15625 possible labelled instrument histories for six consecutive observation horizons and five admissible preparations. It verifies normalization, the vanishing signed mean, the unrestricted finite-\(n\) displacement-variance formula at these values, and stationary quadratic-variation variance. It additionally checks 29 exact squared-jump lag autocovariances and 50 sharp Bloch-envelope values.

The reported limiting variance is evaluated from the displayed exact geometric-series expression, not extrapolated from finite simulation. Critical statements for all integers follow from the algebraic channel decomposition and geometric summation in RESULT.md; no finite computational enumeration is described as an infinite proof.

The source Kraus operators and previous literature are provided in RESULT.md. No external auditor or formal proof assistant has assessed this package.
