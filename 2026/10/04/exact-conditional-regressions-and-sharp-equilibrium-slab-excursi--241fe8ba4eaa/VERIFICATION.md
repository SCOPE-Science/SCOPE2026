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
The packaged `verify.py` uses exact sparse-polynomial arithmetic over rational coefficients in the formal variables \(x,y,z,a,b\).

It verifies
\[
L(ax+y-z)=az^2+bz
\]
and, after clearing the displayed division,
\[
L\!\left(abz^2+ab^2x+b^2y\right)
=
a x^2+b^2x-a(x-bz)^2.
\]
It also checks that the two canonical points \((0,0,0)\) and \((-2,4,-2)\) are equilibria for \(a=1/2\), \(b=1\).

The stored checker output is `VERIFY_OK`.

The checker validates the algebraic certificates. Conditional expectations are proved analytically in `RESULT.md` from invariance against arbitrary one-coordinate test functions, and the equality classification uses invariant-support tangency rather than finite simulation.
