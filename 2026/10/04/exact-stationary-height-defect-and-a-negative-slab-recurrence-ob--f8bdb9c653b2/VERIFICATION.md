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
The packaged `verify.py` uses only the Python standard library and exact sparse-polynomial arithmetic over rational coefficients.

It verifies, for
\[
\dot x=y-ax+byz,\qquad
\dot y=cy-xz+z,\qquad
\dot z=dxy-mz,
\]
the identities
\[
Lz=dxy-mz,
\]
\[
L(z^2)=2dxyz-2mz^2,
\]
\[
L(x^2)=2xy-2ax^2+2bxyz,
\]
and the combined certificate
\[
\frac d2L(x^2)-Lz-\frac b2L(z^2)
=
mz+bmz^2-adx^2.
\]

The stored checker output in `verification_output.txt` is `VERIFY_OK`.

The checker certifies the algebraic steps. The conditional-expectation conclusion follows from the invariant-measure identity for arbitrary test functions of \(z\), while equality rigidity and the slab consequence are proved analytically in `RESULT.md`.
