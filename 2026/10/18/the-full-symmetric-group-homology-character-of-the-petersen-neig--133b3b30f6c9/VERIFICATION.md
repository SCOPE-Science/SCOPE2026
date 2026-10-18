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

# Reproduction and limits
Run `python3 verify.py` with Python 3 and no external dependencies. The script constructs the graph on the ten two-subsets of five points, defines the open-neighborhood complex using all common-neighbor subsets, and verifies its ten vertices, thirty edges and ten triangles. It checks ten elementary free-face collapses to a connected graph with twenty edges and eleven independent cycles. It then enumerates all 120 permutations of the five underlying points, computes signed traces on every simplicial chain group and verifies the complete seven-class character, exact six- and five-dimensional formulas, and character inner products equal to 120, with cross product zero.

The theoretical derivation is the signed-induced-chain-module decomposition via Pieri's rule stated in `RESULT.md`; independently checking finite traces does not by itself establish broader claims about other Kneser graphs. No integral equivariant lattice classification, equivariant homotopy equivalence, or external scientific audit is asserted.
