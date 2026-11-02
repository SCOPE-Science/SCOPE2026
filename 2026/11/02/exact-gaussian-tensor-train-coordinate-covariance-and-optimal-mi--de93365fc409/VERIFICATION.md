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

# Reproducibility and verification

Execute `python3 CHECK.py` from the same directory as this file. The checker has no external dependencies and prints `CHECKS_PASSED 22694` on success.

The test program constructs each Gaussian fourth moment from a direct four-path Wick expansion (independent of the claimed transfer formula), as well as an exact three-state transfer implementation. It enumerates binary mismatch configurations for four parameter pairs, compares the formula against the transfer recurrence throughout larger finite ranges, tests both extremal mismatch-spacing formulas through eleven modes, and verifies the two-spike example with exact rational arithmetic.

The accompanying analytic proof is the evidence for quantification over all tensor orders, bond ranks, and mismatch locations. The tests are finite and do not establish historical originality or provide an independent mathematical audit.
