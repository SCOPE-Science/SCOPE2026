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

Run `python3 verify.py` with a standard Python 3 interpreter.

The script reconstructs the 77 tetrahedra from the six difference cycles, derives all lower-dimensional faces, checks the face vector, computes the ranks of the first two boundary maps over F_3, verifies an explicit nontrivial 1-cocycle, enumerates all 210 empty triangles, classifies their cocycle evaluations, constructs all 15 cyclic translation orbits, identifies the two null-homologous orbit gap types, and checks that one-step translation negates the cocycle.

Expected final output:

`VERIFY_OK f=14,91,154,77 H1_F3=1 empty3=210 essential3=182 null3=28 essential_orbits=13 null_orbits=2 null_gaps=1:5:8,3:6:5 classes=91,91 translation=-1 systole=3`

The finite enumeration proves only the stated result for this 14-vertex complex. The topological identification with L(3,1) is taken from the cited primary classification; the verifier does not independently prove the homeomorphism type.
