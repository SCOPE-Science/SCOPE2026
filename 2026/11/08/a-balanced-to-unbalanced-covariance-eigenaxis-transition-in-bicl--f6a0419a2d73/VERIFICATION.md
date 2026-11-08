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

Run `python verify.py` with Python 3 and NumPy. The checker enumerates the uniform vertex sets of all 36 ordered pairs of block sizes \(2\le p,q\le7\), totaling 2,988 vertex occurrences. It exactly reconstructs the mean and all covariance entries using rational arithmetic, compares them to the closed block formula, and then numerically verifies the four spectral classes and extremal ordering. This is a bounded finite consistency test, not a proof for infinitely many part sizes.

The paper's analytical proof checks \(p=q\) and \(p>q\) independently, with explicit treatment of strict inequalities and eigenvalue multiplicities. No assessment has been performed by an independent mathematical auditor; historical novelty is subject to the separately documented source-access and equivalent-formulation risks.
