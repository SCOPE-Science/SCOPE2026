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

The reproduction command is `python verify.py` (Python 3 with NumPy). The script explicitly constructs the \(2(a+b)\)-dimensional modular map, verifies predicted exact matrix orders for all \(a,b\in\{1,\dots,7\}\) and \(s\in\{1,\dots,10\}\), checks the two scalar congruences against matrix identity for 2,250 exponent choices, and directly iterates 407,376 configurations across twelve smaller instances. It verifies that each enumerated instance has at least one orbit with the full predicted primitive period. See the adjacent `verification.txt` for the recorded four success lines.

The mathematical inference for all parameters is supplied separately by the polynomial identity, the exact valuation table, the matrix-squaring lemma, and the proper-subgroup argument in `RESULT.md`. The code examines finite instances only and is not an infinite proof; this result has not undergone an independent audit.
