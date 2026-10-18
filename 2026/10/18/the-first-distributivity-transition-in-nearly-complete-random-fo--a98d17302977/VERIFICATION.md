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

The standalone `verify.py` is executable using Python 3 and the standard library only. Running `python3 verify.py` checks every tree with at most six labelled vertices using the Prüfer-code bijection; every three-by-three missing-incidence pattern; and one concept-lattice direct-product example. The check verifies the unique six-vertex-tree obstruction and its \(360\) labelled realizations, along with all \(512\) three-by-three matrices.

The analytic critical-window proof uses graph component bounds and the standard dependency-graph Stein–Chen inequality. These limits are not consequences of the finite tests. Self-review has been performed, but independent audit and independent validation have not been performed.
