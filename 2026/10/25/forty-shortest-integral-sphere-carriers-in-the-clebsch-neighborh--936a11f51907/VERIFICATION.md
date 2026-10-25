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

# Reproduction

With Python 3 and only the standard library, run `python3 verify.py certificate.json` from the extracted directory. The program deterministically builds the 16-vertex graph, its simplicial open-neighborhood complex, all 40 induced tetrahedral two-spheres, and the signed chain maps, and checks the affine action. The integer certificate uses the zero-based sorted-face indices embedded in `certificate.json`; the complete 95-by-95 minor is rebuilt, not read from a precomputed matrix. Its determinant is checked using 95 unit pivots and exact elementary integer operations. The code checks rank profiles over the finite fields of orders 2, 3, and 101, together with every consecutive boundary composition. The theorem's integral conclusion follows from the explicit unimodular minor and a rank/saturation argument, not from numerical experiments or homology-library output.

**Limits of verification.** The program covers precisely the finite object stated and makes no assertion for infinitely many folded cubes. Full literature priority and independent peer verification are not computationally certified.
