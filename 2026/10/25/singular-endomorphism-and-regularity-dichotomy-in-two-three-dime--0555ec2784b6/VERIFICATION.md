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

# Computational verification

Run `python verify.py` with Python 3.8 or newer; the script has no third-party dependencies. It enumerates bracket-preserving maps from the defining bilinear multiplication tables, calculates ranks using modular elimination, checks idempotents by direct matrix multiplication, and for three small cases checks von Neumann regularity against every potential inner inverse.

Observed output ends with `VERIFY_OK`. Tested prime fields and parameters: first algebra at orders 2, 3 and 5; anisotropic second algebra at `(q,lambda)=(3,1),(5,2),(7,4)`. The tests at `q=2,3` for the first algebra and `q=3` for the second exhaustively check all possible regularity witnesses. All other regularity figures are computed by the proved classification and compared with the reconstructed counts. The unbounded finite-field formulas and limiting proportions require the written argument, and the tests do not verify them on their own.
