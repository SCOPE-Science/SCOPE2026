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

Use Python 3 and NetworkX 3.x. Execute `python recursive_census.py`, `python atlas_census.py`, `python witness_analysis.py`, and `python cross_check.py` in the folder containing all four files and the corresponding `.out` records. The first two complete censuses generate a total of 1484 connected distance-hereditary isomorphism types on eight vertices and identify exactly two pointed obstruction graph types, one distinguished root each. The output text embedded alongside each script is from actual executions. The explicit witnesses have 14 and 21 edges, stable colour sizes 1+7, and orbit sizes 1+3+4. Cross-check independently matches the two census witness lists to these explicit graph constructions.

The enumeration claim depends on exact algorithms and the characterization of distance-hereditary graphs by pendant and twin insertions. Verifying finitely many instances of an infinite family is not at issue: the theorem is restricted to the exhaustively enumerated finite orders. All graph isomorphism checks are deterministic and exact, but the included code has not been independently formally certified.
