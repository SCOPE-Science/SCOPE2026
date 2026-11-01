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

# Reproducibility and verification limits

Run `python verify.py` with Python 3, NumPy, and mpmath installed. The program needs no internet access and fixes its random seed. The following checks were successfully run with the packaged program:

- The three exact density pieces numerically integrate to total probability one at 50-digit working precision; the first chamber has the stipulated exact cumulative formula.
- The second moment calculated directly from the density equals the closed mean central-section area divided by \(\pi\), and the independent gnomonic integral equals the same analytic expression.
- Every one of 18,000 deterministic-seed random unit directions gives matching radial distances from the sorted-coordinate expression and the twelve supporting halfspaces.
- For each sampled normal, the polygon formed by intersecting its plane with the independently enumerated 24 polyhedron edges has four, six, or eight vertices. Its Euclidean shoelace area produces a sample mean close to the exact predicted mean.
- The empirical frequencies in the three radial chambers agree with exact integrated masses within specified finite-sample tolerances; the density is continuous at its two interior boundaries.

The finite-sample area and frequency tolerances are diagnostic, not uncertainty bounds for the exact mathematical statements. The analytic proof is contained in RESULT.md. No independent mathematical audit has been performed.
