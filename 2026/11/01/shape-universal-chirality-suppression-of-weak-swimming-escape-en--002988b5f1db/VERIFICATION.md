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

Run `python verify.py` with Python 3, NumPy and SciPy installed. A completed run returned `PASS: 126 deterministic checks`, with an interval coefficient of approximately `0.011111111111107692` (target exactly `1/90`) and a disk coefficient of `0.0026041666666666665` (target exactly `1/384`). Four finite-difference backward equations at distinct angular parameter pairs agreed with the truncated Dirichlet series within two percent at the chosen mesh, and their two small-speed measurements agreed with the quadratic discrete response. The numerical solution was even in swimming speed and showed shorter spatial-angular mean exit times for tested positive speeds.

The analytical verification consists of: Dirichlet Poincaré bound for the unperturbed inverse; convergent Neumann series around zero swimming; orientation reversal removing odd terms; an adjoint-integral calculation of the negative quadratic coefficient; the first-harmonic resolvent, Dirichlet Parseval, and strictly positive Stieltjes derivatives; an equality-case analysis for the global average exit bound. The independent elementary interval constant-drift calculation and disk polynomial Poisson solution check normalization factors.

**Scope limits:** finite grids cannot prove statements for all shapes, diffusivities, chirality values or derivative orders. Neither the tests nor this self-review constitute independent validation or publication-priority certification. The claims do not extend to reflecting boundary segments or nonuniform initial distributions.
