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

The exact theorem follows from the mathematical proof in RESULT.md. A local Python 3 program, `verify_cycle_diff.py`, implements the nine-state cyclic Laurent transfer and a separate direct update operator on integer configurations. It needs only the standard library.

The program evaluates transfer coefficients for every integer cycle length \(3\le n\le12\). Independently, for \(3\le n\le8\), it constructs all cyclic integer edge-difference lists satisfying \(\sum_i e_i=0\) and \(|e_i|\le3\) and tests the two-step update directly. The finite alphabet is justified by a theorem, not by the search itself. Direct and transfer counts coincide for all checked lengths. Explicit witnesses of the sharp gap bound are verified directly for \(3\le n\le20\).

To replay, place the two standalone files beside this document and run `python3 verify_cycle_diff.py`. The record `verification_output.txt` contains the actual successful replay, ending in `CYCLE_DIFFUSION_ALL_CHECKS_PASSED` and `SHARP_GAP_WITNESSES_PASSED n=3..20`.

These finite checks do not prove completeness at untested lengths; the edge-flux, closure, and transfer bijection in RESULT.md supplies that proof. No independent external audit was performed.
