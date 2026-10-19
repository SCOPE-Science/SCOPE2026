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
# Reproducibility and limits

Execute `python3 verify.py` from the directory containing this file. It uses only the Python 3 standard library and exact rational arithmetic. A completed execution yielded `VERIFY_OK 200 exact rational assertion groups`.

Tests cover multiple vertex counts (3 through 11), weighted-path polynomial eigenvalue identities, the affine eigenvector and budget, discrete Brownian-bridge covariance identities, positive-semidefinite certificates for several rational price-face points, and exact singularity at the small-order critical endpoint. The symbolic proof in RESULT.md establishes the theorem for arbitrary orders; the finite test set is not exhaustive over all real budgets and edge prices, and it does not certify novelty or independent validation.

For every real \(B>0\), the price threshold and the full equality-price face follow from the analytical proof. There is no asserted formula for the optimizer inside the lower-price regime, no rate estimate for the auxiliary spectral gap as the cycle grows, and no claim for asymmetric generators or discrete-time transition matrices.
