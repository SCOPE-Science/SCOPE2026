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

# Reproducibility

Run `python3 verify_balanced_johnson.py` with standard Python 3. The verifier independently enumerates actual simplicial faces of balanced Johnson clique complexes and counts the signed action on every invariant simplex. For \(k=4\), all 22 conjugacy classes of \(S_8\) and their complement twists are compared against the symbolic cycle formulas. For \(k=5\), eight representative conjugacy classes and their twists are checked. The exact output includes `VERIFY_OK cases=60 signed_face_tests=443240`.

A second calculation in the same program builds all boundary matrices for \(k=4\) and performs exact bit-vector elimination over \(\mathbb F_2\), yielding `GF2_HOMOLOGY_OK 8 [0, 0, 181, 0, 0]`. This is an independent finite topological consistency check. It does not replace the proof of vanishing in arbitrary dimension, the rational representation identities, or the universal \(k\ge4\) statement.

# Limits

No independent external audit or certification has been performed. The full text of one related 2026 preprint could not be inspected, and the novelty conclusion retains that explicit risk. The result is restricted to the stated balanced Johnson graphs, the natural symmetry action, and scale one.
