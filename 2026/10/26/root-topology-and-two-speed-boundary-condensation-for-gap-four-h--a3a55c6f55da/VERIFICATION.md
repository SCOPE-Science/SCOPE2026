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

# Verification

Run `python verify_gap4.py` with a version of SymPy supporting exact polynomials and limits. The checker verifies all coefficient identities for symbolic index `q` in the two odd congruence classes, the palindromic degree-eight polynomial, quartic reduction, strict rational Bernstein coefficients, shifted positive coefficients for large real arguments, and the asymptotic root balances.

The written proof supplies Descartes' rule, IVT crossings, reciprocal inversion, and analytic implicit-function arguments; these are not outsourced to finite experiments. The original 2025 preprint date was read from arXiv metadata, while the mathematical formulas and qualitative prior claims were checked in the full published open-access article. No independent audit has been performed.
