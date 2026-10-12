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

# Verification record

Run `python3 verify.py` in the result directory using a Python 3 interpreter; it has no third-party dependencies. Expected first line:

`VERIFY_OK: 4 classical operand pairs; 32 exceptional-status constancy cases; 16 ordinary-status separations`

Here the four operand pairs are the four ordered classical input pairs to the unary/binary propositional operations. The thirty-two constancy cases are the four ordered classical world-value assignments times eight exceptional-status operators. The sixteen separations compare each target modality in a constant model and a one-world-flipped model, while verifying that all eight exceptional-status modalities agree between the models.

Scientific limits: the executable checks finitely many base situations. An induction using the published semantic definitions proves invariance for unrestricted formula depth. The exact nondefinability is a statement about formulas in the restricted language, not formulas with primitive necessity/possibility. It is not independently audited.
