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

# Reproduction

Place `verify.py`, `census.tsv` and `optima.tsv` in the same directory, and run `python3 verify.py` using standard Python 3. The run exhaustively reconstructs the eligible oriented words, all compatibility edges and all cliques for every length from two to ten. It checks every recorded count, independently tests all twelve listed length-ten codebooks directly on their prefixes, suffixes and deletion outputs, and partitions the maxima into three four-element reversal/complement orbits.

The replay on the packaged files returned `VERIFY_OK`. The length-ten oriented graph has 142 vertices, six maximum nine-vertex cliques, and no clique of size ten or more. The complete clique counts by size zero through nine are `1,142,4566,51196,216875,347859,200412,37440,1800,6`. An independently built integer linear program based on forbidden word pairs reported an optimum of nine at length ten; the proof certificate does not require the solver.

# Proof boundaries

The increasing-index traversal is exhaustive because every finite clique has exactly one strictly increasing enumeration; the code imposes compatibility with each previously selected vertex through bitset intersection. The independent word-level test of the listed codebooks confirms attainability. These finite procedures do not establish any statement for lengths greater than ten or an end-to-end continuous-stream decoder. Historical originality has not been independently audited.
