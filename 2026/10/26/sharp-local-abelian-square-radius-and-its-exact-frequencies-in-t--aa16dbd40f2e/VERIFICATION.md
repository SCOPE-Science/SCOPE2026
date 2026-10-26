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

Run `python3 verify.py` with `templates.csv` in the same folder. Only Python standard-library modules are used. It checks complete two-letter source-language closure, the entire 256-template table with two independent abelian-square tests, the 200 distinct length-26 factors, the exact minimal-root histogram, the four sharp templates, the two sharp binary factors, and a separate 65,536-symbol arithmetic generator. The universal proof uses source-pair closure and 32-position substituted blocks; it is not based on extrapolating the checked prefix. The density proof uses the unique primitive-substitution pair frequencies rather than numerical frequency estimates.

The finite table asserts only the stated minimum root lengths and factor counts. It neither tests nor claims higher-order abelian powers, arbitrary automatic words, nor independent human audit.
