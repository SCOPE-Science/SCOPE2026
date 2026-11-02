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

# Verification of the exact impurity-binding threshold theorem

Execute `python verify.py` in an environment with the dependencies in `requirements.txt`. The script uses a fixed random seed, checks the analytic Green inverse against the independently constructed full kernel, verifies the first derivative of the inverse at the threshold, solves the finite Birman–Schwinger secular equation, and compares its energies against separate long finite-chain Jacobi spectra. It tests the local quadratic onset only when endpoint weights are sufficiently well-conditioned to avoid artificial cancellation. Finally, it compares all equal-spaced path spectra and endpoint coefficients for 104 geometries with closed trigonometric expressions.

The recorded output from this execution is embedded separately as `verify_output.txt`. The finite comparisons cannot certify every integer spacing or arbitrary lattice size; those cases rest on the mathematical proof in `RESULT.md`. Threshold equalities are treated as bounded nonsquare-summable resonances, not as bound modes. No independent scientific audit has been performed.
