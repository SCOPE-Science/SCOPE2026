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
The bundled `artifacts/verify.py` uses only the Python standard library and exact integer/bitset arithmetic. It reconstructs the message graph directly from the weight-three/weight-four connection set, checks its character spectrum and common-neighbor parameters, and then enumerates all maximal cliques and cocliques by exact Bron–Kerbosch search.

The replay verifies exactly \(64\) maximum cocliques, all equal to translates of \(T\); exactly \(30\) special three-dimensional direction spaces; exactly \(240\) maximum cliques, all affine cosets of those spaces; and exactly \(240\) resulting unordered extension partitions. It checks every partition on all \(64\) messages and obtains local distance distribution \(35\) at distance \(25\), \(7\) at distance \(30\), and \(21\) at distance \(31\). The count of labeled extension-coordinate functions is \(240\cdot8!=9{,}676{,}800\).

A successful replay ends with `VERIFY_OK`. The universal equivalence-orbit assertion additionally uses the explicit structural argument in `RESULT.md`; the finite search is a check of the classification and counts, not a substitute for that equivalence proof.
