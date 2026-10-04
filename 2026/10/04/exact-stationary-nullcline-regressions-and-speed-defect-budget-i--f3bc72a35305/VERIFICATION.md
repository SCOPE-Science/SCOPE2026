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
The packaged `verify.py` uses only the Python standard library and exact rational sparse-polynomial arithmetic.

For
\[
\dot v=v-\frac{v^3}{3}-w+I,
\qquad
\dot w=\varepsilon(v+a-bw),
\]
it verifies the residual identities
\[
F(v)-w=\dot v,
\qquad
v+a-bw=\frac{\dot w}{\varepsilon},
\]
where
\[
F(v)=v-\frac{v^3}{3}+I.
\]

It also verifies that substitution of
\[
w=F(v)
\]
into the linear recovery-nullcline equation gives the equilibrium polynomial
\[
\frac b3v^3+(1-b)v+a-bI=0.
\]

For the standard coefficients
\[
b=\frac45,
\qquad
\varepsilon=\frac{2}{25},
\]
it checks exactly
\[
b^2=\frac{16}{25},
\qquad
\varepsilon^{-2}=\frac{625}{4}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker verifies the algebraic certificates only. Conditional expectations, variance decompositions, equality rigidity, and sign-crossing use analytic stationarity and invariant-support arguments recorded in `RESULT.md`.
