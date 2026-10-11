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

`verify.py` constructs the nine-vertex complex both from the path-deletion definition and from the three difference cycles and asserts equality. It then checks the face vector, forms an exact integral first-homology presentation after collapsing a spanning tree, and computes its Smith normal form. The diagonal has twenty-seven unit entries and one free generator, so the integral first homology is infinite cyclic.

The script exhausts all eighty-four triples. It verifies that exactly thirty are missing triangles, with the four cyclic gap types and orbit sizes in the claim. It checks the signed least-residue winding sum on every face triangle and every missing triangle, and confirms invariance under all nine cyclic translations.

Replay command: `python verify.py`

Expected terminal line: `VERIFY_OK f=9,36,54,27 H1=Z empty3=30 gap_orbits=1:4:4x9,2:3:4x9,2:4:3x9,3:3:3x3 winding=1_all_missing shift_action=+1`

Limits: this exact computation certifies the finite complex and the stated integral homology claim. It does not search longer cycle representatives or other triangulations.
