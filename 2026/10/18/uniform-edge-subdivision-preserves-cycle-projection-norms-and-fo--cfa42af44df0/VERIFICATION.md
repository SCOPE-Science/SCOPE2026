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

The companion `verify_subdivision.py` uses exact rational arithmetic and two distinct linear-algebra constructions. For each connected test graph, it computes the projector of the **expanded graph** from the inverse of a reduced incidence Laplacian. Separately it builds the equivalent weighted original-graph matrix \(H\) from another reduced weighted Laplacian. Every projected matrix entry is compared exactly to the asserted path-block formula, and all column sums are checked against both analytical norm identities.

The tests cover seven base graph families and five length patterns each: uniform lengths \(1,2,3\); nonuniform lengths all at least two; and mixed unsubdivided and subdivided edges. There are 35 configurations and 10,264 exact projector entries; all passed. The checker also checks the \(K_5\) strict order reversal and the exact values \(8/5,9/5,11/5\).

Run: `python verify_subdivision.py`. Only Python 3 standard-library modules are needed.

These tests establish only the named finite cases, not the universal theorem. The general statements are proved by the cycle-lift/Gram identities and exact absolute-column-sum argument in `RESULT.md`. An independent audit of the mathematical result has not been performed.
