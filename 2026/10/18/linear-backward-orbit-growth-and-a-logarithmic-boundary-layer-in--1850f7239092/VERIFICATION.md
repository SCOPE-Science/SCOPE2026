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

The analytic proof establishes the full-dimensional inverse-fiber reduction, the exact scalar branching geometry and critical-root conventions, the \(2n+1\) count for every iteration and the logarithmic law for all sufficiently small nonzero target offsets. No finite computation is used in place of an infinite argument.

Run `python check_preimages.py` in Python 3 with NumPy and SciPy. In the saved package the checker returned `ALL NUMERICAL DIAGNOSTICS PASSED`. It directly solves the three monotone branches using Brent bracketing for \(d\in\{2,3,5,9\}\), \(c\in\{1.2,1.5,1.9\}\), and \(1\le n\le7\); it compares full star updates with the scalar map, tests fiber stabilization and the logarithmic slope at finitely many offsets. Double-precision tolerances, tested dimensions, and finite-depth tests impose no restriction on the analytic theorem.

Bibliographic sources and comparison limits are documented in the review. Independent verification has not been performed.
