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

The theorem is proved in `RESULT.md` by four cyclic paperfolding templates, a rotation-moment congruence, and an induction on a signed-prefix range. Running `python3 checker.py` independently constructs the finite template profiles for \(k=2,\ldots,10\) and compares with profiles from literal paperfolding prefixes. Direct character-by-character scattered-pair enumeration is also compared for \(k=2,\ldots,7\). The final line must be `ALL_CHECKS_PASS`.

Finite tests do not constitute an infinite proof. The only allowed input is the Python standard library. The theorem is restricted to the stated word and dyadic lengths. The work has not undergone independent audit.
