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

# Reproducibility

The exact claim follows from the Routh–Hurwitz determinants, absolute-ratio Cauchy density, elementary Gaussian sign-angle formula, and a compact-interval substitution proved in `RESULT.md`. The inherited exact middle-index relation is from Cima–Gasull–Mañosa (2021), Corollary 5.2 / Table 5.1.

Run `python3 check_quartic_probability.py` from the extracted standalone files to obtain a numerical quadrature check using no dependencies. A separate 65-digit arbitrary-precision integration gave \(h=0.0092838447242981189571499241965554345313\ldots\). This is a numerical consistency check, not a validated enclosure of the infinite-precision integral.

Finite Monte Carlo simulation was also consistent at its statistical precision. These calculations do not replace the infinite probability proof. The result has not undergone independent audit.
