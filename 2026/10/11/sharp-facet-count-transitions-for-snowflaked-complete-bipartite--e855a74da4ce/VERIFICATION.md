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

# Verification

The exact statement and proof are in `RESULT.md`; the Python file `verify_snowflake_biclique_vertices.py` independently enumerates all rational vertices of six finite dual Lipschitz polytopes by selecting linearly independent active constraints, solving over exact fractions, filtering all inequalities, and deduplicating intersection points. It uses only the Python standard library.

Run `python verify_snowflake_biclique_vertices.py`. Expected output:

```
m=2, n=2, t=1: vertices=14 expected=14 PASS
m=2, n=2, t=3/2: vertices=18 expected=18 PASS
m=2, n=2, t=2: vertices=6 expected=6 PASS
m=2, n=3, t=1: vertices=30 expected=30 PASS
m=2, n=3, t=3/2: vertices=42 expected=42 PASS
m=2, n=3, t=2: vertices=10 expected=10 PASS
```

The active-constraint connectedness proof covers all real \(t\in[1,2]\) and all integer \(m,n\ge2\); the finite checker is not a substitute for that proof. Bibliographic novelty remains conditional on the coverage limitations stated in `REVIEW.md` and `AUDIT.json`.
