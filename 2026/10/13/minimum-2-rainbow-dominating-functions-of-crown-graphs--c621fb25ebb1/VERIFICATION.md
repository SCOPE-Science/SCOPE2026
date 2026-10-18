---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For crown Cr_n = K_{n,n} with a perfect matching deleted, an empty a_i sees both colors exactly if B_1\{i} and B_2\{i} are nonempty, and similarly swapping sides. Every feasible function of weight at most 3 is impossible for n≥3; weight 4 is realized by matching doubly colored vertices. For n≥5 all minima have side weights (2,2), forcing either aligned double labels on the same index (n choices) or independently colored singleton pairs on the same two indices (4 binom(n,2) choices). At n=4 twelve zero-side singleton configurations supplement 28 core functions; at n=3 twelve zero-side (1,2,3)-permutations and 24 (1,3)-split configurations supplement 15. Independent literal label enumeration through n=8 confirms minima 51,40,45,66,91,120 and no smaller weights. This is a symbolic all-n proof; the finite census is corroboration only.

## originality

PASS

The 2005/2008 rainbow-domination papers define the parameter and establish its weight-preserving G×K2 prism correspondence; that is credited, not claimed. A published Resultary theorem completely classifies all 2-rainbow functions on complete multipartite graphs, but Cr_n is not complete multipartite: deleting matched edges creates index-sensitive nonneighbors; the prior theorem does not imply the crown-specific counts. Published restrained- and perfect-Roman crown-graph results involve different feasibility constraints. No exact crown 2-rainbow min-function classification found under crown/bipartite Kneser/tensor-product aliases.

## value

PASS

The full set of minimum functions and exact multiplicity 2n²−n, with exceptional orders 3 and 4, is a natural extremal classification on an important near-complete bipartite family. Through the standard prism correspondence it simultaneously counts distinct minimum dominating sets of a graph product, giving a reusable exact invariant rather than merely an obvious bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
