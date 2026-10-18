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

# Reproducible checks and limits

Run `python3 verify_pcf_bouquets.py` from a directory containing the script. This script uses only Python's standard library and constructs each clique-bouquet adjacency list directly. It compares the graph-theoretic open-neighborhood predicate with the inclusion-exclusion coefficient identity, then independently enumerates proper colorings in additional cases. Its deterministic output is supplied as `verification_output.txt`.

The checks cover 423,262 assignments over 44 graph/palette cases; 21 additional proper-coloring enumeration cases; 24 minimum-palette specializations; and first/second factorial moments at three heterogeneous bounded-block critical-window examples. All recorded checks passed.

Finite enumeration cannot establish a universal asymptotic limit. The proof of the stated Poisson window requires the uniform error estimates and all fixed factorial moments established in `RESULT.md`. The block sizes must stay bounded; the claim does not include arbitrary unbounded clique orders. No independent audit has been performed.
