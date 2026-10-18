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
# Reproduction and mathematical limitations

Run `python3 verify.py` in the same directory; the program uses only the Python standard library. It verifies exact rational polynomial moments of product-beta exit laws, tests both positive and negative parameters and their reversed moment inequalities, checks the logarithmic endpoint, and evaluates the strict parameter and high-dimensional limits. It reports 4,230 consistency cases passing. The verification code is finite evidence, not an exhaustive proof; the proof is self-contained in RESULT.md. The uninspected full 2007 simplex article remains a historical priority limitation, and no independent audit has been performed.
