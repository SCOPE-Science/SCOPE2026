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
# Verification information

The accompanying `verify_covariance.py` is executable under Python 3 using only its standard library, with integer and exact-rational computations. It enumerates all 46,230 permutations of sizes 3 through 8 and verifies the mixed moment, the normalized mean, strict positivity, and the lower bound for every permitted subsequence length. It then checks 2,242 exact rational assertions in total, including direct larger finite parameter evaluations. It does not establish the infinite theorem by enumeration: the complete analytic proof is in `RESULT.md`.

The literature comparison relied on primary full-text inspection of an openly available 2004 increasing-subsequence paper and a 2026 fixed-point/inversion paper. The 1981 marginal-count predecessor's full text was not inspected. Historical originality remains vulnerable to an unlocated general joint-statistic theorem. The result is not an independently audited or certified mathematical theorem.
