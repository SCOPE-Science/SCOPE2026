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

The standalone `verify.py` uses exact integer, rational, and SymPy polynomial arithmetic. It verifies symbolic run-composition variance identities, all four parity difference identities and positivity substitutions; it also independently enumerates every fixed-composition binary word through total length 15, then checks a larger finite parameter grid.

The mathematical proof of the all-integer statements is in `RESULT.md`, especially the positive-coefficient formulas (2)–(5). Enumeration is finite corroboration and not a substitute for that proof. No external independent audit has been conducted.
