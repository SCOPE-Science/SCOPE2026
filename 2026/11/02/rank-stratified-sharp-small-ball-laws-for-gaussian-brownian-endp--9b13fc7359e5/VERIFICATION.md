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

# Verification of the rank-stratified Brownian endpoint small-ball result

The complete analytic proof is in RESULT.md. A runnable Python 3 standard-library-only reproduction file, `verify.py`, accompanies it; run with `python3 verify.py`. The saved scientific output is `verification_output.txt` and records 2381 passed deterministic checks.

The script verifies the elementary eigenfunction comparison on finite grids, the explicit spectral remainder sandwich over endpoint grids and multiple positive tolerances, classical pinned-bridge and Brownian-motion survival series, and separate numerical quadratures for singular and nonsingular Gaussian endpoint covariances. It checks the exact fixed-rank small-tolerance constants for multiple eigendirections. The program requires no external files or network.

**Limits:** Numerical quadrature and finite grids are corroboration, not an exhaustive proof of uniformity, rank limits, or conditional convergence. The proof's full quantifiers follow from the killed-heat-kernel eigenfunction inequality, the explicit Gaussian integrals, and bounded relative likelihood ratios. The historical-priority assessment is qualified by uninspected older literature; no independent audit has been performed.
