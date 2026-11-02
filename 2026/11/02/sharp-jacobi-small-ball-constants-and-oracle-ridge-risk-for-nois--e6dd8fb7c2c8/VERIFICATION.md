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
# Reproducibility and verification

Run `python3 verify.py` from the extracted directory. The checker uses the standard Python library and exactly verifies rational ridge bias--variance identities and derivatives for parameter grids; it checks rational homogeneity of the centered quadratic form, elementary two-point uniform calibration, and the geometric four-point uniform coefficient. It also performs a seeded 200,000-trial Monte Carlo diagnostic for the four-point uniform lower tail. The diagnostic is probabilistic and is not an exact certificate or a proof of the endpoint limits.

The theorem is proved analytically in `RESULT.md`. The proof relies on the mean/deviation orthogonal Jacobian, convergent endpoint integrals, and a truncated logarithmic integral at equality; no finite computation is substituted for these general steps. The endpoint constants are given by explicit convergent integrals, not by unevidenced numerical approximations.

Scientific limitations: independent and identically distributed beta sites, unpenalized intercept, oracle slope-dependent penalty, independent equal-variance observation noise, fixed number of samples at least four. The continuous-density branch and the inverse-moment threshold have known antecedents. Specialist independent priority and correctness audits have not been performed.
