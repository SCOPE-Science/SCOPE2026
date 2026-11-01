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

The statement is proved analytically by a trace recurrence, symmetric tridiagonal realization, exact eigenvalue inertia at the focus boundary, a variational estimate of the hyperbolic branch, and rank-one spectral interlacing.

The included `verify_resonance.py` contains exact-rational comparisons between two-by-two matrix products and the scalar trace recurrence for \(1\le n\le14\), independently checks tridiagonal determinants, verifies Sturm counts through \(n=24\), and checks the published four-step formula. Running `python verify_resonance.py` reports 2,450 passing exact checks. Finite checks are not substituted for infinite-degree proofs.

Itinerary feasibility and periodic-orbit existence are not certified by the zero-slope equations. Publication-priority claims remain conditional on the inspected literature; no independent scientific audit has been performed.
