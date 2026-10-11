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

It verifies the pointwise nonlinear-forcing residual
\[
(x^2-cx-by)-az=\dot z.
\]

It verifies
\[
cm-m^2=m(c-m)
\]
and the sharp completion-of-the-square identity
\[
m(c-m)
=
\frac{c^2}{4}
-
\left(m-\frac c2\right)^2.
\]

It also verifies the abstract conditional-regression variance and covariance decomposition used for
\[
Q=az+\dot z
\]
when
\[
\mathbb E[\dot z\mid z]=0.
\]

At the standard parameter values
\[
a=\frac65,
\qquad
b=\frac{73}{25},
\qquad
c=6,
\]
the checker verifies
\[
c^2/4=9
\]
and the exact slope
\[
a=\frac65.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation identities, endpoint rigidity, and zero-speed equality classification are analytic proofs in `RESULT.md`; they are not inferred from finite numerical sampling.
