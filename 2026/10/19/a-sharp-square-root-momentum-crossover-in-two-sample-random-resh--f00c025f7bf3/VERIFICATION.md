---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Both component updates have the same companion matrix A with first row (1+b-r,-b). The two gradient shifts occur as opposite signs, so the epoch has matrix A^2 and innovation (A-I)(r,0)^T times an independent sign. The strict quadratic Schur inequalities are 1-b>0, r>0 and 2(1+b)-r>0, as needed. For deterministic starting states the transient mean decays and the covariance is the unique solution of the convergent discrete Lyapunov series. I solved the vectorized four-entry problem over the rational function field independently, recovering the two phase variances, their cross entry and the iid formula (replay: python /workspace/branches/independent-continuous.py reshuffling). The denominator is positive since its last factor is (r-1-b)^2+(1-b)^2. The leading fixed-b coefficients for the epoch and odd variances are respectively b^2/(1-b^4) and 1/(1-b^4); at b=0 the epoch numerator starts one power later. In the joint limit the numerator bracket is 4b^2+r+O((r+b)(b^2+r)) and the denominator is 4+O(r+b), proving the relative error uniformly as both go to zero. This gives precisely b=O(sqrt(r)) for an O(r^3) epoch floor and the stated constants in the limiting regimes. The proof concerns the invariant second moments, not pathwise convergence of constant-step iterates.

## originality

PASS

The with-replacement formula, zero-momentum completed-epoch formula and phase-averaged heavy-ball reshuffling variance have direct prior coverage. The distinct content is the exact phase-specific covariance at positive momentum and the uniform vanishing-momentum crossover in the completed-epoch floor. The strongest published covariance source was read in primary text and does not give separate phase variances in its analytic RR formula; the averaging removes the distinction that drives the crossover.

## value

PASS

End-of-epoch output is a natural algorithm choice. This smallest noninterpolating equal-Hessian pair separates what a practitioner sees at that output from the mean over all individual iterates. In particular the cubic floor is lost at any fixed positive momentum and preserved exactly for momentum schedules bounded on the square-root stepsize scale. That precise balance, and the contrasting odd phase, explain behavior not visible in the established phase mixture. The result is a benchmark, not a general heavy-ball guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
