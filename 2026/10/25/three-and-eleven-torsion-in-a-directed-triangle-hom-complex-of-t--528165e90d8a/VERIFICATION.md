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

# Reproducibility and limits

The file `check_hom_p11.py` is a standalone Python standard-library checker for the complete integral cellular chain complex of the directed Hom complex. Execute `python3 check_hom_p11.py` from its directory. Its independent cell enumerations agree; the final counts are 165 vertices, 495 edges, 165 triangle cells and 165 square cells, with no cells above dimension two. Boundary composition vanishes and the one-skeleton is connected.

Exactly 329 integral unit pivots split off, leaving one column whose 33 nonzero entries have absolute value 33. Exact integral Smith invariants therefore include 329 units and one 33. The modular ranks agree: 329 modulo 3 and 11, 330 modulo 2, 5 and 13. This proves \(H_1\cong\mathbb Z\oplus\mathbb Z/33\mathbb Z\) and trivial higher homology for this finite complex. The computation is exhaustive for the stated complex but does not certify any result about an infinite family, homotopy groups, or uniqueness in all literature.

The scientific review and checker are provided for reproducibility. An independent audit has not been performed.
