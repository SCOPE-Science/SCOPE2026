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

# Verification of the stated geometric probability law

Execute `python3 checker.py` from the extracted result directory (standard library only). The code checks 325 exact rational shoelace/corner identities across 25 quadrilateral diagonal-ratio pairs, exact variance-covariance constants, differentiation and symmetry of the analytic density and CDF at interior points, plus reproducible independent uniform-side Monte Carlo tests with fixed pseudorandom seed (180,000 draws for each of four affine shapes, 720,000 total). Positive numerical tolerances pertain only to randomized comparisons.

The proof relies on the explicitly written samplewise area identity, covariance calculation, diagonal-coordinate parametrization, and the elementary product-density integral; those steps, rather than the finite computational tests, establish its universal statements. The strict-convexity hypothesis and degenerate limiting variance supremum are essential. Only parallelograms have the full claimed density; other shapes are covered only by exact mean and variance. The result has not undergone independent mathematical validation.
