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

Writing \(q\) for the formal value \(f(x)\), it verifies for
\[
\dot x=y,\qquad
\dot y=z,\qquad
\dot z=q-y-\beta z
\]
the identities
\[
L\left(\frac12y^2\right)=yz,
\qquad
L\left(\frac12x^2\right)=xy,
\]
\[
L(yz)=z^2+qy-y^2-\beta yz,
\]
\[
L(xy)=y^2+xz,
\]
and
\[
L(xz)=yz+xq-xy-\beta xz.
\]

The checker also verifies, on exact rational symbolic substitutions for the piecewise parameters, continuity of the three branches, the roots
\[
0,\qquad \pm\left(1+\frac{\alpha}{\mu}\right),
\]
and the harmonic equality substitution when \(\beta=\mu\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificates. The invariant-measure conclusions additionally use stationarity and support invariance; the period statement additionally uses the classical equality case of Wirtinger's inequality.
