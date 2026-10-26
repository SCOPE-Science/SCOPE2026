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

# Reproducibility and limits

Run `python3 verify.py` with Python 3. The verifier uses `fractions.Fraction` and exact Gaussian elimination to construct finite second-difference resolvents and induced monotone-jump-to-output-slope matrices. It checks row sums and signs at rational parameters bracketing the exact boundaries, the four-point corner formula, and the four-point extremal defect. An optional NumPy check (skipped if NumPy is absent) corroborates fixed-strength failures on long grids. Expected terminal marker: `VERIFY_OK`.

The algebraic sign certificates and the Fourier-moment argument in `RESULT.md` are the proofs. Parameter samples and long-grid numerical experiments are corroboration only. The assertions about eventual positivity at each fixed sample length and lack of a common positive parameter are proved analytically and cannot be inferred from finite experiments.

The unexamined full text of de Jong–Sakarya (2016) is a residual historical-overlap risk. No independent audit or independent validation has been performed.
