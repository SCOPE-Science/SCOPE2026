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

The independent mathematical proof appears in `RESULT.md`; computational cross-checks appear in `verify.py`. The program uses NumPy and SciPy and is invoked with `python verify.py`.

The two-disk calculation uses an analytic overlap-area integral to cross-check a special case where the individual planar stationary law is uniform on a disk. The general checks sample the finite-dimensional beta-disk convolution using scrambled Sobol points, compare characteristic functions against exact Fourier–Bessel expressions, and test the positive-definite angular Hessian determinant identity. These are finite numerical checks; they do not establish a limit or prove noncoverage by another theorem. The analytic endpoint argument supplies the proof. The work has not undergone independent external audit.
