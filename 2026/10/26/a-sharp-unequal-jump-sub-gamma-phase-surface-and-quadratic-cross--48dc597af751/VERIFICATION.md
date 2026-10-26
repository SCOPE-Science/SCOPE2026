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
# Reproducibility and limitations

Run `python verify.py` with Python 3 and available `scipy` and `mpmath`. The program computes the moment-generating function independently from the distributions, checks the exact rational coefficient comparison for a finite degree range, and verifies phase and near-critical values at multiple parameter pairs. Its observed output was `PASS {'exact_coefficients': 1680, 'phase_examples': 21, 'near_critical': 10}`.

The non-computational steps essential to correctness are the uniform ratio inequality for all coefficients, the strict local Taylor obstruction, the compactness argument for interior attainment, the uniform separation from the critical global supremum, and the implicit-function expansion. Neither a numerical optimizer nor finitely many coefficients can prove an infinite-domain sub-gamma inequality, and no claim of independent validation is made.
