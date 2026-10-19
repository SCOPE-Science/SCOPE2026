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

# Verification and reproducibility

Run `python check.py` in an environment with NumPy and SciPy (`requirements.txt` lists the package dependencies). The numerical verification suite computes the bivariate mixed law by two independent quadrature schemes, compares finite-population Gaussian union probabilities against the Hüsler–Reiss limit, verifies the Gaussian integral leading to the universal tail dependence, checks strict non-max-stability at representative points, tests the small- and large-lag endpoints, and simulates empirically width-normalized Gaussian maxima from the conditional common-age model.

The executable bundled with the result was run successfully: `PASS 82 cross-check assertions`. Its Monte Carlo two-time empirical probability was approximately `0.229429` against its finite-population Gaussian oracle probability `0.240443`; these probabilities pertain to the explicitly coded conditional age and particle count, not the age-mixed limiting probability. The computed age-mixed limiting probability at both zero thresholds and scaled lag one was approximately `0.200088880`, and the independent error-function integral gave the tail-dependence coefficient at scaled lag one as `0.367879441`.

Finite checks do not prove convergence or uniqueness. The mathematical proof conditions on an exponential backward reset age, derives the correlated Gaussian extreme-value limit for every positive age, controls the empirical-standardization error, applies bounded convergence, and evaluates the dependence coefficient by an exact Gaussian integral. Neither an independent external audit nor a definitive priority review is asserted.
