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
# Reproducibility notes

Run `python CHECK.py` with Python 3 and NumPy. The checker constructs the exact second-moment map from first principles with rational arithmetic and checks the proposed equicorrelation Lyapunov identity for windows 2 through 7 at six mean multipliers, five correlations, and six noise levels: 1080 distinct rational parameter cases, including equality and supercritical cases. It checks the stationary covariance equation in stable cases and verifies the two endpoint noise capacities in 14 additional all-rational cases. Finite-dimensional eigenvalue computations are secondary cross-checks, not a replacement for the all-window proof.

The theorem's necessary-and-sufficient interval, the positive definiteness of the \(m\)-step sum, stationary uniqueness, and the optimal correlation comparison are established in `RESULT.md` analytically. Finite testing cannot verify those for all dimensions or all parameter values. The motivating preprint's complete text could not be retrieved; bibliographic coverage is not certified. No independent audit was performed.
