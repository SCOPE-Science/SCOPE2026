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

The line graph is rebuilt from the ten two-element subsets of a five-element alphabet. The source graph's fifteen disjointness edges become the vertices of the line graph; incidence gives its thirty edges. The code `verify.py` has no external dependencies and is deterministic.

**Actual completed checks:** running `python3 verify.py` produced `VERIFY_OK`, reported \(2280\) optimum configurations and \(21\) symmetry orbits, and returned all \(2598060\) distinct unordered-pair exchange distances. The checker compared a bit-mask closure against a distinct set-valued closure on every initial mask, tested every seed through size seven, checked the entire group orbit partition and all shortest-path counts. The binary-mask representatives are also recorded in `ORBIT_TABLE.csv`.

**Scientific limits:** The computation proves exact facts about this single finite labelled graph, not a parameter formula for a graph family. The recorded self-review is not an independent external audit. Historical novelty cannot be certified by finite searches; unindexed earlier data remain possible.
