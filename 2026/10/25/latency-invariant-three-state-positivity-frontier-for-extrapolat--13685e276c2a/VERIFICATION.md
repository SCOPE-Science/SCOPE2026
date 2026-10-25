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

Run `python verify.py` with SymPy 1.10 or newer from the same directory. The executed standalone check returned:

`VERIFY_OK 2-state exact delayed-power identity through p=7; 3-state identities through p=8; threshold signs`

The program derives the full two-state weight-dependent symbolic identities; independently forms the two upper-triangular three-state products, checks every relevant entry and row sum, and evaluates exact rational values across the algebraic transition. The infinite-delay result, sharp dimension statement, and positivity inequalities are proved analytically in `RESULT.md`, not inferred from a finite sample. No floating-point data, numerical timeouts, or external prover certificates are used as evidence for a universal assertion.

Independent audit and independent scientific validation have not been performed.
