---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Direct differentiation gives div f=-a z=-a xdot and therefore div(exp(a x)f)=0. Liouville's formula integrates the divergence to the endpoint expression exactly. Bounded x makes its time-average vanish; a periodic orbit makes the monodromy determinant one and the two nontrivial Floquet multipliers reciprocal in product. On any bounded trapping region the positive density has finite nonzero measure, while strict compact containment would lower that invariant measure, a contradiction. A fresh symbolic replay reproduced both divergence identities.

## originality

PASS

The 2017 source explicitly labels the exact ODE dissipative and writes a state-dependent volume contraction expression, while the audited Liouville calculation shows the divergence is the exact derivative -a xdot and produces an invariant positive density. Targeted Resultary comparison found no prior source-specific correction with the exact Jacobian, Floquet product and trapping obstruction. The result therefore corrects the mathematical interpretation of the published continuous-time system.

## value

PASS

This is a substantive correction to a published chaotic-flow interpretation: it distinguishes instantaneous Euclidean divergence from cumulative dissipation and rules out the usual attracting-limit-set interpretation for the exact ODE. The invariant density and Floquet obstruction are reusable structural facts, not merely a numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
