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

The accompanying `verify.py` is a standalone Python 3 program without external dependencies. Run `python3 verify.py`. It checks the claimed minimum-function coefficient for each even order from 6 through 42 by enumerating independent zero supports and counting proper colourings of the induced inequality graph, and directly enumerates all four-symbol assignments at orders 6, 8, and 10. The expected outcome is `VERIFY_OK direct_labelings_n=6,8,10 all_minimum_counts_n=6..42_even cases=19`.

This finite execution does not prove the universal statement. The unlimited argument is the row-alternation and triangle-chain classification in RESULT.md and the independently cited published minimum-weight theorem. No independent audit has been performed.
