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
The packaged `verify.py` uses only the Python standard library and exact arithmetic.

It verifies the general algebraic implication
\[
a\mathbb E[x^2]+(1-b)m-1=0
\]
\[
\Longrightarrow
\]
\[
a\operatorname{Var}(x)
=
1-(1-b)m-a m^2.
\]
Together with Vieta's relations for the roots of
\[
a r^2+(1-b)r-1=0,
\]
this is exactly
\[
\operatorname{Var}(x)=(r_+-m)(m-r_-).
\]

For the classical parameters
\[
a=\frac75,
\qquad
b=\frac3{10},
\]
the checker represents \(\sqrt{609}\) exactly in the quadratic field \(\mathbb Q(\sqrt{609})\) and verifies
\[
r_\pm=\frac{-7\pm\sqrt{609}}{28}
\]
as exact roots, together with their Vieta sum and product and the fixed-point relation \(y=bx\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The measure-theoretic sign argument and support-rigidity argument are proved analytically in `RESULT.md`; they are not inferred from finite enumeration or simulation.
