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
# Verification

The checkerboard density has exact rational cell heights and uniform margins. The analytical proof supplies the factorization through adjacent averaging matrices, the Cauchy–Binet argument for TP2 and a uniform perturbation bound controlling the strict negative PMI contrast. The accompanying exact-rational verifier checks the displayed matrix, all 225 ordered two-by-two minors, both marginal sums, strict positivity after smoothing, and the negative reflection contrast on the specified open rectangle.

To reproduce, execute `python3 verify_positive_tp2_not_pmi.py` in a Python 3 standard-library environment. A successful run prints three PASS/contrast lines. The finite computations are not being used as an infinite search: the density is piecewise constant on a six-by-six grid, so the matrix minors exhaust all ordered-point TP2 inequalities, and the exact open-cell PMI defect disproves the measure property. Boundary conventions are chosen consistently and have no effect on the induced copula measure.

No claim is made that the checkerboard counterexample has a smooth density, minimizes the number of cells, or violates particular integrated concordance inequalities.
