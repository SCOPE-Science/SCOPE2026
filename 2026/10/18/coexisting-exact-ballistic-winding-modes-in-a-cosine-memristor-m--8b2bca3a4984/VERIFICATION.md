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

# Verification of the phase-locked transport theorem

Execute `python3 checks.py` using an ordinary Python 3 installation. The executable uses only Python standard-library arithmetic, complex roots and direct normalized-map iteration. Its finite tests cross-check the exact rational parameter identities, the winding exclusions and strict Schur inequalities for selected winding indices. It also tests local numerical convergence near the sinks.

The general conclusions for every winding index are proved in `RESULT.md` by exact algebra, \(\pi^2<10\), the quadratic Schur test and standard local sink dynamics. Numerical iterations are not an infinite-time proof, and neither a complete higher-period classification nor independent priority validation is supplied.
