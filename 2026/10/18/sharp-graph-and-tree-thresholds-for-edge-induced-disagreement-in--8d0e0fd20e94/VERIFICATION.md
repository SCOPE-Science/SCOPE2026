---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Connectedness makes the follower Dirichlet Laplacian positive definite. The grounds do not move or change their incident edges, so edge insertion is an exact rank-one Laplacian update with the same right-hand side. Applying the full n-vertex centering matrix after extending the update by zero on the pins gives the stated variance change (not an electrical-energy change). Independently reproduced the finite universal lower bounds in branches/29d0165f-3ac8-4e8c-a229-42a7c1c12741/replay_exact.py, with output replay_full.out in that directory, using rational forward elimination and back substitution and connected edge subsets instead of Prüfer words for trees. Pin relabeling is bijective and the connected edge masks and connected (n−1)-edge subsets are exhaustive in the respective ranges. There are 956 connected comparisons through order 5 and 5417 initial-tree comparisons through order 6, all nonincreasing, with the decrease/tie counts agreeing by order. For the two larger witnesses the same exact replay gives changes 43/36504 and 137/6776; each insertion is a genuine follower nonedge. Trees are restricted only before insertion. The supplied scripts were inspected, not executed.

## originality

PASS

The variance metric, harmonic equations and rank-one update are known ingredients; the assessed result is the pair of exact minimal graph orders under the fixed two-pin and follower-edge hypotheses. No inspected source states or entails both thresholds in this model, or supplies the individual thresholds as an existing census.

## value

PASS

Settles the first orders at which a natural monotonicity intuition fails, with a separate sharp answer for tree initial conditions. The minimal witnesses distinguish all-vertex opinion variance from energy on the links and give concrete small regression cases for a standard two-boundary model. The cutoff is the first possible counterexample in each class, not an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
