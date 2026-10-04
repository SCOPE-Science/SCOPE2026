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
The packaged `verify.py` uses exact sparse-polynomial arithmetic over rational coefficients.

It verifies
\[
L(xy-z)=x^2-4y^2,
\]
\[
Lz=xz+3y^2,
\]
\[
L(yz)=xz+z^2+xyz+3y^3,
\]
the reversibility condition
\[
f(Ru)=-Rf(u),
\]
and the eliminated jerk identity
\[
x'''-xx''+x'-x^2+3(x')^2=0.
\]

It also checks that the equality-case substitutions
\[
x''=-\frac14x,\qquad x'''=-\frac14x'
\]
reduce the jerk equation to
\[
\frac34\left(x'-x^2+4(x')^2\right)=0.
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the algebraic certificate. The invariant-measure conclusions use the standard identity \(\int Lh\,d\mu=0\). The strict period statement additionally uses the classical equality case of Wirtinger's inequality.
