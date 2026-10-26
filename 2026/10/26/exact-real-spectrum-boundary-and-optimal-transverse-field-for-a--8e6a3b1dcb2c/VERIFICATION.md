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

# Verification and reproduction

The attached \(\texttt{check_threshold.py}\) was executed with Python, SymPy, and mpmath. It independently assembles the full eight-by-eight Pauli Hamiltonian and verifies the characteristic factorization as a polynomial identity in \(\gamma\), \(h\), and spectral parameter. It then checks the cubic discriminant, exact sign identities bracketing the two positive roots, the elimination resultant determining all possible stationary fields, both asymptotic coefficients, and the separate zero-field limit. Its high-precision root evaluation reproduces the displayed optimal field and critical strength. Each analytic conclusion is also proved in \(\texttt{RESULT.md}\), so numerical root finding is not used as a global uniqueness certificate.

The exact calculations are reproducible with \(\texttt{python check_threshold.py}\) after installing SymPy and mpmath. No specialized hardware, external dataset, or external proof assistant is required.

The result does not imply the same stability floor for longer chains, nor does it certify positive-metric quasi-Hermiticity or any dynamical response. An independent scientific audit has not been performed.
