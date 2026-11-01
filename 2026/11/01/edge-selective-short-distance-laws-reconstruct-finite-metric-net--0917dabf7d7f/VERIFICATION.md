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

# Reproducible checks

Run `python check.py` with NumPy installed. The independent checker enumerates conditional geodesic distances between points on ordered pairs of edges via the vertex shortest-path matrix and 16-point Gaussian quadrature. It compares the resulting continuous two-coordinate probabilities with the exact short-radius formula for five different connected simple networks, 19 edges in total, including cyclic and acyclic examples. Exact `fractions.Fraction` calculations test the recovered 0/1 line-graph incidence and the triangle/claw local-law obstruction.

Expected final marker: `ALL_CHECKS_PASSED`. This finite computation is a consistency check only. The all-graphs derivation, the sharp ambiguity, and the Whitney-based reconstruction are mathematical arguments in `RESULT.md`, not computationally certified for infinitely many graphs. No independent mathematical audit was conducted. The checker has no dependence on any prior research package.
