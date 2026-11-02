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

The graph universe is exactly the twenty-eight two-element subsets of an eight-element set. Adjacencies and three Seidel switching sets are fully specified in RESULT.md.

`verify.py` constructs four integer adjacency matrices, checks degree and common-neighbor parameters, enumerates all distinct ordered triples and ordered quadruples for the three rank-four predicates, and canonicalizes each of the 20,475 four-vertex induced subgraphs using the full permutation group on four labels. It also prints explicit witnesses for the two missing-pattern assertions.

`verify_independent.cpp` independently constructs bitset adjacency matrices and uses separately coded extension tests and 24-permutation canonical encoding. It reproduces the same four truth vectors, ordered witness counts (36 for the special triangle in the \(C_3\sqcup C_5\) switch, 48 for the special edge in the matching switch), and eleven-type saturation in each Chang graph. Both programs check \((28,12,6,4)\) directly.

The analytically proven three-round Duplicator strategy uses four strictly positive extension counts around every ordered adjacent or nonadjacent pair. Exact exhaustion, rather than a statistical sample, verifies the finite rank-four certificate. Build commands and output are included. These checks have not been independently audited by a separate mathematical reviewer.
