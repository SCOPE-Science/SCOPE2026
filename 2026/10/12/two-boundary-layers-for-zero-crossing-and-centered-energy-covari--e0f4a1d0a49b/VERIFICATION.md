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

# Verification and proof boundaries

The file `verification.py` is standalone Python 3 source and uses only the standard library. Run `python3 verification.py`. The output reports 65 exact rational projected/decomposed covariance comparisons, three exact negative values at \(n=7,8,9\) and \(\rho=1/2\), 23 exact geometric-distance coefficient checks, plus numerical diagnostics for the two asymptotic layers. The finite rational computations test the identity but do **not** prove the inequalities at larger \(n\) or either limit.

For correctness of the unbounded claims consult the uniform bounds and exact summations in RESULT.md: the inequality \(F_n(1/2)<0\) for all \(n\ge10\), the positive leading Taylor coefficient at \(\rho=1\), and the two deterministic limits of the projected-distance sums. Source limitations: Lindgren's complete 1974 text could not be checked; published multivariate crossing and general Gaussian-integration formulas may encode parts of these quantities. No independent audit has been conducted. Root uniqueness, global uniformity, nonlinear prediction and non-Gaussian extension are unproved.
