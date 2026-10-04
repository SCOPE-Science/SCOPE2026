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
# Verification

The embedded `verify.py` is dependency-free and uses exact rational sparse-polynomial arithmetic. It checks the following identities for
\[
\dot x=-z,\qquad \dot y=x-y,\qquad \dot z=ax+y^2+bz:
\]

1. With \(K=z+bx-ay\), it verifies \(LK=y(y+a)\).
2. With \(w=x-y\), \(v=Lw=y-x-z\), and
\[
H=wv+\frac{1-b}{2}w^2+\frac a2y^2+\frac13y^3,
\]
it verifies
\[
LH=v^2-(a-b)w^2.
\]
3. It verifies the eliminated scalar equation
\[
\dddot y+(1-b)\ddot y+(a-b)\dot y+ay+y^2=0.
\]
4. It verifies that \((0,0,0)\) and \((-a,-a,0)\) are equilibria symbolically.

The replay output embedded in `verification_output.txt` is `VERIFY_OK`.

The checker verifies the algebraic certificates, not the general analytic facts about invariant measures or Wirtinger's inequality. Those steps are stated explicitly in the proof. No independent audit has been performed.
