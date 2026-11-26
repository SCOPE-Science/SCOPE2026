---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The stale term after initialization is the gradient of the other component at the preceding iterate, and averaging the components gives h=alpha/2. The scalar cycle product has trace 1-2(a+b)h+ab h^2 and determinant ab h^2. The three strict Jury quantities are 1-ab h^2, 2(a+b)h and 2(1-ah)(1-bh). The last factor gives a root -1 at h=1/max(a,b). For h above that threshold, either the smaller-curvature factor is still positive, so p(-1)<0 gives a root below -1, or h times the smaller curvature is at least one, so the determinant is strictly greater than one. This includes the second endpoint h=1/min(a,b) in the unequal case, which the frozen prose leaves implicit. Orthogonal simultaneous diagonalization gives the criterion for all initialized lifted histories; one unstable cycle mode suffices. In the scalar case the larger positive root decreases strictly before the first coalescence t=2 sqrt(ab) h, by implicit differentiation (t'<0 and d'>0). The determinant bound rho>=sqrt(ab)h strictly excludes every step above the coalescence, stable or not. At coalescence the upper off-diagonal is nonzero, so the Jordan power formula gives the claimed norm order. Replayed exact representative endpoints in reproductions/frozen_checks.py (argument 4); these are consistency checks, not the universal proof.

## originality

PASS

The periodic lifted IAG dynamics and general linear convergence for a sufficiently small step are inherited. The supported distinction is the exact necessary-and-sufficient boundary for two commuting SPD components and the unique scalar spectral-rate optimizer, realized at a defective positive eigenvalue. The closest same-algorithm literature gives the general period map or sufficient estimates, not a covering exact classification. The retrieved nearby exact frontiers govern different updates. This is a bounded best-of-knowledge comparison, not certification of priority.

## value

PASS

Two components are the first case where one stored component gradient is genuinely stale. The result calibrates sufficient delays-based step bounds by an exact stability ceiling for an entire commuting class and identifies a unique useful scalar tuning rule. The defective optimum explains why root-asymptotic and finite-horizon performance need not agree. No optimal matrix step or extension to noncommuting, nonlinear, or finite-precision settings is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
