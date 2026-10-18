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

# Reproducibility and verification

Run `python3 verify_minimal_cds_rook.py` in a standard Python 3 installation; no external packages are needed. The program builds rook graph adjacency directly from pairs of row/column coordinates. It checks connectivity, domination and removal of each selected vertex on every nonempty subset for all nine specified boards, then compares the resulting cardinality histogram with a separate computation of the Stirling formula. The recorded stdout is `verify_minimal_cds_rook_output.txt`.

The evaluated nonempty subsets total exactly 1,413,959 across the nine boards; these finite exhaustive cases are not a proof for unbounded board sizes. The general argument proceeds through the row-or-column coverage criterion, tree obstruction, leaf characterization, and bipartite Prüfer identity, as detailed in `RESULT.md`. The independent-audit channel is not performed; the evidence consists of the stated self-review and reproducible checks only.
