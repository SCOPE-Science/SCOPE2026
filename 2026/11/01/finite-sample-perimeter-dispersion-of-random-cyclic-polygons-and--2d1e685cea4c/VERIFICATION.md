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
The embedded reproducibility program `check_random_cyclic_perimeter.py` was run with Python and `mpmath`. It compares exact oscillatory finite sums with separately integrated Dirichlet-beta marginals for integer polygon sizes 3 through 10; checks explicit finite exact cases; validates the rational Dirichlet-power variance and covariance identities; and simulates independent iid uniform circle arguments at 3, 4, 7, and 12 vertices.

The run reported `ALL_CHECKS_PASSED`. The analytic derivation in RESULT.md, including the Taylor-remainder argument, proves the universal identities and asymptotics; finite numerical checks neither prove an infinite claim nor establish historical originality. Independent audit has not been performed.
