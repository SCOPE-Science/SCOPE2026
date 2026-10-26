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

# Exact finite verification

Execute `python3 verify.py`. This enumerates each valid canonical prefix of the three-symbol alphabet through length 33, enforcing each newly arising inequality with integer LCS values. The complete expected list of level cardinalities is included in the executable assertions, not merely in a transcript. A distinct dynamic program computing insertion-and-deletion edit distance tests all 54,560 adjacent interval pairs of the ten terminal words. An independent labeled alphabet enumeration at length eight yields 78 valid words.

The exhaustive enumeration is a computer-assisted finite proof: completeness rests on the prefix-extension and canonical-renaming lemmas written in RESULT.md, and the checker explicitly evaluates their recurrence. No theorem about larger parameters or infinite words is inferred from these outputs. The verification has not been independently audited.
