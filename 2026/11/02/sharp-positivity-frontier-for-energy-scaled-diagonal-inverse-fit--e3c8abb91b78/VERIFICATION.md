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

# Evidence and reproduction

The closed-form normal equations are \((A\circ A)x=\operatorname{diag}(A)\). Writing \(H=R\circ R\) after normalizing the SPD matrix by its positive diagonal yields a strictly positive-definite Hessian. The displayed formulas follow from exact three-by-three cofactors. The star-family cone-constrained optimizer is certified by its gradient and the nonnegative orthant's KKT conditions; its objective gap is a rational identity. An explicit rational witness has SPD leading principal minors \(1,19/100,3/125\) and exact fitted coefficients \((-650,950,950)/889\).

To reproduce the computational checks, execute `python verify.py` with a standard Python 3 interpreter from the directory containing the extracted file. The verified output was `PASS: 3614 exact-rational assertions / grouped checks; analytic proof required for universal quantifiers.` Its seeded finite grids support the exact identities without serving as proof for all SPD matrices or all parameters.

No independent validation, floating-point error analysis, or general-purpose PDE implementation is asserted. Historical novelty remains subject to wider archival review.
