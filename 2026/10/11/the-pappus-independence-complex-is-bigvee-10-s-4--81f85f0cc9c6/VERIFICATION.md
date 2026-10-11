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

The bundled `verify.py` uses only the Python standard library. It reconstructs the explicit 18-vertex graph, enumerates every nonempty independent set, reproduces the fixed sequential element matching, validates each Hasse-cover pair, and checks acyclicity by a complete topological sort of the oriented Hasse diagram.

The replay reports \(2597\) faces, \(11430\) Hasse covers, \(1293\) matched pairs, one critical \(0\)-simplex, and ten critical \(4\)-simplices. No other critical dimensions remain. The same program independently computes the mod-2 boundary ranks and obtains reduced Betti rank \(10\) in degree \(4\) and zero elsewhere.

The computation is finite and exhaustive. It does not establish any family-level statement about other incidence graphs or cubic symmetric graphs. Originality searches and literature comparisons are summarized in `REVIEW.md` and `AUDIT.json`; no independent audit has been performed.
