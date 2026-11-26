---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

All simplex summands have constant coordinate sum and the summand on the full connected set has dimension n-1, so the polytope has that dimension. The standard face/tubing correspondence gives dimension n-1-k for k proper tubes. I reproduced the complete enumeration with new code: generate unlabeled trees by all single-leaf extensions, which suffice because every nonsingleton tree has a leaf, and deduplicate by the minimum recursive unordered rooted encoding over all possible roots (a complete unrooted isomorphism test). For face polynomials, group tubings by the union U of inclusion-maximal tubes. U is proper because maximal tubes are pairwise disjoint and nonadjacent and the ambient graph is connected; the components of G[U] are exactly those tubes. Recursing on their proper tubings counts each family once. The order census was 1,1,1,2,3,6,11,23. The only repeated vertex count at any fixed order was 2952 at order eight, on the displayed degree-distinct trees; the full face vectors independently agree as stated. For angular counts, Gaussian coordinate rankings are uniform. Each connected-set summand contributes the highest ranked coordinate. The overall root is recoverable from the resulting vertex: its coordinate attains the upper bound given by all connected sets containing it, and each other coordinate misses at least the full graph contribution. Subtracting the root contribution and restricting to each deleted-root component proves recursively that ranks yield the same vertex exactly when they yield the same elimination tree. A fixed elimination tree has ranking probability 1/H, where H is the product of all subtree sizes, by independent uniform component rankings conditional on the first vertex (or the rooted hook-length count n!/H). The independent hook histogram sums 1/H² with multiplicities and gives 14239/4838400 and 76393/33868800, with difference 97/141120. Thus equal vertex count was used only to eliminate alternatives; equal full face vectors for the pair were checked separately.

## originality

PASS

Best-of-knowledge pass for the concrete least-order equal-face-vector witness distinguished by these exact angular collisions. Standard tubings, search trees, and random-search-tree collisions are not credited as new. Primary and local comparisons support the distinction between prior counting/sampling frameworks and this joint threshold and witness; the bounded comparison is not a priority guarantee.

## value

PASS

Face vectors are a standard combinatorial summary, while Gaussian collisions measure the concentration of a vertex law induced by the canonical realization. A pair proving that the first summary does not determine the second is mathematically motivated, and the exact least order and uniqueness at that order make this a sharp finite witness rather than an arbitrary table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
