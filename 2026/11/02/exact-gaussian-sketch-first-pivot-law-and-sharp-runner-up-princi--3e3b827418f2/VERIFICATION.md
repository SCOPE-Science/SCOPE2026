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

# Verification details

The exact formulas and asymptotic equivalences are proved in `RESULT.md`. The standalone `verify.py` uses Python, NumPy, SciPy and SymPy, with package requirements in `requirements.txt`.

It checks the joint-exceedance exponent gap by exact symbolic factorization; reconstructs the even-sketch-height first-pivot failure probability using rational arithmetic; independently compares it with a gamma-integral quadrature for five norm configurations; verifies beta-tail union bounds and the integer-beta polynomial identity; and tests the actual sketched-column-norm pivot decision with fixed-seed Gaussian simulations. It also checks representative finite-dimensional ratios against the first-order endpoint-Laplace asymptotic. The packaged verifier passed 80 assertions/check groups.

The random experiments are probabilistic consistency checks and cannot establish all-dimensional exact identities or asymptotic statements. The analytic proof covers fixed finite column count and a unique longest nonzero orthogonal column under exact arithmetic. No independent external audit or certification has been performed.
