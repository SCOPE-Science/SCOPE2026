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

# Computational verification and limitations

Execute `python3 verify.py` in the same directory as this file. No nonstandard packages are required. The script exhaustively checks the admissibility equation for all 8-element transpositions and shifts, then compares every carrier-inclusive state to the derived fixed-count formula for 504 cases; it also checks 16 selected 16-element cases. The mixed example has exactly 64 two-cycles and 96 four-cycles with no fixed point. The adjacent `verification_output.txt` preserves actual stdout from an execution of the distributed script. Universal identities and exponential proportions require the symbolic proof; finite checks do not establish unrestricted claims. Independent audit: not performed.
