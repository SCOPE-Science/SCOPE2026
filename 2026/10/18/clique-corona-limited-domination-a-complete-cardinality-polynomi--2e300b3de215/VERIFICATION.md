---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Condition on the exact core intersection B. An omitted core requires a private selection to cover its cluster; each selected private vertex then sees s+1−j outside, so the lower cutoff for its occupancy is max(1,s+1−k). A selected core covers its cluster and sees s−j+d_B(v) outside, which dominates the private vertices' outside count. This gives cutoff max(0,s+d_B(v)−k), including the empty range, and binomial multiplicity on each of the disjoint private cliques. It proves the full polynomial without double-counting. Every cluster has at least max(1,s+1−k) selected, and the all-private construction attains that bound. For k≤s, equality in an included-core cluster forces d_B(v)=0, equivalently the whole component must be chosen, with the two binomial weights as stated. For k>s equality forces one vertex per cluster and bounds d_B(v) by k−s; each omitted core contributes s choices. Both descriptions agree at k=s; k≥s+Δ(H) makes every core set feasible. Independent set-based enumeration checked the full distributions and minimum classifications by core choice in 71 configurations including connected and disconnected cores. Replay: python /workspace/branches/independent_replay.py 1.

## originality

PASS

The supported contribution is the full cardinality distribution and equality-case transition for arbitrary uniform clique coronas. It is not the scalar minimum in known regimes, ordinary domination, or a new general equivalence to domination with degree-dependent requirements. In the sources inspected, none of these known equivalences or different graph-family formulas gives the new core-cut enumeration at limited capacities. The relationship paragraph's characterization of Tepeh as studying Cartesian products of leaf coronas is not substantiated by the passages checked; that attribution is not needed for the mathematical result or originality decision.

## value

PASS

The whole distribution and equality classification separate two genuinely different ways core geometry enters the constraint. In the low regime the minimum count depends only on component sizes; at k=s+1, even connected cores of the same order can differ: on three vertices P₃ has two admissible singleton core sets (its ends), whereas K₃ has none; larger core sets are all admissible in both, giving a minimum-count difference 2s². This is a meaningful exact structural refinement of the topology-independent scalar minimum, not a claim to improve computational complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
