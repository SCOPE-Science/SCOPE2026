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

The full Python-standard-library program `verify.py` enumerates all three-element independent sets for each circular ladder with circumference 4 through 10 and expands every complementary facet to its complete nonempty face poset. It performs a deterministic sequence of element matchings at the vertices in order, constructs indegrees for every arrow of the complete Hasse graph with matched edges reversed, and removes every node by a topological sort. The checks assert exact face and facet counts and every critical-cell multiplicity. Run `python3 verify.py` from a directory containing only the supplied program; no dependencies are needed.

The verified outputs include seven exact acyclic matching certificates. For the largest case there are 1,047,519 faces, 523,731 pairs, 57 critical cells and 10,467,920 cover incidences. This is a complete finite argument only for the seven declared circumferences; no finite computation is treated as an infinite induction. The existing published homology table contains the same ranks, and the additional contribution is the certified homotopy type. Independent assessment has not been performed.
