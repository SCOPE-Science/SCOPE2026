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
# Verification

The conserved quantity was differentiated symbolically. The exact original-time density was obtained from the coordinate derivative on a quadrant and independently compared to finite-level numerical quadrature in the included `verify.py` script. The script evaluates two unequal coefficient ratios and an inverse-logarithmic contrast, checking period-asymptotic coefficients and localization; its outputs do not certify all parameter values or infinite limits.

The proof of the general assertion is the dominated-convergence argument in RESULT.md, including explicit endpoint singularity bounds and beta-integral normalization. No claim is made about higher-order errors or about the coefficient-zero boundary. Independent audit has not been performed.
