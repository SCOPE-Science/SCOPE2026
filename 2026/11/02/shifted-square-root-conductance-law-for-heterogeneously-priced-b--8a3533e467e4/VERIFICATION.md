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

## Reproducibility

Run `python check_biclique.py` with NumPy, SciPy, and SymPy. The checker independently builds weighted Laplacian matrices and computes nonzero eigenvalues; it does not assume the resistance reduction used in the proof. An exact-rational \(K_{3,4}\) test compares a direct pseudoinverse with the analytically reduced resistance objective.

## Actual checks

The script completed one exact-rational identity, 96 spectrum-versus-formula comparisons, 96 budget-and-KKT comparisons, 2,400 independently asymmetric budget-feasible allocation comparisons, four unrestricted SLSQP numerical optimizer comparisons, and three large-right-class asymptotic samples. The root equation was solved by bracketing on its proven admissible interval. The independent optimizers used arbitrary edge variables rather than enforcing row symmetry.

## Logical scope

Finite tests do not establish uniqueness, a global lower bound, or large-\(q\) limits. Those follow from strict convexity, the electrical reduction, unique scalar-root characterization, and asymptotic analysis in `RESULT.md`. The numerical optimizer is an additional check rather than a certificate of global optimality. Full-text coverage of all possible historical sources is not asserted.
