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

# Reproducibility and scope
Run `python verify_width.py` with Python 3.10 or newer, NumPy and SciPy. The script deterministically builds all signed edge roots of \(K_{p,q}\), projects Gaussian directions to the sum-zero subspace, and independently compares the direct vertex support calculation with the exact four-extreme reduction for \(2\le p\le7\) and \(2\le q\le8\). It also uses independent numerical quadrature to compare the integral CDF of a sum of two Gumbels against the Bessel-\(K_1\) expression at five arguments.

Expected completion line: `VERIFY_OK root_support_comparisons=840 Bessel_integral_checks=5`. The tests were executed against this same standalone source file. They verify finite support and integral formulas only. The all-dimensional assertions rely on the analytical Gaussian-tail and chi-square estimates in `RESULT.md` and are not claimed as computer-certified. Independent auditing was not performed.
