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

# Verification and limits

The exact proof in `RESULT.md` is primary evidence. It reduces every horizontal reflected-Minkowski slice to a homothetic copy of the centered symmetric base using explicit feasible height pairs, integrates its \((n-1)\)-dimensional measure, and compares the resulting polynomial coefficient by coefficient. Strict parameter monotonicity follows from the elementary decreasing function \(t/(e^{ut}-1)\); index concavity is an exact second difference. The high-dimensional limit follows from elementary exponential asymptotics.

The companion `verify.py` was run against its actual bytes and reported `VERIFY_OK 1830 tests`. Checks include 14 dimensions, five rational taper values and four rational Minkowski scale values; normalized reflected coefficients, endpoints, strict concavity, and 24 additional convex-hull volume comparisons in dimensions three and four. Independent numeric hull geometry is a diagnostic of the analytic cross-section identity. NumPy and SciPy are needed for that diagnostic; the exact rational arithmetic uses only standard Python. The finite suite is not an exhaustive proof of infinitely many instances, and the method makes no external or independent audit claim.
