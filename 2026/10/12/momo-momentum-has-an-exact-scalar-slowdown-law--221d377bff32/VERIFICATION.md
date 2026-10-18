---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The exact MoMo source initialization yields x2=x1/2 and gamma_k=2 weighted_loss_k. From an uncapped previous step follows weighted_loss_(k-1)=x_k d_(k-1), yielding residual h_k=(1-beta)a*x_k^2/2. Inductively the iterate preserves its sign and d_k>=a*x_k ensures tau_k<=1/(2a). The dimensionless z_k evolves by F(z)=beta(1+z)^2/(z+1/2), with derivative beta*z*(z+1)/(z+1/2)^2<beta<1; its unique fixed point yields beta=q(2q-1), hence q=(1+sqrt(1+8beta))/4. At beta=0 the exact ratio is 1/2. The limiting normalized learning rate 2(1-q)/(2q+1) follows algebraically. Independent direct source recurrence and reduced recurrence agreed for 30 steps across 5 beta and 3 curvatures; long recurrence fixed points checked.

## originality

PASS

The exact statement and its implications were compared against the defining primary source, nearest general theorems, differently named invariants and Resultary published records. No dominating prior result was found among genuinely examined material; any inaccessible or unindexed potential coverage is retained as a residual risk, not treated as evidence of novelty.

## value

PASS

The defining MoMo mechanism and practical default beta=.9 are naturally benchmarked on the simplest strongly convex interpolating objective, where momentum can slow the objective factor from 1/4 to about .93295 and collapse the adaptive rate. The phenomenon isolates a genuine algorithmic limitation from stochasticity or conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
