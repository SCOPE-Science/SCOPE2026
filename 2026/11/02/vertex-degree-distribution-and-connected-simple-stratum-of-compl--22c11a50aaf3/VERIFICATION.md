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

# Exact reproducibility

Execute `python3 verify_direct.py` and `python3 verify_simple.py` using Python 3's standard library. The first constructs every directed orientation of the labeled complete-split graph for the five parameter pairs \((r,s)=(2,1),(2,2),(2,3),(3,1),(3,2)\), rejects directed cycles, computes transitive-reduction (cover) arcs by path reachability, and compares the degree histogram against the canonical-gap formula. All five matched exactly; for \((3,2)\) there were 96 acyclic orientations, 84 of degree 4 and 12 of degree 5. The second enumerates canonical gap states independently, checks that the induced local-move graph on all simple states is connected, and verifies the closed count for each of 16 combinations \(2\le r\le5\), \(1\le s\le4\); all passed, including 77,760 simple configurations at \((5,4)\).

These tests are limited to the listed finite instances; all-parameter claims are established by the constructive proof in `RESULT.md`. The two code paths are separate computational implementations, not independent external audits. No external validation has been performed.
