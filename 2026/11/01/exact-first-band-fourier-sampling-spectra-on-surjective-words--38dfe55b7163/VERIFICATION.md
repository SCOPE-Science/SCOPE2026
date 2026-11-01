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

# Reproducibility
Run `python3 surjection_checker.py` using Python 3 standard library. The implemented complete enumerations for \(2\le q\le4\), \(q\le n\le q+3\) report 3006 exact moment comparisons. The checker uses rational probabilities to avoid floating-point approximations. These finite checks cannot certify the universal asymptotic theorem; the proof in `RESULT.md` does.
