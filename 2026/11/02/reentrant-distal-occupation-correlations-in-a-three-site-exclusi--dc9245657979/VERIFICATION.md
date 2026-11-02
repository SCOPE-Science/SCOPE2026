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

# Reproducibility and scope of checks

The standalone `verify.py` uses exact rational polynomial arithmetic with no third-party dependencies. It constructs the physical three-site generator from independent injection, extraction, rightward hops and each eligible particle-specific reset. It verifies all row sums, every stationarity balance polynomial, normalization and the three exact pair-covariance numerator identities against formulas in `RESULT.md`. The two positive covariance threshold roots are counted analytically using Descartes' rule and strict exact-rational signs; root-isolation and neighboring-covariance signs are checked exactly.

An independent rational Gaussian elimination routine constructs eight stationary solutions at resetting rates \(0,1/5,1/2,1,2,3,10,100\) and compares all eight components with the displayed algebraic formula. The finite samples confirm calculations but are not used as proofs of statements for all nonnegative resetting rates.

To reproduce: extract `verify.py` alongside the other files and run `python3 verify.py`. The exact parameter scope and all unproved generalizations are recorded in `RESULT.md`. Independent external validation has not been performed.
