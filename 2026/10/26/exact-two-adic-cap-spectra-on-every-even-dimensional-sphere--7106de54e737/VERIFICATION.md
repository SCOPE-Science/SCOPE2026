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

The proof is a complete all-degree and all-even-dimension argument. The key independently testable steps are: Gegenbauer/Funk--Hecke normalization; a derivative identity; unique least two-adic terms for the Gegenbauer value and cap mass; the factorial cancellation in the eigenvalue valuation; and Hilbert--Schmidt compactness.

With Python 3 and SymPy installed, run `python check.py` alongside the provided files. It evaluates exact rational expressions and checks direct cap integrals against the closed spectral formula for five even dimensions, seven reduced rational cutoffs, and degrees 0–18. `check_output.txt` records the observed result. The finite checks do not replace the infinite proof. Independent validation has not been performed.
