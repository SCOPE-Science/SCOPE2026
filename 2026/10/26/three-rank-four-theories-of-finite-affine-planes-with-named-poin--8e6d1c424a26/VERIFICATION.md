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
# Verification notes

Run `python affine_sorted_check.py` followed by `python affine_geom_lemma_check.py` from one folder. The first program independently constructs finite coordinate affine planes over orders 2, 3, 4, and 5 and recursively computes exact first-order types of all pebbled tuples with four moves remaining. Its recorded output ends `VERIFY_OK` and finds class identifiers 0, 1, 2, 2. The second separately computes geometric-diagram extension sets and confirms that the one-, two-, and three-pebble tables for orders four and five coincide, including 64 three-position geometric diagram keys.

These computations are exhaustive for the specified finite structures but are not an exhaustive test of all finite affine planes. The universal claim relies on the geometric extension lemma and the explicit size and incidence bounds in the proof. The implementation uses no random sampling or external formal verification.
