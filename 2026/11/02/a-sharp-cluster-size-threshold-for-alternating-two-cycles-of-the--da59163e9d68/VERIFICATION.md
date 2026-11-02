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

# Verification

The original map was evaluated directly on the two proposed cluster states to check both equations of the two-cycle. The full Jacobian matrices were formed from the actual trigonometric interaction, not a reduced symbolic formula, and the eigenvalues of the two-step product were compared against the proposed formula. A separate spectral-radius computation checked attraction and instability for sampled group sizes and coupling values. `check_clusters.py` executes these tests for network sizes two through nine using NumPy and SciPy; the checks passed in the construction environment.

The exact claims for every network size and every coupling in the open interval rest instead on the invariant-subspace decomposition, the monotonicity of the scalar orbit equation, the covariance proof for the threshold, and the endpoint integrals. Finite tests cannot establish those infinite quantifiers. A full-text historical comparison with the recent motivating preprint and an independent mathematical audit have not been performed. The sign at the nonhyperbolic equality does not resolve nonlinear stability.
