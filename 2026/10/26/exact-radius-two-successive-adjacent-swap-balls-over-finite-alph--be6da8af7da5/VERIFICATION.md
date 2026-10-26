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

# Verification of radius-two adjacent-swap ball formulas

Run `python3 verify_adjacent_radius_two.py` from the directory containing this file. Its dependencies are only Python standard-library `itertools`, `fractions` and `math`. The accompanying `verification_output.txt` records the actual execution. All loops are finite and deterministic.

The checker constructs all distinct words reached after zero, one or two successive adjacent swaps independently of the closed formula. It checks every binary center through length 11, every ternary center through length 8, and every four-symbol center through length 6, a total of 19,394 words. It also calculates exact rational mean values, confirms the sharp maximum and extremizer count on each finite space, and confirms the exact binary boundary-bit deficit identity through 13 boundary sites (all possible bit patterns).

The final line `VERIFY_OK total_direct_centers=19394` indicates these finite tests completed. Those finite tests cannot certify assertions for all lengths or alphabets, for which the analytic proof in `RESULT.md` is necessary. No external or independent audit was performed.
