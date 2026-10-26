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
# Reproducibility and proof checks

Run `python verify.py` with Python 3 and the standard library. The script recomputes the positive root using a bisection routine independent of the symbolic root proof. It checks the exact reset-rate moment identity, all finite-second-moment boundaries, the sign of exponent bias on parameter grids, 4th-moment parameter wedges, strict 4th-moment inequalities and the singular small-reset expansion. Record the count printed by the script. The checker is finite and does not by itself prove a statement for all real parameters or an infinite tail. The analytical proof supplies these universal quantifiers, using the cited Goldie renewal theorem for the positive perpetuity tail and Breiman's product-tail lemma for the Gaussian mixture.

**Scope and external reliance.** No independent mathematical audit was performed. No exact elementary closed form for the Pareto amplitude is asserted. The asymptotic is for a fixed positive resetting amplitude before taking the spatial threshold to infinity; no uniform double-scaling claim is made.
