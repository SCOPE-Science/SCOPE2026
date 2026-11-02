---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The exact 18 Frucht edges are provided and the script checks isomorphism to the canonical 12-vertex LCF model. A face is precisely a vertex subset with internal induced degree≤1. Independent bitmask enumeration of all 2^12 subsets gives 824 nonempty faces and f-vector (12,66,190,293,209,53,1). The frozen script was inspected function-by-function: deterministic vertex matching, full directed Hasse acyclicity topological sort of every incidence, exact signed boundary reductions in degree 4→3, signed integral 3-cycle lifting and projection to full Morse generators. It yields 410 matched pairs in the full case with one critical 0-cell, two critical 3-cells and one critical 4-cell; integer differential (0,1), so K≃S³. Each deletion has only a 0-cell and b_v 3-cells except v=8 where the remaining 4-cell has integral unit boundary. Thus each deletion genuinely has a wedge-of-three-spheres homotopy model, not just Betti numbers. The signed integral projection gives zero images on v∈{0,6,8,9}, and primitive unit coefficient elsewhere. Independently reconstructed 825 total faces including the empty face, every mod-2 Betti rank and each of the twelve mod-2 inclusion images (all consistent with the integral calculation). Mod-2 evidence alone does not prove Z-surjectivity, which rests on the examined integer cycle lifts.

## originality

PASS

Qualified best-of-knowledge ORIGINALITY PASS for the specific final claim, NOT a declaration that known nonequivariant calculations or general frameworks are new. Published Resultary Frucht graph independence/deletion record studies ordinary Ind_1(F), with wedge of three 2-spheres and vertex deletion ranks. This is a different face condition from Ind_2(F); its Ind_1 invariants do not imply the 12 Ind_2 deletion H3 inclusion images. The already-known full Ind_2(F)≃S³ is expressly credited rather than claimed new. Ghosh–Selvaraja, Shellability of Higher Independence Complexes of Graphs (arxiv:2505.06614), works on structural shellability families such as chordal/block graphs, whereas Frucht has cycles and is not such a block-tree instance. Sawant, On the vertex decomposability of r-independence complexes of trees (arxiv:2605.25150), proves tree results and cannot encompass the cyclic cubic Frucht graph. Residual priority risks are stated; no stronger indexed result was identified which logically implies the assessed claim.

## value

PASS

A complete deletion-and-inclusion census for a canonical asymmetric cubic graph is a meaningful exact invariant of a natural 2-independence complex. It shows that equal deletion Betti numbers do not determine whether integral H3 generators survive under inclusion; this is an intrinsic topological classification that could be reused when studying higher-independence cofibration/deletion arguments, not a random small-parameter negative check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
