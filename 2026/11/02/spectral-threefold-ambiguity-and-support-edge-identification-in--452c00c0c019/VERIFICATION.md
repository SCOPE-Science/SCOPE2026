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

The theorem follows analytically from the exact two-state Markov sign autocovariance, linear transfer-factorization, real polynomial irreducibility, and positivity of a damped mechanical Green kernel. In particular, an exactly observed stationary power spectrum determines the numerator scale and monic cubic spectral denominator, not the physical labels attached to its three overdamped poles. The proof enumerates every label assignment. For the stationary support, constant-sign histories of arbitrarily long finite length have positive probability and saturate the Green-kernel bound in essential supremum. Those are infinite-range arguments; neither a finite numerical check nor a graphical spectral match proves them.

For computational reproduction, run `python verify.py` with Python 3 and its standard library. The included script verified 23,003 deterministic assertions with a fixed random seed. Assertions check rational cubic identities, the explicit three-realization witness at multiple frequencies, generator stationarity second moments, repeated-pole collisions, underdamped discriminant signs, and the support-edge decoding formula. A successful script run independently confirms those finite algebraic instances but cannot certify publication priority, finite-sample inference, or the general theorem without the above proof.

Independent scientific audit: not performed. The exact support endpoint and all-lag covariance are ideal population data, not measurements assumed available from finite time series.
