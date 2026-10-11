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

The proof was reconstructed from the explicit graph definition. The critical general step is deterministic: outside the common edge, a matching uses at most one edge incident with \(u\) and at most one edge incident with \(v\), so it blocks at most two of the pairwise disjoint middle edges \(q_i\). For \(n\ge 3\), one middle edge remains compatible with the whole matching. This identifies the entire matching complex with the star cluster of the simplex \(\{q_1,\ldots,q_n\}\), and the standard flag-complex star-cluster theorem supplies an actual simplicial collapse.

`verify_book_matching.py` performs an independent finite check for \(1\le n\le 7\). It enumerates all subsets of graph edges, retains exactly the matchings, builds mod-2 boundary matrices, computes reduced Betti ranks, and directly checks which faces are outside the star cluster. The stored output ends in `VERIFY_OK`.

The finite computation is not an infinite certificate and is not used as one. It checks the two boundary cases and several instances of the general argument. No claim is made about books built from cycles longer than four, generalized matching complexes, or alternative triangular-book conventions.
