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
# Verification and limits

The proof in `RESULT.md` uses the known exact rank weight, the exact cubic expansion at its continuous maximum, and an integer recurrence preserving the equation \((7n+4)^2-7m^2=9\) and the congruence \(n+m\equiv5\pmod6\). The first pairs \((n,k_n)\) on the recurrence are \((24,14),(391,237),(6240,3791),(99457,60432)\). These finite examples can be checked by the integer forward-difference formula; the proof of infinitely many equal-exponent pairs and of their limiting probabilities is analytic. The frozen small-field enumeration of the exact rank weight is background only; it does not check the asymptotic claim.
