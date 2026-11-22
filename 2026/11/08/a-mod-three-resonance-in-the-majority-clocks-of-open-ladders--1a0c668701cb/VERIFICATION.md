---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scope of the focused theorem

The focused result classifies the all-vertex-flipping configurations on every open ladder by a local proof: every rung is mixed; endpoint horizontal changes are compulsory; adjacent zero changes are forbidden. Its exact count is 2F_{n-1} by the standard Fibonacci no-adjacent-zero recurrence. Global complement symmetry gives the primitive two-cycle orbit count F_{n-1}.

The archived `verification/bruteforce_verify.py` independently constructs open ladder neighbor sets, applies the strict open-neighbor majority/tie-retention map and checks all 4^n states through n=10, including the full-flip count. The archived `verification/transfer_verify.py` separately verifies all 256 coordinates of the original full-periodic transfer identity and compares the pure-flip sector through n=80. Their saved output files are retained unchanged. A separate independent direct n=2,...,9 exhaustive enumeration also produced 2,2,4,6,10,16,26,42 pure-flip states. None of these finite runs is treated as an all-length proof.

The exact all-periodic and fixed-state formulas displayed only for comparative rarity were published November 1, 2026 and are not a new verification claim of this focused document. The original source snapshot remains retrievable; no external expert or Lean proof has been performed. Historical priority of the narrowed sector is subject to the recorded best-of-knowledge limitations.
