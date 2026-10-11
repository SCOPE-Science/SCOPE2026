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

`verify.py` starts from the six published facet-orbit representatives for the affine \(13{:}3\) action and expands them independently.

It verifies orbit sizes \(39,39,39,13,13,13\), reconstructs the full face vector \((13,78,286,533,468,156)\), and checks that all \(286\) vertex triples are triangular faces.

Over \(\mathbf F_2\), it computes triangle-to-edge rank \(66\) and tetrahedron-to-triangle rank \(219\), hence \(\dim H_2=1\). It then evaluates all \(182\) missing tetrahedral boundaries and requires every one to be nonzero.

Finally, it acts with all \(39\) affine maps on the complete missing-four-set family, obtaining six orbits with sizes \(13,13,39,39,39,39\) and the stated representatives. It independently computes the two affine pair types and all six pair-type signatures.

Exact successful output:

`VERIFY_OK f=13,78,286,533,468,156 H2_F2_dim=1 missing4=182 all_missing4_nonzero=yes affine_orbits=13,13,39,39,39,39 reps=12410|12911|12311|1246|12412|1278 pair_signatures=3:3|3:3|4:2|3:3|3:3|2:4`

The integral interpretation uses the published homology \(H_2\cong\mathbb Z/2\), \(H_1=0\) and the universal coefficient theorem; no unsupported integer-homology inference is made from a mod-two calculation alone.
