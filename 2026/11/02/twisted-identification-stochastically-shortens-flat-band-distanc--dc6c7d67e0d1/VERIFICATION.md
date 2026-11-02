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

# Reproducible verification and limits

With Python 3 and NumPy installed as declared in `requirements.txt`, run `python3 checks/verify_twist.py`. It exercises the original minimum of the two flat Möbius deck-distance branches (not the simplified defect law as its integrand) and the cylinder distance in independently evaluated three-dimensional Gauss–Legendre quadrature for aspect ratios \(1/2\), \(1\), \(1.3\), \(2\), and \(4\). It additionally verifies the cylinder squared moment, performs seeded direct independent uniform point-pair sampling at three ratios, checks the exact small-width rational branch, checks fourth-order onset coefficients and checks a broad strict-monotonicity numerical grid. The analytic proof in RESULT.md, not this finite test suite, establishes assertions for every positive real aspect ratio.

Observed output on replay included `RATIONAL_SMALL_BAND_DEFECT`, `QUADRATURE`, `MONTE_CARLO`, `ONSET_COEFFICIENT`, `MONOTONICITY_GRID_AND_LIMITS_PASSED`, and `ALL_CHECKS_PASSED`. The largest recorded quadrature discrepancy over the five tested ratios was below \(2.4\times10^{-5}\) in unit-circumference squared-length units. Checks use reproducible deterministic quadrature and a fixed pseudorandom seed.

No check asserts a finite-experiment proof of an infinite inequality, claims an optimal transport coupling, or independently certifies novelty. The public verification record reports only the scientific reproducibility conditions and mathematical limits.
