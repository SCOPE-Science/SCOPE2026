---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Preassigned killed trajectories give directed root reachability and exact forbidden-set avoidance Q_s=(1+mu*s/(n-1))^-1. Target indegree-zero factorial moments for k vertices are (n-1)_k Q_(k-1)^k Q_k^(n-k), or exponent n-k-1 on excluding root arcs, then uniform small-k estimates with truncated inclusion-exclusion give Poisson law to o(mu^-2). After a first jump the active population is at least two; supermartingale rho^a with rho=2(1-p)/p bounds extinction before n/2 discoveries by O(mu^-2). A union bound for internally connected but externally inaccessible subsets s<=n/2 is O(mu/n), so unvisited and indegree-zero counts couple. The root no-jump event is independent of root-excluded indegree-zero variable and has exact probability q. Independent rational absorbing-recursion versus closed-reachable-set recursion passed n=2..8 for several rational p. The mathematical proof contains analytic estimates for all large n, not inferred from finite tests.

## originality

PASS

Poisson survivor limit and O(1/log n) error in almost-geometric severe epidemic models are explicitly prior art, and Ball–Barbour already suggest Poisson/early-extinction mixtures. The specified exact coefficient one and O(mu^-2) quantitative finite-frog mixture were not derived in material read; residual possibility of a sharper epidemic theorem noted.

## value

PASS

A sharp first-order refinement of a natural frog/epidemic coverage limit: isolates the exact q~1/log n mass at macroscopic early extinction from late isolated-vertex Poisson fluctuations. Quantitative coefficient and coverage correction matter because earlier general results stated only order bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
