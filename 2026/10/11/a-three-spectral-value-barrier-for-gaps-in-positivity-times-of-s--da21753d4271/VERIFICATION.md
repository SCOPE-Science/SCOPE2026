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

The spectral-projector formula gives the exact off-diagonal entries for every pair of coordinates and every positive time. The proof of strict monotonicity uses the elementary exponential inequality, with no finite cutoff assumption.

The finite cutoff matrix has an exact spectral decomposition over radicals and three distinct eigenvalues; the nonzero entry cutoff is the exact logarithm of a rational number. The infinite construction uses a pairwise antisymmetric projection and a normalized positive vector, with a direct entry formula for arbitrarily distant pairs.

For the four-point path witness, the first sign window follows from the monotonicity of a two-eigenvalue even functional calculus, and the second from the sign of a third divided difference. The all-time positivity at and beyond exponent two uses the published theorem for doubly nonnegative matrices, arXiv:1303.4701. No numerical extrapolation is used for the claimed intervals.

Run the included Python standard-library program `verify_spectral_times.py` for independently reproducible exact finite identities. Its floating-point samples are consistency checks only, not proof. Independent external audit has not been performed.
