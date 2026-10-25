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

The complete combinatorial proof is given in `RESULT.md`. The exact-rational program `verify.py` exhaustively enumerates uniform perfect matchings for sizes \(2\le n\le7\), checking the marginal second moments, mixed moment, positional deletion formula, regression slope and correlation. It also independently checks the conditional-moment recurrence for LR-pair counts for all integer sizes through \(200\).

To reproduce, run `python verify.py` with a standard Python 3 interpreter. The script has no third-party dependencies. This is a finite verification of a proof stated separately; it does not establish the unrestricted theorem by enumeration. The comparison with previously published work remains subject to historical-priority uncertainty. No independent audit has been performed.
