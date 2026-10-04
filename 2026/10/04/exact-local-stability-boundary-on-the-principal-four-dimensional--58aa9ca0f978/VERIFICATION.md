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

The exact replay is `verify.py` and requires only the Python standard library. It performs these checks:

1. It forms \(\lambda I-J\) at either nonzero equilibrium using \(k^2=2q\) and reconstructs the determinant by an exact permutation expansion over rational coefficients.
2. It checks that the determinant is exactly
\[
\lambda^4+8\lambda^3+(2q+65/4)\lambda^2+(18q+17/2)\lambda+16q.
\]
3. It reconstructs \(\Delta_2\) and \(\Delta_3\) from the quartic coefficients and checks their exact polynomial forms.
4. It verifies algebraically that \(q_H=191/12+\sqrt{10153}/6\) is the unique positive zero of \(48q^2-1528q-1377\), that \(r_H=q_H+5/4=(103+\sqrt{10153})/6\), and that \(q_H<243/4\).
5. It checks the exact boundary factorization and the formula \(\omega_H^2=(295+3\sqrt{10153})/8\).
6. It checks the two Routh first-column sign regimes on either side of \(q=243/4\), and separately checks that the only positive parameter value admitting a nonzero imaginary root is \(q=q_H\).

A successful execution prints `VERIFY_OK`.

The replay verifies exact algebra and spectral counting. It does not test nonlinear Hopf coefficients, global attractors, or basin geometry; none of those are claimed.
