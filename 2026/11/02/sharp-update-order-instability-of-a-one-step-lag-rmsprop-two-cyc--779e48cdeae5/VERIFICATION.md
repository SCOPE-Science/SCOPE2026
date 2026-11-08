---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a primitive period-two orbit, displacements sum to x0/(epsilon+sqrt(v0))=-x1/(epsilon+sqrt(v1)), and memory difference (1+beta)(v1-v0)=(1-beta)a²(x0²-x1²). Unequal spatial magnitudes contradict displacement ordering; hence antipodal equal-memory orbit q=h/2-epsilon/a>0, v=a²q² is unique. Reflection S conjugates the two Jacobians; K=S Jplus has trace 1+beta, det d=2-beta-4(1-beta)epsilon/(ah), and monodromy K². Exact Jury conditions reduce to d<1, equivalent h<4epsilon/a. Discriminant vanishes uniquely at h_nf=16epsilon/[a(7+beta)], distinguishing positive real roots from complex conjugates. At equality h=4epsilon/a unit-circle crossing transversal, nonlinear boundary dynamics not asserted. Independently rederived K determinant and discriminant in symbolic algebra and bounded test cases.

## originality

PASS

Original 2026 Loh et al RMSProp dynamic paper uses newly updated memory v_next in the denominator, not the previous-step v; its cycle/stability results do not transfer without a conjugacy. Li et al block-delayed private adaptive method uses different stochastic/block schedule. Originality limited to the precise lagged deterministic full-state model and sharp β-independent threshold. Broader literature on lagged adaptivity remains a priority risk.

## value

PASS

Using stale versus updated second-moment denominators changes the full-state Floquet matrix and the sharp stability border, despite similar-looking cycles. The exact loss-of-attraction, node-to-spiral transition, and β-independence isolate a motivated mechanism in a natural minimal adaptive optimizer, not merely a generic Jury test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
