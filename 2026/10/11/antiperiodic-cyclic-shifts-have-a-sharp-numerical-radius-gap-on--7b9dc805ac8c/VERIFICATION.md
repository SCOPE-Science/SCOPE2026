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

# Reproducibility and verification

Run `python3 verify_signed_shift.py` with Python 3 (standard library only). The program asserts the cyclic Young-deficit identity and the exact sine normalization, checks the odd-dimensional negative eigenvectors, compares the Hilbert \(p=2\) sine vector with \(\cos(\pi/n)\), and evaluates the recovery-deficit scaled constants in finite examples.

The analytical theorem depends on four steps not certified by finite tests: the global positive lower bound for the homogeneous Young-defect quotient, compactness of the linearly interpolated power transform, lower-semicontinuity localized away from its zero set, and the anti-periodic Poincaré–Wirtinger inequality. These are proved in `RESULT.md`, not assumed from the program.

Scientific limitations: the numerical checks cannot establish a limit along all even integers, exclude uninspected prior formulations, or provide independent mathematical certification.
