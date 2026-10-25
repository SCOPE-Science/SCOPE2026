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

The proof requires two checks for each of the \(n+1\) colors: all color classes are perfect matchings, and the explicit \(2n+1\)-edge witness combines with each monochromatic matching into a connected spanning graph. The lower bound is an integer component-count inequality. The proof in RESULT.md establishes these for all \(n\ge2\).

The Python 3 standard-library program `verify_wild_prism.py` generates independent proper layer colorings by permuting rows, columns, and colors in cyclic Latin squares and constructs every graph edge without relying on a precomputed file. It verifies 97 generated instances for \(2\le n\le12\), 671 monochromatic union connectivity tests, and exhaustively excludes all 794 subsets of fewer than five edges for \(n=2\).

Command: `python3 verify_wild_prism.py`

Observed output: `VERIFY_OK graph_instances=97 connected_color_checks=671 exhaustive_K22_smaller_subsets=794`

Finite testing is not a proof of the infinite theorem. General minimum proper prism colorings with nonuniform vertical colors, unbalanced prisms, and the classification of all minimum witnesses remain unproved here. No independent audit is asserted.
