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
The verifier uses only the Python standard library.

It evaluates the exact finite-\(k\) normalized expectation obtained by integrating the unmarked-tree survival probability. The calculation is performed in logarithmic form to avoid overflow. At the claimed optimum, the values for increasing \(k\) approach the limiting integral from above.

The verifier separately computes the dilogarithm by its convergent power series, solves the degree-\(2\) KKT equation by bisection, and evaluates the limiting integral after the substitution \(t=1-e^{-s}\), which removes the logarithmic endpoint singularity.

These numerical checks do not certify the infinite limit by themselves. The universal argument is the graph-recovery equivalence, exact Poisson component formula, rooted-tree generating-function identity, and dominated-convergence proof in `RESULT.md`.
