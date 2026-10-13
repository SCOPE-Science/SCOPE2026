---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

Run `python verify_graph.py` using only the Python standard library. The script verifies exact rational identities, not floating-point approximations. In its actual completed execution it reported:

`VERIFY_OK graph classification: [(2, 1, 1), (3, 4, 3), (4, 38, 7), (5, 728, 15), (6, 26704, 31)] ; K_2,3 all 32 states exact cancellation; P4 mixed-strategy witness 1/4; exact-profile cases 180099`

The graph census includes every connected labelled loopless simple graph with 2–6 vertices; the middle figure counts such graphs and the last figure counts those satisfying common-neighbor row equality. The profile census ranges over entries \(\{-1,0,1\}\) on each connected graph through five vertices. The two-part example uses exactly unequal nonzero rational comparison constants and two benefit/cost choices, and checks all 32 strategy states. The path calculation certifies a nonzero exponential log-odds shift without evaluating an exponential numerically.

**Mathematical boundary:** finite enumerations cannot establish the unrestricted classification. The unrestricted proof is the competitor-odds identity, coefficient separation for all positive benefit and cost parameters, parity components of the common-neighbor graph, and the complete-bipartite row-equality argument. No formal proof assistant or independent validation is claimed.
