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

Run `python3 verification/paley13_affine.py` in the extracted artifact root. Only Python's standard library is required. The verifier rebuilds all 599 augmented faces from the thirteen translated quadratic-residue neighborhoods, fills all 65 absent triangular boundary loops by three existing triangles, checks 218 free-face collapses, confirms the resulting 2-dimensional face vector, and computes the exact signed reduced Lefschetz character for all 78 elements of the affine symmetry group.

The homotopy decomposition follows from the certified 2-dimensional collapse, the complete-1-skeleton triangular nullhomotopies, Hurewicz and Whitehead; the new equivariant claim follows from Hopf traces and characteristic-zero character theory. No field-by-field homology test is being treated as an integral homotopy proof. The existing nonequivariant wedge type is acknowledged as previously published. An external independent audit has not been performed.
