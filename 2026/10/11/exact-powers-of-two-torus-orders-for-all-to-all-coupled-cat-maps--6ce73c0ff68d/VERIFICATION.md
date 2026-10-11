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

# Reproduction and checks

Run `python3 verify.py` with Python 3 and no additional packages. The program returns `VERIFY_OK; exact assertions: 576` on completion.

Its first test evaluates the entire eight-case residue table in the abstract coefficient algebra `e**2 = n*e` modulo 8, so it covers every integer parameter residue, not just small graph sizes. It then constructs integer 2n-by-2n matrices directly for site counts 2 through 14 and torus exponents 1 through 8, confirming the asserted orders and their relevant proper-divisor exclusions.

The universal lifting argument for all exponents appears in RESULT.md. The independent direct matrix checks are finite and do not establish infinite quantified results on their own. Exact machine arithmetic avoids floating-point ambiguity. Independent audit and validation have not been performed.
