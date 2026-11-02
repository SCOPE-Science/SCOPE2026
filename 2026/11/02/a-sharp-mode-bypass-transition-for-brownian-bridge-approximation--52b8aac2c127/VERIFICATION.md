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
# Mathematical verification

The exact claim follows from the orthogonal Itô integral expansion and the complete cosine basis on the step interval, rather than from empirical enumeration. The coefficient integral, root-equation derivative and summable tail are written explicitly in `RESULT.md`.

The reproducible command is `python3 verify_modes.py`. It runs 127 standard-library supplementary checks: independent composite Simpson quadrature against the closed coefficient formula for randomly selected damping/frequency pairs; ranked weights and parity-initial-segment structure for multiple frequency budgets; a root bisection and the two-mode boundary ordering; direct Fourier sums compared with Parseval residuals using an explicit tail upper bound; and asymptotic small-damping constants. All checks passed in the supplied package before release.

Numerical quadrature and finite tests are not proofs of the claims for all modes, all positive damping parameters, or uniqueness of the threshold. The analytic derivative and projection arguments establish these infinite and continuous-domain statements. The root and error proportions shown in decimal are rounded from the unique exact characterization; no external mathematical audit or independent validation is claimed.
