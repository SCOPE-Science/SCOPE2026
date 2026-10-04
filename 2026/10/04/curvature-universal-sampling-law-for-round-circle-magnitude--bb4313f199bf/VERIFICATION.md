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

For fixed \(\kappa<1\), define
\[
g(s)=e^{-\ell D_\kappa(s)}.
\]
The exact finite reciprocal magnitude is
\[
Q_{n,\kappa}=\frac1n\sum_{j=0}^{n-1}g(j/n),
\]
and the continuum reciprocal magnitude is
\[
Q_\kappa=\int_0^1g(s)\,ds.
\]
Because \(g(0)=g(1)\), the finite average is exactly the composite trapezoidal rule.

The endpoint expansion
\[
D_\kappa(s)=s+\frac{\pi^2(\kappa-1)}6s^3+O(s^5)
\]
implies
\[
g'(1)-g'(0)=2\ell
\]
and
\[
g'''(1)-g'''(0)=2\ell\bigl(\ell^2+\pi^2(\kappa-1)\bigr).
\]
Substitution into Euler–Maclaurin gives the two displayed coefficients. The smoothness of \(D_\kappa\) for fixed \(\kappa<1\) justifies the \(O_{\ell,\kappa}(n^{-6})\) remainder after truncation.

At \(\kappa=1\),
\[
D_1(s)=\min\{s,1-s\},
\]
so the midpoint is not smooth. Splitting the equal-spacing row by parity gives finite geometric series and hence the exact formulas involving \(\coth\) and \(\operatorname{csch}\). Their Taylor series produce the even and odd coefficients.

The embedded `verify.py` was replayed from its packaged path. It uses only the Python standard library and checks direct finite sums against the smooth expansion, the Euclidean chord specialization, the intrinsic exact formulas, and the parity-dependent leading terms. It returned:

`VERIFY_OK round-circle magnitude sampling law`

The replay is a finite consistency check and does not replace the analytic proof.
