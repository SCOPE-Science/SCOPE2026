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

Run the included standalone \(\texttt{verify_power_corona.py}\) with Python 3. It builds full graph adjacency directly from the multipartite definition, independently computes the initial closed-neighborhood observation and iterated unique-neighbor forcing, and enumerates every subset. In a separate function it computes the structural three-case classifier; a third function expands the purported closed polynomial by exact integer coefficient arithmetic. These three implementations agree for parameter profiles \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), and \((2,2,2,2)\), comprising exactly 156,928 tested vertex subsets. The bundled output log is from execution of that file. No failures occurred.

The proof in RESULT.md is essential evidence for the claimed infinite family; enumeration of seven small cases does not amount to exhaustive verification over unbounded part sizes. There is no Lean formalization, external certificate, independent audit, or claimed verification of arbitrary base coronas.
