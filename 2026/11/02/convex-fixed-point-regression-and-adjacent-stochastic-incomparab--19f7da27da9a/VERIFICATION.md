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

Execute `python verify_mapping.py` using Python 3 standard library only. It exhaustively enumerates every map of sizes 3 through 7 and directly computes cycle membership, fixed-point classes, conditional distribution, means, convexity, stochastic tail witnesses, and zero covariance using exact rational arithmetic. It checks the same formulas at sizes 8 through 70 via exact finite products, without enumerating those enormous map spaces. The reference execution produced `PASS 10059 exact checks; exhaustive mappings n=3..7 and formula tests n=8..70`.

These computations test finite instances only. The all-size claims follow instead from the forest determinant, derangement enumeration, cycle-indicator expectation, positive falling-factorial differences, telescoping identities and Gaussian asymptotic argument in `RESULT.md`. No computational claims of infinite exhaustiveness or external certification are made. Independent audit has not been performed.
