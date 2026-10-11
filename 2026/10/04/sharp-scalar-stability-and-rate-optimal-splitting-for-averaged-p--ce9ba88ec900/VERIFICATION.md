---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Independent symbolic reconstruction confirms the recurrence and every boundary. The Jury margins reduce to t(γ+1)/(2(1+γt)), [4+3(γ-1)t]/[2(1+γt)], and a positive third margin, giving the exact finite ceiling only when γ<1. The roots have opposite signs, so the dominant factor is the displayed closed form. For 0<γ<2 the coefficient A changes sign once at t=2/(2-γ); implicit differentiation shows the factor decreases before and increases after this point. For γ at least 2, A stays positive and the factor decreases to one half. Boundary-mode calculations show the prescribed initialization cannot accidentally cancel the unstable mode.

## originality

PASS

Best-of-knowledge originality passes with the same-paper access risk stated explicitly. The current primary abstract says the paper introduces averaged PRG, gives convergence theory, and develops potentially larger adaptive steps, but does not expose a necessary-and-sufficient scalar stability boundary or closed-form rate optimum. Related Resultary records treat unaveraged PRG or forward-reflected-backward skew families with different recurrences. No checked source implies the split-curvature phase diagram.

## value

PASS

The scalar commuting split is the canonical calibration problem for how forward curvature and proximal curvature jointly affect a reflected method. The theorem identifies an exact stability ceiling, the transition to unconditional finite-step stability, and the unique fastest step where it exists. These are motivated algorithm-design boundaries rather than arbitrary scalar numerics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
