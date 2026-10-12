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
# Verification and limits

The proof reconstructs the ramification and genus, the length-two characteristic-two Witt formulas, the simple-pole non-coboundary criterion, the permitted base-coordinate transformations, and the equivalence modulo the two generator choices. The normalizer computation does not depend on finite-field enumeration.

Run `python3 verify.py` beside this document with only the Python standard library. The exact checker runs arithmetic in the 16-element field defined by the irreducible polynomial `u^4+u+1`, checks all 256 ordered parameter pairs, verifies both Witt sum and difference formulas, verifies the inverse/coboundary identity, and confirms that the invariant partitions the 16 parameters into eight pairs. Observed output:

`VERIFY_OK: Witt identities and eight two-point GF(16) parameter orbits`

The finite test is a consistency check and does not extend enumeration to algebraically closed fields, prove the simple-pole lemma, or certify the full automorphism group. The unrestricted characteristic-two proof is in `RESULT.md`. The work has undergone the recorded self-review only; independent audit has not been performed.
