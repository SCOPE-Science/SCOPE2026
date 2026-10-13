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

The theorem has a symbolic proof. Its key steps are: the singleton-ray inequalities force every distinguished negative ray to be a singleton; the zero-sum lattice condition forces one positive coordinate; the two-vertex tube constraints force a leaf and its unique neighbor; converse connectivity proves every leaf supplies a root. Cox derivations then commute because leaf neighbors cannot be leaves in a connected graph of order at least three. The connected group follows from Demazure's complete-toric automorphism theorem.

The standard-library checker `checks/check_roots.py` enumerates all connected labeled graphs on three, four, and five vertices and exhaustively checks the candidate root inequalities against the actual tube rays. This yields 770 verified finite graphs; it neither samples nor certifies larger graphs. The theorem does not depend on this finite test. A separate mathematical literature audit has not been performed.
