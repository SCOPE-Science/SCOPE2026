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
\dot x=By-C(x+p),\qquad
\dot y=xz-y,\qquad
\dot z=1-z-xy,
\]
it verifies
\[
L\left(\frac{y^2+z^2}{2}\right)
=
-y^2+z-z^2,
\]
and
\[
L\left(\frac{(x+p)^2}{2}\right)
=
(x+p)\bigl(By-C(x+p)\bigr).
\]

It also verifies, after clearing the denominator \(B\),
\[
\frac{\dot x}{B}
=
y-\frac{C}{B}(x+p).
\]

For the standard asymmetric coefficients
\[
(B,C)=(102,3),
\]
it checks exactly
\[
\frac{C^2}{B^2}
=
\frac1{1156},
\qquad
\frac1{B^2}
=
\frac1{10404}.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation and equality-rigidity steps are analytic consequences described in `RESULT.md`; they are not inferred from the checker output alone.
