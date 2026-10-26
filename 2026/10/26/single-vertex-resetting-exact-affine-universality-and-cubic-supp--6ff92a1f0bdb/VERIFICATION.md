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

Run `python verify_reset_graph.py` using NumPy and SciPy. The included executable reproduces the finite-dimensional first- and second-moment equations, assesses positivity and singular coefficients across six graph families, verifies the two-vertex closed form, and checks the exact affine flow identity under common timed resets. It reported `PASS 140 independent checks`.

Critical proof checks: the reset map is the coordinate projection `J=I-e_r e_r^T`; its quadratic generator produces the forcing `Omega^2 e_r e_r^T/lambda`, not a Gaussian diffusion term. The grounded minor `B` is positive definite on a connected undirected graph after removing the reset vertex. The Lyapunov inverse and its block expansion prove the asymptotics for every fixed graph. The covariance positivity argument is based on the resolvent of a killed continuous-time random-walk pair, not on finite sampling.

Limitations: finite numerical checks do not prove all-graph assertions. The proof concerns the exact linear jump process; no statement for sine-coupled circle phases, spatially varying reset rates, multiple reset vertices, or graph-size-uniform error terms is verified. This package carries no independent scientific audit.
