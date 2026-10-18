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

The accompanying Python 3 program `verify.py` was executed from the actual embedded package bytes. It independently constructs simple coronas, tests every three-valued labeling for positive-set independence and zero-vertex two-defense, and compares the full computed weight histogram with the two formulas for thirteen small instances. Its raw assignment count is 1,713,969. The program separately multiplies the symbolic transfer matrix with ordinary integer polynomial arithmetic to cycle length 25; it checks the transfer against direct independent-subset summation through length 12, then checks minimum exponents and multiplicities through length 25.

The exact recorded output, also embedded, is:

`VERIFICATION_OK raw_labelings_examined=1713969 graph_cases=13 transfer_cycles=3..25 optimum_cycles=3..25`

Run `python3 verify.py` with the standard Python 3 library. These are finite tests, not exhaustive searches of all graph orders; the unrestricted theorem is proved by the local correspondence and gap enumeration in RESULT.md. No external or independent audit was performed.
