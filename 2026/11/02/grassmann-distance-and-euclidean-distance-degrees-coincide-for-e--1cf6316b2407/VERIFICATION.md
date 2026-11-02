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
Exact computations used Python 3 with SymPy, via `python check_scroll_gd.py`, which returned `VERIFY_OK`. The script constructs a block-diagonal complex symmetric rank-\(d\) projector with real rational coefficients, computes the rational objective and its derivative over the rationals, and checks the predicted generic degree and square-freeness in five instances. Generality in arbitrary exponents follows from the written geometric proof and generic-smoothness argument, not from testing. No independent mathematical audit was performed.
