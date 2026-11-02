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

# Reproducibility and limits

The standalone `verify.py` depends only on Python 3 standard-library modules. Run `python verify.py` from the artifact directory. On the complete packaged program the checks passed: 42 exhaustive-rank assertions, 119 independent mixed-moment recurrence assertions, and 19,998 exact telescoping/sign assertions, 20,159 in total. Exhaustive enumeration includes all 40,320 insertion orders at size eight, plus smaller sizes. The algorithm in `RESULT.md` provides a separate infinite proof; finite testing does not certify arbitrary sizes. The document contains no independent third-party audit.
