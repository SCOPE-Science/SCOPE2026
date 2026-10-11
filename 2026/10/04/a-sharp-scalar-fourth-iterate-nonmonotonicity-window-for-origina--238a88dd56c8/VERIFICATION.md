---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On the invariant eigendirection, the exact global-L FISTA step is multiplication by \(r=1-q\). With \(\beta_1=0\), the first coordinates satisfy \(x_1=rx_0\), \(x_2=r^2x_0\), \(x_3=r^2A(r)x_0\), and \(x_4=r^3B(r)x_0\), where \(A=(1+\beta_2)r-\beta_2\) and \(B=(1+\beta_3)A-\beta_3\). Since \(|A|<1\) on \(0<r<1\), the first three objective comparisons are strict decreases. The fourth rise is equivalent to \((rB-A)(rB+A)>0\); the two quadratic factors have the stated roots \(r_-\), \(1\), and the unique positive \(r_+\), giving exactly \(r_-<r<r_+\). At \(r_0=\beta_2/(1+\beta_2)\), \(A=0\) but \(B=-\beta_3\), so the bare recurrence hits the minimizer at the third point and leaves it at the fourth. The inspected high-precision checker corroborates the root order and direct iterates; the proof is algebraic.

## originality

PASS

The original FISTA source and later literature establish the recurrence, global accelerated rate, and the broad fact that FISTA can be nonmonotone/oscillatory. The monotone-FISTA follow-up explicitly motivates a monotone variant, and Liang–Fadili–Peyré explains local oscillation. No inspected statement gives the exact earliest objective-rise index and sharp curvature interval for the original constant-L recurrence, nor the exact hit-and-leave resonance. Resultary search found related spike/frontier results for other methods or Nesterov parameterizations but no implication-equivalent FISTA theorem. Full primary FISTA text was not accessible through the available publisher route during closeout, so that is retained as a literature risk rather than treated as novelty evidence.

## value

PASS

FISTA's nonmonotonicity is important enough to have motivated monotone variants. Pinning down the earliest possible rise and the exact curvature window on an exact-global-L quadratic gives a clean mechanism, while the optimizer-hit-and-immediate-leave resonance sharply illustrates the role of inertial history. This is a motivated boundary/counterexample rather than an arbitrary tiny-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
