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

The proof is analytic. The accompanying checker performs two independent finite replays.

First, it exhaustively enumerates every mapping \([n]\to[n]\) for \(2\le n\le7\), directly extracts cyclic vertices and connected components from the functional digraph, and compares the resulting joint distribution with the closed formulas.

Second, without enumeration, it reconstructs the cyclic-point tail law and the uniform-permutation cycle-count distribution by exact rational recurrences. It verifies the exact mean and covariance identities, the conditional stochastic ordering, and the conditional-variance decomposition.

Large-\(n\) floating-point evaluations of the normalized covariance and correlation are included only as sanity checks for the analytic limits. The asymptotic theorem itself follows from the Rayleigh tail limit and logarithmic-moment argument in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK mappings_checked=873611 joint_cells_checked=83 tail_checks=27 conditional_cycle_checks=83 covariance_checks=24 stochastic_checks=77 variance_checks=12 asymptotic_sanity_checks=8`.
