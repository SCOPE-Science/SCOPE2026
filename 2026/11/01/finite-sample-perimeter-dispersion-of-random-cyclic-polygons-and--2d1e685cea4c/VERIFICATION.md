---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The same companion checker compares exact oscillatory finite sums with Dirichlet-beta marginal quadratures for sizes 3 through 10, checks explicit triangle and quadrilateral values, and compares with independent iid angle samples for sizes 3, 4, 7 and 12. The frozen verification run reported `ALL_CHECKS_PASSED`. Its factorial moment tests corroborate asymptotic consistency, not a separate claim to the higher-order coefficients. The exact formula rests on the analytic integration in `RESULT.md`; finite numerical tests do not prove a universal identity or establish originality.
