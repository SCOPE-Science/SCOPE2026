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

The standalone checker constructs each crown graph directly, enumerates all vertex subsets, checks domination from the adjacency relation, and tests whether the induced bipartite subgraph has a perfect matching using an augmenting-path matcher. It independently compares those results with the theorem’s criterion \(p=q\ge2\).

It then verifies the coefficient identity \(d_{\mathrm{pr}}(\operatorname{Cr}_n,2t)=\binom{n}{t}^2\), the minimum-set count \(\binom{n}{2}^2\), the total count \(\binom{2n}{n}-n^2-1\), and the assertion that inclusion-minimal paired-dominating sets are exactly the size-
\(4\) sets. The packaged run exhausts \(3\le n\le8\), comprising \(87{,}360\) subsets and graphs of order up to \(16\).

The finite computation is only a stress test. The infinite statement rests on the written Hall-theorem proof. No external solver, table, or probabilistic inference is used.
