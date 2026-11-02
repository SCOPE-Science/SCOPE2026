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

# Reproducibility
Execute `python3 verify.py` with Python 3.9 or later. The code requires only the Python standard library and does not use the claimed structural lemma when testing actual minimal connected dominating subsets: it creates full subdivision adjacency, tests closed-neighborhood coverage, tests induced connectivity, and tests every one-vertex deletion. The property is upward closed, so a connected dominating set with no deletable single vertex is inclusion-minimal.

The separately coded candidate builder enumerates vertex covers, spanning trees, external leaf conditions, and boundary choices to compare actual **sets** for 47 small connected base graphs. A separate exact Stirling formula is compared against full cardinality dictionaries for seven labeled subdivided complete bicliques. Another 144 arithmetic parameter pairs check well-defined positive coefficients.

Validated local result:

`VERIFY_OK general_graphs=47 biclique_graphs=7 direct_subsets=1280106 arithmetic_pairs=144`

The tests comprise 1,280,106 enumerated nonempty vertex subsets in the direct graph cases. They are finite spot checks, not an infinite proof or a computational exhaustion of all graphs. The weighted spanning-tree identity and all-order statements are justified analytically in `RESULT.md`. The general-graph correspondence is intended for connected simple bases with at least three original vertices; the excluded two-vertex base is not implicitly certified.
