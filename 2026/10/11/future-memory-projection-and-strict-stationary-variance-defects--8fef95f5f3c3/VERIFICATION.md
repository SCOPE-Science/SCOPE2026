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
The packaged `verify.py` uses only exact rational arithmetic from the Python standard library.

For the classical coefficients
\[
a=\frac14,\qquad b=3,\qquad c=-\frac12,\qquad d=\frac1{20},
\]
it verifies
\[
-\frac dc=\frac1{10},\qquad
\left(\frac dc\right)^2=\frac1{100},\qquad
\frac1{c^2}=4,\qquad b^2=9.
\]

It verifies the equilibrium relations
\[
y=-w,\qquad z=10w,\qquad x=-\frac{39}{4}w,\qquad w^2=\frac4{13}
\]
by substituting them into all four vector-field components.

It also checks the cleared residual identities
\[
c\left(w+\frac dc z\right)=\dot z
\]
and
\[
w\left(x+\frac bw\right)=\dot w.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure disintegrations, support gap from \(w=0\), equality-rigidity proof, and future-memory representation are analytic arguments in `RESULT.md`; they are not finite experiments.
