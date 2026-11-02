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

Run `python verify.py` with Python 3 and no third-party packages. The program constructs finite fields as explicit prime-field and quadratic towers, evaluates the polynomial on all field elements, accumulates exact target multiplicities, and independently compares them with the displayed closed formulas. This verifies 493 coefficient configurations on field orders 3, 5, 7, 9, 11, 13, 17, 23, 25, 49. Entire coefficient sets are used for 3, 5, 7, 9, 11, 13, with samples at the other orders; both cubic coefficient classes are tested at orders 5, 11, 17, and 23. Expected standard output ends with `VERIFY_OK coefficients= 493 all_target_fibers=PASS`.

The computation is finite and does not independently establish the result for every odd prime power. The algebraic proof supplies the unrestricted quantifiers. No independent external audit has been performed.
