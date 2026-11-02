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

The analytical argument is in `RESULT.md`. Its critical checkable steps are: (1) phase-self-adjoint distance equals the minimum real-part norm over phases, by a contractive projection; (2) the symmetrized numerical-range support equals that norm; (3) inner and outer containing bodies have the prescribed support minima and maxima; (4) their two first-quadrant squared-support integrals evaluate to the displayed closed forms; (5) support uniqueness yields rigidity; (6) Minkowski interpolation and a dense-spectrum diagonal operator realize all values; (7) differentiation gives the exact optimal cubic coefficient, and Taylor expansion gives the upper-bound asymptotic.

Execute `python3 verify_cartesian_profiles.py` in the package directory (Python standard library only). The program was executed on the delivered source and reported `PASS: 235 supplementary profile and finite-spectrum assertions`. It compares high-resolution quadrature to the closed forms, checks the exact interval width, evaluates intermediate Minkowski support profiles, tests 160 deterministic finite diagonal spectral examples, and checks the small-ratio cubic asymptotic. Numerical integration errors are bounded by floating-point/grid tolerances used in the script, not by an independently formalized interval certificate. These finite tests cannot prove universal quantifiers; all such quantifiers follow from the written analytic proof.

Scientific limits: the extremizers describe *closed symmetrized* numerical ranges; the actual numerical range need not be closed. Realizing extremizers uses bounded normal operators on separable infinite-dimensional spaces. Independent mathematical audit has not been performed.
