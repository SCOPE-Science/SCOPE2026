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

It treats
\[
S_x=\sin x,
\qquad
S_y=\sin y,
\qquad
S_z=\sin z
\]
as formal drive variables and verifies
\[
\dot x=S_y-bx,
\qquad
\dot y=S_z-by,
\qquad
\dot z=S_x-bz.
\]

It then checks the exact decompositions
\[
(\dot x)^2-(S_y^2-b^2x^2)=-2bx\dot x,
\]
with the two cyclic analogues, and verifies the summed activity identity.

Under stationarity, the conditional orthogonality established in `RESULT.md` makes the expectation of each right-hand correction term zero. Hence the checker certifies the algebraic part of the variance-speed theorem.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The support bound and equilibrium equality classification are analytic arguments and are not inferred from finite computation.
