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

The exact proof appears in `RESULT.md`. To reproduce independent finite checks, execute `python3 verify.py` using Python 3 and no third-party packages. The program derives shortest lengths and counts by a suffix dynamic program that does not use the theorem's formula internally. It then generates all prescribed binary solo-action schedules over a bounded set of parameters, checks that their outputs contain both input words as subsequences, and compares complete output languages against a direct shortest-supersequence enumerator.

Observed result: `VERIFY_OK dynamic_configurations=448 constructed_words=2592 full_language_configurations=38`.

The dynamic-program test covers \(2\le q\le8\) and \(1\le k,\ell\le8\); constructive tests cover separate bounded configurations. These are finite consistency checks. The proof of the unlimited parameter ranges rests on the deterministic next-letter congruence, the sharp count of common-merge opportunities, and the inverse map from optimal outputs to solo-action schedules. No external expert or independent scientific audit is asserted.
