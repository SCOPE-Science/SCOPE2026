---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructing the disease-free infected subsystem gives K with characteristic polynomial z^2-a z-c. Neither threshold depends on lambda_h; both a and c decrease in delta_h and gamma_h, so their sensitivities are strictly negative. Fresh exact arithmetic reproduced the source-parameter threshold 1.3188521516976628 and elasticities -0.7532247434 and -0.2353827323 for delta_h and gamma_h.

## originality

PASS

The contribution is a source-specific correction rather than a new next-generation method. The primary paper's stated sensitivity analysis is inconsistent with the exact infected subsystem, and targeted Resultary searching found no published correction.

## value

PASS

The corrected signs reverse the interpretation of recovery and disease-induced removal and make loss of immunity exactly irrelevant to invasion. Because the source explicitly uses sensitivity analysis to prioritize epidemic controls, this is a substantive correction despite the short derivative calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
