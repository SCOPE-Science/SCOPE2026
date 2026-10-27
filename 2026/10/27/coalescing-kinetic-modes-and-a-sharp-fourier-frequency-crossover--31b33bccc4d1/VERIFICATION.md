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

# Reproducibility and limits

Use Python 3 with the public `mpmath` package installed, then run `python verify.py`. On the finalized source file, the verification program completed with `PASS: 47 finite Bessel/transform/asymptotic comparisons`.

The program checks the response in two different finite-time ways: direct numerical inverse Laplace transformation, and a Bessel convolution that follows from the renewal equation. It also checks rationalized pole/branch decomposition, the sign and scale of the branch remainder, and representative points of the critical frequency window. Each test is finite and numerical, with explicit tolerances. The asymptotic branch coefficient, its compact-frequency uniformity, and the sharp \(t^{-2}\) window are established by the proof in `RESULT.md`, not certified by numerical finite checks.

The source equations correspond to the continuum kinetic approximation and the chosen initial state; the package does not validate the approximation's error against the original quantum chain. `REVIEW.md` records the separate scientific assessment. No independent external audit has been performed.
