---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Differentiating stated UWG CDF directly gives f(x)=(1−p)αβ(−log x)^{β−1}exp[−α(−log x)^β]/(x[1−p+p exp(−α(−log x)^β)]²). Substituting y=−log x gives exact moment integral retaining exp(−r y); omitting it yields the incorrect gamma term attributed in the record to printed Eq (5.9). For α=β=r=1,p=1/2, direct elementary integration gives E[X]=2log2−1 (strictly between 0 and1); the recorded published series substitution yields 2log2>1, impossible. For β=1, u=x^α gives the stated Gauss 2F1 expression and at α=2,p=1/2,r=1 exactly π/2−1. Independent mpmath quadrature agrees with the beta-one hypergeometric expression on multiple parameter choices. Formula Eq (5.14) formed by substituting false moment expressions likewise cannot be valid as written, though true MGF and its power series exist.

## originality

PASS

Best-of-knowledge PASS for identifying a specific 2026 UWG article equation discrepancy and replacing its raw moments; elementary integration is prior mathematics, not claimed as new general theory. Primary publisher landing/abstract checked, but the publisher full Eq (5.9) could not be independently extracted in this execution; record supplies the literal formula and this remaining source-verification risk is disclosed.

## value

PASS

A concrete source-specific moment/MGF formula error can mislead statistical inference, yet one published numeric row agrees with the corrected result. The self-contained analytic counterexample and repaired β=1 closed form directly resolve a useful model-specific technical point rather than merely restating standard probability identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
