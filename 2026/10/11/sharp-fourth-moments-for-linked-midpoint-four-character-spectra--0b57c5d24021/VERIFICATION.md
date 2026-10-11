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

Execute `python3 checker.py` from the directory containing this file. The code uses only the Python 3 standard library and returns `CERTIFICATE_PASS` upon success.

The checker verifies exact polynomial identities behind the stationary vector, the sign change and derivative lower bound in the rational root interval, positive amplitude parameters, and strict diagonal dominance of the reduced quadratic form using rational arithmetic. It additionally checks direct fourth moments at several nonaliased character orders, positive collision witnesses at each of orders five through eight, and \(1500\) randomly selected coefficient vectors. The exact proof applies to every compact abelian group satisfying the character-order hypothesis; finite tests are corroborative and cannot certify arbitrary inputs. No independent audit has been performed.
