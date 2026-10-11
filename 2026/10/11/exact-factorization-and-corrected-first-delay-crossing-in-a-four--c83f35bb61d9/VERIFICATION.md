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
# Verification

The bundled `verify.py` uses only the Python standard library. It checks the symbolic coefficient map of \(F(\lambda+a e^{-\lambda\theta})\) against the expanded characteristic equation, verifies the exact zero-delay Hurwitz determinants at \(a=1/4\), reconstructs the four quartic roots by Newton iteration, enumerates all positive imaginary-axis crossing frequencies and their smallest phase-compatible delays, and confirms that the earliest one is
\[
(\omega_*,\theta_*)=(0.705570557982711\ldots,0.876243533775502\ldots).
\]
It also checks the characteristic residual at that pair, evaluates the positive transversality derivative, and verifies that the reported \(2.0083\) exceeds every admissible positive crossing frequency.

The exact proof does not depend on a finite frequency scan: the four frequencies arise algebraically from the four roots of \(F\), and all later crossings on a given branch add an integer phase multiple. Numerical evaluation is used only to order and report these finitely many explicit candidates.

Limits: the checker certifies the linear spectral claim only. It does not compute a first Lyapunov coefficient or certify a nonlinear periodic branch.
