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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

It verifies the three pointwise residual identities
\[
y-g(x)
=
-\frac{1+b_1x}{a_1x}\dot x,
\]
\[
Q-d_1
=
\frac{\dot y}{y},
\]
and
\[
f_2(y)-d_2
=
\frac{\dot z}{z}.
\]

It verifies the abstract conditional-regression variance decomposition
\[
\operatorname{Var}(Y)
=
\operatorname{Var}(\mathbb E[Y\mid X])
+
\mathbb E[(Y-\mathbb E[Y\mid X])^2].
\]

It verifies
\[
f_2''(y)
=
-\frac{2a_2b_2}{(1+b_2y)^3}<0
\]
for positive parameters and the classical exact break-even value
\[
y_*=\frac18.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identifications, zero-defect equality classifications, Jensen rigidity, and periodic crossing theorem are analytic proofs in `RESULT.md`; they are not inferred from finite trajectory experiments.
