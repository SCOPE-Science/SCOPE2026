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

Reproduce using `python3 verify.py` (Python 3.9+, standard library). The program checks the 17 open neighborhoods, the complete face vector, signed simplicial identities, ranks of boundaries in characteristic 3 and 101, the 136 affine permutations, all 2380 four-vertex sets, all 510 missing tetrahedra and every ambient mod-three class.

A four-term signed tetrahedron boundary is a cycle. Its reduction against the full third-boundary column span is nonzero for 476 supports and zero for 34. The classification does not independently compute the complete integer Smith form of the global boundary or claim an independent homotopy audit.
