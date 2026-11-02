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

The standard-library `verify_integral.py` reconstructs the 28 Coxeter vertices using the Fano non-line triple rule, tests cubic degree, connectedness and girth seven, builds the integer reduced Laplacian, checks all \(729\) entries of \(RB=56I\) with the included JSON integer matrix, computes its determinant by fraction-free Bareiss elimination, and verifies ranks \(21\) and \(22\) modulo \(2\) and \(7\). The mathematical proof in RESULT.md shows that these three exact arithmetic facts force the displayed six invariant factors.

The independently written `verify_sympy.py` constructs the same graph and invokes exact integer Smith normal form and determinant routines, yielding the same decomposition and spanning-tree number. Both scripts completed without exception; their success messages are `COXETER_INTEGRAL_CERTIFICATE_PASS` and `COXETER_INDEPENDENT_SMITH_PASS`. Both scripts and the standalone 27-by-27 certificate are included. A finite exact computation does not validate broader families or establish publication priority.
