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

## Verification notes

The exact moment formula was differentiated by the arc endpoints, with normalized measure \(d\theta/(2\pi)\). The fixed-measure tangent constraint and common-rotation quotient were realized by \(\sum u_j=\sum v_j=0\), whose coordinate norm is induced from standard Euclidean endpoint distance. The unitary discrete Fourier transform shows two real singular squared values \(k(1\pm|\cos(\pi\rho)|)/(4\pi^2)\), each counted \(k-1\) times; conjugate-frequency pairs and the possible Nyquist mode were explicitly handled. The structural uniqueness proof checks the nondegenerate-arc boundary conditions as well as the endpoint self-inversive identity.

The executable checker implements the exact arc moment integral, constructs the Jacobian using an orthonormal mean-zero coordinate chart, compares the full singular-value list over 12 ranks and 6 occupancies each, and checks analytic endpoint differentiation with symmetric finite differences. It prints a passing count only after 144 assertions. It is a finite diagnostic and supplies no proof for untested ranks or occupancies. Independent mathematical audit and external validation have not been performed.
