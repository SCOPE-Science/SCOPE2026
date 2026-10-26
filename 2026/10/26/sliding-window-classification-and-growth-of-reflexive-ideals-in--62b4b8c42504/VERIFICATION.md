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

The ordinary Python 3 script `verify.py` uses only its standard library. Execute `python verify.py` from the directory containing this document. It performs a direct enumeration of every subset of semigroup gaps in 22 parameter cases for block lengths \(3\le r\le6\), tests ideal closure, directly calculates \(S-I\), then directly calculates \(S-(S-I)\) without using the derived sliding-window formulas, and compares each actual reflexive ideal with the proposed language-derived list. It separately verifies the rational generating function through its coefficient recurrence and direct binary-word enumeration.

Observed output:

`VERIFY_OK cases=22 normalized_ideals=7985 direct_double_quotients=checked word_bijection=checked rational_series=checked`

The formula is proved for all \(r\ge3\) and \(m\ge r+1\) by the finite symbolic arguments in RESULT.md. Finite code checks alone do not establish any infinite theorem; no formal proof assistant or independent mathematical review was used. The tests do not claim to enumerate all parameters.
