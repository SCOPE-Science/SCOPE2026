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

Run `python VERIFY.py` with Python, SymPy and mpmath. The script computes symbolic normalizations, a two-by-two inverse and both state-dependent asymptotic constants, then verifies Laplace-PGF identities and convergent small-Laplace-parameter limits with multiple parameter regimes. It provides corroborating finite checks only.

Proof of the infinite-time statements is in RESULT.md: exact Brownian hitting-time convolution, the Markov ergodic theorem, moment uniform integrability, matrix perturbation and a monotone Tauberian theorem. These analytic steps are not inferred solely from the script.

No numerical inversion of the entire physical-time distribution or simulated verification of the half-normal limit is claimed. All rates are strictly positive, the excursion offset is strictly positive, and the initial position is away from the interface. Independent assessment is not performed.
