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

# Verification and reproducibility

The mathematical result is proved in `RESULT.md`. A separate deterministic standard-library program, `verify.py`, checks the covariance identity by normalizing independent Gaussian coordinates to a spherical normal; verifies exact threshold substitutions, sharp endpoint shapes, sampled interior boxes, and binary configurations in dimensions \(2\) through \(12\); and tests the two high-dimensional limiting expressions.

Executing the embedded program directly with `python verify.py` produced `VERIFY_OK 6436`. The Monte Carlo part uses seven fixed box examples with \(65{,}000\) directions each, and deterministic pseudorandom seeds. The simulation acceptance tolerance is deliberately wider than sampling error to avoid a spurious false failure; it is not a rigorous numerical enclosure. The other computed checks are finite arithmetic consistency tests, not proofs of all-continuum assertions.

The proof relies on standard spherical Dirichlet moments, strict covariance monotonicity after conditioning, convexity in the logarithms of the side lengths, and an asymptotic gamma ratio. The theorem does not require external datasets, proprietary software, or any unembedded file. No independent mathematical audit has been performed.
