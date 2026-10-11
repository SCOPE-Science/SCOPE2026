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
y-x=\frac{\dot x}{a},
\]
\[
x(z+a-c)-cy=-\dot y,
\]
and
\[
xy-bz=\dot z.
\]

It verifies the abstract orthogonal-regression variance and covariance identities used for all three speed defects.

For the classical parameters
\[
a=35,\qquad b=3,\qquad c=28,
\]
it verifies exactly that
\[
2c-a=21,
\qquad
b(2c-a)=63,
\]
and that the nonzero equilibrium relations satisfy all three vector-field equations when
\[
x=y,
\qquad
x^2=63,
\qquad
z=21.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation and equality-rigidity arguments are analytic proofs in `RESULT.md`; they are not inferred from finite numerical sampling.
