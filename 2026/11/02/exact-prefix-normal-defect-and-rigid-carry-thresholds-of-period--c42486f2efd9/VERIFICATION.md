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

The included `checker.py` is a standalone Python 3 script. Running `python3 checker.py` completed successfully. It compares substitution-generated symbols and independent odd-valuation symbols at 4096 positions, verifies the floor-count formula, exhaustively checks all factors of each prefix up to length 4096, validates the odd-position carry bound, and confirms the predicted geometric first-attainment lengths and witnesses through level six. The unrestricted mathematical argument is the carry proof in `RESULT.md`; a finite checker alone would not establish the theorem. No external or independent review has been conducted.
