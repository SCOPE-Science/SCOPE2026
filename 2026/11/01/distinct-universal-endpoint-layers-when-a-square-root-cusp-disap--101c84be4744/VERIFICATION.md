---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Exact inverse-branch formula u=(sqrt(K²+θ(1-x))-K)/θ and Jacobian w=u/(K+θu) yields invariant density fixed equation. At x=1 and 0 it forces boundary traces zero; differentiating gives h'(1)=-h(1/2)/K² and h'(0)=h(1/2)/[K²((1+θ/2)²-1)]. A uniform 2-iterate BV estimate has contraction coefficient 3/(1+θ/2)²<=3/(1.9)²<1 near θ=2: inverse intervals partition the domain, weight product variation is bounded by 2/(1+θ/2)², giving uniform BV. BV compactness plus tent unique invariant density yields L1 convergence, and iterated Lasota–Yorke plus fixed-n transfer continuity yields interior uniform convergence. Substituting 1-ε²z into w gives R(z)=1-(1+16z)^-1/2; iterating the left inverse branch with geometric remainder yields L(z)=sum_{j>=1}2^-j R(z/2^j), uniformly on bounded z. Exact slopes 8,8/3 and h'' lower bound 32/3 follow. Independently checked slopes and renewal series symbolically. The fixed-θ W²,1 existence is a primary-literature assumption; the theorem excludes θ=2 and makes only a lower, not exact, h'' norm statement.

## originality

PASS

Comparisons distinguish evaluated final mathematical statements from source theorems. Best-of-knowledge novelty assessment; inaccessible primary literature is treated as residual risk, not proof of novelty.

## value

PASS

Endpoint layers are natural singular perturbation invariants of a published cusp map family. Distinct dyadically related profiles, quadratic length scale, derivative blowup and failure of W1,1 stability reconcile map/density L1 convergence with boundary concentration; more than a normalization check or generic response theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
