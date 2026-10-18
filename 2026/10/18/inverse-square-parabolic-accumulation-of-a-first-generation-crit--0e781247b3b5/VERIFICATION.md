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

# Verification details

The proof is self-contained once the source theorem's legal-branch uniqueness is quoted. Symbolic checks in `critical_pencil_check.py` verify the trace factorization, continuant coefficient, polynomial identities used at the parabolic limit, and signs determining the positive root. It uses `sympy`, `mpmath`, and standard Python.

With 65-digit arithmetic, the script brackets the small-angle algebraic root between the parabolic trace value and the first Chebyshev half-turn, then replays every branch sign and endpoint at the computed roots and reports observed deviations for multiple interior parameter values and word lengths. These finite tests are not offered as proof of asymptotic validity; the proof uses the exact sine-interpolation legality argument and a Taylor estimate.

The manuscript distinguishes transfer-matrix eigenangle from the dynamical circle rotation number and makes no claim of uniformity at the parameter endpoints. The related 2019 resonance-lobe paper was not accessible as full text, leaving an originality comparison risk. Independent audit has not been performed.
