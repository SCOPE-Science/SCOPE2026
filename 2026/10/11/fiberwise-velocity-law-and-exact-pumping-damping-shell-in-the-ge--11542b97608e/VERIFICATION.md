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

It verifies the pointwise identities
\[
\dot x=y,
\qquad
\dot y=-x+a(1-y^{2n})y,
\]
\[
\frac{d}{dt}\frac{x^2+y^2}{2}
=
a y^2(1-y^{2n}),
\]
and
\[
x-a(1-y^{2n})y=-\dot y.
\]

It checks the stationary moment-shell algebra
\[
\mathbb E[y^{2n+2}]=\mathbb E[y^2],
\]
the zero-covariance consequence of the first conditional law, and the abstract orthogonal-regression variance decomposition.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The conditional-expectation quantifiers, endpoint rigidity, and pumping–damping threshold excursion are analytic proofs in `RESULT.md`; no finite trajectory computation is used to establish them.
