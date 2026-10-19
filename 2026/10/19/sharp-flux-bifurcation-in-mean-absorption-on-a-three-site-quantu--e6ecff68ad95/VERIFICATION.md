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

# Verification of the exact three-site absorbing-ring result

The source package contains \(\texttt{triangle\_absorption\_checker.py}\), designed to be extracted beside this file and run with Python 3 and installed SymPy, NumPy and SciPy.

The checker executed successfully with 390 assertions: symbolic verification of all nine entries of the integrated Lyapunov equation on \(\cos^2\phi+\sin^2\phi=1\), the trace formula, 110 randomly sampled comparisons with a separate numerical matrix solver, independent physical-time quadrature at eight parameter pairs, numerical optimizer comparisons and dark-point long-time survival tests. The analytic proof separately gives the global parameter quantifiers and flux-optimality boundary.

The computation is finite corroboration; it cannot on its own prove statements for all positive sink rates, all fluxes, or all hopping strengths. Those claims rest on the finite symbolic Lyapunov identity, stability argument and strictly convex minimization explicitly reconstructed in RESULT.md. The dark-point survival limit follows from a one-dimensional invariant dark sector and decay of its complementary sector. Independent mathematical validation has not been performed.
