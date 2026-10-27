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

The proof checks are algebraic and probabilistic, not finite-enumeration claims:

- The one-step inclusion probability is \(2x_i-x_i^2\), because either draw may carry colour \(i\) and the overlap event has probability \(x_i^2\).
- Summing these inclusion probabilities gives the conditional expected total increment \(2-\sum_i x_i^2\).
- The normalized drift follows from the exact quotient update and the deterministic bound \(1\le\Delta T\le2\).
- The Lyapunov gap is nonnegative by Cauchy–Schwarz and vanishes precisely at uniform distributions on subsets.
- The total-count bounds imply \(\sum_n T_n^{-2}<\infty\) and \(\sum_n T_n^{-1}\asymp\log n\).
- Conditional Borel–Cantelli proves every colour count diverges; the logarithmic martingale argument excludes convergence to a proper face.

No simulation or finite computation is used to certify the infinite-time conclusion. The theorem does not establish a rate or a fluctuation law.
