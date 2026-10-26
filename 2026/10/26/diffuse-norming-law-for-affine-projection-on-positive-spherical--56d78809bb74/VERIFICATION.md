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

## Reproducibility

Run `python checks/verify.py` with Python 3 and NumPy installed. It verifies the stated exact Gram eigenspaces for dimensions 3, 4, 6, 10, 30, 100 and 500; reproducing-covariance matrix inversion; the folded-normal fluctuation covariance \(1-3/\pi\); and the strict diffuse envelope for a grid of support parameters. Independent direct Gaussian-to-positive-sphere Monte Carlo kernel integrations are compared with the **moving-parameter** leading formula in dimensions 96, 256, 512 and 768.

## Checked mathematical limits

The analytic proof uses a multivariate Lindeberg theorem for independent Gaussian coordinate pairs and a first-order expansion of Gaussian radial normalization. The Monte Carlo tests are finite sanity checks and do not establish an infinite-dimensional limit or global extremality. A uniform second-moment identity for the reproducing kernel supplies the analytic uniform integrability argument. No independent external audit has been carried out.
