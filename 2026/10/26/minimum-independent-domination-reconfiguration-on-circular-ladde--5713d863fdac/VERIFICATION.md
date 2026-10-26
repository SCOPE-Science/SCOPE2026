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

## Reproducible checks
Run `python3 verify_bitmask.py` and `python3 verify_cyclic_words.py` from the directory containing these files. No third-party packages, network calls, or source-data files are required. Their full standard output is stored alongside each script as `verify_bitmask.output.txt` and `verify_cyclic_words.output.txt`.

The direct bit-mask program enumerates independent dominating subsets and constructs jump and slide adjacency for every prism with \(3\le n\le10\). The independent ternary-word program enumerates every cyclic word up to \(n=13\), reconstructs the slide graph, measures degrees and bipartiteness, and checks labeled-gap connectivity over a separate finite parameter range.

## What these checks do not establish
The computational range is finite. All-parameter cardinality, degree, connectivity, and bipartiteness statements rely on the explicit symbolic word-and-gap proof in RESULT.md. Neither script establishes priority in the literature, nor constitutes an independent external audit.
