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

# Verification

The proof invokes Proposition 4.9 of Adamaszek–Adams (2015) for homotopy equivalences of cyclic graph maps. That published result and the cross-polytope orientation determinant establish the theorem for all stated parameters. No finite enumeration is offered as a substitute for this all-parameter deduction.

Run `python3 verification.py` using Python 3 (standard library only). The script enumerates fixed faces under rotations and both reflection-axis types, computes signed simplicial Lefschetz traces, and checks the cross-polytope determinant and small-model contiguity. Its expected final line is `VERIFY_OK_DIHEDRAL_ORIENTATION_CYCLIC_RIPS`.

This calculation only covers the displayed finite ranges. Singular winding ratios, higher-rank equivariant homology, and integral quotient homology are unproved and unclaimed.
