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

# Verification of the Gaussian endpoint variance frontier

The proof is self-contained in `RESULT.md`: its critical hypotheses are finite dimension, positive-definite Gaussian covariances, logarithmic variance under the first Gaussian, and fixed forward relative entropy. The equalities use strict concavity/convexity and do not rely on finite numerical evidence.

The included `verify.py` is a standalone executable requiring `numpy` and `scipy` as stated in `requirements.txt`. It independently evaluates whitening-invariant Gaussian matrix formulas, checks the one-coordinate interpolation and exact boundary equality for prescribed relative entropy, and samples Gaussian log-density ratios to compare with analytical mean/variance. The packaged checker reported **1,585 passing assertions** when run before submission. Its Monte Carlo checks use a fixed seed and declared tolerances; sampled agreement is not an infinite proof. The full interval and equality rigidity are established symbolically in `RESULT.md`.

Scientific access limits: a closely related Gaussian reverse-KL extremal result [2] was inspected with its supplemental argument and differentiated by objective. Broader information-spectrum extremal theory may contain an implicit deduction, and this remains an originality risk, not a certification. Only the exact-score, infinite-forward-time endpoint identity of [1] justifies the stated physical interpretation. No external independent audit or validation has been performed.
