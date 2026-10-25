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

# Reproduction

Run `python verify.py` using Python 3 and no third-party packages. The verifier computes Stirling numbers with integer recurrences; enumerates all set partitions of nine or fewer labels by independent restricted-growth words; computes raw empirical joint counts and exact rational covariances; compares the closed formulas and the claimed strict sign boundaries; and checks a conservative fixed-block conditioning-error bound.

Recorded output: `PASS: exact independent assertions: 4746`.

The unrestricted conclusions come from the explicit counting bijections and recurrences in `RESULT.md`. Finite checks do not constitute an exhaustive infinite proof. No independent scientific audit or historical-priority certification has been performed.
