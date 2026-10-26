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

# Reproducibility and finite certificate

The local cone and its seven lattice points are defined in `RESULT.md`. Run `python3 verify.py`. The checker uses only exact integer arithmetic and the standard library. It first obtains all seventeen unimodular triangles from the seven lattice points. It recursively lists every seven-triangle compatible subset and verifies that there are exactly ten. Since the pentagon has normalized area seven and all candidate faces have area one, compatibility certifies a cover of the entire polygon. Then ten embedded height vectors are checked strictly on each of the eight interior edges; the minimum integer strict-convexity margins are `1,1,1,1,2,1,1,1,3,3`. Finally, exact quadrilateral swaps produce thirteen flop walls, and exhaustive graph breadth-first search yields the degree and shortest-path distributions in `RESULT.md`.

The actual checker execution terminated with `QB_EXACT_VERIFICATION_OK`. A successful run verifies the complete finite toric enumeration but is **not** an independently performed scientific audit and makes no claim about non-toric resolutions or the compact ambient threefold.
