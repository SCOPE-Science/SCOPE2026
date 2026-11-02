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

Run `python3 verify.py` in a directory containing the supplied standalone script. It uses only the Python 3 standard library, exhaustive restricted-growth-string enumeration, exact `Fraction` arithmetic, and exact factorial/binomial identities.

The completed execution reported **2,074,703 exact assertions passed**. Exhaustive noncrossing-partition enumeration was performed for \(n\le10\), including the Catalan totals, the full block-profile formula and all conditional/unconditional moment checks. The independent symbolic-identity implementation checked every admissible integer triple \((n,k,r)\) through \(n=160\), with the exceptional largest block sizes treated separately. The positive polynomial identity used for unconditional strict negativity was also checked exactly.

Finite checks do not establish any statement beyond their enumerated range. The general conclusions rely on the Lagrange-inversion enumeration, binomial factorial-moment algebra, and an explicit sum-of-positive-terms certificate given in `RESULT.md`. No independent review or external certification is asserted.
