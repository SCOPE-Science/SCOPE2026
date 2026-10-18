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

# Verification and reproduction

Analytical checks: the nonnegative squared-coordinate square-root generator is explicit; its stationary first and second moment identities reproduce the rational variance. The derivative numerator is the cubic \(A-Bq-Cq^2-\eta wq^3\), and \(B,C,\eta w>0\) holds for the entire admissible domain. Factoring \(A=(w-w_-)(w-w_+)\) and implicit-root Taylor expansion establishes the two-wing criterion and onset. Critical boundaries and the excluded zero-reset-position limit are stated in the result.

The standalone `check.py` completed **1,826 assertions**, independently comparing the variance with generator moments, exact rational identities, regenerative-age quadratures, finite-difference derivatives, root classifications and direct exact-transition samples. Reproduce with `python check.py` after installing `requirements.txt`. These tests are finite validations; the classification for all positive real parameters follows from the written analytic proof, not from enumeration.

Literature verification: the full source preprint arXiv:2306.08770 was read and compared on objects and observables; another general resetting paper arXiv:1408.1230 was only available at abstract level. No independent scholarly priority review or external mathematical validation has been performed.
