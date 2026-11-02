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

# Verification record

Run `python verify.py` using an ordinary Python 3 interpreter. The independent exact check computes integer binomial coefficients, their powers of two, and base-two carry counts without depending on the symbolic witness derivation. A complete bounded scan examines every positive integer below \(2^{17}\); the verified fibers with weight at most nine are checked against the predicted complete set. The constructive witness checker then tests all \(3541\) allowed parameter pairs through weight sixty and a binary shift for each.

Observed successful output:

`VERIFY_OK direct_integer_binomial_valuations=2400 carry_comparisons=1200 complete_scan_n=131071 constructive_pairs=3541 full_scanned_weight_fibers=1..9`

These are finite tests only. The infinite theorem rests on the self-contained proof using Legendre's digit formula, Kummer's carry theorem, explicit seed expansions and the valuation-preserving padding map. Independent scientific audit remains unperformed.
