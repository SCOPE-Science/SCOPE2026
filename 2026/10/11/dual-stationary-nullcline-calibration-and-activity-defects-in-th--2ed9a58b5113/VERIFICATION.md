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

It verifies the residual identities
\[
uv^2=F(1-u)-\dot u,
\qquad
uv=(F+k)+\frac{\dot v}{v},
\]
the covariance consequences, and the two orthogonal variance decompositions.

It checks that the essential-supremum inequality is exactly
\[
FU^2-FU+(F+k)^2\le0
\]
and therefore requires
\[
1-\frac{4(F+k)^2}{F}\ge0.
\]

At an exact rational parameter point in the positive-equilibrium region it verifies the upper support boundary and its corresponding equilibrium concentration.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifiers and support-envelope proof are analytic arguments in `RESULT.md`; no finite trajectory computation is used.
