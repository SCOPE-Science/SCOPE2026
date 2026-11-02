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

# Verification of the conditional birthday/coverage law

Run `python verify_coupon.py` with Python 3 and no third-party modules. This is a standalone exact-arithmetic checker, not a formal proof system. Its 3,493 successful assertions include: normalized first-collision masses for 35 finite alphabet sizes; a backward occupancy-chain recursion for expected remaining coupon-collection times; exact negative covariances at those sizes; strict conditional mean ordering; a separate occupancy-chain dynamic-programming computation of finite-horizon conditional CDFs through alphabet size eight and horizon 70; and three numerical diagnostics for the sharp \(\sqrt m\) covariance normalization at alphabet sizes 100, 1000 and 10000.

The crucial infinite-size steps are proved analytically in RESULT.md: the memoryless strong-Markov decomposition, a stochastic coupling, a Rayleigh moment limit justified by exponential tails, control of the endpoint event \(B_m=m+1\), and the known coupon-collector geometric variance decomposition. Finite checks cannot prove stochastic order at every sample size or the limit constants. Historical priority is not independently certified.
