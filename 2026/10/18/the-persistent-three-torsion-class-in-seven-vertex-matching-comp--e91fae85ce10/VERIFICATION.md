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

# Exact verification

The package includes `verify_m7_sign.py`, `verify_torsion_inclusions.py` and `torsion_atlas_masks.json`. Run `python verify_torsion_inclusions.py` with Python 3 from the same directory. The test uses only the Python standard library; face enumeration, integral minor, graph canonicalization and symmetry maps are generated from stated definitions.

The first script checks the complete-graph face vector (21,105,105), the connected 1-skeleton's 85-dimensional integral cycle lattice, rank 84 of the second boundary modulo three, a nonzero integer maximal minor of determinant -3, and the signed action of all 5040 graph automorphisms. These imply the integral three-torsion group with no undetected larger invariant factors.

The second script checks the minimal-graph face vector (13,42,30), the 29-dimensional mod-three rank, an explicit mod-three 2-cycle, its integer 1-cycle Bockstein, and its nonzero cocycle evaluation after inclusion into the complete graph (value 2). It then canonically enumerates all 256 spanning supergraphs of the minimal graph and exactly matches their 40 isomorphism classes to the separate forty-entry published atlas record. These are finite exhaustive checks. The independent published census's all-graph Smith invariant computations are used as cited prior results rather than rerun; any error in that external classification is a scientific dependency. The inaccessible original Bouc text and unindexed literature remain originality risks.
