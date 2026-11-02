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

# Reproduction

Run `python verify_depth.py` with Python 3, SymPy, and NumPy. Symbolic assertions check the exact stationary generating function, all-state Poisson equation including the geometric-reset boundary, exact moments, martingale asymptotic variance, and the two critical limits. Finite truncated transition-matrix Green--Kubo sums are also tested at \(p=0.6,0.75,0.95,1\); truncation is illustrative, not exhaustive proof. The infinite-state validity, ergodicity and CLT follow from the written algebraic and geometric-drift argument in RESULT.md.

A separate independent mathematical audit has not been performed.
