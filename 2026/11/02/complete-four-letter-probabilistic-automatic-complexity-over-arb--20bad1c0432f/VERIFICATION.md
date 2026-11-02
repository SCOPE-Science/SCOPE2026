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

The theorem concerns four-letter words over finite alphabets with at least two symbols. The primary proof uses Gill's binary `0100` exclusion and the universal three-state theorem of Kjos-Hanssen for that single exceptional pattern. The positive cases are completely accounted for by fourteen other equality patterns: thirteen exact rational two-state matrices in `CERTIFICATES.json` and one elementary constant-word construction.

From this directory run `python3 verify_fraction.py` and `python3 verify_integer.py`. These inspect all active-alphabet competitors for every included canonical pattern, require strict inequalities, and verify the exact rational gaps. The independent integer checker uses denominator-cleared numerators rather than fraction recurrence evaluation. The output from actual runs is recorded in `FRACTION_OUTPUT.txt` and `INTEGER_OUTPUT.txt`.

The extension to larger alphabets is proved analytically using convex mixtures and is not inferred from finite alphabet trials. The external obstruction at `0100` is a published exact binary result, not an exhaustive numerical claim. Neither program certifies external publication priority, the published theorems, or behavior at length five and beyond. Independent audit has not been performed.
