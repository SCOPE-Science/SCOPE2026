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
Run `python verify.py` with Python 3 and NumPy. The script checks exact-rational renewal mass identities for short horizons at the critical exponent, validates near-critical finite-age normalization and monotonicity, compares computed logarithmic-age CDFs with the claimed limiting formulas, and checks conditional residual-tail scaling. `verification_output.txt` contains the recorded execution output. No simulation or finite calculation proves convergence for all horizon sizes: the proof in RESULT.md uses the renewal generating series, a triangular Laplace-transform limit, monotonicity, and the Markov conditional-tail formula. Independent audit: not performed.
