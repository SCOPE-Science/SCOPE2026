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

# Reproducibility of the exact mixed moments

Run `python verify_quadrilateral.py` in a Python 3 environment with SymPy available. The embedded program evaluates all one-gap and two-gap trigonometric moment integrals from their explicit Dirichlet densities and simplifies each asserted identity to zero. Its recorded execution checked sixteen symbolic identities (eight integral evaluations and eight derived moments, variances, and covariance). It also compared the direct Cartesian polygon construction against the trigonometric-gap formulas for 150,000 seeded uniformly sampled four-point configurations; all samplewise geometry consistency checks passed. The numerical covariance was \(0.388434453\), compared with the exact \(0.389799570\). This simulation is illustrative only; the exact integral evaluations and algebra form the proof.

The distributional premises (iid uniform angles, choice of a random vertex as origin, and Dirichlet spacings) are proven in RESULT.md, not inferred from the numerical experiment. The exact identity does not establish the full joint distribution or any universality beyond uniform independent unit-circle sampling. No independent scientific audit is reported.
