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

# Reproduction and limits

Run `python checks/commutator_check.py` with Python 3, NumPy, and SciPy. The script uses deterministic explicit symmetric positive-definite two- and three-dimensional curvature matrices. It optimizes the orthogonal branch numerically and, separately, evaluates the symmetric-positive-definite normal certificate needed to infer global optimality at those tested points. The predicted generator slopes and scaled model-value gaps converge toward the analytic formulas as the curvature parameter decreases. The proof, not the numerical optimization, establishes all-dimensional and exact claims.

In the planar example with positive singular values \(3,1\), radius \(1\), and the positive-definite factors given in RESULT.md, the analytic generator slope is \(-1/8\) and the model improvement coefficient is \(1/32\). Direct symbolic differentiation of the rotation family gives the displayed expansion in RESULT.md. In the three-dimensional test, positive normal-certificate eigenvalues and small skew residuals verify the chosen computed points up to floating-point tolerances.

The local implicit-function argument relies on the strictly positive singular values of the gradient. It does not extend by continuity to singular gradients without additional analysis. A positive semidefinite normal certificate is exact only at a scaled-orthogonal candidate; the checker is not a general-purpose semidefinite optimizer. No physical-model inference, empirical training-loss claim or independent audit is included.
