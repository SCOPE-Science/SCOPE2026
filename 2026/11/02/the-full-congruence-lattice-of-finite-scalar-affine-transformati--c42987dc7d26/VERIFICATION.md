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

# Verification performed

The proof is algebraic for all finite fields and positive ranks, based on the unique group-of-units/constant-ideal split and the normal-subgroup action on the constant quotient. The exact relation and counting formulas are given in `RESULT.md`.

The standalone executable `verify.py` checks left and right multiplication for each proposed congruence in the cases \((q,r)=(2,1),(2,2),(3,1),(3,2),(5,1),(4,1),(4,2)\). For the first three cases it additionally enumerates every set partition of the entire monoid and proves equality with the proposed collection of congruences by exhaustive filtering. The \(q=4\) tests use explicit multiplication in \(\mathbb F_2[u]/(u^2+u+1)\), not modular integer arithmetic.

`verify_output.txt` records actual observed counts and ends with `VERIFY_OK` and `EXTENSION_FIELD_VERIFY_OK`. Neither the finite tests nor the output by themselves imply the unrestricted theorem; the general proof is required.
