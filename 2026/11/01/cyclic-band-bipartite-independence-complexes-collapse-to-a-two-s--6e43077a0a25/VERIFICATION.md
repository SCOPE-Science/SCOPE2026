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

# Reproduction and limits
Run `python3 verify.py` with Python 3 (standard library only). Its printed transcript is in `verification_output.txt`. The program constructs all relevant bitset complexes, checks the link identities and verifies that every removed lower face has exactly one current immediate coface and that this coface is maximal. Final remainders and pair-count formulas are checked. The tested finite parameter range is not treated as an infinite proof; the uniform inequalities and domination argument in RESULT.md establish the theorem in full.
