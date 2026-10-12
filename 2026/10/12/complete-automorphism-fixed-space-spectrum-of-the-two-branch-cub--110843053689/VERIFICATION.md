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

Execute `python3 verify.py` in the directory containing this file and the standalone verifier. It enumerates the full automorphism normal forms for the prime fields of orders 2, 3, and 5; checks their matrix fixed-space dimensions against the claimed formulas; and directly checks radical-element orbits for orders 2 and 3. The general theorem additionally rests on the symbolic ideal-filtration and finite matrix-rank argument written in `RESULT.md`. Prime-field enumeration alone does not establish the theorem for extension fields. No external audit is claimed.
