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

Use Python 3 and run `python3 verify.py`. The self-contained exact-rational verifier exhaustively checks all one-vacancy binary configurations with up to ten vertices and three rational peaks; it checks every improving transition's requisite monotonicity and searches for longest paths. It separately constructs witnesses through 100 vertices at five rational peaks. Expected message: `PASS states 14871 improving moves 30780 constructive families 490`.

These are finite consistency tests. The general finite improvement property and sharp maximum follow from the combinatorial potential and symbolic witness argument in `RESULT.md`, not from finite enumeration. No independent audit has been performed.
