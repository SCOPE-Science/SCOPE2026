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

Run `python verify.py` with Python standard library only. The script computes the exact transposed influence vector for finite functional networks through indegree-zero peeling and explicit directed-cycle closure, and independently solves rational linear systems by Gaussian elimination. It then brute-forces all sets of intervened innate opinions for small graphs, and verifies the stated unique-highest-indegree decoy construction with different branching parameters.

A successful execution prints these checkpoints and finishes with `ALL_CHECKS_PASS`:

- `EXHAUSTIVE_FUNCTIONAL_GRAPHS 3413`: all tested labeled successor maps, up to five vertices, with fixed one-half susceptibility for outgoing vertices.
- `HETEROGENEOUS_EXACT_TESTS 880`: independent exact-rational centrality comparisons with varying susceptibility and observation weights.
- `OPTIMALITY_BRUTE_FORCE_TESTS 880`: direct exact-rational equilibrium and exhaustive intervention-set comparisons on small graph instances.
- `UNBOUNDED_FAMILY_TESTS 9`: one explicit deep-tree/decoy family for nine depths.
- `BOUNDED_INDEGREE_HIERARCHY_TESTS 27`: varying fixed indegree maxima and depths, with closed-form checks.

These are finite program tests. The all-orders asymptotic bounds are established by the proof in RESULT.md, not inferred from sampled data. The script performs rational arithmetic, not interval-based floating-point certification. Uniform wall-clock and bit operation counts are not claimed to be uniformly linear when exact rational numerators grow.
