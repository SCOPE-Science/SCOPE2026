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
The proof establishes the complete density and cumulative distribution by exact spherical polar geometry and a symbolic antiderivative. Running `python3 verify.py` from this package's directory completed with:

`VERIFY_OK vertices=20 fibonacci_directions=120000 cdf_samples=11 normalization=1 second_moment_unit_edge=6.999193713256 constant_tail_mass=0.658276410373`

The standalone checker uses only the standard library. It rebuilds vertex coordinates, checks the three-neighbor geometry and dot products, tests the analytic derivative relation, integrates density branches, compares the known second moment, and directly evaluates width on a deterministic Fibonacci-sphere grid. Numerical checks are non-exhaustive and do not supersede the geometric proof. No independent audit or external validation has been performed.
