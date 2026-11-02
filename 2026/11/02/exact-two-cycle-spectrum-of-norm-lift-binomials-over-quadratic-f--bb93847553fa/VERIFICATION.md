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

# Reproduction
Run `python verification/verify_cycles.py`. It implements finite fields as polynomial residue rings, iterates the displayed map directly, compares fixed and exact period-two counts with the formula, and verifies norm and exponentiation descriptions agree. The polynomial modulus used for each extension is explicitly listed in the script. The script uses only the Python standard library.

Successful output from the packaged code:

`VERIFY_OK permutation_parameters= 156 general_parameters= 386 direct_power_checks= 5549`

The tested base-field sizes are \(2,3,5,8,9,11,17,23,27\). The 386 coefficient cases exhaust non-base-field coefficients for fields of order at most 11 and sample 40 cases each for larger orders. Algebraic arguments in RESULT.md, not these finite computations, support the all-prime-power quantifiers. No independent mathematical audit was performed.
