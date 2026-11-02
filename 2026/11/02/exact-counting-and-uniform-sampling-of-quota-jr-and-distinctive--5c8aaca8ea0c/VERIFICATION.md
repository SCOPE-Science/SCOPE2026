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

# Verification summary

The self-contained Python 3 program `verify_counting.py` supplies an independently written direct quota-JR predicate (`is_qjr`), the gap construction, the suffix-count recurrence, exact brute-force committee enumeration, and an exact suffix-count-weighted sampler.

Running `python3 verify_counting.py` checks 23,370 exhaustive DR-derived cases and 12,000 deterministic-seed generalized cases; all comparisons passed. Separately, all candidate-interval ballot profiles with four voters and one through five candidates, over all valid committee sizes, supplied 297,176 additional passing comparisons. The combined exhaustive DR verification comprises 320,546 distinct ballot-profile/committee-size cases. This second exhaustive extension was run during the mathematical examination; it is not part of the default script execution. The embedded script itself can reproduce the first two sets.

The example with eight ballots and six candidates yields exactly three DR committees, matching direct enumeration.

These are finite tests; the proof for arbitrary finite input sizes is the gap-equivalence and path-bijection argument in `RESULT.md`. There is no independent audit and no formal proof assistant certificate.
