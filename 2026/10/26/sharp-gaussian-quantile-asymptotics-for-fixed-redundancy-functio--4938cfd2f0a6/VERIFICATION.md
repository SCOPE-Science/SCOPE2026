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

Run `python3 verify_threshold.py` with Python 3.10 or later. The standard library alone is used; no network access or external data files are required. The saved `verification_output.txt` is the actual execution output.

The program independently enumerates short Boolean-cube neighborhoods to check the two enclosing Hamming balls. It then uses exact integer binomial coefficients to check, for each of four fixed redundancies and three error counts, (a) that a balanced-class ball already exceeds its available complement below a fraction of the critical \(t^2\) length, and (b) that the longest potentially relevant binomial interval is smaller than the all-class feasibility allowance above the critical length. All 12 lower and 12 upper exact certificates pass. Constants printed from the standard normal quantile merely orient the finite checks.

The infinite-parameter proof is analytic, using Harper's vertex isoperimetry and the uniform normal approximation for binomial cumulative probabilities. None of the finite checks, or the normal quantile printout, substitutes for either theorem. This work has not received an independent audit.
