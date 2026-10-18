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

# Reproducibility

Run `python verify.py` with Python 3.10+ and NumPy installed. The program prints its four exact enumeration totals, the number of successfully checked full-rank QR cases, and `VERIFICATION_OK` on success. The script is self-contained and builds the mean-zero basis, CountSketch matrices, eigenspectra, and actual QR right preconditioner afresh.

The exhaustive enumerations cover 48,160 signed hash assignments in four small parameter cases; additional seeded random cases test larger dimensions. They validate finite instances only. The proof in `RESULT.md` establishes the universal assertions, including the limiting probabilities. No independent scientific audit has been performed.
