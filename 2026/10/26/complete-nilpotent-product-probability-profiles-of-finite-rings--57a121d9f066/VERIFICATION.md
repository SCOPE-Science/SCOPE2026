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

## Checks
The accompanying `verify.py` independently enumerates all ordered product tuples over four explicit finite rings and counts nilpotent products directly. Tested are \(M_2(\mathbb F_2)\) with \(1\le k\le4\); \(M_2(\mathbb F_3)\) with \(1\le k\le2\); \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) with \(1\le k\le5\); and \(\operatorname{UT}_2(\mathbb F_2)\) with \(1\le k\le5\). Every count equals the formula, with exact rational arithmetic, and the checker prints `VERIFY_OK` on success.

The proof separately establishes radical lifting, the uniform induced-block law, nilpotent matrix counts by Fitting decomposition, and full profile uniqueness by dominant-exponential extraction. No finite test proves the unrestricted statements. No independent or external certification has occurred.
