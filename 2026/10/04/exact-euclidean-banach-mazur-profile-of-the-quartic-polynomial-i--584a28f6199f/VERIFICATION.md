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

The proof was checked symbolically from the defining norm. For an arbitrary positive-definite quadratic form, finite-group averaging keeps the same lower and upper comparison constants and reduces the form to a scalar multiple of the Euclidean quadratic form. This establishes global optimality without a numerical optimizer.

On the Euclidean unit circle, the exact identity
\[
N_\beta(x,y)^4=1+2(\beta-1)x^2y^2
\]
reduces the remaining calculation to the interval \(0\le x^2y^2\le1/4\). Axes and diagonals provide the exact extrema, yielding the two displayed branches.

The bundled `verify.py` uses rational arithmetic only as a supplementary consistency check. It checks representative branch values and verifies exactly that the source transformation \(\gamma=(3-\beta)/(1+\beta)\) carries the upper branch into the lower one. Its output is `VERIFY_OK`. Finite replay is not used as proof of the continuum statement.

Limit: no independent audit has been performed, and no claim is made about nonsymmetric cubic-index-zero planes or classification of every optimal linear map.
