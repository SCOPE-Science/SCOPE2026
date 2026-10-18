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

Run `python3 verify_prefix_normal7.py` with the standard Python 3 library. No external packages are required.

The program independently computes the rational-function identity via symbolic integer polynomial multiplication and six explicit cone terms, then compares its coefficients with exhaustive direct enumeration of all seven-one words of lengths \(7\) through \(25\). Each candidate is checked both by scanning all factors and by the separate gap inequalities. The expected terminal messages are `FORMAL_IDENTITY_PASS` and `ALL_CHECKS_PASS`.

These finite enumerations do not establish the formula beyond the tested lengths; the general finite-cone symbolic summation and formal identity do. The program does not search the mathematical literature or certify novelty, nor has an independent audit been performed.
