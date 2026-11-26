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

Reconstructed GP(8,3) from the 24 stated edges. Each paired-dominating set must be balanced in the parity bipartition, so exhaustive enumeration need only examine t vertices from each side at size 2t. The independent enumeration tests closed-neighborhood coverage and all Hall inequalities; for t=1,2,3,4 it finds 0,0,0,684 sets. A slide crosses the bipartition and destroys balance. For the other moves I classified every unordered pair of optimum sets by its differences, applying Hall again on the common six vertices for partner preservation. Independent BFS reproduces all reported metrics: J has 3504 edges and eccentricities 6:216,7:432,8:36 on its sole component; E has 2016 edges, a 630-state component of eccentricity 6 and 54 isolates; Q has 1392 edges, the same 54 isolates, and components of orders 432,168,30 with eccentricity profiles (9:192,10:240), (9:96,10:72), (4:30). In each pair graph the isolate index set equals the set of optima inducing exactly four edges, hence 4K2 because a perfect matching exists. The certificate's graph, state list, three edge lists, eccentricity arrays and induced-edge counts agree exactly with the fresh computation. Partner preservation is an edge-wise existential condition on vertex sets, not a claim about lifting paths to a space with fixed matching labels.

## originality

PASS

The supported distinct contribution is the exact comparison of move spaces on the same minimum paired-dominating family, especially the induced-4K2 isolation criterion and the splitting under the existential shared-matching condition. The abstract balance obstruction to slides is elementary and not credited as an original claim. The strongest accessible matches concern different state sets or graph families; none supplies or makes routine the stated transition classification. This is a best-of-knowledge judgment, not a priority certificate.

## value

PASS

The smallest paired-dominating states of this named symmetric cubic graph provide an exact comparison where changing the rule has distinct effects: all states communicate by individual jumps; adjacency-only slides disappear; adjacent pair replacement leaves exactly the induced-matching states frozen; preserving partnerships does not freeze new individual states but splits the mobile part into three. The same explicit benchmark and the isolate test are useful for distinguishing instantaneous matchability from retention of a partnership. The complete finite geometry is more informative than an isolated optimum number or an arbitrary metric from a census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
