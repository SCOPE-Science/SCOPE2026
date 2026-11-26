---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The explicit graph is a 7-cycle of b vertices, a 14-cycle ordered c0,...,c6,d0,...,d6 with the required twisted closing edges, and seven a hubs with the three prescribed spokes each. Independent replay (python3 /workspace/branches/reproduction/flower.py) numbers the two cycles consecutively, computes each edge distance by the first vertex layer meeting an endpoint, and exhausts all 3276 triples and 20475 quadruples using injectivity of the 42 signatures. No triple resolves, ruling out all smaller sets by upward closure. There are 1932 resolving quadruples, including {a0,b0,c1,c4}. Triple buckets construct exchange cliques, with every pair of distinct bases sharing exactly one bucket if adjacent and none otherwise, giving 17920 edges without double counting. Integer bitset layer search from every basis reaches all 1932 bases and has last nonempty layer at distance 5 from every root. Hence the exchange graph is connected and its radius and diameter are both 5. This is exhaustive for this graph and this unrestricted replacement move, not a statement about other orders or token slides.

## originality

PASS

The strongest examined flower-snark primary text explicitly leaves the edge dimension undecided at odd orders at least seven; its mixed-dimension theorem is not an edge lower bound. The standard definition and set-cover method are already known. The precise J7 minimum, optimal-basis count and exchange geometry are distinct in the inspected sources; this is not priority certification.

## value

PASS

J7 is the first undecided order in a published family question, not an arbitrary test graph. The exact minimum is useful on its own; the full optimal-state census and constant unrestricted exchange eccentricity further quantify whether and how far apart minimal landmark configurations can be moved. A complete finite benchmark needs no unsupported generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
