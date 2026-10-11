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

# Reproducibility and mathematical boundaries

The accompanying `verify.py` is runnable with Python 3 and NumPy (`python verify.py`). A replay produced `VERIFY_OK 6746 checks`, comparing exact matrix-fiber singular values, cyclic approximants, and fixed-product optimality over prescribed deterministic samples.

The tests are finite and do not establish the universal statement. The proof in RESULT.md gives the exact block Fourier multiplier, continuous minimum singular-value argument, strict fixed-product monotonicity, and norm-attainment versus nonattainment measure classification for all parameters. The formula uses the unnormalized forward difference with shift coefficient exactly one; the case \(|ab|=1\) is noninvertible and has no finite residual-error constant. The independently audited status remains not performed.
