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

The full proof is self-contained in `RESULT.md`. It uses the spanning-tree rank criterion for tight graph-difference inequalities, exact Euclidean centering of binary and ternary potentials, and the span of farthest polar vertices. It proves the result for all stated positive integer multipartite profiles, without reliance on extrapolation from computations.

The standard-library script `check_multipartite.py` was executed successfully with the command `python3 check_multipartite.py` after creating its final version. The returned line was `MULTIPARTITE_EXACT_CHECKS_PASSED 31 nonunique_small 19`; representative exact-rational contact and dimension outputs were printed for the profiles `(3,3,3)`, `(2,2,2,2)`, `(3,3,2)`, `(5,4,1,1)`, `(4,2,2,1)`, `(3,3,3,2)`.

The checker enumerates feasible integer three-level polar potentials in finite examples and computes ranks over rational numbers. Its finite search does not prove the theorem for unbounded dimensions. Literature priority is provisional; independent mathematical audit has not been performed.
