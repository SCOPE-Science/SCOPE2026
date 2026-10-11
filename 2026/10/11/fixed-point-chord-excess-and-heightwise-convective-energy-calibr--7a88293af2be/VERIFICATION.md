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

It verifies the pointwise vector-field identities used in the proof, including
\[
\dot z=y^2-z
\]
and
\[
\frac{d}{dt}(xy)
=
x^2-a xy+b y^2-y^2z.
\]

It verifies the stationary conversion
\[
\mathbb E[z^2]
=
b\,m+\mathbb E[x^2]
\]
into
\[
\operatorname{Var}(z)
=
m(b-m)+\mathbb E[x^2].
\]

It also verifies the abstract orthogonal-residual formulas
\[
\operatorname{Var}(y^2)
=
\operatorname{Var}(z)+\mathbb E[\dot z^2]
\]
and
\[
\operatorname{Cov}(z,y^2)=\operatorname{Var}(z).
\]

At the rational representation
\[
b=\frac{67}{10},
\]
it verifies the fixed-point squared-amplitude and height relations.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The memory representation, conditional expectations, equality rigidity, and positive-mass excursion above \(z=b\) are analytic proofs in `RESULT.md`; no finite orbit computation is used to establish them.
