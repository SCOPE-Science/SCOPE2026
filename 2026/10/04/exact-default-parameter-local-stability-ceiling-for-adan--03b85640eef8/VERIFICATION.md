---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Independent exact algebra confirms the limiting optimization block polynomial and the Schur/Jury inequalities. At s=19800/859, P_s(-1)=0 exactly; the corresponding inequality is positive below and negative immediately above, while the other upper bound is looser and the remaining conditions are positive for s>0. The first-moment-only comparison gives 198 and ratio 859/100. The frozen RESULT.md, however, contains two literal form-feed control bytes corrupting two \frac commands and prints 19800/859 as 23.049; the true value is 23.0500582072.... The repaired final RESULT.md fixes only those transcription defects and leaves the theorem/proof unchanged.

## originality

PASS

The defining Adan paper supplies the recurrence and stochastic optimization theory but not an exact deterministic scalar Schur frontier. Fresh exact-number and quadratic-local-stability searches did not find the rational boundary 19800/859 or an implication-equivalent theorem. Generic control/multistep literature remains a residual alias risk rather than evidence of coverage.

## value

PASS

The exact local stability ceiling and period-doubling boundary quantify a concrete endpoint of the large-step robustness of a widely used adaptive optimizer, and the 8.59 factor isolates the effect of its gradient-difference channel. This is a motivated stability fact rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
