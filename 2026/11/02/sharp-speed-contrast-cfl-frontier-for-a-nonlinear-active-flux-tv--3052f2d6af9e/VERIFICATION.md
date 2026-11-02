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

Verification covers algebraic equivalence of the three displayed feasibility characterizations. The result is an exact theorem about a nonempty interval, not a computationally inferred stability conjecture.

The proof checks positivity of denominators, separates the inactive and active lower-bound cases, reduces feasibility to two linear inequalities in the slope variable, then solves a quadratic for the Courant ceiling. A limiting slope parameter gives the sharp universal-speed-contrast frontier, with finite-slope witnesses beyond it. Each argument is valid for all continuous parameters in the specified domain.

Run `python3 verify_frontier.py` using Python's standard library. Its 34,400 exact-rational comparisons test interval feasibility against the two alternative inequalities, and its boundary and counterexample checks independently exercise the critical algebra. This finite enumeration is supplementary; it cannot establish the continuous-parameter theorem on its own.

The most relevant original manuscript is arXiv:2610.05920v1, Theorem 4. Only the supplied conservative correction interval is studied. No claims are made about existence of other TVD fluxes, about solver-wide positivity or about rigorous convergence at larger Courant numbers. Independent mathematical audit is not performed.
