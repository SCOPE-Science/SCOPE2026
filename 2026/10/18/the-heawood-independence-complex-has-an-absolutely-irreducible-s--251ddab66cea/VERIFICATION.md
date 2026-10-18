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

Run `python3 verify.py` using Python 3.9 or later, without dependencies. The certificate reconstructs every Heawood incidence edge from nonzero vectors of \(\mathbb F_2^3\), and every one of its 458 augmented independent faces by two different methods. It applies the exact pivot matching to all faces and topologically sorts the full directed Hasse diagram, verifying 226 matched pairs and acyclicity across 1582 incidences. Removing the augmented empty pair leaves exactly one zero-dimensional critical cell and six three-dimensional critical cells.

For all 168 point-line preserving elements and 168 point-line swapping elements, the certificate computes signed reduced Lefschetz traces and independently evaluates an invariant-orbit independence polynomial at \(-1\). Each of the 336 pairs of values agrees; the inner-group order counts and outer-coset order counts are exact. The resulting full-group character has squared norm one, establishing complex irreducibility. The output begins with `VERIFY_OK` if and only if all assertions hold.

This is an exhaustive finite computation with elementary combinatorial completeness proofs (14 vertices, 336 actions); it is not an unbounded claim. No assertion of external or independent validation is made. The public 2026 predecessor's indexed summary was accessible but its full supplementary text was not; this limits a categorical claim of literature uniqueness, not the finite proof certificate.
