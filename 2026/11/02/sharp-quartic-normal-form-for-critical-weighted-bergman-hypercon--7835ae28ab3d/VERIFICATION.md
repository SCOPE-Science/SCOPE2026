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

# Verification notes

The argument proves the moment identities using the normalized radial beta distribution. The fourth-power norm is the squared Hilbert norm of a holomorphic square, with dilation weights \(2^{-n}\). The exact decomposition \(f^2=P+R\) isolates the resonant quadratic coefficient, and its remainder begins at degree three. The reproducing-kernel bound on the fixed half-radius converts this into a uniform \(o(|a|^4+\|h\|_2^2)\) estimate. The explicit leading form has positive coefficients for every higher monomial; an elementary comparability argument proves uniqueness of asymptotically optimal correction.

Run `python3 checks/check.py` from the directory containing this file. The script requires only the Python standard library and passed 550 exact rational assertions, including Gaussian-rational complex coefficients. It checks the exact structural remainder rather than relying on floating-point quadrature, as well as the affine family and the nonlinear correcting family. These are supplementary finite checks; the all-function proof and the underlying global hypercontractive inequality require the analytical arguments and the cited primary theorem.

No independent audit or independent validation has been performed.
