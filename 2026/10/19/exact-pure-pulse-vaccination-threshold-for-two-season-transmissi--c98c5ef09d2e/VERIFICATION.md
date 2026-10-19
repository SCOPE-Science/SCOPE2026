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

# Reproduction
Run `python verify.py` alongside this file with Python 3 and no third-party packages. The program directly computes exact two-pulse orbit integrals using affine exponential maps, then tests the analytical first variation against finite-difference changes in total weighted susceptible exposure. It checks both possible endpoint mechanisms and the motivating exact threshold.

# Scope of checking
The numerical computations do not certify infinitely many competing Borel measures. That conclusion follows from strict convexity of the fixed-mass functional and the analytical sign proof for its switching sensitivity. Numerical quantities are reported to approximately 12 decimal places. The first-public-source date is the verified electronic-publication date, not a manuscript receipt date. No independent scientific audit or validation has been performed.
