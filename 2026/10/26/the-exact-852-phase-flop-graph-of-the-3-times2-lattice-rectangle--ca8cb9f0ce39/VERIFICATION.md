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

## Exact replay
Run `python3 VERIFY.py` beside `CERTIFICATES.json` using Python 3 standard library. The data contain 852 integer convex-height witnesses and 2626 integer wall witnesses, all verified on the actual embedded package paths. BFS reconstructs 852 distinct triangulations and all 2626 two-way flips. It checks every triangle has normalized area one and strictly positive other-point height clearance, and every wall has the correct four coplanar vertices and no extra coplanar vertices. It recomputes graph degree distribution, radius, diameter and uniqueness of the diametral pair. The full traversal agrees with the independently published total 852.

## Scientific limits
A published exact count is used as an upper bound for completeness of the reachable triangulation set. This certificate verifies the finite toric flop graph, not the classification of nontoric resolutions and not an independent peer audit. Numerical optimization was used only to discover integral height witnesses, and plays no role in their exact verification.
