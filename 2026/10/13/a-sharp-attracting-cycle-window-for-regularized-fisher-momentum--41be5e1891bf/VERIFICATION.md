---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Using u_t=βu_(t-1)+(1-β)y_(t-1), bias-corrected v_t=u_t/(1-β^t), and ψ(v)=v/(1+v²), the exact scalar update is y_t=y_(t-1)-cψ(v_t). In the limiting autonomous map the ± symmetric orbit satisfies q=(1-β)/(1+β), 1+q²a²=cq/2, so a=√(s/2-1)/q exists uniquely iff s>2. At either phase the Jacobian has determinant β and trace 1+β-(1-β)cψ'(qa); the 3 Jury expressions equal 2(1+β)(4-s)/s, 4(1+β)(s-2)/s and 1-β, proving 2<s<4 exactly. The actual nonautonomous correction is O(β^t). For c=3, β≤.01, weighted sup norm max(|dy|,|du|/4), source first-step entry, derivative bound below 2/3 on paired radius .05 balls, and geometric forcing <=3β^t imply e_t<=.016(2/3)^(t-1). Independently checked symbolic Jury algebra and numerical recurrence over parameter endpoints including the claimed source interval; finite trajectories alone are not the proof. The objective limit is ρ(1-5β)(1+β)/(4h(1-β)²)>0.

## originality

PASS

The SOFIM defining source specifies first-moment bias correction and regularized rank-one Fisher steps (only abstract/accessible source description and exact package reconstruction read this run). Earlier Bock-Weiss prove Adam cycles with a separate second-moment state, which does not directly imply this 2D Fisher map, its exact sharp Jury window or quantitative source basin. PMLR approximate Newton needs Hessian spectral comparison absent here. Full original SOFIM paper inaccessible despite open-access and authorized institutional attempt; priority remains best-of-knowledge with explicit risk.

## value

PASS

A concrete exact stability phase transition plus a nontrivial bias-corrected basin of attraction for an optimizer promoted for convex losses is a meaningful structural dynamics result. It distinguishes the optimizer-specific Fisher/momentum nonlinearity from previously known Adam cycling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
