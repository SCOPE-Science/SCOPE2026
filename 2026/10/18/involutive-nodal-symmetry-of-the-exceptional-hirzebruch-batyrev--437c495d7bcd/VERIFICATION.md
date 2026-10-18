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

# Verification record

The companion `verify.py` is standalone Python 3 code using only the standard library. It reproduces the ordered list of 22 polytope vertices and enumerates every integral stabilizer candidate after necessary vertex-difference pruning. Exactly 52 first-pair choices and 12 second-pair choices survive, so the complete search has 624 candidate quadruples; determinant and all-vertex checks leave two matrices forming \(C_2\).

The code enumerates supporting primitive facet normals from four affinely independent vertices, reconstructs the polar, and finds 72 primal and 68 polar two-faces. The invariant-face classification distinguishes quadrilaterals by the exact opposite-vertex-sum test. It then constructs all 26 polar square-diagonal relation vectors, checks rank 18 and exactly two coloops, checks equivariance under the explicit dual involution, and computes exact plus/minus source, image, and kernel dimensions \((14,9,5)\) and \((12,9,3)\).

The final output is `VERIFY_OK polytope_aut=C2 tested_images=624 primal_nodes=10_pairs mirror_nodes=12_pairs+2_fixed mirror_coloops=exchanged node_relations=5_plus+3_minus`.

This certificate is finite and exhaustive for this explicitly fixed 22-vertex lattice polytope. It does not establish automorphisms of a generic hypersurface, the existence of smoothings, a classification of arbitrary polytopes, or historical priority.
