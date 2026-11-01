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

# Direct reproducibility checks

Run `python3 verify_rankone_nilpotent.py` with Python 3 and no third-party packages. It constructs finite-field vectors, rank-one outer products, multiplication tables and commutation from their defining equations. It then calculates all matrix-level degrees, tuple counts through length three, maximal cliques, connected components and diameters independently of the subspace classification, and compares with the closed formulas.

Verified field/dimension cases: \((2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)\), where each pair denotes \((n,q)\). The checker reports `VERIFY_OK`. Observed highlights: at \((n,q)=(3,3)\), there are \(104\) vertices, degree \(13\), \(26\) maximal cliques of size \(8\), and diameter \(3\); at \((4,2)\), there are \(105\) vertices, degree \(24\), and \(65\) maximal cliques, split into \(30\) of size \(7\) and \(35\) of size \(9\), with diameter \(2\).

These exhaustive **finite** tests corroborate but do not replace the all-prime-power, all-dimension proof. No external proof assistant, independent expert review or independent mathematical audit has been performed.
