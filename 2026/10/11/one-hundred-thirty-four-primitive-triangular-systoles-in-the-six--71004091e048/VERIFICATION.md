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

`verify.py` is standalone and uses only the Python standard library. It reconstructs all faces from the \(96\) tetrahedra, builds the integral cotree presentation, checks an explicit \(28\)-edge cocycle on every triangular face, and verifies a determinant-one \(96\)-relation certificate by fraction-free Bareiss elimination.

It then exhausts every three-vertex clique and evaluates the induced generator on all \(278\) nonfacial triangular cycles.

Exact successful output:

`VERIFY_OK f=16,112,192,96 H1_Z=Z unit_minor_det=1 cliques3=470 facial3=192 empty3=278 null_empty3=144 primitive_systoles=134 oriented_pairings=+1:85,-1:49 cocycle_support=28`

The determinant certificate proves torsion-freeness and rank one directly from the supplied complex. No sampled computation is used for a statement about longer cycles.
