---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the two-dimensional deterministic envelope, surjectivity of the invertible map from initialization to gradient makes the positive ratio of gradient magnitudes arbitrary. After removing a common scalar, minimizing the condition number of the row-scaled matrix reduces to minimizing its Frobenius-squared norm divided by determinant magnitude. The unique arithmetic-geometric-mean minimum occurs when the two scaled row norms agree, and the determinant identity gives the stated closed form in the absolute row correlation. Independent numerical singular-value minimization on two generic positive-definite matrices matched the closed form and the predicted row-equilibrating ratio to numerical precision; the forty-five-degree rotation family reproduced the exact floor equal to the original spectral condition number for several values. For the Gaussian theorem, fixing a vector orthogonal to one row bounds the smallest singular value on a positive-density box where all other gradient coordinates stay away from zero, while the largest singular value grows at least inversely with the first gradient coordinate. The nonsingular Gaussian density is bounded below on that compact box, so integrating the reciprocal singularity gives an infinite first moment. This analytic integral, not finite simulation, proves the all-dimensional statement.

## originality

PASS

The Adam-mini source studies the same instantaneous diagonal preconditioner in random dense quadratic blocks and reports that rotated dense blocks can resist condition-number improvement, but it does not state a Gaussian-initialization infinite-mean law or the exact two-dimensional initialization envelope. Das et al. develop broader quadratic preconditioning analysis and show that non-diagonal Hessians can erase Adam's conditioning advantage, yet the inspected result statements use different condition quantities and do not imply the local reciprocal-coordinate tail or the exact orientation formula. Classical one-sided diagonal-scaling theory is a meaningful priority risk for the deterministic two-dimensional minimum, so originality is accepted primarily for the combined source-specific theorem: the exact attainable floor together with the infinite population mean under the unregularized Gaussian diagnostic.

## value

PASS

The infinite-mean theorem shows that an average condition-number summary for the unregularized Gaussian diagnostic has no finite population target, a direct methodological consequence for interpreting the motivating experiment. The exact two-dimensional floor separately identifies an orientation barrier and explains why diagonal eigenvectors can be perfectly equilibrated while a forty-five-degree rotation can preserve the original condition number. Together these are motivated structural limitations of the diagnostic rather than arbitrary matrix calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
