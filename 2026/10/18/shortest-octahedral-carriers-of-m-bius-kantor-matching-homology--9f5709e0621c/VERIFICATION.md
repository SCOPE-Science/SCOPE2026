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

The standard-library programs `verify.py` and `check_mod2.py` were executed from the package directory and terminated with `VERIFY_OK_MOBIUS_KANTOR_SHORTEST_CARRIERS` and `VERIFY_OK_DIRECT_MOD2`, respectively. It reconstructs the signed cellular chain data, checks the full acyclic discrete Morse matching, enumerates all shortest supports, checks all \(912\) fundamental-cycle boundaries, computes integral quotient coordinates, enumerates the complete automorphism group, and verifies exact orbit ranks and determinant-one lattice certificates. The separate mod-two program constructs unreduced simplicial boundaries, obtains boundary ranks 1935 and 1873, verifies that each of the 912 cycles is nonbounding modulo two, and independently checks the total eight-dimensional span.

The general lower bound and equality characterization for induced supports in flag complexes are proved in `RESULT.md`. The integer arithmetic, not finite-field extrapolation, establishes primitivity and integral generation. The ambient homotopy type and deterministic Morse matching are credited to earlier work; the carrier classification and inclusion images are the separately checked result. No claim is made about fifth-homology carriers, unindexed publications, or independent external certification.
