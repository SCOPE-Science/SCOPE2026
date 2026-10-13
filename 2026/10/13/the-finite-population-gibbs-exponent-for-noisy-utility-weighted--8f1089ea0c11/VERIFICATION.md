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

# Verification of the finite-population weak-noise theorem

The executable `verify.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. In every tested size \(2\le N\le10\) and each of five rational learning rates, it constructs the full collection of unordered-pair averaging matrices and exact projected pair-noise covariances. It verifies the neutral covariance fixed-point equation, the pair-difference identity, the exact stationary disagreement variance, and the time-rescaled drift/diffusion and Gibbs-exponent coefficients. Run `python3 verify.py` from the directory containing this file. Expected output:

`VERIFY_OK: 45 exact rational covariance, mixing and inverse-temperature checks`

These 45 finite checks certify the displayed finite matrix identities only for tested sizes and rates. The unrestricted parameter theorem uses the general algebra and the analytic localization/averaging proof. No computational experiment is treated as a proof of functional convergence, uniqueness for infinitely many parameter choices, or convergence of microscopic stationary distributions.

The invariant law is established only for the limiting one-dimensional diffusion when its proposed density normalizes. No independent audit was performed.
