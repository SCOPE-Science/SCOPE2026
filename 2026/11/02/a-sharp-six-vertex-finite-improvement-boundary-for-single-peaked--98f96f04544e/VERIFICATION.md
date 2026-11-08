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

PASS — Reconstructed payoff-order preservation under the exact reflected-branch assumption: for every attainable local own-color fraction f, the admissible payoff orders agree with min(f/Λ,(1−f)/(1−Λ)). All strict-comparison sign changes for distinct rational fractions in F_n occur at Λ=f/(1+f−g), and evaluating each such boundary and every open interval midpoint gives an exhaustive real-peak partition. Independently built all K_{s,t} color-state graphs (s≤t, s+t≤6) and ran Kahn topological-cycle detection on 3,079 exact graph/composition/peak instances, 140,610 states and 216,828 improving edges, agreeing with the claimed unique K_{3,3}, (r,b,e)=(3,1,2), Λ>2/5 exceptional cycle. Recomputed the four-step labeled witness: red fractions 1→2/3, blue 1/3→1/2, with strict blue improvement precisely Λ>2/5. Distinguishable-agent cycles project to a color cycle; projected acyclicity suffices for the FIP conclusion. Scope requires two occupied colors, ≥1 vacancy, n≤6, connected complete bipartite graph and the specific source-symmetric utility, not arbitrary unimodal payoffs.

## originality

PASS

PASS, bounded — The primary jump-game source already establishes nonconvergent cycles on other graph families and induced-subgraph inheritance; those do not determine the precise bipartite n≤6 classification or universal threshold over Λ. Published swap-game work differs because both agents must improve. Resultary's semantic search returned only different graph and combinatorial finite thresholds, not this model. This is a best-of-knowledge judgment with real risk from the inaccessible full version of the initiating paper, rather than a guarantee of priority.

## value

PASS

PASS — Sharp smallest-order/complete-composition FIP classification on a natural graph class, with a nontrivial exact preference-peak transition and an explicit minimal labeled improvement cycle. It answers a structural dynamic stability question and the finite cutoff is motivated by the smallest witness; this is more than checking a few arbitrary instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
