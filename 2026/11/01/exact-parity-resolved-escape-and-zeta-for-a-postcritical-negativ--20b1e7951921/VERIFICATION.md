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

# Reproducible calculations

`check.py` uses Python and SymPy to calculate the exact six-state adjacency polynomial, the Lebesgue mass generating function and n-step mass for the first twenty steps. It also enumerates branch equations using rational arithmetic for all periods up to twelve, tests every candidate itinerary, and compares actual physical periodic points with the symbolic matrix trace. The general finite-time survival and zeta formulas are proved symbolically in `RESULT.md`; tests for finite periods cannot establish all-period claims. The topological entropy and dimension rely on the analytic Markov/full-shift argument, not simulation. No independent audit has been performed.
