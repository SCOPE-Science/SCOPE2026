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
The packaged `verify.py` uses only the Python standard library and exact sparse-polynomial arithmetic.

For
\[
\dot x=-x+ay+x^2y,\qquad
\dot y=b-ay-x^2y,
\]
it verifies
\[
\dot x+\dot y=b-x.
\]

It also verifies the cleared-denominator residual identity
\[
y\left(
x^2-\left(\frac by-a\right)
\right)
=
-\dot y.
\]

After clearing the positive denominator \(a+b^2\), it verifies that
\[
\left(
b,\frac{b}{a+b^2}
\right)
\]
annihilates both vector-field components.

Finally, with formal moment placeholders, it verifies the algebraic reduction
\[
\mathbb E[x^2]-b^2
=
b\left(
\mathbb E[1/y]-\frac{a+b^2}{b}
\right)
\]
whenever
\[
\mathbb E[x^2]=b\,\mathbb E[1/y]-a.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional expectations, support exclusion, and equality-rigidity arguments are analytic consequences of invariance and are not inferred from the checker alone.
