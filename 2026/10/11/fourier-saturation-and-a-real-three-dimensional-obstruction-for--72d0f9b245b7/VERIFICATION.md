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

# Reproduction and scope

Execute `python3 verification/check_joint_index.py` from the directory containing the embedded files. The source uses only the Python standard library. Actual replay returned:

`VERIFY_OK checks=19847 real_orders=1,2,4,8,16 complex_orders=2,3,5,6,7,9 odd_hadamard_order3=excluded analytical_proof_required=True`

The tests verify finite orthogonal-column constructions and their extreme/sign witnesses, sampled complex phases, the exact nonexistence of a three-by-three real Hadamard matrix, and a finite family of the universal inequality. Finite enumeration does not establish the theorem for arbitrary dimension, arbitrary exponent, all tuples, or infinite-index spaces: these require and receive the independent analytic steps in RESULT.md. The numerical size of the strict gap in real dimension three is unproved and not estimated.
