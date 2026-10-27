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

# Reproducible verification

`checks.py` is standalone and requires only Python 3. Run `python3 checks.py`. It uses exact `fractions.Fraction` arithmetic to reconstruct two cell quadratures for eight rational offsets \(arepsilon=2^{-k}\), \(5\le k\le12\). It checks the exact moments, both nonresidual branch images, their two-cycle and amplitude, the consistent midpoint residual, the sampled nonlinear residual, residual-form fixed point, and six different starting values under five exact contraction steps each.

The checker reports `PASS` when all assertions hold. The general all-parameter theorem, smooth-cutoff existence, and infinite-iterate behavior follow from the explicit algebra in `RESULT.md`; finite tests alone would not establish them.

These checks are self-review only, not an independent audit, formal proof-assistant certificate, or floating-point reliability claim.
