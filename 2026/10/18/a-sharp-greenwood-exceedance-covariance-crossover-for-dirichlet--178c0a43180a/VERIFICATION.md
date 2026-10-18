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
# Reproducibility checks

Run `python checks/verify_dirichlet.py` with the dependency in `requirements.txt`. This script was executed on the enclosed source path. Its checks independently compare the labeled covariance formula to exact beta tail integrals for 114 rational test cases, compare the same formula to high-precision numerical integration for 30 noninteger-parameter cases, and independently integrate the gamma influence-function covariance matrix for six cases. It also prints finite-size symmetric covariances approaching their exact gamma limits for three shape choices and two thresholds. All tests passed after choosing a quadrature tolerance that accounts for the integrable gamma density singularity at shape below one.

The analytic derivation in `RESULT.md` proves arbitrary positive real parameter quantifiers. The finite checks cannot verify the full uncountable family or the central limit theorem on their own. The joint CLT uses a standard moving-threshold empirical-cdf expansion plus the classical multivariate iid CLT. No external/independent audit has been carried out.
