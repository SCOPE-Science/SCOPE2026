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

The standalone `check.py` is run using Python 3 standard libraries only. It constructs, independently of the analytic polynomial proof, the transient generator for each target degree, including independent neighbor deletions and full resets. Exact rational Gaussian elimination is applied to the backward mean equation and Laplace equations.

The reported command was `python check.py`; the observed output was `PASS 1296 exact generator, resolvent, strict-curvature and polynomial checks`. Tested rate pairs use exact rational values; targets through 11 are compared by independent generator inversion, and finite curvature and polynomial identities are also checked at larger thresholds.

These checks are finite. The all-parameter proof is the renewal identity plus the three-term recurrence and falling-factorial difference identities in `RESULT.md`. Reproduction does not require a network simulator, and the program does not establish a theorem about finite networks or continuous target interpolation.
