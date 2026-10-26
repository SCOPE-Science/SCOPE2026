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

The elementary exact moment statement was independently checked by the accompanying finite enumeration program, `verify.py`. The program enumerates integer-frequency solutions to the defining fourth-moment Fourier integral rather than using the closed overlap formula to calculate its purported left-hand side. The actual recorded output is `verification_output.txt`.

The analytic proof also requires the bounded reverse-martingale central limit theorem and ergodic averages of nonconstant Fourier characters. These are standard infinite-time results, not independently verified by finite enumeration. Independence in the exponential limit follows from the full joint real/imaginary covariance and pseudocovariance, not merely marginal second moments. The finite kernel is not characteristic. The 2004 predecessor on empirical bridges was accessible at abstract level only, leaving residual literature-priority uncertainty. No independent audit or certification has been performed.
