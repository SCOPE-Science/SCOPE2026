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

# Verification record

The standalone `verify.py` was run from the packaged source directory with Python 3 and SymPy. It completed `VERIFY_OK 38 symbolic/periodic-quadrature checks`.

Symbolic checks independently reconstructed the transfer characteristic polynomial, the polynomial identity separating one-step and long-run rates, the rational \(\kappa=9\) transfer matrix and its exact radical eigenvalues, and the quadratic line-minimization energy identity. Deterministic midpoint quadrature of eight independent curvature pairs compared the first and fourth angular moments against the derived formulas with tolerance \(2\cdot10^{-10}\).

These checks provide algebraic and finite numerical corroboration. The Poisson-kernel Fourier proof, Perron–Frobenius argument, all-positive-curvature quantifiers, and asymptotic statements are mathematical arguments, not certified by finite quadrature. No external validation was conducted.
