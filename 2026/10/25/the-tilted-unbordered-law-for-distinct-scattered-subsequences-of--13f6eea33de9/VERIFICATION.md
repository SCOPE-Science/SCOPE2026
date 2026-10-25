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

# Verification

The standalone `verify_unbordered.py` reconstructs actual sets of scattered subsequences of every host word up to the stated finite bounds, using exact rational iid weights in six alphabets/probability profiles. It checks 30,260 host words, then compares exact expected counts against geometric waiting-time coefficients and the weighted shortest-border recurrence computed separately. It also independently enumerates short unbordered pattern strings, and compares the fair-binary limiting unbordered density with the established published value.

Expected program terminal line:

`VERIFY_OK exact_source_words=30260 rational_sources=6 full_weighted_pattern_check=TRUE fair_binary_unbordered_limit=0.2677868402178891 fair_ternary_limit=0.556979839764`

The finite checks do not certify the infinite analytic assertions, positivity, or literature originality; these are treated in the mathematical proof and review. External independent auditing has not been performed.
