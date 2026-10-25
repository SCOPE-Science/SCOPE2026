---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The invariant counts, for each k-vertex unrooted tree T, edge subsets by sorted component-order partition, so the rank k-l(mu) equals the edge-subset cardinality. The source constructs all rooted trees as multisets of child rooted codes and identifies all unrooted trees using their centers; these are exhaustive combinatorial bijections, not sampled graph lists. Independently enumerated every unlabelled tree with NetworkX nonisomorphic_trees(k), k=4..10, and counted all 2^(k-1) spanning forests per tree by connected components, obtaining tree counts 2,3,6,11,23,47,106 and exact tau values 2,2,3,3,4,4,6. At k=10 precisely one pair collides at rank five and none at six; its diameters are 6 and 7. Thus tau(10)=6 while all earlier 4..9 meet floor(k/2). The result is restricted to k<=10, not arbitrary orders or the full CSF tree conjecture.

## originality

PASS

Awan proves the general lower bound floor(k/2) and introduces essentially the same truncation parameter, but neither the exact first strict order ten nor its full 106-tree collision census is found in the inspected theorem/Section 4. Zeng considers more complete symmetric-function reconstruction and diameter-restricted methods, which do not imply the rank-five/equal-rank-six distinction. Independently verified the exact k10 computation and searched related published findings. Best-of-knowledge priority, not a universal novelty certification.

## value

PASS

The least number of retained connected-partition layers that reconstruct every unlabelled tree of a fixed order is a natural sharp inverse-invariant cutoff directly motivated by chromatic-symmetric reconstruction. The first strict departure from a published lower bound and explicit unique obstruction are mathematically informative finite boundary data, not an arbitrary graph example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
