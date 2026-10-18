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

# Reproducibility and verification

The complete proof, definitions and quantitative limit are in `RESULT.md`. Run `python verify.py` with Python 3 after installing dependencies listed in `requirements.txt`. The program is self-contained and builds the model algebraically rather than importing unprovided files.

Verified exact symbolic identities: (i) four original equations reduce to the four total-and-composition equations; (ii) the stable total-population matrix and the two quadratic center-manifold invariance identities; (iii) equality between the center-manifold angular-average damping coefficient, its explicit rational formula and the independent relative-entropy dissipation expression; and (iv) for the unit-parameter benchmark, the exact coefficient \(\kappa=9/65\), so \(\lim t\mathcal E=65/9\).

A second, nonproof diagnostic numerically integrates all original population equations for two admissible parameter sets and samples the weighted imbalance energy at three times. The sampled values approach their corresponding analytically predicted constants. Numerical trajectory checks are only corroboration; they do not establish global convergence, exclude unseen orbits, or prove an infinite-time limit.

The analytical argument relies on LaSalle's invariance principle, smooth finite-dimensional center-manifold tracking, a nonvanishing quadratic slaving term, strictly positive averaged quartic dissipation, and a first-order periodic normal-form correction. Its domain is strictly positive initial densities and a strictly positive equal-type coexistence equilibrium at fixed positive ecological parameters. This is a self-review only; no independent audit or external certification has been performed.
