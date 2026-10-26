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

# Verification record

The `verify_braid.py` program requires only Python 3 and no nonstandard packages. Execute `python verify_braid.py` in a directory containing the program. It enumerates faces independently from surjective labeling functions, implements the Tits product as nested nonempty intersections, and directly compares both multiplication orders. Its source and the displayed mathematical proof are self-contained.

Tested ranges: \(1\le n\le5\) for all centralizers and ordered commuting pairs; \(1\le n\le3\) for all ordered commuting triples and quadruples and all unordered clique sizes; \(1\le n\le4\) for all chamber coarsening cliques, commuting adjacency, and pairwise maximal-clique intersections; \(1\le n\le7\) for direct-sum indecomposable-permutation overlap distributions. The program prints per-dimension values and `VERIFY_OK 163882 finite direct product, tuple, centralizer, maximal-clique, and overlap-spectrum checks`. This was observed by executing the supplied program.

The finite tests do not establish any universal quantifier over \(n\) or \(r\), nor do they establish originality. The proof of the unrestricted statements appears in RESULT.md. The numeric tuple sequence has an already-published tree-enumeration identity; its reuse is acknowledged. Independent audit is not performed.
