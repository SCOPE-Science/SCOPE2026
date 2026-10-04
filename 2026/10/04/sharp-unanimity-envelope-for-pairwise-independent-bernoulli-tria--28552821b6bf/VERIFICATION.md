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

The analytic verification has two parts. First, each claimed upper bound is the expectation of an explicit quadratic polynomial that pointwise majorizes the unanimity indicator on the integer success-count support. Second, each branch supplies a nonnegative count distribution for which equality holds and whose first two factorial moments are exactly those forced by pairwise independence.

The accompanying `verify_unanimity.py` uses only Python's exact rational arithmetic. For \(693\) rational parameter cases with \(2\le n\le12\), it enumerates every three-support vertex of the corresponding moment polytope, verifies that the stated envelope equals the largest vertex objective, checks nonnegativity of the explicit extremizer, and checks both factorial moments exactly. The observed terminal line is `CHECK_OK`.

This finite computation is supplementary: it does not stand in for the all-\(n\), all-\(p\) proof. No independent external audit has been performed.
