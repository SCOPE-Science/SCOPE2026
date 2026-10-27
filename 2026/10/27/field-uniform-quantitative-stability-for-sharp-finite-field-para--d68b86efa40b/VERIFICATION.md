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

The exact analytical proof uses finite-field character orthogonality, quadratic Gauss-sum magnitude, Fourier expansion in additive characters, and the global sharp parabolic extension theorem of González-Riquelme and Oliveira e Silva. The zero-mean gauge removes scalar directions, and the half-Hessian is computed separately on real and imaginary mean-zero subspaces.

The standalone `verify.py` checker was run from its own package directory with Python's standard library. The output is embedded as `verification-output.txt`. The checker evaluates prime fields of orders 5, 7, 11, 13 and the nonprime field of order 25, reconstructing the original extension sums and all tested second variations. A nonprime field is implemented as a quadratic polynomial quotient. The tests verify the exact Gauss-magnitude patterns, predicted curvature coefficients, chirp-shift invariance and the uniform local inequality at a test radius smaller than 1/64. The full proof is not reduced to or certified by this finite battery.

Reproduce with `python verify.py`; expected final line: `ALL_VERIFIED total_checks=1069. Finite tests are not the universal proof.` The field-uniform radius follows from the analytic Hölder remainder bound, not from the finite experiments. The radius is sufficient, not claimed best possible. Independent mathematical audit has not been performed.
