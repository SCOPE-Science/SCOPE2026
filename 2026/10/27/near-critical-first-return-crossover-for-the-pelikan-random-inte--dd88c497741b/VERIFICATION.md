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

# Reproduction and limits

Run `python verify.py` with Python 3 and NumPy from the package directory. The program compares exact finite-horizon first-return masses from the ballot formula with an independently implemented rational dyadic-level transition evolution. For several fixed critical-window biases it compares independently evolved survival tails at two increasing horizons to the proved Gaussian profile, and also checks the elementary eventual escape and mean-return identities. The program is a reproducibility check, not a certificate of an infinite limit or a substitute for the analytical dominated-convergence argument in RESULT.md.

Independent audit has not been performed. No external formal verification or independent validation is asserted.
