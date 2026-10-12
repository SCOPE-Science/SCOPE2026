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

The proof is analytic. The accompanying checker exhaustively enumerates every mapping on \([n]\) for
\[
2\le n\le6.
\]

For each functional digraph it reconstructs all directed cycles directly, counts cyclic vertices, and records every cycle length.

It verifies the exact cyclic-point distribution and tail law, every admissible conditional factorial moment in the master identity, covariance reductions for several test functions of \(L_n\), independence of a specified fixed-point indicator from \(L_n\), exact mean independence of the full fixed-point count, and the second-moment covariance formula.

The exhaustive replay is finite evidence only. The theorem for all \(n\) follows from the rooted-forest decomposition and exact cycle counting in a uniform permutation.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK mappings=50068 dist_checks=40 conditional_checks=187 covariance_checks=120 indicator_independence_checks=20 fixed_mean_checks=25 second_moment_checks=5`.
