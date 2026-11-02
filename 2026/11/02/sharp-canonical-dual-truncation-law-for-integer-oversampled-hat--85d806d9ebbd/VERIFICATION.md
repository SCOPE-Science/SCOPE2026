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

# Verification and reproducibility

The exact Zak multiplier, its inverse Fourier coefficients, the canonical-dual unit-cell formulas and the Laplace expansion are all established analytically in `RESULT.md`. The rate and prefactor depend on the displayed fixed integer \(q\); no uniformity as \(q\to\infty\) is inferred.

The accompanying executable `checker.py` is standalone and uses only Python 3 standard-library modules. Running `python3 checker.py` produces a success line after 528 assertions. Tests include direct finite sums for the Zak multiplier, numerical Fourier inversion, symmetry identities, positivity and sharp frame-bound endpoints, and large-index quadrature against the asymptotic constants for multiple redundancies. Asymptotic numerical tests use explicit finite-index tolerances; they are supplementary and do not imply proof of convergence. Historical originality comparisons remain subject to an inaccessible 1996 full text. Independent audit is not performed.
