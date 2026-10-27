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

Run `python check.py` with Python 3, NumPy, SciPy and SymPy. The check reconstructs the reduction's discriminant symbolically and verifies its rotated version, integrates the normalized Student density, tests the two exact low-dimensional constants, numerically integrates the probability and near-collision factor, verifies a real positive-definite matrix with a nonreal sketched conjugate pair, and compares 60,000 independent Gaussian sketches per each of three oversampling levels with the exact integrals. All these computations were executed successfully on the packaged code in a local Python environment.

These finite numerical and symbolic test cases do not establish the universal law or asymptotic claims; their mathematical justification is the conditional-Gaussian/Wishart density calculation, discriminant criterion, dominated convergence and exact beta/polar integrations in `RESULT.md`. The numerical quadrature uses SciPy tolerances and its printed decimals are approximations, not certified interval enclosures.
