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

# Reproduction and scope

The asymptotic result is proved in `RESULT.md` by bounding the total omitted extension mass, bounding the discrepancy from repeat extensions, and normalizing the resulting positive binomial mixture. The proof of the total-variation bound does not require a finite computational certificate.

The unchanged `cycle_square_zero_checker.py` uses Python 3.10 or later and only the standard library. Its finite checks enumerate candidate maps directly through \(n=12\) to compare with the previously established exact rank polynomial. The separate calculations at \(n=81,82,121,122\) give numerical checks for the leading count and the conditional mean and variance. That script does not prove the asymptotic statements or test the exponential total-variation bound.
