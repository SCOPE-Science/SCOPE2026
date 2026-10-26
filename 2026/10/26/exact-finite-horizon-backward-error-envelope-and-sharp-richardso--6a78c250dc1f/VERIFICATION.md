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

The stated claims concern all integers \(k\ge1\) and all dimensions. Their proof is the spectral reduction, monotonicity, exact endpoint witnesses, unique minimax intersection and parity argument in `RESULT.md`; finite computation does not certify universal quantifiers.

## Reproducible checks

Run `python3 check.py` with a Python 3 standard library. It tests the exact \(k=2\) root and safe-window boundary, selected minimax root locations, a dense spectral grid, randomized diagonal positive-semidefinite instances and constructed sharp endpoint witnesses. It also verifies that \(\alpha<1\) and \(\alpha>1+1/\sqrt3\) have explicit violating examples. The checker requires no external dependencies.

## Limits

No numerical test exhausts real step factors, all PSD matrices, or all positive integers. Arithmetic is exact in the mathematical theorem, while `check.py` uses floating-point for illustrative consistency tests. No claims about finite-precision backward stability, varying steps, non-PSD matrices or external independent auditing are implied.
