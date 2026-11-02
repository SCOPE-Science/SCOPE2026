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

# Verification of the Rule 30 cyclic image law

Run `python3 verify.py` with `certificate.json` present in the same directory. Both files are self-contained except for the Python standard library. The checker prints `VERIFY_OK` if every assertion succeeds.

The exact checks are: generation of all 41 distinct monoid transformations from the two inverse maps; closure and all 82 labeled transitions; acceptance of exactly 30 fixed-point transformations; exact comparison against every transformation, transition, bit, polynomial coefficient, and 49 stored series coefficients; equality of the first 49 coefficients of the 41-state rational series with the claimed rational formula; direct exhaustive binary-ring enumeration for each length from 1 through 17; and consistency of the formula for lengths 1 through 27 with the independently published May 2016 finite Rule 30 census of Faulkenberry, Table 6.

The infinite proof uses an explicit degree bound. The 41-state rational series has a numerator of degree at most 40 and denominator of degree at most 41. The claimed rational function has numerator and denominator of degree 7. Their cross-multiplied difference has degree at most 48, and the exact 49-coefficient comparison proves this polynomial vanishes identically. Therefore the check of finitely many integer coefficients certifies a formal all-length identity rather than merely extrapolating a numeric trend. The document `RESULT.md` gives the pair-state equivalence, the algebra to the recurrence, and the root-asymptotic deduction.

This is a reproducible exact computational certificate and a self-review, not a separately performed independent mathematical audit. The public literature record may contain an equivalent earlier result not identified by the cited comparisons.
