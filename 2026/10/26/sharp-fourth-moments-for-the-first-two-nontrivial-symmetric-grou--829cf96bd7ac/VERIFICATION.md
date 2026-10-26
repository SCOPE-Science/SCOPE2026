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
# Verification of the two-character fourth-moment theorem

The supplied `verify.py` uses only the Python standard library. Its exact rational conjugacy-class enumeration reproduces the five mixed fourth moments for every integer degree from four through fourteen, checks the two-character orthonormality identities, and separately enumerates every permutation through degree seven. The same checker bisects the unique positive algebraic optimizer for each of the five regimes and verifies the sharp numerical constants and comparison inequalities against trial coefficient ratios.

The execution returned `VERIFY_OK independent_cycle_class_moments_n=4..14 permutation_moments_n=4..7 assertions=84`. Independently, direct symbolic differentiation of each displayed quotient yields the stated derivative factorizations. The all-degree proof does not rely on testing finitely many degrees: factorial cycle moments are exact and all relevant cycle weights are at most eight. The checker corroborates finite cases, normalization, root isolation and numerical approximations; it is not a separate proof of originality or an independent audit.

Literature comparisons concern mathematical statements and implications. Remaining historical-priority risk is disclosed in the review. No external audit or validation has been performed.
