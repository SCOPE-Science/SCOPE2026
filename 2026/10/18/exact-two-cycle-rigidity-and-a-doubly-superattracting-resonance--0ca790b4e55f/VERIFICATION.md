---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The sum of vertical increments over a primitive two-cycle is c(x0+x1)=0. Because c≠0, x1=−x0; x0=0 would imply a fixed point. Thus the two horizontal multipliers are both −1, forcing a=−2(1+y0²)=−2(1+y1²). The ordinates differ by cx0≠0, so they are exactly u and −u with u>0, and the horizontal coordinates follow. Reversal of sign merely exchanges the two points. Direct substitution gives existence for all a<−2 and the equality endpoint gives no primitive cycle. At both points xy=−2u²/c; the derivative is the same trace-zero matrix with entries (−1, −8u²/[c(1+u²)]; c, 1). Its square is minus its determinant times the identity, i.e. (1−7u²)/(1+u²) I. This gives the sink/source windows and the repeated −1 endpoint. At a=−16/7 the return derivative is the zero operator, not merely a matrix with two zero eigenvalues. Since the return is smooth on the plane, at each point the return error obeys a local O(norm(error)²) bound and hence converges for sufficiently small initial errors. No nonlinear classification follows at the repeated −1 endpoint. Independent bounded replay: python3 /workspace/branches/independent_replays.py, function cycle, checked both orbit points and coordinate directions for ten rational cases and the three multiplier parameters. The identity and exhaustion are analytic, not inferred from the samples.

## originality

PASS

Pass is for the exact global primitive two-cycle census and scalar two-step derivative in the zero-offset family, including the isolated quadratic-attraction parameter. No source examined states a matching theorem. The parent model and the numerical two-cycle observation attributed to its authors are not credited as new. The parent primary text remains inaccessible in the bounded lawful attempts; the scientific verdict does not assert what that text omits.

## value

PASS

The parameter slice is motivated by reported period-two behavior in the parent map. The result resolves an exact all-plane orbit count and its full two-step linearization, not just a numerical stability fit. The scalar return exposes distinct exact boundaries, especially a zero return operator with quadratic attraction, giving testable parameters and a starting point for an analysis of the unsolved nonlinear endpoint. The contribution is the combined family-specific classification, not the standard trace-zero matrix identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
