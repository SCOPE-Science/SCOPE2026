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

# Reproducibility

Run `python CHECK.py` with SymPy. It verifies the exact symbolic trophic cancellation after imposing the spatial matching condition, the weighted ground-state divergence identity, the explicit nonproportional equilibrium substitution in each PDE, Neumann endpoints, and strict example bounds using the elementary inequality \(\pi^2<10\). The script was run successfully and printed `PASS`.

The infinite-dimensional convergence proof is mathematical, using standard semilinear parabolic maximum principles, boundedness and smoothing. The checker is not an independent verification or a substitute for these estimates. The theorem assumes strictly positive initial data; it does not state a uniform exponential convergence rate. The matched profile assumption can be checked pointwise for a proposed equilibrium.
