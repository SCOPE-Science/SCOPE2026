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
# Verification and scope

The analytic proof in RESULT.md checks every connected finite weighted undirected graph with one reset vertex, all constant real frequency vectors, and every positive coupling and reset rate. In particular, it uses the exact jump map, not a numerical approximation to stochastic reset events.

The included `verify.py` was executed with Python, SymPy, and NumPy. It verified 16 rooted weighted graph cases (including paths, a triangle, a star, and a cycle), with exact graph-Poisson identities, finite-rate stationary mean identities, covariance matrix equations, frequency-shape invariance, and all principal minors. It also verified the general-parameter two-vertex covariance symbolically. A separate simulation sampled 180,000 Poisson pre-reset events from the exact two-vertex linear flow and matched the stationary mean and covariance within fixed tolerances; Poisson-arrival sampling uses the standard prearrival stationary distribution. These finite diagnostics do not certify the infinite network theorem.

To reproduce, run `python verify.py` from the directory containing this file; dependencies are SymPy and NumPy. The program prints three PASS lines if all assertions hold. Independent auditing has not occurred. The stochastic model is unwrapped and linear; the theorem does not certify nonlinear phase coherence at finite rate.
