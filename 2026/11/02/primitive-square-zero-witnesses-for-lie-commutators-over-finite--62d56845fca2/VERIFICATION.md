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

## Reproduction
Save `verify.py` and `verify_nilpotent.py` alongside this file and execute `python verify_nilpotent.py` with Python 3 and only the standard library. The independent-enumeration program constructs finite field/chain-ring additions and multiplications, exhaustively loops over all primitive square-zero traceless first matrices and unrestricted traceless second matrices, then checks every target against the theorem.

## Actual tests
- `PASS q=3 length=1 mixed=False nilpotent_X=8 tested_pairs=216 images=21`
- `PASS q=3 length=2 mixed=False nilpotent_X=72 tested_pairs=52488 images=417`
- `PASS q=5 length=1 mixed=False nilpotent_X=24 tested_pairs=3000 images=85`
- `PASS q=9 length=1 mixed=False nilpotent_X=80 tested_pairs=58320 images=441`
- `PASS q=3 length=2 mixed=True nilpotent_X=72 tested_pairs=52488 images=417`
- `PRIMITIVE_NILPOTENT_SL2_FIBERS_OK`

The length-one cases test limiting consistency; the theorem's principal claim concerns length at least two. Finite tests do not certify all ring lengths. Independent mathematical audit has not been performed.
