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

Analytically derived the exact Wigner identity (1), exhaustive global support localization for the negative part, the rescaled Laguerre polynomial at each stellar root, the Jacobian, coefficient, and positivity of that coefficient. The proof treats all degrees but only fixed finite Fock polynomials.

To reproduce computational checks, execute `python verify.py` with NumPy and SciPy. A Fock-basis density-matrix calculation based directly on the independent pure-loss Kraus sum is evaluated with generalized Laguerre Wigner matrix elements and compared against the polynomial derivative representation. The check covers 720 combinations and includes complex amplitudes. Numerical polar quadrature of finite negative regions tests 12 asymptotic coefficient cases for Fock, squarefree, and mixed-multiplicity states. The test is not exhaustive over infinitely many states or parameter values, and its threshold tolerances are diagnostic, not formal interval certificates.

The onset theorem is not a new proof of the general 50-percent negativity-survival boundary; that boundary is recognized as prior art. Remaining risk is an equivalent publication-priority result not identified in the inspected sources. No independent external audit or certification has been performed.
