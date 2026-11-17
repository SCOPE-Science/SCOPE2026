---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The one-step transition from agreeing hubs forces all leaves to the hub color and keeps hubs agreeing; it reaches a fixed state or the deterministic two-cycle in one update except at an initial terminal state. Opposed hubs create an independent Bin(m,1/2) new leaf count, with hub outputs equal below/above r=m/2 and opposed at the exact tie. The balanced stage survives each round with probability c_m and so its exit is geometric with 1-c_m>0, independent of the next fresh-binomial H stage; this gives the stated outcome probabilities, PGFs E[z^tau], E tau, Var tau, unbiased initial law and m->infinity limit. All boundary k=0,r,m and m=2 are covered; no odd m claimed.

## originality

PASS

PASS on the exact stated triangular-book absorption law as a best-knowledge priority assessment. The full conditional transition reconstruction isolates a nonbipartite adjacent-hub family; the closest established stochastic all-profile result is for complete bipartite graphs (the hub edge is absent), while general random-majority and cycle-graph theorems do not yield the exact three-class probabilities and first-entrance generating functions. No earlier exact triangular-book statement identified. Search failure is not a priority proof.

## value

PASS

A connected natural book graph with unbounded triangle count supplies a genuinely exact all-initial-state law for independent fair-tie stochastic opinion dynamics; the persistent two-cycle probability tending to 1/2 and the geometric delay at hub disagreement ties are mathematically significant distinctions beyond broad convergence bounds and finite simulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
