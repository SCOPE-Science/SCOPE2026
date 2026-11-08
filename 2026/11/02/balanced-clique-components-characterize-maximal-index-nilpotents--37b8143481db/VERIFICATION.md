---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Index-n nilpotent partial bijection on n labels is exactly one spanning directed path; its unique vertex ordering v0,...,v(n-1) determines the shift. Induced partial-graph isomorphism requires adjacency in the first n-1 vertices exactly equal after one shift, i.e. symmetric Toeplitz adjacency matrix in that ordering. In a cluster graph, adjacency iff clique-label equality; the smallest repeated label separation d propagates equality at every distance-d pair, and no two positions modulo d carry one label, forcing d=r and a periodic clique-label word. Hence clique sizes must be floor(n/r) or ceil(n/r), and choosing clique residues gives r! if all equal, else t!(r-t)!; independent labeled-vertex order within each clique yields product s_i!. Conversely every such periodic ordering defines a partial automorphism. Independent exhaustive permutation checks of every integer partition of n=2,...,7 (43 configurations) agreed with the formula and equivalence, including singleton and single-clique cases. Finite checks corroborate, while symbolic shift-invariance proves all n.

## originality

PASS

General inverse-semigroup and monogenic inverse-monoid counts precede this result; Toeplitz graph theory already explains periodic component partitions. However the inspected literature does not state the exact labeled maximal-nilpotency-index enumeration in PAut of cluster graphs, nor the ordering bijection with all Toeplitz adjacency matrices. The combination, sharp existence criterion and multiplicity are assessed as new with possible equivalences via partial automorphisms of equivalence relations.

## value

PASS

Maximal nilpotency index and multiplicity are natural structural invariants of graph partial-automorphism monoids. A sharp necessary/sufficient balance criterion and exact labeled-element counts are independently useful for semigroup enumeration and the related multipartite complements; not merely a renaming of graph regularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
