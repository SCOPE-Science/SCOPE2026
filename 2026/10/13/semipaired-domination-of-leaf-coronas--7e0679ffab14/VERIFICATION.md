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

The verifier constructs the leaf corona of a connected base graph and independently checks the definition of semipaired domination:

1. the selected set dominates every corona vertex;
2. the selected set has even cardinality;
3. its vertices admit a perfect pairing in the graph whose edges join vertices at distance at most \(2\).

For every connected labeled simple graph of orders \(2\) through \(5\), it enumerates all even corona subsets until it finds the true optimum. The total number of connected base graphs checked is \(771\), and every optimum equals
\[
2\left\lceil\frac n2\right\rceil.
\]

The verifier separately implements the constructive proof. It checks the spanning-tree-square matching routine on all Prüfer-coded labeled trees of orders \(2\) through \(7\), totaling \(18{,}248\) trees, and checks deterministic connected graphs through order \(50\).

Recorded output:

```text
VERIFY_OK
n=2: connected_labeled_graphs=1, exact_corona_checks=1
n=3: connected_labeled_graphs=4, exact_corona_checks=4
n=4: connected_labeled_graphs=38, exact_corona_checks=38
n=5: connected_labeled_graphs=728, exact_corona_checks=728
n=2: prufer_trees_checked=1
n=3: prufer_trees_checked=3
n=4: prufer_trees_checked=16
n=5: prufer_trees_checked=125
n=6: prufer_trees_checked=1296
n=7: prufer_trees_checked=16807
connected_graphs_bruteforce_optimum_checked = 771
labeled_trees_constructively_checked = 18248
deterministic_construction_range = 2..50
all checks matched least_even_at_least_n
```

The finite checks do not prove the arbitrary-order theorem. The proof for all connected \(G\) is the private-leaf lower bound plus the longest-path matching induction in `RESULT.md`.
