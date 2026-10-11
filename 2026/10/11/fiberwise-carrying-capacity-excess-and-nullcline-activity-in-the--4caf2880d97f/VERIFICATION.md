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

It checks the prey regression residual
\[
y-H(x)
=
-\frac{x+h}{c}\frac{\dot x}{x}
\]
and the predator harmonic residual
\[
\frac1x-\frac{\gamma}{y}
=
-\frac{\gamma}{s}\frac{\dot y}{y^2}.
\]

It verifies the algebraic identity
\[
\frac{(x-y/\gamma)^2}{x}
=
x-\frac{2y}{\gamma}+\frac{y^2}{\gamma^2x}
\]
and its conversion to
\[
\frac{x}{s^2}\left(\frac{\dot y}{y}\right)^2.
\]

It also checks the sign structure of the positive-equilibrium quadratic: negative leading coefficient, positive constant term, opposite signs at \(0\) and \(K\), and therefore exactly one positive root in \((0,K)\).

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure conditional expectations, equality rigidity, and two-sided nullcline crossing claims are analytic arguments in `RESULT.md`; no finite trajectory sampling is used.
