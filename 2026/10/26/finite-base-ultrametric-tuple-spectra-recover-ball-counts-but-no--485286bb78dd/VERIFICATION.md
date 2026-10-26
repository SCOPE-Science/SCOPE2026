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

# Reproducibility and limitations

Execute `python3 verify_ultrametric_types.py` (Python standard library only). It enumerates nested equivalence relations directly and compares extension-type coefficients to the analytic formula. The finite program reports 99 exhaustive base configurations across tested small metric alphabets and the sharp four-point collision, matching `verify_ultrametric_types.out`. This is finite corroboration only. Infinite arities, all integer distance bounds, and the full converse rest on the direct labelled-SET proof and the growth-independence lemma in `RESULT.md`. No independent audit has been performed.
