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

# Verification of the tall-pyramid Steiner-root theorem

The mathematical proof in `RESULT.md` is analytic and applies to every compact convex planar base with positive area, without a smooth-boundary hypothesis, and any fixed horizontal apex position. It explicitly establishes the exact volume, two asymptotic Steiner coefficients with controlled remainders, the limiting quadratic, and the critical discriminant splitting.

The included `verify.py` is a supplementary reproducibility check. Run `python verify.py` with Python 3, NumPy, and SymPy installed. This checked the symbolic first-correction and splitting identities exactly, then independently computed volume, surface area and mean-curvature coefficients from faces and exterior edge angles of convex polyhedral pyramids. Six different regular-polygon base types were tested at height \(3000\), all with the same off-center apex. A critical-quotient rectangle was tested at heights \(300\), \(3000\), and \(30000\); all tested bounded roots were real and the rescaled half-gap approached the analytically predicted coefficient. Each check completed without an assertion failure.

Finitely many polygon configurations do not certify the theorem over all convex bases or infinitely many heights. The generic asymptotic claim depends on compact-uniform control of the Steiner coefficients. The critical-case two-real-root statement depends on the exact strict inequality \(13>3\pi\), not numerical root plots. Claims of external or independent validation are not made.
