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

Run `python3 verify.py` with the standard Python 3 library. The checked source belongs to this package and uses rational arithmetic for the two exact sign certificates, with numerical bisection only to illustrate root locations. The local execution reported:

`VERIFY_OK exact_rational_witnesses=2 numerical_root_brackets=3 forward_cycle_checks=4`

The exact critical steps are the positive-term series bounds for \(e^5\) and \(e^7\), the simple bound \(e<3\), algebraic multiplier factorization, and continuity at the sign transitions. The checker does not prove intensity-amplitude monotonicity, the universal limiting signs, or open-interval persistence; these are proved in the written argument.

No independent audit was performed. Numerical root approximations are not validated mathematical certificates.
