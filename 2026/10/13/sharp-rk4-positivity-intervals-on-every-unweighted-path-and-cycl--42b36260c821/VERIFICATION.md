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
# Reproducible exact-rational checks

Run `python3 verify.py` with Python 3 and no third-party packages. The checker computes all four powers of each path/cycle negative Laplacian with integer operations, forms the RK4 matrix polynomial with `fractions.Fraction`, and reconstructs the exhaustive local off-diagonal polynomial lists. It checks that all Bernstein coefficients of seven distance-one cubics and five distance-two quadratics are strictly positive on \(0\le h\le2/3\). It verifies exact entrywise sign decisions at 13 rational timestep samples over 57 path/cycle graphs (dimensions through 30), checking 245752 exact-rational matrix entries.

Expected stdout:

`VERIFY_OK local_nearest_patterns=7 local_distance_two_patterns=5 path_cycle_sizes=57 exact_matrix_entry_tests=245752`

The finite tests are regression checks. The infinite-size conclusion relies on the radius-four walk argument and explicit sign facts established in RESULT.md; tested timesteps are not an exhaustive real interval.
