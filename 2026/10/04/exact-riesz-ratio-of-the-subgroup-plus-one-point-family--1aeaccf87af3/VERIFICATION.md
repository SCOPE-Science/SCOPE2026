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

The canonical reduction was replayed from the Fourier matrices. After unitary row and column transformations, each basis matrix depends only on the root-of-unity difference \(z\) in the repeated restriction class. The Gram matrix then splits into an \((m-2)\)-dimensional \(m\)-eigenspace and a three-dimensional block.

The accompanying `verify.py` directly constructs Fourier matrices for many \(m\) and \(k\), checks at several values of \(\lambda\) that
\[
\det(\lambda I-T^*T)
=(\lambda-m)^{m-2}
\left[\lambda^3-(4m+1)\lambda^2+(4m^2+mt)\lambda-m^2t\right],
\]
with \(t=|1-e^{2\pi i k/m}|^2\). It then locates the three cubic roots by bisection, verifies that the best condition number occurs at maximal \(t\), checks the even-modulus identity \(\rho(E_m)=2m\), and tests the odd-modulus asymptotic. The script prints `VERIFY_OK`.

These are finite consistency checks only. The infinite statement is established by the analytic unitary reduction, exact characteristic polynomial, root signs, and implicit-differentiation argument in `RESULT.md`.
