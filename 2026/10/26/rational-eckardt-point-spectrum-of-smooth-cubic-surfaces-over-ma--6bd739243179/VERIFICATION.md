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

# Reproduction and evidence

Run `cubic_enum.cpp` and `direct_enum.cpp` as independent C++17 executables; the former enumerates 142 coefficient orbits and 36 smooth orbits, while the latter scans all nonzero coefficient vectors and outputs 24 refined profiles. Run `eckardt.py` after the orbit generator to classify Eckardt points by factor splitting, and `check_groebner.py` to check the 36 smooth orbit representatives over the algebraic closure using exact ideals. Full instructions and mathematical criteria are in `RESULT.md`.

Actual completed checks: direct enumeration found 384840 rationally nonsingular cubics and 322560 geometrically smooth ones; orbit enumeration found 36 smooth orbits accounting for 322560 equations; split-tangent computation found marginal distribution 0:189952, 1:115920, 2:10080, 3:2800, 4:3360, 7:420, 15:28; direct enumeration agreed on all 24 joint profiles; exact affine-chart Gröbner checks succeeded for all 36 smooth orbit representatives, with zero failures.

Limitations: exhaustive finite enumeration is not an external independent audit, although exact checks are supplied for replay. No claim over infinite families of base fields is made. Publication priority against unpublished and inaccessible mathematical tables is unresolved.
