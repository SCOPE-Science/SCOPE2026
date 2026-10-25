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
# Reproducibility and checks

The standalone program `verify.py` uses only the Python standard library and can be executed with `python3 verify.py`. It evaluates eight independent half-normal integrals against exact analytic constants using composite Simpson quadrature with 120,000 subintervals. It also constructs the defining parking-function vertices for dimensions 2–6 and checks the support-function pair-maximum representation, its opposite-direction counterpart, and the kernel width identity for 320 deterministic pseudorandom Gaussian directions. Expected output begins `VERIFY_OK gaussian_integrals=8 support_comparisons= 320` and ends with `variance= 0.017778933035221097` (subject to normal floating-point variation).

An additional simulation with independent Gaussian samples at dimensions 16, 64, and 256 produced centered-rescaled width variances approximately 0.0155357, 0.0171156, and 0.0175090 respectively, versus predicted limit 0.0177789330, and near-zero covariance with the rescaled number of negative coordinates. These finite-sample checks are not proofs of limiting normality or independence.

The proof's potentially delicate steps are the precise Hoeffding degeneracy estimate, order-\(n\) effect of random radial normalization, the exact half-normal integral identities, and the even-versus-odd projection symmetry. All are explicitly addressed in `RESULT.md`. The program provides finite verification only, not an infinite-dimensional certificate. No independent audit has been performed.
