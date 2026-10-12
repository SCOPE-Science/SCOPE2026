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

Run `python3 verify.py` using the standalone standard-library script distributed in the same folder as RESULT.md. The completed checker printed `PASS 413 exact and boundary checks`. It compares the independently summed row-covariance formula to the factored closed expression at rational parameter values for all integer sample sizes from 2 to 38; tests exact polynomial endpoint coefficients for sizes 2 to 30; and checks several fixed-parameter boundary approximations and sign witnesses with rational arithmetic.

The infinite conclusion does **not** follow from these finite tests. Its proof is the Gaussian exponential-tilt calculation, exact finite-sum reduction, and asymptotic binomial expansion stated in RESULT.md. Verified limits assume fixed positive scaling parameter \(c\) and sample size tending to infinity. The theorem shows at least two zeros for sufficiently large even samples, not exact root counts for all sizes or signs at the critical constants. The Sinn–Keller article was not inspected in full; unrecognized historical coverage remains a risk. No independent audit has been conducted.
